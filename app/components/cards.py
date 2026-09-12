import streamlit as st
def metric_card(title, value, icon, delta=None, color="#2563EB"):

    delta_html = ""

    if delta:
        delta_html = f"""
        <div style="font-size:15px;
                    color:#16a34a;
                    margin-top:8px;
                    font-weight:600;">
            ▲ {delta}
        </div>
        """

    st.markdown(
        f"""
<div class="metric-card">

<div style="display:flex;
justify-content:space-between;
align-items:center;">

<div>

<div style="
font-size:15px;
color:#64748B;
font-weight:600;">
{title}
</div>

<div style="
font-size:34px;
font-weight:700;
margin-top:8px;
color:{color};">
{value}
</div>

{delta_html}

</div>

<div style="
font-size:42px;">
{icon}
</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )

def show_home_cards(
        products,
        customers,
        countries,
        transactions,
):
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "Products",
            f"{products:,}",
            "📦"
        )

    with c2:
        metric_card(
            "Customers",
            f"{customers:,}",
            "👥"
        )

    with c3:
        metric_card(
            "Countries",
            f"{countries:,}",
            "🌍"
        )

    with c4:
        metric_card(
            "Transactions",
            f"{transactions:,}",
            "🧾"
        )

def show_dashboard_cards(
        revenue,
        customers,
        products,
        transactions,
        avg_order,
        countries,
):
    c1, c2, c3 = st.columns(3)

    with c1:

        metric_card(
            "Revenue",
            f"${revenue:,.2f}",
            "💰",
        )

    with c2:

        metric_card(
            "Customers",
            f"{customers:,}",
            "👥",
        )

    with c3:

        metric_card(
            "Transactions",
            f"{transactions:,}",
            "🧾",
        )

    c4, c5, c6 = st.columns(3)

    with c4:

        metric_card(
            "Products",
            f"{products:,}",
            "🛒",
        )

    with c5:

        metric_card(
            "Average Order",
            f"${avg_order:,.2f}",
            "📈",
        )

    with c6:

        metric_card(
            "Countries",
            f"{countries:,}",
            "🌍",
        )

def show_customers_segmentation_cards(
    customers,
    segments,
    avg,
    recency,
):
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "Customers",
            f"{customers:,}",
            "👥",
        )

    with c2:
        metric_card(
            "Segments",
            f"{segments}",
            "🎯",
        )

    with c3:
        metric_card(
            "Avg Spend",
            f"${avg:,.2f}",
            "💰",
        )

    with c4:
        metric_card(
            "Avg Recency",
            f"{recency:.0f} Days",
            "📅",
        )

def show_eda_cards(
        revenue,
        customers,
        products,
        transactions,
):
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "Revenue",
            f"${revenue:,.2f}",
            ""
        )

    with c2:
        metric_card(
            "Customers",
            f"{customers:,}",
            "👥"
        )

    with c3:
        metric_card(
            "Products",
            f"{products:,}",
            "🛒"
        )

    with c4:
        metric_card(
            "Transactions",
            f"{transactions:,}",
            "🧾"
        )