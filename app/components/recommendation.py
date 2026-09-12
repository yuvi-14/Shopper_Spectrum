import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
from pathlib import Path
from io import BytesIO

# ---------------------------------------
# Paths
# ---------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "models"

# ---------------------------------------
# Load Models
# ---------------------------------------

@st.cache_resource
def load_model():

    products = joblib.load(MODEL_DIR / "products.pkl")
    similarity = joblib.load(MODEL_DIR / "similarity.pkl")

    return products, similarity


# ---------------------------------------
# Plotly Theme
# ---------------------------------------

def plot_theme():

    return (
        "plotly_dark"
        if st.get_option("theme.base") == "dark"
        else "plotly_white"
    )


# ---------------------------------------
# Recommendation Engine
# ---------------------------------------

def recommend(product_name, top_n=5):

    products, similarity = load_model()

    if product_name not in products:
        return None

    index = products.index(product_name)

    distances = similarity.iloc[index]

    similar_items = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:top_n + 1]

    recommended_products = []
    similarity_scores = []

    for item in similar_items:

        recommended_products.append(products[item[0]])
        similarity_scores.append(round(item[1] * 100, 2))

    result = pd.DataFrame({
        "Product": recommended_products,
        "Similarity (%)": similarity_scores
    })

    return result

# ---------------------------------------
# Product Recommendation Page
# ---------------------------------------

def recommendation_page():

    st.subheader("🛒 Product Recommendation System")

    products, similarity = load_model()

    st.caption(f"📦 Total Products : {len(products)}")

    selected = st.selectbox(
        "Select Product",
        products
    )

    num = st.slider(
        "⭐ Number of Recommendations",
        min_value=3,
        max_value=10,
        value=5
    )

    button = st.button(
        "🚀 Get Recommendations",
        type="primary",
        use_container_width=True
    )

    if button:

        if not selected:
            st.warning("Please Select Product")

            st.stop()

        with st.spinner("Finding Similar Products..."):

            result = recommend(selected, num)

        if result is None:
            st.error("Product Not Found")

            return

        st.toast("Recommendations Ready! 🎉")

        # -----------------------------
        # Metrics
        # -----------------------------

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Products Recommended",
            len(result)
        )

        c2.metric(
            "Best Similarity",
            f"{result.iloc[0]['Similarity (%)']}%"
        )

        c3.metric(
            "Average Similarity",
            f"{result['Similarity (%)'].mean():.2f}%"
        )

        st.divider()

        # -----------------------------
        # Selected Product
        # -----------------------------

        st.markdown("## 📦 Selected Product")

        st.info(selected)

        # -----------------------------
        # Best Match
        # -----------------------------

        top = result.iloc[0]

        st.success(f"""
    ### 🏆 Best Match

    **{top['Product']}**

    Similarity : **{top['Similarity (%)']}%**
    """)

        st.divider()

        # -----------------------------
        # Similar Products
        # -----------------------------

        st.subheader("⭐ Similar Products")

        for _, row in result.iterrows():
            st.write(f"**{row['Product']}**")

            st.progress(row["Similarity (%)"] / 100)

            st.caption(f"{row['Similarity (%)']}% Match")

        st.divider()

        # Show Table

        result.insert(
            0,
            "Rank",
            range(1, len(result) + 1)
        )

        st.dataframe(
            result,
            use_container_width=True
        )

        # ---------------------------------------
        # Recommendation Chart
        # ---------------------------------------

        st.subheader("📊 Recommendation Score")

        fig = px.bar(
            result,
            x="Similarity (%)",
            y="Product",
            orientation="h",
            text="Similarity (%)",
            color="Similarity (%)",
            color_continuous_scale="Blues",
            template=plot_theme(),
            title="Top Similar Products"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            height=550,
            xaxis_title="Similarity %",
            yaxis_title="Products",
            yaxis=dict(categoryorder="total ascending"),
            coloraxis_showscale=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # ---------------------------------------
        # Business Insights
        # ---------------------------------------

        st.subheader("💡 Business Insights")

        col1, col2 = st.columns(2)

        with col1:

            st.success(f"""
        ### 📈 Cross Selling

        ✅ Promote **{result.iloc[0]['Product']}**

        ✅ Bundle with **{selected}**

        ✅ Show on Product Detail Page

        ✅ Recommend during Checkout
        """)

        with col2:

            st.info(f"""
        ### 🎯 Marketing Strategy

        ✔ Email Campaign

        ✔ Festival Offer

        ✔ Combo Discount

        ✔ Personalized Recommendation
        """)

        st.divider()

        # ---------------------------------------
        # Download CSV
        # ---------------------------------------

        csv = result.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download CSV",
            data=csv,
            file_name="recommendation.csv",
            mime="text/csv",
            use_container_width=True
        )

        # ---------------------------------------
        # Download Excel
        # ---------------------------------------

        output = BytesIO()

        with pd.ExcelWriter(
                output,
                engine="openpyxl"
        ) as writer:

            result.to_excel(
                writer,
                index=False
            )

        st.download_button(
            "📊 Download Excel",
            data=output.getvalue(),
            file_name="recommendation.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )