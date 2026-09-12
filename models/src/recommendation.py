"""
==========================================================
Shopper Spectrum
Customer Segmentation & Product Recommendation
----------------------------------------------------------
File : recommendation.py
Purpose : Item-Based Collaborative Filtering
==========================================================
"""

import pandas as pd
import joblib

from sklearn.metrics.pairwise import cosine_similarity


class ProductRecommendation:

    def __init__(self, df):

        self.df = df.copy()

        self.product_matrix = None

        self.similarity_matrix = None

        self.product_names = None

    # ----------------------------------------------------------

    def create_product_matrix(self):

        print("=" * 60)
        print("Creating Customer-Product Matrix")
        print("=" * 60)

        self.product_matrix = self.df.pivot_table(

            index="CustomerID",

            columns="Description",

            values="Quantity",

            aggfunc="sum",

            fill_value=0

        )

        print("Shape :", self.product_matrix.shape)

    # ----------------------------------------------------------

    def calculate_similarity(self):

        print("\nCalculating Cosine Similarity...")

        similarity = cosine_similarity(

            self.product_matrix.T

        )

        self.similarity_matrix = pd.DataFrame(

            similarity,

            index=self.product_matrix.columns,

            columns=self.product_matrix.columns

        )

        print("Similarity Matrix Created")

    # ----------------------------------------------------------

    def recommend(self, product_name, top_n=5):

        product_name = product_name.upper()

        products = {

            p.upper(): p

            for p in self.similarity_matrix.index

        }

        if product_name not in products:

            print("\nProduct Not Found")

            return []

        actual_name = products[product_name]

        recommendations = (

            self.similarity_matrix[actual_name]

            .sort_values(ascending=False)

            .iloc[1:top_n+1]

        )

        print("\nRecommended Products")

        print("-" * 40)

        for i, product in enumerate(recommendations.index, start=1):

            print(f"{i}. {product}")

        return list(recommendations.index)

    # ----------------------------------------------------------

    def save_model(self):

        joblib.dump(

            self.similarity_matrix,

            "models/similarity.pkl"

        )

        joblib.dump(

            list(self.product_matrix.columns),

            "models/products.pkl"

        )

        print("\nSimilarity Model Saved")

        print("Product List Saved")

    # ----------------------------------------------------------

    def business_insights(self):

        print("\nBUSINESS INSIGHTS")

        print("=" * 60)

        print("""

• Recommend similar products.

• Improve Cross Selling.

• Increase Average Order Value.

• Improve Customer Experience.

• Personalized Shopping.

""")

    # ----------------------------------------------------------

    def run(self):

        self.create_product_matrix()

        self.calculate_similarity()

        self.save_model()

        self.business_insights()