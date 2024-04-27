from sklearn.metrics.pairwise import cosine_similarity

class UserBasedCF:
    def __init__(self, user_data, user_item_interactions):
        # Create user-item interaction matrix
        self.user_item_matrix = user_item_interactions.pivot_table(
            index="user_id", columns="product_id", values="interaction_type", fill_value=0
        )

    def recommend(self, user_id):
        # Calculate user similarity based on cosine similarity
        user_similarities = cosine_similarity(self.user_item_matrix.loc[user_id], self.user_item_matrix.T)
        # Get top N similar users
        top_n_users = user_similarities.argsort()[::-1][:10]  # Replace 10 with desired number of recommendations
        # Recommend items based on similar users' purchases
        recommendations = self.user_item_matrix[top_n_users].dot(self.user_item_matrix).idxmax(axis=1)
        return recommendations[user_id]  # Exclude user's own purchases

class ItemBasedCF:
    def __init__(self, product_data, user_item_interactions):
        # Create item-item similarity matrix
        item_similarities = cosine_similarity(
            product_data[["features"]].fillna(0), dense_output=False
        )
        self.item_similarities = item_similarities.toarray()

    def recommend(self, user_id):
        # Get user's purchased items
        user_purchases = user_item_interactions[user_item_interactions["user_id"] == user_id]["product_id"]
        # Calculate item similarity scores for purchased items
        item_sim_scores = self.item_similarities[user_purchases]
        # Recommend items with highest similarity scores (excluding purchased items)
        recommendations = item_sim_scores.argsort()[::-1][1:]  # Replace 1 with desired number of recommendations
        return recommendations[~recommendations.isin(user_purchases)]
