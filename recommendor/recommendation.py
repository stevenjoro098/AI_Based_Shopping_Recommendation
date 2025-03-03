import pandas as pd
from surprise import SVD, Dataset, Reader
import os


def recommend_items(user_id, selected_categories, num_recommendations=5):
    csv_path = os.path.join(os.path.dirname(__file__), 'shopping_trends.csv')
    df = pd.read_csv(csv_path)

    # Ensure correct columns
    df = df[['Customer ID', 'Item Purchased', 'Purchase Amount (USD)']]
    df['Customer ID'] = df['Customer ID'].astype(str)

    # Normalize data for consistency
    df['Item Purchased'] = df['Item Purchased'].astype(str).str.strip().str.lower()
    selected_categories = [str(item).strip().lower() for item in selected_categories]

    # Define reader and load data
    reader = Reader(rating_scale=(df['Purchase Amount (USD)'].min(), df['Purchase Amount (USD)'].max()))
    data = Dataset.load_from_df(df, reader)
    trainset = data.build_full_trainset()
    print(f"Trained:{trainset}")
    # Train model
    model = SVD()
    model.fit(trainset)

    # Fix filtering using set intersection
    filtered_items = list(set(df['Item Purchased']) & set(selected_categories))

    if not filtered_items:
        print("⚠️ No matching items found for the selected categories.")
        return []

    recommendations = []
    for item in filtered_items:
        print(f"Predicting for User: {user_id}, Item: {item}")
        pred = model.predict(str(user_id), item)
        recommendations.append((item, pred.est))

    if not recommendations:
        print("⚠️ No predictions could be made.")
        return []

    # Sort and return top recommendations
    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)[:num_recommendations]
    print(recommendations)
    return [item[0] for item in recommendations]
recommend_items(user_id=1, selected_categories=['Clothing','Footwear'])