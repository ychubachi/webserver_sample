import sqlite3
import streamlit as st
import os

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

# ユーザー登録
def register_user(username, email, password):
    conn = sqlite3.connect("kame_users.db")
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
    conn = sqlite3.connect("kame_users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

# ページ切り替え関数
def switch_page(page):
    st.session_state["page"] = page

# サイコロの種類に応じて、動的にページを切り替える部分
def saikoro_page(choice):
    # 現在のスクリプトファイルのディレクトリを取得
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # kame/pages/ディレクトリの絶対パスを作成
    path1 = os.path.join(current_dir, 'kame', 'pages', 'saikoro_6.py')
    path2 = os.path.join(current_dir, 'kame', 'pages', 'saikoro_12.py')
    path3 = os.path.join(current_dir, 'kame', 'pages', 'saikoro_17.py')

    # 各オプションに応じたロジック
    if choice == "６種類":
        try:
            with open(path1, encoding="UTF-8") as f1:
                content1 = f1.read()
                exec(content1)  # ファイルの内容を実行
        except FileNotFoundError:
            st.error(f"{path1} が見つかりません")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    elif choice == "12種類":
        try:
            with open(path2, encoding="UTF-8") as f2:
                content2 = f2.read()
                exec(content2)  # ファイルの内容を実行
        except FileNotFoundError:
            st.error(f"{path2} が見つかりません")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    elif choice == "17種類":
        try:
            with open(path3, encoding="UTF-8") as f3:
                content3 = f3.read()
                exec(content3)  # ファイルの内容を実行
        except FileNotFoundError:
            st.error(f"{path3} が見つかりません")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")

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
            switch_page("saikoro")  # ログイン成功後にサイコロ選択ページへ移動
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
                switch_page("saikoro")  # 登録成功後にサイコロ選択ページへ移動
            else:
                st.error(message)
        else:
            st.error("全てのフィールドを正しく入力してください。")

    st.button("ログインはこちら", on_click=lambda: switch_page("login"))

# サイコロ選択ページ
def saikoro_select_page():
    st.title("サイコロ選択")
    options = ["６種類", "12種類", "17種類"]
    choice = st.selectbox("サイコロの種類を選択してください", options)

    # Sidebar に選択肢を表示
    with st.sidebar:
        st.header("現在の選択")
        st.write(f"サイコロの種類: **{choice}**")

    saikoro_page(choice)

# 設定でサイドバー非表示
st.markdown("""
    <style>
        .css-1v3fvcr { display: none; }
    </style>
""", unsafe_allow_html=True)

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
    elif st.session_state["page"] == "saikoro":
        saikoro_select_page()