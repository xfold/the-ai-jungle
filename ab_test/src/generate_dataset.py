import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Setting seed for reproducibility
np.random.seed(42)
days = pd.date_range(start="2023-01-01", end="2023-06-30", freq='D')

# Helper function to generate normally distributed sales
def generate_normal_sales(mean, std_dev, days):
    sales = np.random.normal(mean, std_dev, days).astype(int)
    # Ensure no negative sales
    sales[sales < 0] = 0
    return sales

# Standard deviation for both stores
std_dev_A = 5
std_dev_B = 5

# Generate sales for store A (no price increase, so sales are stable)
sales_A = generate_normal_sales(mean=45, std_dev=std_dev_A, days=len(days))

# Generate sales for store B (price increase in March, so sales decrease after that)
sales_B = np.concatenate([
    generate_normal_sales(mean=40, std_dev=std_dev_B, days=len(days[:60])),
    generate_normal_sales(mean=30, std_dev=std_dev_B, days=len(days[60:]))
])

#generate a sales B scaled equivalent to sales A * 1.5
sales_B_scaled = sales_A * 1.5

# Create a dataframe
data_daily_normal = pd.DataFrame({
    'Day': days,
    'Sales_Store_A': sales_A,
    'Sales_Store_B': sales_B,
    'Sales_Store_B_scaled': sales_B_scaled,

})

data_daily_normal.to_csv('../data/daily_sales_data_normal.csv')