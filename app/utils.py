import streamlit as st
from pathlib import Path


def load_css():

    css = (
        Path(__file__).parent
        / "assets"
        / "style.css"
    )

    with open(css) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )