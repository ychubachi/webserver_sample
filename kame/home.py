import streamlit as st

# タイトル
st.title("おみくじアプリ")

# オプションを選択するセレクトボックス
options = ["６種類", "12種類", "17種類"]
choice = st.selectbox("サイコロの種類を選択してください", options)

# Sidebar に選択肢を表示
with st.sidebar:
    st.header("現在の選択")
    st.write(f"サイコロの種類: **{choice}**")

# ファイルパスの指定
path1 = 'kame/pages/saikoro_6.py'
path2 = 'kame/pages/saikoro_12.py'
path3 = 'kame/pages/saikoro_17.py'

# 各オプションに応じたロジック
if choice == "６種類":
    try:
        with open(path1, encoding="UTF-8") as f1:
            content1 = f1.read()
            exec(content1)  # ファイルの内容を実行
    except FileNotFoundError:
        st.error(f"{path1} が見つかりません")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
elif choice == "12種類":
    try:
        with open(path2, encoding="UTF-8") as f2:
            content2 = f2.read()
            exec(content2)  # ファイルの内容を実行
    except FileNotFoundError:
        st.error(f"{path2} が見つかりません")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
elif choice == "17種類":
    try:
        with open(path3, encoding="UTF-8") as f3:
            content3 = f3.read()
            exec(content3)  # ファイルの内容を実行
    except FileNotFoundError:
        st.error(f"{path3} が見つかりません")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")

# 設定でサイドバー非表示
st.markdown("""
    <style>
        .css-1v3fvcr { display: none; }
    </style>
""", unsafe_allow_html=True)