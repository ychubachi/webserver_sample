import streamlit as st

#テキスト関連
st.title('うさぎさんが占う、ちょーおおざっぱなあなたの今日の運勢')
st.caption('質問に応えてください！')

# タイトルと説明
st.title("今日の運勢占い")
st.write("次の質問に「はい」または「いいえ」で答えてください。")

# 質問リスト（質問内容は自由に変更できます）
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

# ユーザーの回答を保存するためのリスト
answers = []

# 二択の質問を表示し、ユーザーの回答を取得
for i, question in enumerate(questions, 1):
    answer = st.radio(question, ("はい", "いいえ"), key=f"question_{i}")
    answers.append(answer)

# 送信ボタン
if st.button("運勢を占う"):
    # 回答を基に運勢を占う
    score = answers.count("はい")  # "はい"の数を数えてスコアにする

    # スコアに基づいて運勢を決定
    if score >= 6:
        result = "良い一日になりそ～今日も元気に行こ～"
    elif score >= 4:
        result = "楽しく過ごせそ～かも"
    else:
        result = "ゆっくり休む日をつくろっか～"

    # 結果を表示
    st.write(f"あなたの運勢は：{result}")
