import pandas as pd
from utils import data_preprocessing
from models import UserBasedCF, ItemBasedCF

# Load data
data = pd.read_csv("data.csv")

# Preprocess data
user_data, product_data, user_item_interactions = data_preprocessing(data)

# Choose and train models
model_cf_user = UserBasedCF(user_data, user_item_interactions)
model_cf_item = ItemBasedCF(product_data, user_item_interactions)

# Generate recommendations
user_id = 123  # Replace with specific user ID
user_recommendations_cf_user = model_cf_user.recommend(user_id)
user_recommendations_cf_item = model_cf_item.recommend(user_id)

# Print recommendations
print("User-based CF recommendations:", user_recommendations_cf_user)
print("Item-based CF recommendations:", user_recommendations_cf_item)
