import random
import streamlit as st
import pandas as pd
from PIL import Image

if "omikuji" not in st.session_state:
   st.session_state.omikuji = []

st.title("おみくじ")

if st.button("おみくじをひく"):
    result = random.randint(1, 120)
    if result%6 == 1:
       result2 = "大吉"
       st.write(f"{result}番 {result2}です。")
       st.session_state.omikuji.append((result, result2))
    elif result%6 == 2:
       result2 = "中吉"
       st.write(f"{result}番 {result2}です。")
       st.session_state.omikuji.append((result, result2))
    elif result%6 == 3:
       result2 = "小吉"
       st.write(f"{result}番 {result2}です。")
       st.session_state.omikuji.append((result, result2))
    elif result%6 == 4:
       result2 = "吉"
       st.write(f"{result}番 {result2}です。")
       st.session_state.omikuji.append((result, result2))
    elif result%6 == 5:
       result2 = "末吉"
       st.write(f"{result}番 {result2}です。")
       st.session_state.omikuji.append((result, result2))
    else:
       result2 = "凶"
       st.write(f"{result}番 {result2}です。")
       st.session_state.omikuji.append((result, result2))

#画像
image = Image.open('kame/6omikuji.png')
st.image(image, width=700)

df = pd.DataFrame(st.session_state.omikuji, columns=["おみくじ番号", "運勢"])
st.dataframe(df)
st.write("おみくじをひいた回数", len(st.session_state.omikuji))

if st.button("結果"):
   st.bar_chart(df["運勢"].value_counts())