import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("火星のスペクトルデータの可視化")

uploaded_file = st.file_uploader("ファイルをアップロードしてください", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.write(df)

    options = st.multiselect(
        '表示するスペクトルを選択してください',
        df.columns[1:],
        default=df.columns[1]
    )

    if options:
        fig, ax = plt.subplots()
        for column in options:
            ax.plot(df.iloc[:, 0], df[column], label=column)

        ax.set_xlabel(df.columns[0])
        ax.set_ylabel("refrectance")
        ax.legend()
        st.pyplot(fig)
    else:
        st.write("少なくとも一つの列を選択してください")
        