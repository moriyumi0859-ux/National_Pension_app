import streamlit as st
import os
import sys  # 👈 忘れずに追加
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

st.sidebar.markdown('<div class="sidebar-title">🌸 国民年金Q&A Pod</div>', unsafe_allow_html=True)

# 1. 一つ上の階層にある style.py を読み込む設定
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from style import set_common_style

load_dotenv()
st.set_page_config(layout="wide")

# 2. デザインを一発適用（style.py に任せる）
set_common_style("back_sky.png")
st.sidebar.markdown('<div class="sidebar-title">🌸 国民年金Q&A Pod</div>', unsafe_allow_html=True)

# 3. コンテンツ（座布団の中にタイトルを入れる）
st.markdown('<div class="white-box"><h1>📖 専門用語の「噛み砕き」辞書</h1>難しい言葉を、身近な例え話で解説します。</div>', unsafe_allow_html=True)

word = st.selectbox("解説してほしい言葉を選んでください", options=["", "老齢基礎年金", "老齢厚生年金", "繰下げ受給", "振替加算", "加給年金"])

if word:
    with st.spinner(f"「{word}」を噛み砕いています..."):
        llm = ChatOpenAI(model_name="gpt-4o")
        # 優しいプロンプト
        res = llm.invoke(f"「{word}」という年金用語を、中学生にもわかるように、身近な例え話（お小遣いやおやつ、ゲームなど）を使って、優しく親しみやすい言葉で200文字程度で解説して。")
        
        # 回答部分も style.py の白い座布団で包む
        st.markdown(f'''
            <div class="white-box">
                <h3 style="color:#2C3E50;">🌸 {word} を噛み砕くと...</h3>
                <p style="line-height: 1.8;">{res.content}</p>
            </div>
        ''', unsafe_allow_html=True)