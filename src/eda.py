"""
==========================================================
Shopper Spectrum
Customer Segmentation & Product Recommendation
----------------------------------------------------------
File : eda.py
Purpose : Exploratory Data Analysis
==========================================================
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

class EDA:

    def __init__(self, df):
        self.df = df

        self.output_dir = "images/eda"
        os.makedirs(self.output_dir, exist_ok=True)

    # -----------------------------------------------------

    def transaction_by_country(self):

        country = self.df.groupby("Country")["InvoiceNo"].count()

        country = country.sort_values(ascending=False).head(10)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=country.values,
            y=country.index
        )

        plt.title("Top 10 Countries by Number of Transactions")
        plt.xlabel("Transactions")
        plt.ylabel("Country")

        plt.tight_layout()
        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "01_transaction_by_country.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -----------------------------------------------------

    def top_products(self):

        products = self.df.groupby("Description")["Quantity"].sum()

        products = products.sort_values(ascending=False).head(10)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=products.values,
            y=products.index
        )

        plt.title("Top 10 Selling Products")

        plt.tight_layout()
        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "02_top_products.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -----------------------------------------------------

    def monthly_sales(self):

        monthly = self.df.copy()

        monthly["Month"] = monthly["InvoiceDate"].dt.to_period("M")

        sales = monthly.groupby("Month")["TotalAmount"].sum()

        plt.figure(figsize=(14,6))

        plt.plot(
            sales.index.astype(str),
            sales.values,
            marker="o"
        )

        plt.xticks(rotation=45)

        plt.title("Monthly Sales Trend")

        plt.tight_layout()

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "03_monthly_sales.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -----------------------------------------------------

    def transaction_distribution(self):

        plt.figure(figsize=(10,6))

        sns.histplot(
            self.df["TotalAmount"],
            bins=50,
            kde=True
        )

        plt.title("Transaction Amount Distribution")

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "04_transaction_distribution.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -----------------------------------------------------

    def top_customers(self):

        customer = self.df.groupby("CustomerID")["TotalAmount"].sum()

        customer = customer.sort_values(
            ascending=False
        ).head(10)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=customer.index.astype(str),
            y=customer.values
        )

        plt.xticks(rotation=45)

        plt.title("Top 10 Customers by Spending")

        plt.tight_layout()

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "05_top_customers.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -----------------------------------------------------

    def top_country_sales(self):

        sales = self.df.groupby("Country")["TotalAmount"].sum()

        sales = sales.sort_values(
            ascending=False
        ).head(10)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=sales.values,
            y=sales.index
        )

        plt.title("Top Countries by Revenue")

        plt.tight_layout()

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "06_country_revenue.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -----------------------------------------------------

    def quantity_distribution(self):

        plt.figure(figsize=(10,6))

        sns.histplot(
            self.df["Quantity"],
            bins=40,
            kde=True
        )

        plt.title("Quantity Distribution")

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "07_quantity_distribution.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -----------------------------------------------------

    def unitprice_distribution(self):

        plt.figure(figsize=(10,6))

        sns.histplot(
            self.df["UnitPrice"],
            bins=40,
            kde=True
        )

        plt.title("Unit Price Distribution")

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "08_unitprice_distribution.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -----------------------------------------------------

    def correlation_heatmap(self):

        numeric = self.df.select_dtypes(include="number")

        plt.figure(figsize=(8,6))

        sns.heatmap(
            numeric.corr(),
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Correlation Heatmap")

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "09_correlation_heatmap.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -----------------------------------------------------

    def business_insights(self):

        print("\nBUSINESS INSIGHTS")
        print("="*60)

        print("""
1. Identify countries generating maximum sales.

2. Understand best-selling products.

3. Find premium customers.

4. Observe monthly sales growth.

5. Detect abnormal quantity purchases.

6. Analyze pricing pattern.

7. Study transaction amount distribution.

8. Prepare features for customer segmentation.
        """)

    # -----------------------------------------------------

    def run_all(self):

        self.transaction_by_country()

        self.top_products()

        self.monthly_sales()

        self.transaction_distribution()

        self.top_customers()

        self.top_country_sales()

        self.quantity_distribution()

        self.unitprice_distribution()

        self.correlation_heatmap()

        self.business_insights()

        print("=" * 60)
        print("All EDA graphs saved successfully.")
        print(f"Location: {self.output_dir}")
        print("=" * 60)