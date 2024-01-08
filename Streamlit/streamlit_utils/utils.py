import streamlit as st


# Utils ...

def line_break(n=1):
    for i in range(n):
        st.markdown('''
        <br>
        ''', unsafe_allow_html=True)


def heading(title="Title", sub_title="Sub-title", title_color="white", top=30):
    st.markdown(f'''
    <h2 align="center" style="color:{title_color}; margin-top:-{top}px">{title}</h2>
    <hr>
    <p align="center" style="font-size: 1.4rem;">{sub_title}</p>
    ''', unsafe_allow_html=True)
