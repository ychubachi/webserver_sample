import random
import streamlit as st
import pandas as pd
import requests
import io

st.title("おみくじ")

if st.button("おみくじをひく"):
    suuji = random.randint(1, 100)
    if suuji % 12 == 11:
        st.write(f"{suuji}番 大凶です。")
    elif suuji % 12 == 10:
        st.write(f"{suuji}番 末凶です。")
    elif suuji % 12 == 9:
        st.write(f"{suuji}番 半凶です。")
    elif suuji % 12 == 8:
        st.write(f"{suuji}番 小凶です。")
    elif suuji % 12 == 7:
        st.write(f"{suuji}番 凶です。")
    elif suuji % 12 == 6:
        st.write(f"{suuji}番 末小吉です。")
    elif suuji % 12 == 5:
        st.write(f"{suuji}番 末吉です。")
    elif suuji % 12 == 4:
        st.write(f"{suuji}番 半吉です。")
    elif suuji % 12 == 3:
        st.write(f"{suuji}番 吉です。")
    elif suuji % 12 == 2:
        st.write(f"{suuji}番 小吉です。")
    elif suuji % 12 == 1:
        st.write(f"{suuji}番 中吉です。")
    else: st.write(f"{suuji}番 大吉です。")

from PIL import Image
url='https://www.omikuji-do.com/wordpress/wp-content/uploads/2021/05/62a17d5dd53e1a946b4ed3038613e256.png'
img = Image.open(io.BytesIO(requests.get(url).content))
st.image(img, use_container_width=True)