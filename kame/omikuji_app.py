import random
import streamlit as st
import pandas as pd

if "omikuji" not in st.session_state:
   st.session_states.omikuji = []

st.title("おみくじ")

if st.button("おみくじをひく"):
    result = random.randint(1, 6)
    st.session_state.omikuji.append((result))
    if result == 1:
       st.write(f"あなたの運勢は「大吉」です")
    elif result == 2:
       st.write(f"あなたの運勢は「中吉」です")
    elif result == 3:
       st.write(f"あなたの運勢は「小吉」です")
    elif result == 4:
       st.write(f"あなたの運勢は「末吉」です")
    elif result == 5:
       st.write(f"あなたの運勢は「凶」です")
    else:
       st.write(f"あなたの運勢は「大凶」です")

df = pd.DataFrame(st.session_state.omikuji, colums=["おみくじ番号"])
st.dateframe(df)
st.write("おみくじをひいた回数", len(st.session_state.omikuji))