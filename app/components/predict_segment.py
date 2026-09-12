import streamlit as st
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

from config import KMEANS_MODEL, SCALER_MODEL

# -----------------------------
# Load Models
# -----------------------------
@st.cache_resource
def load_models():
    model = joblib.load(KMEANS_MODEL)
    scaler = joblib.load(SCALER_MODEL)
    return model, scaler

def health_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Customer Health Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, 40], 'color': "red"},
                {'range': [40, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "lightgreen"},
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

SEGMENT_INFO = {
    0: {
        "name": "High Value Customer",
        "icon": "👑",
        "color": "green",
        "score": 95,
        "recommendation": [
            "Premium Membership",
            "Exclusive Discounts",
            "Early Product Access",
            "Reward Points"
        ]
    },
    1: {
        "name": "Regular Customer",
        "icon": "🌟",
        "color": "blue",
        "score": 80,
        "recommendation": [
            "Loyalty Rewards",
            "Bundle Offers",
            "Referral Program",
            "Birthday Coupons"
        ]
    },
    2: {
        "name": "Occasional Shopper",
        "icon": "🛍️",
        "color": "orange",
        "score": 60,
        "recommendation": [
            "Discount Coupons",
            "Festival Offers",
            "Email Marketing",
            "Cross Selling"
        ]
    },
    3: {
        "name": "At Risk",
        "icon": "⚠️",
        "color": "red",
        "score": 25,
        "recommendation": [
            "Win Back Campaign",
            "Heavy Discount",
            "Personalized Email",
            "Limited Time Offer"
        ]
    }
}


def predict_customer():

    st.subheader("🤖 Predict Customer Segment")

    col1, col2, col3 = st.columns(3)

    with col1:
        recency = st.number_input(
            "📅 Recency (Days)",
            min_value=0,
            value=30,
            step=1
        )

    with col2:
        frequency = st.number_input(
            "🛒 Frequency",
            min_value=1,
            value=5,
            step=1
        )

    with col3:
        monetary = st.number_input(
            "💰 Monetary",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )

    if st.button("🚀 Predict Segment", use_container_width=True):

        with st.spinner("Predicting Customer Segment..."):

            model, scaler = load_models()

            X = np.array([[recency, frequency, monetary]])

            X = scaler.transform(X)

            cluster = int(model.predict(X)[0])

            info = SEGMENT_INFO.get(cluster)

        st.success("Prediction Completed Successfully!")

        st.markdown("---")

        st.markdown(f"""
## {info['icon']} {info['name']}

**Cluster ID :** {cluster}
""")

        health_gauge(info["score"])

        st.caption(f"Customer Health Score : {info['score']}%")

        st.markdown("### 🎯 Business Recommendations")

        for rec in info["recommendation"]:
            st.write(f"✅ {rec}")

        st.markdown("---")

        history = pd.DataFrame({
            "Recency": [recency],
            "Frequency": [frequency],
            "Monetary": [monetary],
            "Cluster": [cluster],
            "Segment": [info["name"]]
        })

        st.subheader("📄 Prediction Summary")

        st.dataframe(history, use_container_width=True)

        csv = history.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download Prediction",
            csv,
            "prediction.csv",
            "text/csv",
            use_container_width=True
        )