# Week 3: Linear Regression with Adjustment & Metrics - Practice Assessment (Q2)
#
# Problem Statement:
# Build a simple linear regression model to understand how Product Price
# influences Sales using the provided product dataset.

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data.csv')

# Write your code here

# Step 3: Prepare the features and target
# Keep x as a DataFrame so it is 2D, as sklearn expects.
x = df[['Product Price']]
y = df['Sales']

# Step 4: Fit the Linear Regression model
lr = LinearRegression()
lr.fit(x, y)
