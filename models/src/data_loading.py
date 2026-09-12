"""
==========================================================
Shopper Spectrum
Customer Segmentation & Product Recommendation
----------------------------------------------------------
File : data_loading.py
Purpose : Load Dataset and Perform Initial Data Analysis
==========================================================
"""

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")


class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Load CSV Dataset
        """

        try:
            self.df = pd.read_csv(self.file_path, encoding='latin1')

            print("=" * 60)
            print("Dataset Loaded Successfully")
            print("=" * 60)

            return self.df

        except Exception as e:
            print("Error :", e)

    def dataset_shape(self):

        print("\nDataset Shape")
        print("-" * 40)

        print(f"Rows    : {self.df.shape[0]}")
        print(f"Columns : {self.df.shape[1]}")

    def dataset_columns(self):

        print("\nColumns")
        print("-" * 40)

        for col in self.df.columns:
            print(col)

    def data_types(self):

        print("\nData Types")
        print("-" * 40)

        print(self.df.dtypes)

    def dataset_info(self):

        print("\nDataset Information")
        print("-" * 40)

        print(self.df.info())

    def missing_values(self):

        print("\nMissing Values")
        print("-" * 40)

        missing = self.df.isnull().sum()

        missing_percent = round(
            (missing / len(self.df)) * 100,
            2
        )

        missing_df = pd.DataFrame({
            "Missing": missing,
            "Percentage": missing_percent
        })

        print(missing_df)

    def duplicate_records(self):

        print("\nDuplicate Records")
        print("-" * 40)

        print(self.df.duplicated().sum())

    def summary_statistics(self):

        print("\nSummary Statistics")
        print("-" * 40)

        print(self.df.describe())

    def categorical_summary(self):

        print("\nCategorical Summary")
        print("-" * 40)

        print(self.df.describe(include='object'))

    def unique_values(self):

        print("\nUnique Values")
        print("-" * 40)

        for col in self.df.columns:
            print(f"{col:15} : {self.df[col].nunique()}")

    def memory_usage(self):

        print("\nMemory Usage")
        print("-" * 40)

        memory = self.df.memory_usage(deep=True).sum() / 1024 ** 2

        print(f"{memory:.2f} MB")

    def negative_values(self):

        print("\nNegative Values")
        print("-" * 40)

        print("Negative Quantity :",
              (self.df["Quantity"] < 0).sum())

        print("Negative Price :",
              (self.df["UnitPrice"] < 0).sum())

    def cancelled_orders(self):

        print("\nCancelled Orders")
        print("-" * 40)

        cancelled = self.df["InvoiceNo"].astype(str).str.startswith("C").sum()

        print(cancelled)

    def customerid_missing(self):

        print("\nMissing CustomerID")
        print("-" * 40)

        print(self.df["CustomerID"].isnull().sum())

    def preview(self):

        print("\nFirst Five Rows")
        print("-" * 40)

        print(self.df.head())

        print("\nLast Five Rows")
        print("-" * 40)

        print(self.df.tail())

    def full_report(self):

        self.preview()

        self.dataset_shape()

        self.dataset_columns()

        self.data_types()

        self.dataset_info()

        self.missing_values()

        self.duplicate_records()

        self.summary_statistics()

        self.categorical_summary()

        self.unique_values()

        self.memory_usage()

        self.negative_values()

        self.cancelled_orders()

        self.customerid_missing()

        print("\nInitial Dataset Analysis Completed")