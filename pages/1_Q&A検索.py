import streamlit as st
import os
import base64
import sys  # 👈 これが必要です！
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. 一つ上の階層にある style.py を読み込む設定
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from style import set_common_style

load_dotenv()
st.set_page_config(layout="wide")

# 2. デザインを一発適用（背景画像と白い座布団の設定が style.py から読み込まれます）
set_common_style("back_sky.png")
st.sidebar.markdown('<div class="sidebar-title">🌸 国民年金Q&A Pod</div>', unsafe_allow_html=True)

# コンテンツ
st.markdown('<div class="white-box"><h1>🔍 年金の疑問を検索</h1>資料を確認して、AIコンシェルジュが丁寧にお答えします。</div>', unsafe_allow_html=True)

# 3. 知識ベースの準備
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "pension_deta")

@st.cache_resource
def get_vectorstore():
    if not os.path.exists(DATA_DIR) or not os.listdir(DATA_DIR): return None
    loader = PyPDFDirectoryLoader(DATA_DIR)
    docs = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(loader.load())
    return FAISS.from_documents(docs, OpenAIEmbeddings())

vs = get_vectorstore()

if vs:
    query = st.text_input("質問を入力してください（例：付加年金について教えて）")
    if query:
        with st.spinner("資料を確認しています..."):
            llm = ChatOpenAI(model_name="gpt-4o")
            prompt = ChatPromptTemplate.from_template("""
            あなたは、年金の不安を抱える方に寄り添う、とても優しくて頼りになるコンシェルジュです。
            資料の内容を元に、相手を安心させるような丁寧な日本語で答えてください。
            【ルール】
            ・「ご質問ありがとうございます。大切なことですので、丁寧にお伝えしますね。」と始めてください。
            ・専門用語を避け、やさしい言葉に言い換えてください。
            ・引用番号や[1]などの記号は一切出さないでください。
            ・最後に「他にも不安なことがあれば、いつでも聞いてくださいね」と結んでください。
            ・敬語を使ってください。急にタメ口にならないでください。
            ・分からない部分や資料にない内容は、無理に答えず「申し訳ございませんが、その点については詳しく説明が必要なので窓口へ相談してください。」とお伝えしてください。
            
            <context>{context}</context>
            質問: {question}
            """)
            chain = ({"context": vs.as_retriever(), "question": RunnablePassthrough()} | prompt | llm | StrOutputParser())
            res = chain.invoke(query)
            # style.py の .white-box クラスを使って回答を表示
            st.markdown(f'<div class="white-box"><h3>AIの回答</h3>{res}</div>', unsafe_allow_html=True)
else:
    st.info("pension_detaフォルダにPDFを入れてください。")