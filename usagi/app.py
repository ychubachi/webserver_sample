import streamlit as st
import sqlite3
import hashlib

# スタイルを設定
def set_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFF0F5; /* 全体の背景をピンク */
        }
        input, textarea, select {
            background-color: #FFFFFF !important; /* 入力フィールドとドロップダウンの背景を白 */
            color: #000000 !important; /* 入力文字を黒 */
            border: 1px solid #DDDDDD; /* 境界線を薄いグレー */
            border-radius: 5px;
            padding: 8px;
        }
        input:focus, textarea:focus, select:focus {
            border: 1px solid #FF69B4; /* フォーカス時の境界線をピンク */
            outline: none;
        }
        select {
            background-color: #FFFFFF !important; /* 選択後のドロップダウンも白 */
        }
        select option {
            background-color: #FFFFFF !important; /* ドロップダウンリストの背景も白 */
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# データベースの初期化
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT,
            password TEXT
        )
    """)
    try:
        c.execute("ALTER TABLE users ADD COLUMN birthdate TEXT")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE users ADD COLUMN gender TEXT")
    except sqlite3.OperationalError:
        pass
    conn.commit()
    conn.close()

# パスワードのハッシュ化
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ユーザーログイン
def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    if user:
        stored_password = user[2]
        if stored_password == hash_password(password):
            return True
        else:
            return "パスワードが間違っています"
    else:
        return "ユーザー名が存在しません"
    conn.close()

# ユーザー登録
def register_user(username, email, password, birthdate, gender):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute(
            """
            INSERT INTO users (username, email, password, birthdate, gender) 
            VALUES (?, ?, ?, ?, ?)
            """, 
            (username, email, hash_password(password), birthdate, gender)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True

# 占い結果を生成
def get_fortune(answers):
    hobby, season, mood = answers
    if hobby == "旅行" and season == "春" and mood == "普通":
        return "春の旅行は新たな発見をもたらします！"
    elif hobby == "料理" and season == "秋" and mood == "最高":
        return "秋の料理で心を満たしてください！"
    else:
        return "今日は素敵なことが起きる予感！"

# ログアウトボタンの表示
def logout_button():
    if st.sidebar.button("ログアウト"):
        if "username" in st.session_state:
            del st.session_state['username']
            st.session_state["menu"] = "ログイン"
            st.session_state["login_username"] = ""
            st.session_state["login_password"] = ""
            st.session_state["logout_message"] = "ログアウトしました。ログインしてください。"

# 初期化
init_db()

# スタイル設定
set_styles()

# ページの初期化
if "menu" not in st.session_state:
    st.session_state["menu"] = "会員登録"

# 初期値の設定（ログイン入力欄を管理）
if "login_username" not in st.session_state:
    st.session_state["login_username"] = ""
if "login_password" not in st.session_state:
    st.session_state["login_password"] = ""

# サイドバーでページ選択
menu = st.sidebar.radio("ページを選んでください", ["会員登録", "ログイン", "占い"], index=["会員登録", "ログイン", "占い"].index(st.session_state["menu"]))

# 会員登録ページ
if menu == "会員登録":
    st.title("会員登録")
    with st.form("register_form"):
        username = st.text_input("ユーザー名")
        email = st.text_input("メールアドレス")
        password = st.text_input("パスワード", type="password")
        birthdate = st.date_input("生年月日")
        gender = st.selectbox("性別", ["男性", "女性", "その他"])
        submit_button = st.form_submit_button("登録")
        if submit_button:
            if username and email and password and birthdate and gender:
                if register_user(username, email, password, str(birthdate), gender):
                    st.success("登録が完了しました！ログインしてください。")
                else:
                    st.error("このユーザー名はすでに使用されています。")
            else:
                st.error("全ての項目を入力してください。")

# ログインページ
elif menu == "ログイン":
    st.title("ログイン")
    logout_button()

    # ログアウトメッセージの表示
    if "logout_message" in st.session_state:
        st.warning(st.session_state["logout_message"])
        del st.session_state["logout_message"]

    with st.form("login_form"):
        username = st.text_input("ユーザー名", value=st.session_state["login_username"], key="username_field")
        password = st.text_input("パスワード", type="password", value=st.session_state["login_password"], key="password_field")
        submit_button = st.form_submit_button("ログイン")
        if submit_button:
            login_result = login_user(username, password)
            if login_result == True:
                st.session_state["username"] = username
                st.success(f"ようこそ、{username}さん！")
            else:
                st.error(login_result)

# 占いページ
elif menu == "占い":
    st.title("今日の占い")
    logout_button()
    if "username" in st.session_state:
        st.write(f"こんにちは、{st.session_state['username']}さん！")
        with st.form("fortune_form"):
            q1 = st.radio("趣味は？", ["旅行", "料理", "読書", "スポーツ", "映画鑑賞"], index=0)
            q2 = st.radio("好きな季節は？", ["春", "夏", "秋", "冬", "特になし"], index=0)
            q3 = st.radio("今日の気分は？", ["最高", "良い", "普通", "少し疲れた", "最悪"], index=2)
            submit_button = st.form_submit_button("占う")
            if submit_button:
                answers = [q1, q2, q3]
                result = get_fortune(answers)
                st.success(f"結果: {result}")
    else:
        st.error("ログインしてください！")