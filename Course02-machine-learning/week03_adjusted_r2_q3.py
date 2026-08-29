# Week 3: Linear Regression with Adjustment & Metrics - Practice Assessment (Q3)
#
# Problem Statement:
# Build a linear regression model to estimate total sales of a product using
# only its price, then evaluate with Mean Squared Error (MSE).

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('data.csv')

# Write your code below:

# Step 3: Prepare the features and target
# Keep x as a DataFrame so it is 2D, as sklearn expects.
x = df[['Product Price']]
y = df['Sales']

# Step 4: Fit the Linear Regression model
lr = LinearRegression()
lr.fit(x, y)

# Step 5: Make predictions
y_pred = lr.predict(x)

# Step 6: Calculate MSE
mse = mean_squared_error(y, y_pred)
print(mse)
