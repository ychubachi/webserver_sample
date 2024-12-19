import random
import streamlit as st

st.title("おみくじ")

if st.button("おみくじをひく"):
    result = random.randint(1, 6)
    if result % 37 == 0:
       st.write(f"{result}番 大吉です。")
    elif result % 31== 0:
       st.write(f"{result}番 中吉です。")
    elif result % 29 == 0:
       st.write(f"{result}番 小吉です。")
    elif result % 23 == 0:
       st.write(f"{result}番 末吉です。")
    elif result % 19 ==0:
       st.write(f"{result}番  凶です。")
    else:
       st.write(f"{result}番 大凶 です。")