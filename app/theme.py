import streamlit as st

def load_theme():
    return st.get_option("theme.base")


def is_dark():
    return load_theme() == "dark"

def get_plotly_template():
    theme = st.get_option("theme.base")

    if theme == "dark":
        return "plotly_dark"

    return "plotly_white"