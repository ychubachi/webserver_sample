import streamlit as st

st.title("絶対に大吉が出るアプリ")
##st.write("以下からオプションを選択してください。")

# オプションを選択するセレクトボックス
options = ["６種類", "12種類", "17種類"]
choice = st.selectbox("サイコロの種類を選択してください", options)

# Sidebar に選択肢を表示
with st.sidebar:
    st.header("現在の選択")
    st.write(f"サイコロの種類: **{choice}**")

# 各オプションに応じたロジック
if choice == "６種類":
    # ページのロジックを関数化して直接呼び出す
    st.subheader("６種類のサイコロ")
    st.write("ここでは６種類のサイコロを使います！")
    # ここに６種類のロジックを実装する
elif choice == "12種類":
    st.subheader("12種類のサイコロ")
    st.write("ここでは12種類のサイコロを使います!")
    # ここに12種類のロジックを実装する
elif choice == "17種類":
    st.subheader("17種類のサイコロ")
    st.write("ここでは17種類のサイコロを使います!")
    # ここに17種類のロジックを実装する
