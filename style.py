import streamlit as st
import os
import base64

def set_common_style(bg_image_name):
    # 1. パス計算
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bg_path = os.path.join(current_dir, bg_image_name)

    # 2. 背景画像の設定
    bg_css = ""
    if os.path.exists(bg_path):
        with open(bg_path, "rb") as f:
            bin_str = base64.b64encode(f.read()).decode()
        bg_css = f'background-image: url("data:image/png;base64,{bin_str}"); background-size: cover; background-position: center; background-attachment: fixed;'

    # 3. 共通デザインの定義
    st.markdown(f'''
        <style>
        /* 画面全体 */
        .stApp {{ {bg_css} }}

        /* 🌸 ホーム画面：後光文字 */
        .omamori-text {{
            font-family: 'Hiragino Maru Gothic ProN', sans-serif;
            color: #2C3E50;
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            padding-top: 150px;
            line-height: 1.5;
            text-shadow: 
                0 0 15px rgba(255, 255, 255, 1.0),
                0 0 30px rgba(255, 255, 255, 0.9),
                0 0 50px rgba(255, 255, 255, 0.8),
                0 0 70px rgba(255, 255, 255, 0.6),
                0 0 100px rgba(255, 255, 255, 0.4);
            background: none !important;
        }}

        /* 🌸 サイドバー本体：磨りガラス風 */
        [data-testid="stSidebar"] {{
            background-color: rgba(255, 255, 255, 0.45) !important;
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(255, 255, 255, 0.3);
            width: 300px !important;
        }}

        /* 🌸 サイドバーの看板：一番上に固定 */
        .sidebar-title {{
            font-family: 'Hiragino Maru Gothic ProN', sans-serif;
            color: #2C3E50;
            font-size: 1.4rem;
            font-weight: bold;
            text-align: center;
            
            /* 一番上に固定するための設定 */
            position: fixed;
            top: 0;
            left: 0;
            width: 300px; /* サイドバーの幅に合わせる */
            z-index: 999;
            
            padding: 40px 10px 20px 10px; /* 上を少し空けてバランスを整える */
            background-color: rgba(255, 255, 255, 0.2); /* 看板の下を少しだけ色付け */
            border-bottom: 1px solid rgba(255, 255, 255, 0.3);
            text-shadow: 1px 1px 10px white;
        }}

        /* 🌸 メニューが看板と重ならないように下に押し下げる */
        [data-testid="stSidebarNav"] {{
            padding-top: 110px !important;
        }}

        /* サイドバーのメニュー項目 */
        [data-testid="stSidebarNav"] li {{
            background-color: rgba(255, 255, 255, 0.25);
            margin: 10px 15px;
            border-radius: 15px;
            transition: 0.3s all ease;
        }}
        
        [data-testid="stSidebarNav"] li:hover {{
            background-color: rgba(255, 255, 255, 0.6);
            transform: translateX(5px);
        }}

        /* 白い座布団 */
        .white-box {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 40px;
            border-radius: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            color: #2C3E50;
            margin-bottom: 30px;
        }}

        /* 入力欄の角 */
        .stTextInput>div>div>input, .stSelectbox>div>div {{
            border-radius: 15px !important;
        }}
        </style>
        ''', unsafe_allow_html=True)