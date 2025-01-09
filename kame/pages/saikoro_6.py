import random
import streamlit as st

st.title("おみくじ")

if st.button("おみくじをひく"):
    result = random.randint(1, 6)
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