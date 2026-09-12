import streamlit as st
import pandas as pd

from config import SEGMENT_DATA
from utils import load_css
from components.header import page_header
from components.footer import footer

from components.segmentation import (
    segmentation_cards,
    cluster_distribution,
    cluster_scatter,
    cluster_pie,
    recommendations,
    cluster_comparison,
)
from components.predict_segment import predict_customer

# ===========================================
# Page Config
# ===========================================

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👤",
    layout="wide",
)

# ===========================================
# Load CSS
# ===========================================

load_css()

# ===========================================
# Header
# ===========================================

page_header(
    "👤 Customer Segmentation",
    "Machine Learning Based Customer Analysis"
)

# ===========================================
# Load Dataset
# ===========================================

@st.cache_data(show_spinner=False)
def load_data():
    return pd.read_csv(SEGMENT_DATA)

df = load_data()

# ===========================================
# Sidebar Filters
# ===========================================

st.sidebar.header("🎯 Filters")

clusters = sorted(df["Cluster"].unique())

selected_cluster = st.sidebar.multiselect(
    "Select Cluster",
    clusters,
    default=clusters,
)

filtered = df[df["Cluster"].isin(selected_cluster)]

# ===========================================
# Empty Check
# ===========================================

if filtered.empty:
    st.warning("No customer data available.")
    st.stop()

# ===========================================
# Tab
# ===========================================
tab1, tab2 = st.tabs([
    "📊 Dashboard",
    "🤖 Predict Segment"
])

with tab1:

    # ===========================================
    # KPI Cards
    # ===========================================

    segmentation_cards(filtered)

    st.divider()

    # ===========================================
    #   Row 1
    # ===========================================

    col1, col2 = st.columns(2)

    with col1:
        cluster_distribution(filtered)

    with col2:
        cluster_pie(filtered)

    st.divider()

    # ===========================================
    # Row 2
    # ===========================================

    cluster_scatter(filtered)

    st.divider()

    # ===========================================
    # Dataset
    # ===========================================

    st.subheader("📄 Customer Segment Dataset")

    st.dataframe(
        filtered,
        use_container_width=True,
        height=450,
    )

    st.divider()

    # ===========================================
    # Download
    # ===========================================

    csv = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Segmentation Data",
        data=csv,
        file_name="customer_segments.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.divider()

    # ===========================================
    # Cluster Overview
    # ===========================================
    cluster_comparison(filtered)

    st.divider()

    # ===========================================
    # Business Strategy
    # ===========================================

    recommendations(filtered)

with tab2:
    predict_customer()

# ===========================================
# Footer
# ===========================================

footer()