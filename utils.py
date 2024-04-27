import pandas as pd

def data_preprocessing(data):
    # Extract user data, product data, and user-item interactions
    user_data = data[["user_id", "demographics"]]
    product_data = data[["product_id", "features", "categories"]]
    user_item_interactions = data[["user_id", "product_id", "interaction_type"]]
    # Preprocess data (e.g., handle missing values, encode categorical features)
    # ...
    return user_data, product_data, user_item_interactions
