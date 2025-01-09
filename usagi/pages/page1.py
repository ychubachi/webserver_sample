import streamlit as st
import datetime
from PIL import Image


st.title('ウサギの友人相性占い')

col1, col2=st.columns(2)
with col1:
    image_1 = Image.open('./data/img_4.png')
    st.image(image_1, width=100)

with col2:
     image_2 = Image.open('./data/img_5.png')
     st.image(image_2, width=100)

# 占いロジック
def get_fortune(answers):
    m_s_1, m_s_2, animal_1, animal_2, food_1, food_2= answers
    #3つ同じ
    if  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性90%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性90%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性90%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性90%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性90%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性90%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性90%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性90%"
    #2つ同じ（犬猫以外）
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性85%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性85%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性85%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性85%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性85%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="山" and food_1=="和食" and food_2=='和食':
        return "相性85%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性85%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性85%"
    #2つ同じ（山海以外）
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性83%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性83%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性83%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性83%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性83%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性83%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性83%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性83%"
    #2つ同じ（和洋以外）
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性80%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性80%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性80%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性80%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性80%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性80%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性80%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性80%"
    #1つ同じ（和洋同じ）
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性75%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性75%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='和食':
        return "相性75%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='和食':
        return "相性75%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性75%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性75%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='洋食':
        return "相性75%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='洋食':
        return "相性75%"
    #1つ同じ（山海同じ）
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性71%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性71%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性71%"
    elif  m_s_1=="山" and m_s_2=="山" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性71%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性71%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="犬" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性71%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性71%"
    elif  m_s_1=="海" and m_s_2=="海" and animal_1=="猫" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性71%"
    #1つ同じ（犬猫同じ）
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性68%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性68%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="和食" and food_2=='洋食':
        return "相性68%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="犬" and animal_2=="犬" and food_1=="洋食" and food_2=='和食':
        return "相性68%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性68%"
    elif  m_s_1=="山" and m_s_2=="海" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性68%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="和食" and food_2=='洋食':
        return "相性68%"
    elif  m_s_1=="海" and m_s_2=="山" and animal_1=="猫" and animal_2=="猫" and food_1=="洋食" and food_2=='和食':
        return "相性68%"
    else:
        return "相性50%"

with st.form("fortune_form"):
            q1 = st.radio("あなたは山と海どちらに行くのが好きですか？", ["山", "海"], index=0)
            q2 = st.radio("相手は山と海どちらに行くのが好きですか？", ["山", "海"], index=0)
            q3 = st.radio("あなたは犬と猫のどちらが好きですか？", ["犬", "猫"], index=0)
            q4 = st.radio("相手は犬と猫のどちらが好きですか？", ["犬", "猫"], index=0)
            q5 = st.radio("あなたは和食と洋食のどちらが好きですか？", ["和食", "洋食"], index=0)
            q6 = st.radio("相手は和食と洋食どちらが好きですか？", ["和食", "洋食"], index=0)
        
            
            submit_button = st.form_submit_button("占う")
            cancel_btn = st.form_submit_button('キャンセル')

            if submit_button:
                answers = [q1, q2, q3,q4,q5,q6]
                result = get_fortune(answers)
                st.success(f"結果: {result}")


mail_subscribe=st.checkbox('占い結果をメールアドレスに送る')

