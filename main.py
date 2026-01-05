import streamlit as st
from style import set_common_style

# 基本設定（一番上に書く）
st.set_page_config(page_title="国民年金Q&A Pod", layout="wide")

# 🌸 style.pyを呼び出して、背景とデザインを一発適用！
set_common_style("all_family.png")
st.sidebar.markdown('<div class="sidebar-title">🏥 国民年金Q&A Pod</div>', unsafe_allow_html=True)

# メインコンテンツ
st.markdown('<div class="omamori-text">『あなたと家族を守る、年金のお守り』</div>', unsafe_allow_html=True)

st.sidebar.success("左のメニューから「Q&A検索」や「辞書」を選んでくださいね。")