import streamlit as st

st.title("おみくじアプリ")
##st.write("以下からオプションを選択してください。")

# オプションを選択するセレクトボックス
options = ["６種類", "12種類", "17種類"]
choice = st.selectbox("サイコロの種類を選択してください", options)

# Sidebar に選択肢を表示
with st.sidebar:
    st.header("現在の選択")
    st.write(f"サイコロの種類: **{choice}**")

#ファイルパス
path1='./pages/saikoro_6.py'
path2='./pages/saikoro_12.py'
path3='./pages/saikoro_17.py'

# 各オプションに応じたロジック
if choice == "６種類":
    # ページのロジックを関数化して直接呼び出す
    #st.subheader("６種類のサイコロ")
    #st.write("ここでは６種類のサイコロを使います！")
    try:
        with open(path1, encoding="UTF-8") as f1:
            content1 = f1.read()
            exec(content1)
    except FileNotFoundError:
        st.error(f"{path1} が見つかりません")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
    # ここに６種類のロジックを実装する
elif choice == "12種類":
    #st.subheader("12種類のサイコロ")
    #st.write("ここでは12種類のサイコロを使います!")
    try:
        with open(path2, encoding="UTF-8") as f2:
            content2 = f2.read()
            exec(content2)
    except FileNotFoundError:
        st.error(f"{path2} が見つかりません")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
    # ここに12種類のロジックを実装する
elif choice == "17種類":
    #st.subheader("17種類のサイコロ")
    #st.write("ここでは17種類のサイコロを使います!")
    try:
        with open(path3, encoding="UTF-8") as f3:
            content3 = f3.read()
            exec(content3)
    except FileNotFoundError:
        st.error(f"{path3} が見つかりません")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")

    # ここに17種類のロジックを実装する

