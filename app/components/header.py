import streamlit as st


def page_header(title, subtitle=""):

    st.title(title)

    if subtitle:
        st.caption(subtitle)

    st.divider()