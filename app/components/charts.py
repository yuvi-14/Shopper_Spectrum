import streamlit as st
import plotly.express as px


# ---------------------------------------
# Plotly Theme
# ---------------------------------------

def get_template():
    theme = st.get_option("theme.base")
    return "plotly_dark" if theme == "dark" else "plotly_white"


# ---------------------------------------
# Revenue Trend
# ---------------------------------------

def revenue_trend(df):

    template = get_template()

    daily = (
        df.groupby(df["InvoiceDate"].dt.date)["TotalAmount"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        daily,
        x="InvoiceDate",
        y="TotalAmount",
        markers=True,
        title="📈 Revenue Trend",
        template=template,
    )

    fig.update_layout(height=420)

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------
# Monthly Revenue
# ---------------------------------------

def monthly_revenue(df):

    template = get_template()

    monthly = (
        df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalAmount"]
        .sum()
        .reset_index()
    )

    monthly["InvoiceDate"] = monthly["InvoiceDate"].astype(str)

    fig = px.area(
        monthly,
        x="InvoiceDate",
        y="TotalAmount",
        title="📅 Monthly Revenue",
        template=template,
    )

    fig.update_layout(height=420)

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------
# Top Products
# ---------------------------------------

def top_products(df):

    template = get_template()

    top = (
        df.groupby("Description")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top,
        x="TotalAmount",
        y="Description",
        orientation="h",
        color="TotalAmount",
        title="🛒 Top Revenue Products",
        template=template,
    )

    fig.update_layout(height=450)

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------
# Top Customers
# ---------------------------------------

def top_customers(df):

    template = get_template()

    top = (
        df.groupby("CustomerID")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top,
        x="CustomerID",
        y="TotalAmount",
        color="TotalAmount",
        title="🏆 Top Customers",
        template=template,
    )

    fig.update_layout(height=450)

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------
# Revenue by Country
# ---------------------------------------

def revenue_country(df):

    template = get_template()

    country = (
        df.groupby("Country")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        country,
        x="Country",
        y="TotalAmount",
        color="TotalAmount",
        title="🌍 Revenue by Country",
        template=template,
    )

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------
# World Map
# ---------------------------------------

def world_map(df):

    template = get_template()

    sales = (
        df.groupby("Country", as_index=False)["TotalAmount"]
        .sum()
    )

    fig = px.choropleth(
        sales,
        locations="Country",
        locationmode="country names",
        color="TotalAmount",
        hover_name="Country",
        color_continuous_scale="Blues",
        template=template,
        title="🌎 World Sales Map",
    )

    fig.update_geos(projection_type="natural earth")

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------
# Revenue Distribution
# ---------------------------------------

def revenue_distribution(df):

    template = get_template()

    fig = px.histogram(
        df,
        x="TotalAmount",
        nbins=50,
        title="💰 Revenue Distribution",
        template=template,
    )

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------
# Quantity Distribution
# ---------------------------------------

def quantity_distribution(df):

    template = get_template()

    fig = px.histogram(
        df,
        x="Quantity",
        nbins=40,
        title="📦 Quantity Distribution",
        template=template,
    )

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------
# Customer Segment Donut
# ---------------------------------------

def segment_chart(segment_df):

    template = get_template()

    segment = (
        segment_df["Cluster"]
        .value_counts()
        .reset_index()
    )

    segment.columns = ["Cluster", "Customers"]

    fig = px.pie(
        segment,
        names="Cluster",
        values="Customers",
        hole=.55,
        title="👥 Customer Segments",
        template=template,
    )

    st.plotly_chart(fig, use_container_width=True)