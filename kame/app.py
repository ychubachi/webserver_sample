import sqlite3
import streamlit as st

# データベース接続と初期化
def init_db():
    conn = sqlite3.connect("users.db")
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

# ユーザー登録
def register_user(username, email, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()
        return True, None
    except sqlite3.IntegrityError:
        conn.close()
        return False, "このユーザー名は既に登録されています。"

# ログイン認証
def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

# ページ切り替え関数
def switch_page(page):
    st.session_state["page"] = page

# タイトルコールページ
def title_call_page():
    st.title("おみくじアプリ")
    st.write("このアプリへようこそ！以下のボタンでログインまたは会員登録を行ってください。")
    st.button("ログイン", on_click=lambda: switch_page("login"))
    st.button("会員登録", on_click=lambda: switch_page("register"))

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
            switch_page("home")  # ログイン成功後にホームページへ移動
        else:
            st.error("ユーザー名またはパスワードが間違っています。")

    st.button("会員登録はこちら", on_click=lambda: switch_page("register"))

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
        elif username and email and password:
            success, message = register_user(username, email, password)
            if success:
                st.success(f"{username}さん、登録が完了しました！")
                switch_page("home")  # 登録成功後にホームページへ移動
            else:
                st.error(message)
        else:
            st.error("全てのフィールドを正しく入力してください。")

    st.button("ログインはこちら", on_click=lambda: switch_page("login"))

# ページ表示
if __name__ == "__main__":
    init_db()  # データベース初期化

    if "page" not in st.session_state:
        st.session_state["page"] = "title_call"

    # ページの状態に応じて表示
    if st.session_state["page"] == "title_call":
        title_call_page()
    elif st.session_state["page"] == "login":
        login_page()
    elif st.session_state["page"] == "register":
        register_page()
    elif st.session_state["page"] == "home":
        try:
            # home.py を動的に読み込む
            with open("home.py", "r", encoding="utf-8") as f:
                exec(f.read())
        except FileNotFoundError:
            st.error("home.py が見つかりません")