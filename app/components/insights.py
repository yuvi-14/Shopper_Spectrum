import streamlit as st


def business_insights(df):

    st.subheader("📈 Business Insights")

    revenue = df["TotalAmount"].sum()

    customers = df["CustomerID"].nunique()

    orders = df["InvoiceNo"].nunique()

    avg_order = revenue / orders if orders else 0

    top_country = (
        df.groupby("Country")["TotalAmount"]
        .sum()
        .idxmax()
    )

    top_customer = (
        df.groupby("CustomerID")["TotalAmount"]
        .sum()
        .idxmax()
    )

    top_product = (
        df.groupby("Description")["TotalAmount"]
        .sum()
        .idxmax()
    )

    best_month = (
        df.groupby("Month")["TotalAmount"]
        .sum()
        .idxmax()
    )

    c1, c2 = st.columns(2)

    with c1:

        st.info(f"""
### 🌍 Geography

**Top Country**

{top_country}

**Total Customers**

{customers:,}

**Orders**

{orders:,}
""")

    with c2:

        st.success(f"""
### 💰 Sales

**Revenue**

${revenue:,.2f}

**Average Order**

${avg_order:,.2f}

**Best Month**

{best_month}
""")

    st.warning(f"""
### 🏆 Top Performers

👤 **Top Customer:** {top_customer}

🛒 **Best Product:** {top_product}
""")