"""
==========================================================
Shopper Spectrum
Customer Segmentation & Product Recommendation
----------------------------------------------------------
File : data_preprocessing.py
Purpose : Clean Dataset & Feature Engineering
==========================================================
"""

import pandas as pd


class DataPreprocessing:

    def __init__(self, df):
        self.df = df.copy()

    def remove_missing_customer(self):
        """Remove rows where CustomerID is missing"""
        before = len(self.df)

        self.df = self.df.dropna(subset=["CustomerID"])

        after = len(self.df)

        print(f"Removed Missing CustomerID Rows : {before-after}")

    def remove_cancelled_orders(self):
        """Remove invoices starting with C"""

        before = len(self.df)

        self.df = self.df[
            ~self.df["InvoiceNo"].astype(str).str.startswith("C")
        ]

        after = len(self.df)

        print(f"Removed Cancelled Orders : {before-after}")

    def remove_invalid_quantity(self):
        """Remove Quantity <= 0"""

        before = len(self.df)

        self.df = self.df[self.df["Quantity"] > 0]

        after = len(self.df)

        print(f"Removed Invalid Quantity : {before-after}")

    def remove_invalid_price(self):
        """Remove UnitPrice <= 0"""

        before = len(self.df)

        self.df = self.df[self.df["UnitPrice"] > 0]

        after = len(self.df)

        print(f"Removed Invalid UnitPrice : {before-after}")

    def remove_duplicates(self):
        """Remove duplicate rows"""

        before = len(self.df)

        self.df = self.df.drop_duplicates()

        after = len(self.df)

        print(f"Removed Duplicate Rows : {before-after}")

    def convert_datetime(self):
        """Convert InvoiceDate into datetime"""

        self.df["InvoiceDate"] = pd.to_datetime(
            self.df["InvoiceDate"]
        )

        print("InvoiceDate Converted Successfully")

    def create_total_amount(self):
        """Create TotalAmount Feature"""

        self.df["TotalAmount"] = (
            self.df["Quantity"] *
            self.df["UnitPrice"]
        )

        print("TotalAmount Feature Created")

    def final_shape(self):

        print("\nFinal Dataset Shape")

        print(self.df.shape)

    def save_dataset(
            self,
            output_path="dataset/cleaned_online_retail.csv"
    ):

        self.df.to_csv(
            output_path,
            index=False
        )

        print(f"\nClean Dataset Saved Successfully\n{output_path}")

    def preprocess(self):
        """Run complete preprocessing"""

        print("=" * 60)
        print("STARTING DATA PREPROCESSING")
        print("=" * 60)

        self.remove_missing_customer()

        self.remove_cancelled_orders()

        self.remove_invalid_quantity()

        self.remove_invalid_price()

        self.remove_duplicates()

        self.convert_datetime()

        self.create_total_amount()

        self.final_shape()

        self.save_dataset()

        print("=" * 60)
        print("DATA PREPROCESSING COMPLETED")
        print("=" * 60)

        return self.df