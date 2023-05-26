import pandas as pd

# Read the original CSV file
df = pd.read_csv("daily_sales_data_2.csv")

# Filter and select rows with 'pink morsel' product
filtered_df = df[df["product"] == "pink morsel"]

# Create the 'sales' column by multiplying 'price' and 'quantity'
filtered_df["sales"] = (
    filtered_df["price"].str.replace("$", "").astype(float) * filtered_df["quantity"]
)

# Select only the desired columns
modified_df = filtered_df[["product", "sales", "date", "region"]]

# Write the modified DataFrame to a new CSV file
modified_df.to_csv("modified_sales_data_2.csv", index=False)
