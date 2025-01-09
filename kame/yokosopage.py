import streamlit as st

# ページ設定
st.set_page_config(page_title="ログインと会員登録", page_icon="🔒")

# セッションステートの初期化
if "page" not in st.session_state:
    st.session_state["page"] = "login"  # 初期表示を「ログイン」に設定

# ページ切り替え関数
def switch_page(page):
    st.session_state["page"] = page

# ログインページ
def login_page():
    st.title("ログイン")
    st.write("アカウントをお持ちの場合は、以下にログイン情報を入力してください。")
    
    # 入力フォーム
    with st.form("login_form"):
        username = st.text_input("ユーザー名")
        password = st.text_input("パスワード", type="password")
        login_button = st.form_submit_button("ログイン")
    
    # ログイン処理
    if login_button:
        if username == "test" and password == "1234":  # 仮の認証
            st.success(f"ようこそ、{username}さん！")
            st.session_state["username"] = username
        else:
            st.error("ユーザー名またはパスワードが間違っています。")
    
    # 会員登録ページへのリンク
    st.button("会員登録はこちら", on_click=lambda: switch_page("register"))

# 会員登録ページ
def register_page():
    st.title("会員登録")
    st.write("以下のフォームに必要事項を入力して会員登録を行ってください。")
    
    # 入力フォーム
    with st.form("register_form"):
        username = st.text_input("ユーザー名")
        email = st.text_input("メールアドレス")
        password = st.text_input("パスワード", type="password")
        confirm_password = st.text_input("パスワード確認", type="password")
        agree = st.checkbox("利用規約に同意します")
        register_button = st.form_submit_button("登録")
    
    # 会員登録処理
    if register_button:
        if not agree:
            st.error("利用規約に同意する必要があります。")
        elif password != confirm_password:
            st.error("パスワードが一致しません。")
        elif username and email and password:
            st.success(f"{username}さん、登録が完了しました！")
            st.session_state["username"] = username
            switch_page("login")  # 登録後にログインページへ移動
        else:
            st.error("全てのフィールドを正しく入力してください。")
    
    # ログインページへのリンク
    st.button("ログインはこちら", on_click=lambda: switch_page("login"))

# ページ表示
if st.session_state["page"] == "login":
    login_page()
elif st.session_state["page"] == "register":
    register_page()