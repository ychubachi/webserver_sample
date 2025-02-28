import random
import streamlit as st
import pandas as pd

if "omikuji" not in st.session_state:
   st.session_state.omikuji = []

st.title("おみくじ")

if st.button("おみくじをひく"):
    result = random.randint(1, 6)
    st.session_state.omikuji.append((result))
    if result == 1:
       st.write(f"{result}番 大吉です。")
    elif result == 2:
       st.write(f"{result}番 中吉です。")
    elif result == 3:
       st.write(f"{result}番 小吉です。")
    elif result == 4:
       st.write(f"{result}番 末吉です。")
    elif result == 5:
       st.write(f"{result}番  凶です。")
    else:
       st.write(f"{result}番 大凶 です。")

df = pd.DataFrame(st.session_state.omikuji, columns=["おみくじ番号"])
st.dataframe(df)
st.write("おみくじをひいた回数", len(st.session_state.omikuji))

if st.button("結果"):
   st.bar_chart(df["おみくじ番号"].value_counts())