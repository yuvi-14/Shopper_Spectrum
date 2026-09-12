import streamlit as st
import pandas as pd

from config import (
    CLEAN_DATA,
    SEGMENT_DATA,
)

from utils import load_css

from components.cards import show_dashboard_cards
from components.filters import sidebar_filters
from components.header import page_header
from components.footer import footer

from components.charts import (
    revenue_trend,
    monthly_revenue,
    top_products,
    top_customers,
    revenue_country,
    world_map,
    revenue_distribution,
    quantity_distribution,
    segment_chart,
)

from components.insights import business_insights

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Business Dashboard",
    page_icon="📊",
    layout="wide",
)

# =====================================================
# LOAD CSS
# =====================================================

load_css()

# =====================================================
# HEADER
# =====================================================

page_header(
    "📊 Business Dashboard",
    "Customer Segmentation & Product Recommendation"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data(show_spinner=False)
def load_data():

    df = pd.read_csv(CLEAN_DATA)

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    df["Year"] = df["InvoiceDate"].dt.year

    df["Month"] = df["InvoiceDate"].dt.strftime("%B")

    return df


@st.cache_data(show_spinner=False)
def load_segment():

    return pd.read_csv(SEGMENT_DATA)


with st.spinner("Loading Dashboard..."):

    df = load_data()

    segment_df = load_segment()

# =====================================================
# SIDEBAR FILTERS
# =====================================================

filtered_df = sidebar_filters(df)

# =====================================================
# EMPTY DATA CHECK
# =====================================================

if filtered_df.empty:

    st.warning("No data available for selected filters.")

    st.stop()

# =====================================================
# KPI VALUES
# =====================================================

revenue = filtered_df["TotalAmount"].sum()

customers = filtered_df["CustomerID"].nunique()

products = filtered_df["Description"].nunique()

transactions = filtered_df["InvoiceNo"].nunique()

countries = filtered_df["Country"].nunique()

avg_order = (
    revenue / transactions
    if transactions
    else 0
)

# =====================================================
# KPI SECTION
# =====================================================

show_dashboard_cards(
    revenue=revenue,
    customers=customers,
    products=products,
    transactions=transactions,
    avg_order=avg_order,
    countries=countries,
)

st.divider()

# =====================================================
# DASHBOARD OVERVIEW
# =====================================================

st.markdown(
    """
### 📈 Dashboard Overview

Explore sales performance, customer behavior,
country-wise revenue, customer segmentation,
and product analytics using interactive charts.
"""
)

st.divider()

# =====================================================
# ROW 1
# Revenue Trend | Monthly Revenue
# =====================================================
revenue_trend(filtered_df)

st.divider()

# =====================================================
# ROW 2
# Monthly Revenue
# =====================================================
monthly_revenue(filtered_df)

st.divider()

# =====================================================
# ROW 3
# Top Products | Top Customers
# =====================================================

col1, col2 = st.columns(2)

with col1:
    top_products(filtered_df)

with col2:
    top_customers(filtered_df)

st.divider()

# =====================================================
# ROW 4
# Country Revenue | World Map
# =====================================================

col3, col4 = st.columns(2)

with col3:
    revenue_country(filtered_df)

with col4:
    world_map(filtered_df)

st.divider()

# =====================================================
# ROW 5
# Revenue Distribution | Quantity Distribution
# =====================================================

col5, col6 = st.columns(2)

with col5:
    revenue_distribution(filtered_df)

with col6:
    quantity_distribution(filtered_df)

st.divider()

# =====================================================
# ROW 6
# Customer Segment
# =====================================================

st.subheader("👥 Customer Segmentation Overview")

segment_chart(segment_df)

st.divider()

# =====================================================
# BUSINESS INSIGHTS
# =====================================================

st.markdown("## 💡 Business Insights")

business_insights(filtered_df)

st.divider()

# =====================================================
# DATA PREVIEW
# =====================================================

with st.expander("📄 View Filtered Dataset", expanded=False):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=400,
    )

st.divider()

# =====================================================
# DOWNLOAD SECTION
# =====================================================

st.markdown("## 📥 Export Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

excel = filtered_df.to_excel("filtered_data.xlsx", index=False)

col1, col2 = st.columns(2)

with col1:

    st.download_button(
        "📄 Download CSV",
        data=csv,
        file_name="filtered_dataset.csv",
        mime="text/csv",
        use_container_width=True,
    )

with col2:

    from io import BytesIO

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        filtered_df.to_excel(
            writer,
            index=False,
            sheet_name="Dashboard"
        )

    st.download_button(
        "📊 Download Excel",
        data=output.getvalue(),
        file_name="filtered_dataset.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True,
    )

st.divider()

# =====================================================
# QUICK SUMMARY
# =====================================================

st.markdown("## 📋 Dashboard Summary")

summary = pd.DataFrame(
    {
        "Metric": [
            "Revenue",
            "Customers",
            "Transactions",
            "Products",
            "Countries",
            "Average Order Value",
        ],
        "Value": [
            f"${revenue:,.2f}",
            customers,
            transactions,
            products,
            countries,
            f"${avg_order:,.2f}",
        ],
    }
)

st.dataframe(summary, use_container_width=True)

st.divider()

# =====================================================
# FOOTER
# =====================================================

footer()