from src.data_loading import DataLoader
from src.data_preprocessing import DataPreprocessing
from src.eda import EDA
from src.rfm_analysis import RFMAnalysis
from src.clustering import CustomerClustering
from src.recommendation import ProductRecommendation


FILE_PATH = "dataset/online_retail.csv"

# Load Dataset
loader = DataLoader(FILE_PATH)

df = loader.load_data()

loader.full_report()

# -----------------------------
# Data Preprocessing
# -----------------------------

preprocessor = DataPreprocessing(df)

clean_df = preprocessor.preprocess()

# -----------------------------
# Exploratory Data Analysis
# -----------------------------

eda = EDA(clean_df)

eda.run_all()

# ----------------------------------
# RFM Analysis
# ----------------------------------

rfm = RFMAnalysis(clean_df)

rfm_df, scaled_rfm = rfm.run()

# ----------------------------------
# Customer Segmentation
# ----------------------------------

cluster = CustomerClustering(

    rfm_df,

    scaled_rfm

)

customer_segments = cluster.run()

# ----------------------------------
# Product Recommendation
# ----------------------------------

recommendation = ProductRecommendation(clean_df)

recommendation.run()

# Recommendation

recommendation.recommend(

    "WHITE HANGING HEART T-LIGHT HOLDER"

)