"""
==========================================================
Shopper Spectrum
Customer Segmentation & Product Recommendation
----------------------------------------------------------
File : clustering.py
Purpose : Customer Segmentation using KMeans
==========================================================
"""
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


class CustomerClustering:

    def __init__(self, rfm_df, scaled_rfm):

        self.rfm = rfm_df.copy()

        self.scaled = scaled_rfm

        self.model = None

        self.output_dir = "images/clustering"
        os.makedirs(self.output_dir, exist_ok=True)

    # --------------------------------------------------

    def elbow_method(self):

        inertia = []

        K = range(2,11)

        for k in K:

            model = KMeans(
                n_clusters=k,
                random_state=42,
                n_init=10
            )

            model.fit(self.scaled)

            inertia.append(model.inertia_)

        plt.figure(figsize=(8,5))

        plt.plot(K, inertia, marker="o")

        plt.xlabel("Number of Clusters")

        plt.ylabel("Inertia")

        plt.title("Elbow Method")

        plt.grid(True)

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "Elbow_Method.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # --------------------------------------------------

    def silhouette_scores(self):

        print("\nSilhouette Scores")

        print("-"*40)

        for k in range(2,11):

            model = KMeans(
                n_clusters=k,
                random_state=42,
                n_init=10
            )

            labels = model.fit_predict(self.scaled)

            score = silhouette_score(
                self.scaled,
                labels
            )

            print(f"K = {k}  Score = {score:.4f}")

    # --------------------------------------------------

    def train_model(self, n_clusters=4):

        self.model = KMeans(
            n_clusters=n_clusters,
            random_state=42,
            n_init=10
        )

        self.rfm["Cluster"] = self.model.fit_predict(
            self.scaled
        )

        print("\nModel Trained Successfully")

        return self.rfm

    # --------------------------------------------------

    def label_clusters(self):

        labels = {

            0: "High Value",

            1: "Regular",

            2: "Occasional",

            3: "At Risk"

        }

        self.rfm["Segment"] = self.rfm["Cluster"].map(labels)

        print("\nCluster Labels Assigned")

    # --------------------------------------------------

    def cluster_summary(self):

        print("\nCluster Summary")

        print("="*60)

        summary = self.rfm.groupby("Segment")[

            ["Recency","Frequency","Monetary"]

        ].mean()

        print(summary)

    # --------------------------------------------------

    def visualize(self):

        plt.figure(figsize=(10,7))

        sns.scatterplot(

            data=self.rfm,

            x="Recency",

            y="Monetary",

            hue="Segment",

            palette="Set2"

        )

        plt.title("Customer Segments")

        plt.tight_layout()
        plt.savefig(
            os.path.join(self.output_dir, "Customer_Segments.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()

    # --------------------------------------------------

    def save_model(self):

        joblib.dump(

            self.model,

            "models/kmeans.pkl"

        )

        self.rfm.to_csv(

            "dataset/customer_segments.csv"

        )

        print("\nKMeans Model Saved")

        print("Customer Segments Saved")

    # --------------------------------------------------

    def business_insights(self):

        print("\nBUSINESS INSIGHTS")

        print("="*60)

        print("""

High Value
------------
• Premium Customers
• Give Loyalty Rewards

Regular
------------
• Offer Combo Deals

Occasional
------------
• Increase Engagement

At Risk
------------
• Win-back Campaigns

""")

    # --------------------------------------------------

    def run(self):

        self.elbow_method()

        self.silhouette_scores()

        self.train_model()

        self.label_clusters()

        self.cluster_summary()

        self.visualize()

        self.save_model()

        self.business_insights()

        print("=" * 60)
        print("All Clustering graphs saved successfully.")
        print(f"Location: {self.output_dir}")
        print("=" * 60)

        return self.rfm