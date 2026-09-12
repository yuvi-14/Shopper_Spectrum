from pathlib import Path

# ---------------------------------------------------
# Project Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

DATASET_DIR = BASE_DIR / "dataset"
MODEL_DIR = BASE_DIR / "models"
IMAGE_DIR = BASE_DIR / "images"
ASSET_DIR = BASE_DIR / "app" / "assets"

# ---------------------------------------------------
# Dataset Files
# ---------------------------------------------------

CLEAN_DATA = DATASET_DIR / "cleaned_online_retail.csv"
RFM_DATA = DATASET_DIR / "rfm_dataset.csv"
SEGMENT_DATA = DATASET_DIR / "customer_segments.csv"

# ---------------------------------------------------
# Model Files
# ---------------------------------------------------

KMEANS_MODEL = MODEL_DIR / "kmeans.pkl"
SCALER_MODEL = MODEL_DIR / "scaler.pkl"

TFIDF_MODEL = MODEL_DIR / "tfidf.pkl"
COSINE_MODEL = MODEL_DIR / "cosine_similarity.pkl"

# ---------------------------------------------------
# Images
# ---------------------------------------------------

EDA_IMAGES = IMAGE_DIR / "eda"
CLUSTER_IMAGES = IMAGE_DIR / "clustering"
RFM_IMAGES = IMAGE_DIR / "rfm_analysis"

# ---------------------------------------------------
# App Information
# ---------------------------------------------------

APP_NAME = "Shopper Spectrum"

APP_VERSION = "1.0"

AUTHOR = "Yuvraj Verma"