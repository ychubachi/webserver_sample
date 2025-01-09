import streamlit as st

# ページ設定
st.set_page_config(page_title="アカウント登録", page_icon="📝")

# ヘッダー
st.title("アカウント登録ページ")
st.write("以下のフォームに必要事項を入力してください。")

# 入力フォーム
with st.form("register_form"):
    username = st.text_input("ユーザー名", placeholder="例: johndoe123")
    email = st.text_input("メールアドレス", placeholder="例: example@example.com")
    password = st.text_input("パスワード", type="password", placeholder="セキュアなパスワードを入力してください")
    confirm_password = st.text_input("パスワード確認", type="password", placeholder="もう一度パスワードを入力してください")

    # 利用規約同意チェックボックス
    agree = st.checkbox("利用規約に同意します")

    # フォームの送信ボタン
    submit_button = st.form_submit_button("登録")

# フォーム送信後の処理
if submit_button:
    if not agree:
        st.error("利用規約に同意する必要があります。")
    elif password != confirm_password:
        st.error("パスワードが一致しません。")
    elif username and email and password:
        st.success("アカウント登録が完了しました！")
        # データ保存や次の処理をここに追加
    else:
        st.error("全てのフィールドを正しく入力してください。")