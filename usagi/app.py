import streamlit as st
import sqlite3
import hashlib

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
    c.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?", 
        (username, hash_password(password))
    )
    user = c.fetchone()
    conn.close()
    return user

# ログアウトボタンの表示
def logout_button():
    if st.sidebar.button("ログアウト"):
        if "username" in st.session_state:
            del st.session_state['username']
            st.session_state["menu"] = "ログイン"

# 占いロジック
def get_fortune(answers):
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

# 初期化
init_db()

# ページの初期化
if "menu" not in st.session_state:
    st.session_state["menu"] = "会員登録"

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
    with st.form("login_form"):
        username = st.text_input("ユーザー名")
        password = st.text_input("パスワード", type="password")
        submit_button = st.form_submit_button("ログイン")
        if submit_button:
            user = login_user(username, password)
            if user:
                st.session_state["username"] = username
                st.success(f"ようこそ、{username}さん！")

# 占いページ
elif menu == "占い":
    st.title("今日の占い")
    logout_button()
    if "username" in st.session_state:
        st.write(f"こんにちは、{st.session_state['username']}さん！")
        with st.form("fortune_form"):
            q1 = st.radio("趣味は？", ["旅行", "料理", "読書", "スポーツ", "映画鑑賞"], index=0)
            q2 = st.radio("好きな季節は？", ["春", "夏", "秋", "冬", "特になし"], index=0)
            q3 = st.radio("今日の気分は？", ["最高", "良い", "普通", "少し疲れた", "最悪"], index=0)
            submit_button = st.form_submit_button("占う")
            if submit_button:
                answers = [q1, q2, q3]
                result = get_fortune(answers)
                st.success(f"結果: {result}")
    else:
        st.error("ログインしてください！")