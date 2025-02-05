import sqlite3
import streamlit as st
import re
import os
from PIL import Image  # 画像を表示するために追加
import requests
import io

# データベース接続と初期化
def init_db():
    conn = sqlite3.connect("kame_users.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# ユーザー登録時のパスワードをそのまま保存
def register_user(username, email, password):
    conn = sqlite3.connect("kame_users.db")
    c = conn.cursor()

    # パスワードのバリデーション（条件削除）
    if not validate_email(email):
        conn.close()
        return False, "メールアドレスが無効です。"
    
    try:
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()
        return True, None
    except sqlite3.IntegrityError:
        conn.close()
        return False, "このユーザー名は既に登録されています。"

# ログイン時のパスワードを直接比較
def authenticate_user(username, password):
    conn = sqlite3.connect("kame_users.db")
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    stored_password = c.fetchone()
    conn.close()

    if stored_password:
        return stored_password[0] == password  # パスワードを直接比較
    return False

# 入力されたメールアドレスの形式をチェック
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# ページ切り替え関数
def switch_page(page):
    st.session_state["page"] = page

# サイコロの種類に応じて、動的にページを切り替える部分
def saikoro_page(choice):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_map = {
        "６種類": os.path.join(current_dir, 'kame', 'pages', 'saikoro_6.py'),
        "12種類": os.path.join(current_dir, 'kame', 'pages', 'saikoro_12.py'),
        "17種類": os.path.join(current_dir, 'kame', 'pages', 'saikoro_17.py')
    }
    
    # 該当するサイコロページのファイルを読み込む
    path = path_map.get(choice)
    if path and os.path.exists(path):
        with open(path, encoding="UTF-8") as f:
            content = f.read()
            exec(content)  # ファイル内容を実行
    else:
        st.error(f"サイコロページのファイルが見つかりません: {path}")


# ホームに戻るボタンを表示
def home_button():
    if st.button("ホームに戻る"):
        switch_page("choose")  # トップページに戻る

# ログアウトボタンを表示
def logout_button():
    if st.button("ログアウト"):
        del st.session_state["username"]  # セッションを削除
        switch_page("choose")  # ログアウト後にトップページに戻る

# ログインまたは会員登録を選択するページ
def choose_page():
    #st.title("おみくじアプリ")
    st.markdown("<h2 style='text-align: center;'>おみくじアプリ</h2>", unsafe_allow_html=True)
    st.write("以下のボタンでログインまたは会員登録を行ってください。")
    
    # 中央寄せにするためのCSS
    col1, col2 = st.columns(2)

    with col1:
        if st.button("ログイン", use_container_width=True):
            switch_page("login")
    
    with col2:
        if st.button("会員登録", use_container_width=True):
            switch_page("register")
    url='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmg2kn9DyMES8p81iw0-civQjYw0bIDleQAH8gOAp_mv75OnJaeBgcv6vsVIRNnHT-BTuDfmmQ4X8bgRi3U6tQdG-m5C0nYzWahyDp4vyYTPs7BvcsAZVIhzkHt-scsWxKhE3B3JMs_Y8/s400/syougatsu2_omijikuji2.png'
    img = Image.open(io.BytesIO(requests.get(url).content))
    # CSSスタイルを設定して画像をページ下部に配置
    st.markdown("""
        <style>
            .bottom-image-container {
                display: flex;
                justify-content: center;
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: white;
                padding: 10px 0; /* 画像周りに余白を追加 */
            }

            .bottom-image-container img {
                max-width: 100%;
                height: auto; /* 縦横比を維持 */
                max-height: 40vh; /* 必要に応じて変更 */
            }
        </style>
        <div class="bottom-image-container">
            <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmg2kn9DyMES8p81iw0-civQjYw0bIDleQAH8gOAp_mv75OnJaeBgcv6vsVIRNnHT-BTuDfmmQ4X8bgRi3U6tQdG-m5C0nYzWahyDp4vyYTPs7BvcsAZVIhzkHt-scsWxKhE3B3JMs_Y8/s400/syougatsu2_omijikuji2.png">
        </div>
    """, unsafe_allow_html=True)


# ログインページ
def login_page():
    st.title("ログイン")
    st.write("アカウントをお持ちの場合は、以下にログイン情報を入力してください。")
    
    with st.form("login_form"):
        username = st.text_input("ユーザー名", placeholder="例: user123")
        password = st.text_input("パスワード", type="password", placeholder="例: password123")
        login_button = st.form_submit_button("ログイン")
    
    if login_button:
        if authenticate_user(username, password):
            st.success(f"ようこそ、{username}さん！")
            st.session_state["username"] = username
            switch_page("saikoro")  # ログイン成功後にサイコロ選択ページへ移動
        else:
            st.error("ユーザー名またはパスワードが間違っています。")

    home_button()  # ホームに戻るボタン

# 会員登録ページ
def register_page():
    st.title("会員登録")
    st.write("以下のフォームに必要事項を入力して会員登録を行ってください。")
    
    with st.form("register_form"):
        username = st.text_input("ユーザー名", placeholder="例: user123")
        email = st.text_input("メールアドレス", placeholder="例: example@example.com")
        password = st.text_input("パスワード", type="password", placeholder="例: password123")
        confirm_password = st.text_input("パスワード確認", type="password", placeholder="例: password123")
        agree = st.checkbox("利用規約に同意します")
        register_button = st.form_submit_button("登録")
    
    if register_button:
        if not agree:
            st.error("利用規約に同意する必要があります。")
        elif password != confirm_password:
            st.error("パスワードが一致しません。")
        elif not validate_email(email):
            st.error("メールアドレスが無効です。")
        elif username and email and password:
            success, message = register_user(username, email, password)
            if success:
                st.success(f"{username}さん、登録が完了しました！")
                st.session_state["username"] = username  # 登録完了と同時にログイン状態にする
                switch_page("saikoro")  # 登録成功後にサイコロ選択ページへ移動
            else:
                st.error(message)
        else:
            st.error("全てのフィールドを正しく入力してください。")

    home_button()  # ホームに戻るボタン

# サイコロ選択ページ
def saikoro_select_page():
    st.title("サイコロ選択")
    options = ["６種類", "12種類", "17種類"]
    choice = st.selectbox("サイコロの種類を選択してください：", options)

    # Sidebar に選択肢を表示
    with st.sidebar:
        st.header("現在の選択")
        st.write(f"サイコロの種類: **{choice}**")

    # 画像を表示
    ##display_image(choice)

    saikoro_page(choice)  # サイコロページを表示
    logout_button()  # ログアウトボタン

# 設定でサイドバー非表示
st.markdown("""
    <style>
        .css-1v3fvcr { display: none; }
    </style>
""", unsafe_allow_html=True)

# ページ表示
if __name__ == "__main__":
    init_db()  # データベース初期化

    # 最初に表示するページをログインまたは会員登録選択ページに変更
    if "page" not in st.session_state:
        st.session_state["page"] = "choose"  # ログインまたは会員登録を選択するページに設定

    # ページの状態に応じて表示
    if st.session_state["page"] == "choose":
        choose_page()
    elif st.session_state["page"] == "login":
        login_page()
    elif st.session_state["page"] == "register":
        register_page()
    elif st.session_state["page"] == "saikoro":
        saikoro_select_page()