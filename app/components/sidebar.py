import streamlit as st
from pathlib import Path
from config import APP_VERSION

def sidebar():

    theme = st.get_option("theme.base")

    assets = Path(__file__).resolve().parents[1] / "assets"

    logo = assets / (
        "logo_dark.png"
        if theme == "light"
        else "logo_light.png"
    )

    with st.sidebar:

        # Logo
        if logo.exists():
            st.image(str(logo), use_container_width=True)

        # Title
        st.markdown("## 🛒 Shopper Spectrum")

        st.caption("Customer Segmentation & Product Recommendation")

        st.divider()

        st.success("🚀 Machine Learning Dashboard")

        st.markdown("---")

        st.write(f"Version: {APP_VERSION}")