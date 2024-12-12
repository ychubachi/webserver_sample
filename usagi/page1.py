import streamlit as st
import datetime

with st.form(key='profile_form'): #送信されないとリロードされない
    #テキストボックス
        name = st.text_input('名前')
        #print(name) カーソルずれたら名前ターミナルに表示される
        address = st.text_input('住所')

        #セレクトボックス
        age_category = st.radio(  #selectboxなら上からピロピロ radioは〇で選択
            '年齢層',
            ('子供(18才未満)','大人(18才以上)'))
        
        #複数選択
        hobby = st.multiselect(
            '趣味',
            ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理'))

        #チェックボックス
        mail_subscribe = st.checkbox('メールマガジンを購読する')

        #スライダー
        height = st.slider('身長',min_value=110, max_value=210)

        #日付
        start_date=st.date_input(
            '開始日',
            datetime.date(2024,12,1))
        
        #カラーピッカー
        color = st.color_picker('テーマカラー','#00f900')

        #ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
    #print(f'submit_btn: {submit_btn}') 押されるとターミナルにTrueと表示
    #print(f'cancel_btn: {cancel_btn}')
        if submit_btn:
            st.text(f'ようこそ！{name}さん！{address}に書籍を送りました') #Web画面に表示
            st.text(f'年齢層：{age_category}')
            st.text(f'趣味： {", ".join(hobby)}') #区切り