import pandas as pd

df = pd.read_csv("data/cart_data.csv")

print("First 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

# abandoned column
df["abandoned"] = (df["added_to_cart"] == 1) & (df["purchased"] == 0)

print("\nAbandoned column preview:")
print(df[["user_id", "category", "purchased", "abandoned"]].head())

category_summary = df.groupby("category").agg(
    total_carts=("user_id", "count"),
    abandoned_carts=("abandoned", "sum")
)

category_summary["abandonment_rate"] = (
    category_summary["abandoned_carts"] / category_summary["total_carts"]
) * 100

print("\nCategory-wise abandonment summary:")
print(category_summary)
overall_rate = df["abandoned"].mean() * 100
print("\nOverall cart abandonment rate:", round(overall_rate, 2), "%")

import matplotlib.pyplot as plt

# bar chart for abandonment rate
category_summary["abandonment_rate"].plot(
    kind="bar",
    title="Category-wise Cart Abandonment Rate",
    ylabel="Abandonment Rate (%)",
    xlabel="Category",
    rot=45
)

plt.tight_layout()
plt.savefig("plots/abandonment_rate_by_category.png")
plt.show()
