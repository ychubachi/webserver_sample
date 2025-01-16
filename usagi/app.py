import streamlit as st
import sqlite3
import hashlib
from PIL import Image

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

# 占い1: シンプル占い
def get_fortune_1(answers):
    hobby, season, mood = answers
    if hobby == "旅行" and season == "春" and mood == "普通":
        return "春の旅行は新たな発見をもたらします！"
    else:
        return "今日は素敵なことが起きる予感！"

# 占い2: 相性占い
def get_fortune_2(answers):
    m_s_1, m_s_2, animal_1, animal_2, food_1, food_2 = answers
    if m_s_1 == "山" and m_s_2 == "山" and animal_1 == "犬" and animal_2 == "犬" and food_1 == "和食" and food_2 == "和食":
        return "相性90%"
    else:
        return "相性50%"

# 占い3: 質問ベースの運勢
def get_fortune_3(answers):
    score = answers.count("はい")
    if score >= 6:
        return "良い一日になりそ～今日も元気に行こ～"
    elif score >= 4:
        return "楽しく過ごせそ～かも"
    else:
        return "ゆっくり休む日をつくろっか～"

# ログアウトボタン
def logout_button():
    if st.sidebar.button("ログアウト"):
        if "username" in st.session_state:
            del st.session_state['username']
            st.session_state["menu"] = "ログイン"

# 初期化
init_db()
set_styles()

# ページ選択
menu = st.sidebar.radio("ページを選んでください", ["会員登録", "ログイン", "占い1", "占い2", "占い3"])

# 会員登録
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

# ログイン
elif menu == "ログイン":
    st.title("ログイン")
    logout_button()
    with st.form("login_form"):
        username = st.text_input("ユーザー名")
        password = st.text_input("パスワード", type="password")
        submit_button = st.form_submit_button("ログイン")
        if submit_button:
            login_result = login_user(username, password)
            if login_result == True:
                st.session_state["username"] = username
                st.success(f"ようこそ、{username}さん！")
            else:
                st.error(login_result)

# 占い1: シンプル占い
elif menu == "占い1":
    st.title("占い1")
    if "username" in st.session_state:
        st.write(f"こんにちは、{st.session_state['username']}さん！")
        logout_button()
        with st.form("fortune_form_1"):
            q1 = st.radio("趣味は？", ["旅行", "料理", "読書", "スポーツ", "映画鑑賞"])
            q2 = st.radio("好きな季節は？", ["春", "夏", "秋", "冬", "特になし"])
            q3 = st.radio("今日の気分は？", ["最高", "良い", "普通", "少し疲れた", "最悪"])
            submit_button = st.form_submit_button("占う")
            if submit_button:
                answers = [q1, q2, q3]
                st.success(get_fortune_1(answers))
    else:
        st.error("ログインしてください！")

# 占い2: 相性占い
elif menu == "占い2":
    st.title("占い2")
    if "username" in st.session_state:
        st.write(f"こんにちは、{st.session_state['username']}さん！")
        logout_button()
        with st.form("fortune_form_2"):
            q1 = st.radio("あなたは山と海どちらに行くのが好きですか？", ["山", "海"])
            q2 = st.radio("相手は山と海どちらに行くのが好きですか？", ["山", "海"])
            q3 = st.radio("あなたは犬と猫のどちらが好きですか？", ["犬", "猫"])
            q4 = st.radio("相手は犬と猫のどちらが好きですか？", ["犬", "猫"])
            q5 = st.radio("あなたは和食と洋食のどちらが好きですか？", ["和食", "洋食"])
            q6 = st.radio("相手は和食と洋食どちらが好きですか？", ["和食", "洋食"])
            submit_button = st.form_submit_button("占う")
            if submit_button:
                answers = [q1, q2, q3, q4, q5, q6]
                st.success(get_fortune_2(answers))
    else:
        st.error("ログインしてください！")

# 占い3: 質問ベースの運勢
elif menu == "占い3":
    st.title("占い3")
    if "username" in st.session_state:
        st.write(f"こんにちは、{st.session_state['username']}さん！")
        logout_button()
        questions = [
            "7時間以上寝ましたか？",
            "朝すぐにふとんから出られましたか？",
            "今日は晴れですか？",
            "朝ごはんは食べましたか？",
            "風は気持ち良いですか？",
            "何か動物を見ましたか？",
            "今日の予定は楽しみですか？",
            "推しはいますか？",
        ]
        answers = []
        for i, question in enumerate(questions):
            answer = st.radio(question, ("はい", "いいえ"), key=f"q3_{i}")
            answers.append(answer)
        if st.button("占う"):
            st.success(get_fortune_3(answers))
    else:
        st.error("ログインしてください！")