import random
import streamlit as st
import pandas as pd

if "dices" not in st.session_state:
    st.session_state.dices = []

st.title("おみくじ")

if st.button("おみくじを引く"):
    suuji = random.randint(1, 100)
    if suuji %  59 == 0:
        st.write(f"{suuji}番 凶後大吉です。")
    elif suuji % 53 == 0:
        st.write(f"{suuji}番 凶後吉です。")
    elif suuji % 47 == 0:
        st.write(f"{suuji}番 小吉後吉です。")
    elif suuji % 43 == 0:
        st.write(f"{suuji}番 吉凶相央です。")
    elif suuji % 41 == 0:
        st.write(f"{suuji}番 吉凶相半です。")
    elif suuji % 37 == 0:
        st.write(f"{suuji}番 吉凶相交末吉です。")
    elif suuji % 31 == 0:
        st.write(f"{suuji}番 吉凶不分末吉です。")
    elif suuji % 29 == 0:
        st.write(f"{suuji}番 末吉です。")
    elif suuji % 23 == 0:
        st.write(f"{suuji}番 後凶です。")
    elif suuji % 19 == 0:
        st.write(f"{suuji}番 小吉です。")
    elif suuji % 17 == 0:
        st.write(f"{suuji}番 中吉です。")
    elif suuji % 13 == 0:
        st.write(f"{suuji}番 吉です。")
    elif suuji % 11 == 0:
        st.write(f"{suuji}番 吉凶末分末大吉です。")
    elif suuji % 7 == 0:
        st.write(f"{suuji}番 末大吉です。")
    elif suuji % 5 == 0:
        st.write(f"{suuji}番 向大吉です。")
    elif suuji % 3 == 0:
        st.write(f"{suuji}番 大吉です。")
    else: st.write(f"{suuji}番 大大吉です。")