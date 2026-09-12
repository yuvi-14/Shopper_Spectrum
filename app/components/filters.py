import streamlit as st


def sidebar_filters(df):
    """
    Sidebar Filters
    """

    st.sidebar.header("🔎 Dashboard Filters")

    # -------------------------
    # Country
    # -------------------------

    countries = sorted(df["Country"].dropna().unique())

    selected_country = st.sidebar.multiselect(
        "🌍 Country",
        countries,
        default=countries,
    )

    filtered = df[df["Country"].isin(selected_country)]

    # -------------------------
    # Year
    # -------------------------

    years = sorted(filtered["Year"].unique())

    years = ["All"] + list(years)

    selected_year = st.sidebar.selectbox(
        "📅 Year",
        years,
    )

    if selected_year != "All":
        filtered = filtered[
            filtered["Year"] == selected_year
        ]

    # -------------------------
    # Month
    # -------------------------

    months = [
        "All",
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]

    month = st.sidebar.selectbox(
        "🗓 Month",
        months,
    )

    if month != "All":
        filtered = filtered[
            filtered["Month"] == month
        ]

    # -------------------------
    # Product Search
    # -------------------------

    product = st.sidebar.text_input(
        "🔍 Search Product"
    )

    if product:

        filtered = filtered[
            filtered["Description"]
            .str.contains(
                product,
                case=False,
                na=False
            )
        ]

    # -------------------------
    # Revenue Slider
    # -------------------------

    min_sales = int(filtered["TotalAmount"].min())
    max_sales = int(filtered["TotalAmount"].max())

    revenue = st.sidebar.slider(
        "💰 Revenue Range",
        min_sales,
        max_sales,
        (min_sales, max_sales),
    )

    filtered = filtered[
        filtered["TotalAmount"].between(
            revenue[0],
            revenue[1]
        )
    ]

    st.sidebar.markdown("---")

    st.sidebar.success(
        f"Showing **{len(filtered):,}** Records"
    )

    return filtered