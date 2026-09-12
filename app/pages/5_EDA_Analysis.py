import streamlit as st

from utils import load_css
from components.header import page_header
from components.footer import footer

from components.eda import *

st.set_page_config(
    page_title="EDA Analysis",
    page_icon="📈",
    layout="wide"
)

load_css()

page_header(
    "📈 Exploratory Data Analysis",
    "Business Intelligence & Visual Analytics"
)

df = load_data()

filtered = filters(df)

kpi_cards(filtered)

st.divider()

monthly_sales(filtered)

st.divider()

col1, col2 = st.columns(2)

with col1:
    country_sales(filtered)

with col2:
    top_products(filtered)

st.divider()

col3, col4 = st.columns(2)

with col3:
    revenue_distribution(filtered)

with col4:
    quantity_distribution(filtered)

st.divider()

correlation_heatmap(filtered)

st.divider()

col5, col6 = st.columns(2)

with col5:
    boxplot(filtered)

with col6:
    pareto_analysis(filtered)

st.divider()

col7, col8 = st.columns(2)

with col7:
    sales_by_weekday(filtered)

with col8:
    sales_by_hour(filtered)

st.divider()

business_insights(filtered)

st.divider()

dataset_preview(filtered)

st.divider()

download_dataset(filtered)

footer()