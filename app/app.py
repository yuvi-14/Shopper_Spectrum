import streamlit as st
from utils import load_css
from components.sidebar import sidebar
from components.header import page_header
from components.footer import footer

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------
# Load Custom CSS
# -----------------------------------

load_css()

# -----------------------------------
# Sidebar
# -----------------------------------

sidebar()

# -----------------------------------
# Header
# -----------------------------------

page_header(
    "🛒 Shopper Spectrum",
    "Customer Segmentation & Product Recommendation System"
)

# -----------------------------------
# Welcome Container
# -----------------------------------

st.markdown(
    """
<div class="custom-card">
    <h3>👋 Welcome</h3>
    <p>
        Welcome to <b>Shopper Spectrum</b>.
        This application helps businesses analyze customer purchasing behavior,
        perform customer segmentation using Machine Learning, and generate
        intelligent product recommendations.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------
# Features
# -----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 📊 Dashboard

- Business KPIs
- Sales Trends
- Revenue Analysis
""")

with col2:
    st.success("""
### 👤 Customer Segmentation

- RFM Analysis
- KMeans Clustering
- Business Strategy
""")

with col3:
    st.warning("""
### 🛒 Recommendation

- Similar Products
- Cosine Similarity
- Cross Selling
""")

st.divider()

st.info("⬅️ Select any page from the sidebar to explore the project.")

# -----------------------------------
# Footer
# -----------------------------------

footer()