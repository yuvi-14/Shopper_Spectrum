import streamlit as st

from utils import load_css
from components.header import page_header
from components.footer import footer

from components.recommendation import recommendation_page

# -----------------------------------

st.set_page_config(
    page_title="Product Recommendation",
    page_icon="🛒",
    layout="wide"
)

load_css()

page_header(
    "🛒 Product Recommendation",
    "Machine Learning Based Similar Product Recommendation"
)

recommendation_page()

footer()