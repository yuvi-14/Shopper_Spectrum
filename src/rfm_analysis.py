"""
==========================================================
Shopper Spectrum
Customer Segmentation & Product Recommendation
----------------------------------------------------------
File : rfm_analysis.py
Purpose : RFM Feature Engineering
==========================================================
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.preprocessing import StandardScaler


class RFMAnalysis:

    def __init__(self, df):
        self.df = df.copy()
        self.rfm = None
        self.scaled_rfm = None

        self.output_dir = "images/rfm_analysis"
        os.makedirs(self.output_dir, exist_ok=True)

    # -------------------------------------------------

    def create_rfm(self):

        snapshot_date = self.df["InvoiceDate"].max() + pd.Timedelta(days=1)

        self.rfm = self.df.groupby("CustomerID").agg({

            "InvoiceDate": lambda x: (snapshot_date - x.max()).days,

            "InvoiceNo": "nunique",

            "TotalAmount": "sum"

        })

        self.rfm.columns = [

            "Recency",
            "Frequency",
            "Monetary"

        ]

        print("=" * 60)
        print("RFM Table Created Successfully")
        print("=" * 60)

        print(self.rfm.head())

        return self.rfm

    # -------------------------------------------------

    def summary(self):

        print("\nRFM Summary")

        print(self.rfm.describe())

    # -------------------------------------------------

    def distributions(self):

        fig, ax = plt.subplots(1, 3, figsize=(18, 5))

        sns.histplot(self.rfm["Recency"], bins=30, kde=True, ax=ax[0])
        ax[0].set_title("Recency Distribution")

        sns.histplot(self.rfm["Frequency"], bins=30, kde=True, ax=ax[1])
        ax[1].set_title("Frequency Distribution")

        sns.histplot(self.rfm["Monetary"], bins=30, kde=True, ax=ax[2])
        ax[2].set_title("Monetary Distribution")

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "Distribution.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # -------------------------------------------------

    def scale_features(self):

        scaler = StandardScaler()

        self.scaled_rfm = scaler.fit_transform(self.rfm)

        joblib.dump(
            scaler,
            "models/scaler.pkl"
        )

        print("\nScaler Saved Successfully")

        return self.scaled_rfm

    # -------------------------------------------------

    def save_dataset(self):

        self.rfm.to_csv(
            "dataset/rfm_dataset.csv"
        )

        print("\nRFM Dataset Saved")

    # -------------------------------------------------

    def business_insights(self):

        print("\nBUSINESS INSIGHTS")
        print("=" * 60)

        print("""
1. Lower Recency = Recently Active Customers

2. Higher Frequency = Loyal Customers

3. Higher Monetary = High Revenue Customers

4. RFM dataset is now ready for clustering.
        """)

    # -------------------------------------------------

    def run(self):

        self.create_rfm()

        self.summary()

        self.distributions()

        self.scale_features()

        self.save_dataset()

        self.business_insights()

        print("=" * 60)
        print("RFM_Analysis graph saved successfully.")
        print(f"Location: {self.output_dir}")
        print("=" * 60)

        return self.rfm, self.scaled_rfm