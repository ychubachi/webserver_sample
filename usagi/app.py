import streamlit as st
import sqlite3
import hashlib
import datetime
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
    if hobby == "旅行" and season == "春" and mood == "最高":
        return "春の旅行は幸運を運びます。計画を立てましょう！"
    elif hobby == "旅行" and season == "夏" and mood == "良い":
        return "夏の旅行は新しい出会いを引き寄せます！"
    elif hobby == "料理" and season == "秋" and mood == "普通":
        return "秋の味覚を楽しむ料理が運気を上げます。"
    elif hobby == "料理" and mood == "少し疲れた":
        return "疲れた日は簡単なレシピで楽しみましょう。"
    elif hobby == "読書" and season == "冬" and mood == "最悪":
        return "静かな時間を読書に使うと心が穏やかになります。"
    elif hobby == "スポーツ" and season == "春" and mood == "最高":
        return "アウトドアスポーツでエネルギーをチャージ！"
    elif hobby == "スポーツ" and season == "秋" and mood == "良い":
        return "新しいスポーツを始めるチャンスです！"
    elif hobby == "映画鑑賞" and season == "冬" and mood == "普通":
        return "暖かい部屋で映画を楽しむとリラックスできます。"
    elif hobby == "映画鑑賞" and mood == "最悪":
        return "お気に入りの映画があなたを元気づけます！"
    elif season == "夏" and mood == "最高":
        return "夏の日差しがあなたの幸運を引き寄せます！"
    elif season == "秋" and mood == "少し疲れた":
        return "秋の景色を楽しむと心が癒されます。"
    elif season == "冬" and mood == "良い":
        return "冬の星空を眺めてリフレッシュしましょう！"
    elif mood == "普通":
        return "普通の日でも、小さな幸せを見つけることが大事です。"
    elif mood == "最悪":
        return "今日は深呼吸をして気持ちを切り替えましょう！"
    else:
        return "新しい挑戦があなたの運勢を切り開きます！"
# 占い2: 相性占い
def get_fortune_2(answers):
    m_s_1, m_s_2, animal_1, animal_2, food_1, food_2 = answers
     #3つ同じ
    if  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性90%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性90%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性90%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性90%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性90%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性90%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性90%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性90%"
    #2つ同じ（犬猫以外）
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性85%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性85%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性85%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性85%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性85%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="山" and food_1=="和食" and food_2=='和食':
        return "相性85%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性85%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性85%"
    #2つ同じ（山海以外）
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性83%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性83%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性83%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性83%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性83%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性83%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性83%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性83%"
    #2つ同じ（和洋以外）
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性80%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性80%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性80%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性80%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性80%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性80%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性80%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性80%"
    #1つ同じ（和洋同じ）
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性75%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性75%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性75%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性75%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性75%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性75%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性75%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性75%"
    #1つ同じ（山海同じ）
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性71%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性71%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性71%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性71%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性71%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性71%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性71%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性71%"
    #1つ同じ（犬猫同じ）
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性68%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性68%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性68%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性68%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性68%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性68%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性68%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性68%"
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
menu = st.sidebar.radio("ページを選んでください", ["会員登録", "ログイン", "うさぎのシンプル占い", "ウサギの友人相性占い", "うさぎさんが占う、ちょーおおざっぱなあなたの今日の運勢"])

# 会員登録
if menu == "会員登録":
    st.title("会員登録")
    with st.form("register_form"):
        username = st.text_input("ユーザー名")
        email = st.text_input("メールアドレス")
        password = st.text_input("パスワード", type="password")
        birthdate = st.date_input(
            "生年月日", 
            min_value=datetime.date(1920, 1, 1),  # 生年月日の最小値を1920年に設定
            max_value=datetime.date.today()  # 生年月日の最大値を今日の日付に設定
        )
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
elif menu == "うさぎのシンプル占い":
    st.title("うさぎのシンプル占い")
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
elif menu == "ウサギの友人相性占い":
    st.title("ウサギの友人相性占い")
    if "username" in st.session_state:
        st.write(f"こんにちは、{st.session_state['username']}さん！")
        logout_button()
        col1, col2 = st.columns(2)
        with col1:
            image_1 = Image.open('./usagi/data/img_4.png')
            st.image(image_1, width=100)
        with col2:
            image_2 = Image.open('./usagi/data/img_5.png')
            st.image(image_2, width=100)
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
elif menu == "うさぎさんが占う、ちょーおおざっぱなあなたの今日の運勢":
    st.title("うさぎさんが占う、ちょーおおざっぱなあなたの今日の運勢")
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