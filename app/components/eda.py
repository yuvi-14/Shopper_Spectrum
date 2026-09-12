import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
from components.cards import show_eda_cards

# ----------------------------------------
# Dataset
# ----------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATASET = BASE_DIR / "dataset" / "cleaned_online_retail.csv"


@st.cache_data
def load_data():

    df = pd.read_csv(DATASET)

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    df["Year"] = df["InvoiceDate"].dt.year

    df["Month"] = df["InvoiceDate"].dt.strftime("%B")

    df["Weekday"] = df["InvoiceDate"].dt.day_name()

    df["Hour"] = df["InvoiceDate"].dt.hour

    return df

# ----------------------------------------
# Sidebar Filters
# ----------------------------------------

def filters(df):

    st.sidebar.subheader("🔎 Filters")

    country = st.sidebar.multiselect(
        "Country",
        sorted(df["Country"].unique()),
        default=sorted(df["Country"].unique())
    )

    year = st.sidebar.selectbox(
        "Year",
        ["All"] + sorted(df["Year"].astype(str).unique())
    )

    filtered = df[df["Country"].isin(country)]

    if year != "All":

        filtered = filtered[
            filtered["Year"] == int(year)
        ]

    return filtered

# ----------------------------------------
# KPI Cards
# ----------------------------------------

def kpi_cards(df):

    revenue = df["TotalAmount"].sum()

    customers = df["CustomerID"].nunique()

    products = df["Description"].nunique()

    transactions = df["InvoiceNo"].nunique()

    show_eda_cards(
        revenue,
        customers,
        products,
        transactions
    )


    '''c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "💰 Revenue",
        f"${revenue:,.0f}"
    )

    c2.metric(
        "👥 Customers",
        customers
    )

    c3.metric(
        "🛒 Products",
        products
    )

    c4.metric(
        "🧾 Orders",
        invoices
    )'''

import plotly.express as px

# ----------------------------------------
# Monthly Revenue Trend
# ----------------------------------------

def monthly_sales(df):

    st.subheader("📈 Monthly Revenue Trend")

    monthly = (
        df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalAmount"]
        .sum()
        .reset_index()
    )

    monthly["InvoiceDate"] = monthly["InvoiceDate"].astype(str)

    fig = px.line(
        monthly,
        x="InvoiceDate",
        y="TotalAmount",
        markers=True,
        title="Monthly Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Country-wise Sales
# ----------------------------------------

def country_sales(df):

    sales = (
        df.groupby("Country")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        sales,
        x="TotalAmount",
        y="Country",
        orientation="h",
        title="🌍 Top Revenue Countries"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Top Products
# ----------------------------------------

def top_products(df):

    top = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top,
        x="Quantity",
        y="Description",
        orientation="h",
        title="🛒 Top Selling Products"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Revenue Distribution
# ----------------------------------------

def revenue_distribution(df):

    fig = px.histogram(
        df,
        x="TotalAmount",
        nbins=50,
        title="💰 Revenue Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Quantity Distribution
# ----------------------------------------

def quantity_distribution(df):

    fig = px.histogram(
        df,
        x="Quantity",
        nbins=40,
        title="📦 Quantity Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Correlation Heatmap
# ----------------------------------------

def correlation_heatmap(df):

    st.subheader("🔥 Correlation Heatmap")

    corr = df[[
        "Quantity",
        "UnitPrice",
        "TotalAmount"
    ]].corr()

    fig = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        colorscale="Blues",
        text=corr.round(2).values,
        texttemplate="%{text}"
    ))

    fig.update_layout(height=500)

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Boxplot
# ----------------------------------------

def boxplot(df):

    st.subheader("📦 Revenue Outliers")

    fig = px.box(
        df,
        y="TotalAmount",
        title="Revenue Outliers"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Pareto Analysis
# ----------------------------------------

def pareto_analysis(df):

    st.subheader("📊 Pareto Analysis (80/20 Rule)")

    sales = (
        df.groupby("Description")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    sales["CumPercent"] = (
        sales["TotalAmount"].cumsum()
        / sales["TotalAmount"].sum()
    ) * 100

    fig = px.line(
        sales.head(20),
        x="Description",
        y="CumPercent",
        markers=True
    )

    fig.update_layout(
        xaxis_tickangle=-60,
        yaxis_title="Cumulative %",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Weekday Sales
# ----------------------------------------

def sales_by_weekday(df):

    st.subheader("📅 Sales by Weekday")

    weekday = (
        df.groupby("Weekday")["TotalAmount"]
        .sum()
        .reset_index()
    )

    order = [
        "Monday","Tuesday","Wednesday",
        "Thursday","Friday","Saturday","Sunday"
    ]

    weekday["Weekday"] = pd.Categorical(
        weekday["Weekday"],
        categories=order,
        ordered=True
    )

    weekday = weekday.sort_values("Weekday")

    fig = px.bar(
        weekday,
        x="Weekday",
        y="TotalAmount"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Hourly Sales
# ----------------------------------------

def sales_by_hour(df):

    st.subheader("⏰ Sales by Hour")

    hourly = (
        df.groupby("Hour")["TotalAmount"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        hourly,
        x="Hour",
        y="TotalAmount",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Dataset Preview
# ----------------------------------------

def dataset_preview(df):

    st.subheader("📄 Dataset Preview")

    rows = st.slider(
        "Number of Rows",
        min_value=5,
        max_value=100,
        value=10
    )

    st.dataframe(
        df.head(rows),
        use_container_width=True
    )

# ----------------------------------------
# Business Insights
# ----------------------------------------

def business_insights(df):

    st.subheader("💡 Business Insights")

    best_country = (
        df.groupby("Country")["TotalAmount"]
        .sum()
        .idxmax()
    )

    best_product = (
        df.groupby("Description")["TotalAmount"]
        .sum()
        .idxmax()
    )

    best_month = (
        df.groupby("Month")["TotalAmount"]
        .sum()
        .idxmax()
    )

    best_day = (
        df.groupby("Weekday")["TotalAmount"]
        .sum()
        .idxmax()
    )

    best_hour = (
        df.groupby("Hour")["TotalAmount"]
        .sum()
        .idxmax()
    )

    c1, c2 = st.columns(2)

    with c1:

        st.success(f"""
### 🏆 Top Performance

🌍 Best Country : **{best_country}**

🛒 Best Product :

**{best_product}**

📅 Best Month :

**{best_month}**
""")

    with c2:

        st.info(f"""
### 📈 Customer Behaviour

📆 Peak Day :

**{best_day}**

⏰ Peak Hour :

**{best_hour}:00**

🎯 Recommendation

Increase marketing during peak hours.
""")

# ----------------------------------------
# Download Dataset
# ----------------------------------------

def download_dataset(df):

    st.subheader("📥 Download Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Filtered Dataset",
        data=csv,
        file_name="EDA_Filtered_Dataset.csv",
        mime="text/csv",
        use_container_width=True
    )

