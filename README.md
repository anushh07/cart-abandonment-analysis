# cart-abandonment-analysis

Project Overview

This project analyzes online shopping cart abandonment using Python. Cart abandonment occurs when users add items to their shopping cart but do not complete the purchase. The aim of this project is to understand cart abandonment behavior across different product categories and identify trends using data analysis and visualization.

Objective-

1- Identify abandoned shopping carts.
2- Analyze category-wise cart abandonment.
3- Visualize abandonment rates using a bar chart.

Dataset Description-
The dataset used in this project is a CSV file containing user-level shopping activity. It includes the following columns:

1- user_id — Unique identifier for each user
2- category — Product category (Electronics, Books, Clothing, Beauty, Grocery, Home, Sports)
3- added_to_cart — Indicates whether the product was added to the cart (1 = Yes)
4- purchased — Indicates whether the purchase was completed (1 = Yes, 0 = No)

![1_BNKvsGxPnH_vM3wyB5vyyw](https://github.com/user-attachments/assets/80ce2821-4605-4865-9860-00d667f261be)

Libraries Used-

Pandas — Used for loading, cleaning, and analyzing the dataset.
Matplotlib — Used for visualizing cart abandonment rates.


Methodology-
1-The CSV dataset was loaded using Pandas.
2-A new column called abandoned was created to identify carts where items were added but not purchased.
3-Data was grouped category-wise using the Pandas groupby function.
4-Cart abandonment rates were calculated for each product category.
5-Cart abandonment rates were calculated for each product category.
6-A bar chart was generated to visualize category-wise abandonment trends.

Outputs:

Terminal Output-
After running the Python script, the following outputs are displayed in the terminal:

1-First five rows of the dataset.
2-Shape of the dataset (number of rows and columns).
3-Preview of the abandoned cart column.
4-Category-wise abandonment summary.

Example:

Category-wise abandonment summary:
Beauty       → 40%
Books        → 75%
Clothing     → 0%
Electronics  → ~71%
Grocery      → 20%
Home         → 50%
Sports       → 100%

Graphical Output-
A bar chart titled “Category-wise Cart Abandonment Rate” is generated to visually compare abandonment rates across categories.

X-axis: Product Categories.
Y-axis: Abandonment Rate (%).

The chart visually compares abandonment rates across categories.
The graph is saved as an image file inside the plots folder-
abandonment_rate_by_category.png

Results and Insights-

1-Sports category shows the highest cart abandonment rate.
2-Books and Electronics also have high abandonment rates.
3-Clothing category shows the lowest abandonment.
4-Cart abandonment behavior varies significantly across product categories.

Project Structure-
cart_abandonment_project/
├── analysis.py
├── README.md
├── data/
│   └── cart_data.csv
└── plots/
    └── abandonment_rate_by_category.png
    
How to Run the Project-

Install the required libraries:
pip install pandas matplotlib

Run the Python script:
python analysis.py

Conclusion-
This project demonstrates how simple data analysis techniques can be used to understand customer behavior in online shopping. By analyzing cart abandonment patterns across different categories, businesses can identify problem areas and take steps to improve conversion rates.





Anushka Tiwari
