import random
import streamlit as st
import pandas as pd


if "dices" not in st.session_state:  # セッションデータの初期化
    st.session_state.dices = []

st.title("おみくじを引くアプリ")

if st.button("おみくじを振る"):
    suuji = random.randint(1, 100)
    if suuji % 37 == 0:
        st.write(f"{suuji}番 大凶です。")
    elif suuji % 31 == 0:
        st.write(f"{suuji}番 末凶です。")
    elif suuji % 29 == 0:
        st.write(f"{suuji}番 半凶です。")
    elif suuji % 23 == 0:
        st.write(f"{suuji}番 小凶です。")
    elif suuji % 19 == 0:
        st.write(f"{suuji}番 凶です。")
    elif suuji % 17 == 0:
        st.write(f"{suuji}番 末小吉です。")
    elif suuji % 13 == 0:
        st.write(f"{suuji}番 末吉です。")
    elif suuji % 11 == 0:
        st.write(f"{suuji}番 半吉です。")
    elif suuji % 7 == 0:
        st.write(f"{suuji}番 吉です。")
    elif suuji % 5 == 0:
        st.write(f"{suuji}番 小吉です。")
    elif suuji % 3 == 0:
        st.write(f"{suuji}番 中吉です。")
    else: st.write(f"{suuji}番 大吉です。")