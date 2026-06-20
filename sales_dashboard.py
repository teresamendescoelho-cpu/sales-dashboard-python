import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df)

total_sales = df["Sales"].sum()

print("\nTotal Sales:")
print(total_sales)

best_month = df.loc[df["Sales"].idxmax()]

print("\nBest Month:")
print(best_month)
