import streamlit as st

from utils import load_css
from components.header import page_header
from components.footer import footer
from pathlib import Path
import pandas as pd
from components.cards import show_home_cards

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

load_css()

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATASET = BASE_DIR / "dataset" / "cleaned_online_retail.csv"


@st.cache_data
def load_data():

    df = pd.read_csv(DATASET)

    return df


df = load_data()

page_header(
    "🏠 Shopper Spectrum",
    "Customer Segmentation & Product Recommendation System"
)

# -------------------------------------------------------
# Welcome
# -------------------------------------------------------

st.markdown("""
<div class="custom-card">
    <h3>👋 Welcome</h3>
    <p>
        Welcome to <b>Shopper Spectrum</b>,
        an Business Intelligence dashboard
        designed to help businesses analyze customer purchasing behavior,
        perform customer segmentation, and recommend products using
        Machine Learning techniques.
    </p>
</div>
""",
    unsafe_allow_html = True,
)

st.divider()

# -------------------------------------------------------
# Features
# -------------------------------------------------------

st.subheader("🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 👤 Customer Segmentation

- RFM Analysis
- K-Means Clustering
- Customer Groups
- Business Strategy
""")

with col2:
    st.success("""
### 🛒 Product Recommendation

- Similar Products
- Cosine Similarity
- Cross Selling
- Personalized Suggestions
""")

with col3:
    st.warning("""
### 📊 Business Dashboard

- Sales KPIs
- Revenue Analysis
- Interactive Charts
- Business Insights
""")

st.divider()

st.subheader("📌 Project Modules")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("""
🏠 Home

📊 Dashboard
""")

with c2:

    st.info("""
👤 Customer Segmentation

🛒 Product Recommendation
""")

with c3:

    st.warning("""
📈 EDA Analysis

ℹ️ About
""")

st.divider()

# -------------------------------------------------------
# Technologies
# -------------------------------------------------------

st.subheader("🛠 Technologies Used")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
### Programming

- Python
- Pandas
- NumPy
""")

with c2:
    st.info("""
### Visualization

- Streamlit
- Plotly
- Matplotlib
""")

with c3:
    st.warning("""
### Machine Learning

- Scikit-Learn
- K-Means
- RFM Analysis
- Cosine Similarity
""")

st.divider()

# -------------------------------------------------------
# Workflow
# -------------------------------------------------------

st.subheader("🏗 Project Workflow")

st.code("""
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Feature Engineering
   │
   ▼
Customer Segmentation
   │
   ▼
Product Recommendation
   │
   ▼
Business Dashboard
""")

st.divider()

# -------------------------------------------------------
# Project Highlights
# -------------------------------------------------------

st.subheader("✨ Project Highlights")

# -------------------------------------------------------
# Project Statistics
# -------------------------------------------------------

products = df["Description"].nunique()

customers = df["CustomerID"].nunique()

countries = df["Country"].nunique()

transactions = df["InvoiceNo"].nunique()

show_home_cards(
    products,
    customers,
    countries,
    transactions
)

st.divider()

st.success("""
### 🎯 Business Goals

✅ Understand Customer Behaviour

✅ Increase Customer Retention

✅ Improve Product Recommendation

✅ Boost Cross-selling Opportunities

✅ Support Data-driven Decision Making
""")

st.divider()

st.subheader("🚀 Why Shopper Spectrum?")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### Business Benefits

✔ Customer Segmentation

✔ Product Recommendation

✔ Sales Analysis

✔ Customer Retention

✔ Revenue Growth
""")

with col2:

    st.success("""
### AI Features

🤖 Machine Learning

📊 Business Intelligence

📈 Interactive Dashboard

🎯 Cross Selling

🛍 Personalized Recommendation
""")

footer()