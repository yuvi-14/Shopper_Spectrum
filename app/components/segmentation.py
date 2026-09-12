import streamlit as st
import pandas as pd
import plotly.express as px
from jupyter_client.session import default_secure

from components.cards import show_customers_segmentation_cards

# =====================================================
# Plotly Theme
# =====================================================
def template():

    return (
        "plotly_dark"
        if st.get_option("theme.base")=="dark"
        else "plotly_white"
    )

def segmentation_cards(df):
    # =====================================================
    # KPI VALUES
    # =====================================================
    customers = df["CustomerID"].nunique()
    segments = df["Cluster"].nunique()
    avg = df["Monetary"].mean()
    recency = df["Recency"].mean()

    # =====================================================
    # KPI Cards
    # =====================================================
    show_customers_segmentation_cards(
        customers,
        segments,
        avg,
        recency,
    )

# =====================================================
# Cluster Distribution
# =====================================================
def cluster_distribution(df):

    chart=(
        df["Cluster"]
        .value_counts()
        .reset_index()
    )

    chart.columns=["Cluster","Customers"]

    fig=px.bar(
        chart,
        x="Cluster",
        y="Customers",
        color="Customers",
        title="Cluster Distribution",
        template=template()
    )

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# Scatter Plot
# =====================================================
def cluster_scatter(df):

    fig=px.scatter(
        df,
        x="Recency",
        y="Monetary",
        color="Cluster",
        size="Frequency",
        title="Customer Segments",
        template=template()
    )

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# Pie Chart
# =====================================================
def cluster_pie(df):

    chart=(
        df["Cluster"]
        .value_counts()
        .reset_index()
    )

    chart.columns=["Cluster","Customers"]

    fig=px.pie(
        chart,
        names="Cluster",
        values="Customers",
        hole=.55,
        title="Customer Segment Share",
        template=template()
    )

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# Business Recommendations
# =====================================================
def recommendations(df):

    strategies = {
        0: {
            "title": "💎 High Value Customers",
            "color": "#1f4d2e",
            "items": [
                "VIP Offers",
                "Loyalty Rewards",
                "Exclusive Membership",
                "Early Product Launch",
                "Personalized Recommendations"
            ]
        },
        1: {
            "title": "👥 Regular Customers",
            "color": "#1e3a5f",
            "items": [
                "Email Marketing",
                "Cross-selling",
                "Reward Points",
                "Product Bundles",
                "Seasonal Promotions"
            ]
        },
        2: {
            "title": "🛍️ Occasional Customers",
            "color": "#5a5a14",
            "items": [
                "Discount Coupons",
                "Festival Offers",
                "Personalized Deals",
                "Product Recommendations",
                "Limited-Time Promotions"
            ]
        },
        3: {
            "title": "⚠️ At Risk Customers",
            "color": "#5b2323",
            "items": [
                "Win-back Campaign",
                "Personalized Email",
                "Special Discount",
                "Reactivation Offers",
                "Customer Feedback Survey"
            ]
        }
    }

    st.subheader("💡 Business Strategy")

    clusters = sorted(df["Cluster"].unique())

    cols = st.columns(2)

    for i, cluster in enumerate(clusters):

        strategy = strategies.get(cluster)

        if strategy:
            items = "<br>".join(
                f"✅ {item}" for item in strategy["items"]
            )

            card = f"""
            <div style="
                background:{strategy['color']};
                padding:20px;
                border-radius:12px;
                min-height:250px;
                color:white;
                margin-bottom:25px;
            ">

            <h3>{strategy['title']}</h3>

            <p style="font-size:17px; line-height:2; margin-top:15px;">
            {items}
            </p>

            </div>
            """

            with cols[i % 2]:
                st.markdown(card, unsafe_allow_html=True)

def cluster_comparison(df):

    st.subheader("📊 Cluster Overview")

    summary = (
        df.groupby("Cluster")
        .agg({
            "Recency": "mean",
            "Frequency": "mean",
            "Monetary": "mean"
        })
        .round(2)
        .reset_index()
    )

    summary.columns = [
        "Cluster",
        "Avg Recency",
        "Avg Frequency",
        "Avg Monetary"
    ]

    st.dataframe(summary, use_container_width=True)