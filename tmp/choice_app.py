import random
import streamlit as st

st.title("文字列から単語を選択するアプリ")#タイトル出してる
# 入力ボックス
text = st.text_input("スペース区切りで単語を入力してください。") #st.text_input：入力ボックスが完了
# スペース区切りでリスト化
words = text.replace("　", " ").split(" ") #text.replace：ある文字をある文字に置き換えてる。今回は、全角スペースを感覚スペースに置き換えてる。#split：区切られてる文字列を切り分けている
# リストを表示
st.write("入力した単語: ", words)

# ボタンを設置し、ボタンが押されたら実行
if st.button("一つを選ぶ"):
    choice = random.choice(words)  # ランダムに1つだけを選択
    st.write("選択された単語: ", choice)  # 選択されたものを表示