import pandas as pd

# Read the modified CSV files
df1 = pd.read_csv("modified_sales_data_0.csv")
df2 = pd.read_csv("modified_sales_data_1.csv")
df3 = pd.read_csv("modified_sales_data_2.csv")

# Concatenate the DataFrames vertically
combined_df = pd.concat([df1, df2, df3])

# Perform additional formatting or manipulation if needed

# Write the final DataFrame to a new CSV file
combined_df.to_csv("combined_sales_data.csv", index=False)
