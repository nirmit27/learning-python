import streamlit as st


# Utils ...

def line_break(n):
    for i in range(n):
        st.markdown('''
        <br>
        ''', unsafe_allow_html=True)


def heading(title="Title", sub_title="Sub-title", title_color="white"):
    st.markdown(f'''
    <h2 align="center" style="color:{title_color}">{title}</h2>
    <hr>
    <p align="center" style="font-size: 1.5rem">{sub_title}</p>
    ''', unsafe_allow_html=True)
