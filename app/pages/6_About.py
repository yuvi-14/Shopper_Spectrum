import streamlit as st
from utils import load_css
from components.header import page_header
from components.footer import footer
from config import APP_VERSION

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

load_css()

page_header(
    "ℹ️ About Shopper Spectrum",
    "Customer Segmentation & Product Recommendation System"
)

# --------------------------------------------------
# Project Overview
# --------------------------------------------------

st.subheader("📌 Project Overview")

st.markdown("""
Shopper Spectrum is an AI-powered Business Intelligence dashboard developed to analyze customer purchasing behavior.

The system helps organizations:

- 📊 Analyze sales performance
- 👤 Segment customers using Machine Learning
- 🛒 Recommend similar products
- 📈 Generate business insights
- 💼 Support strategic business decisions
""")

st.divider()

# --------------------------------------------------
# Dataset
# --------------------------------------------------

st.subheader("📂 Dataset")

c1, c2 = st.columns(2)

with c1:

    st.info("""
### Dataset Details

• Online Retail Dataset

• UK Based E-commerce

• Customer Transactions

• Invoice Details

• Product Information

• Country Wise Sales
""")

with c2:

    st.success("""
### Dataset Features

✔ Invoice Number

✔ Product Code

✔ Description

✔ Quantity

✔ Unit Price

✔ Customer ID

✔ Country

✔ Total Amount
""")

st.divider()

# --------------------------------------------------
# Machine Learning
# --------------------------------------------------

st.subheader("🤖 Machine Learning Models")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Customer Segmentation

- K-Means Clustering

- RFM Analysis

- Customer Clusters

- Business Strategy
""")

with col2:

    st.markdown("""
### Product Recommendation

- Cosine Similarity

- Recommendation Engine

- Similar Products

- Cross Selling
""")

st.divider()

# --------------------------------------------------
# Technologies
# --------------------------------------------------

st.subheader("🛠 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

tech1.success("""
### Programming

Python

Pandas

NumPy
""")

tech2.info("""
### Visualization

Plotly

Streamlit

Matplotlib
""")

tech3.warning("""
### ML & Tools

Scikit-Learn

Joblib

GitHub
""")

st.divider()

# --------------------------------------------------
# System Workflow
# --------------------------------------------------

st.subheader("🏗 System Workflow")

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
Dashboard & Business Insights
""")

st.divider()

# --------------------------------------------------
# Business Benefits
# --------------------------------------------------

st.subheader("📈 Business Benefits")

st.success("""
✅ Customer Segmentation

✅ Personalized Marketing

✅ Product Recommendation

✅ Cross Selling

✅ Increase Customer Retention

✅ Improve Business Decisions

✅ Revenue Growth
""")

st.divider()

# --------------------------------------------------
# Developer
# --------------------------------------------------

st.subheader("👨‍💻 Developer")

col1, col2 = st.columns([1,2])

with col1:

    st.markdown("### 👤 Yuvraj Verma")

with col2:

    st.info("""
Project:

Shopper Spectrum

Customer Segmentation & Product Recommendation System
""")

st.divider()

# --------------------------------------------------
# Version
# --------------------------------------------------

st.write(f"Version: {APP_VERSION}")

footer()