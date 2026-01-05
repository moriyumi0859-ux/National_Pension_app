import streamlit as st
import os
import base64

def set_common_style(bg_image_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bg_path = os.path.join(current_dir, bg_image_name)

    bg_css = ""
    if os.path.exists(bg_path):
        with open(bg_path, "rb") as f:
            bin_str = base64.b64encode(f.read()).decode()
        bg_css = f'background-image: url("data:image/png;base64,{bin_str}"); background-size: cover; background-position: center; background-attachment: fixed;'

    st.markdown(f'''
        <style>
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

        /* 🌸 サイドバー：磨りガラス風 */
        [data-testid="stSidebar"] {{
            background-color: rgba(255, 255, 255, 0.45) !important;
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(255, 255, 255, 0.3);
            width: 300px !important;
        }}

        /* 🌸 サイドバーの看板デザイン（よりお守りらしく！） */
        .sidebar-title {{
            font-family: 'Hiragino Maru Gothic ProN', sans-serif;
            color: #2C3E50;
            font-size: 1.4rem;
            font-weight: bold;
            text-align: center;
            padding: 20px 10px;
            /* 上下に薄い光の線を引く */
            border-top: 1px solid rgba(255, 255, 255, 0.5);
            border-bottom: 1px solid rgba(255, 255, 255, 0.5);
            margin-bottom: 20px;
            text-shadow: 1px 1px 10px white;
        }}

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

        .white-box {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 40px;
            border-radius: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            color: #2C3E50;
            margin-bottom: 30px;
        }}

        .stTextInput>div>div>input, .stSelectbox>div>div {{
            border-radius: 15px !important;
        }}
        </style>
        ''', unsafe_allow_html=True)