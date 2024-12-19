import random
import streamlit as st

st.title("おみくじ")

if st.button("おみくじをひく"):
    result = random.randint(1, 6)
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