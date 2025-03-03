import pandas as pd
import os

# Load Data
csv_path = os.path.join(os.path.dirname(__file__), 'shopping_trends.csv')
df = pd.read_csv(csv_path)

# Normalize data
df['Item Purchased'] = df['Item Purchased'].astype(str).str.strip().str.lower()
selected_categories = ['blouse', 'shoes']  # Example categories
selected_categories = [str(item).strip().lower() for item in selected_categories]

# Print debug info
print("Processed Unique Items in Dataset:", list(df['Item Purchased'].unique()))
print("Processed Selected Categories:", list(selected_categories))

# Test manual filtering
sample_item = df['Item Purchased'].iloc[0]  # Pick first item
print(f"Checking if '{sample_item}' is in selected_categories:", sample_item in selected_categories)

# Try filtering with .isin()
filtered_items = df[df['Item Purchased'].isin(selected_categories)]['Item Purchased'].unique()
print("Filtered Items using isin():", filtered_items)

# Try alternative filtering
filtered_items_alt = list(set(df['Item Purchased']) & set(selected_categories))
print("Filtered Items (Alternative Method):", filtered_items_alt)
