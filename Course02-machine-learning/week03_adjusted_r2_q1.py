# Week 3: Linear Regression with Adjustment & Metrics - Practice Assessment (Q1)
#
# Problem Statement:
# Create a linear regression model named `model` to predict annual_expenditure
# from annual_income_in_usd and evaluate performance using adjusted R-squared.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('data.csv')

# Write your code below:

# Step 1: Prepare the Features and Target Variable
# Keep X as a DataFrame so it is 2D, as sklearn expects.
X = df[['annual_income_in_usd']]
y = df['annual_expenditure']

# Step 2: Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 3: Create and Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make Predictions on the Test Set
y_pred = model.predict(X_test)

# Step 5: Calculate the Adjusted R-squared Value
r_squared = model.score(X_test, y_test)
adjusted_r_squared = 1 - (1 - r_squared) * (len(y_test) - 1) / (
    len(y_test) - X_test.shape[1] - 1
)
print(adjusted_r_squared)
