# Week 3: Linear Regression with Train-Test Splits - Practice Assessment (Q2)
#
# Problem Statement:
# Use linear regression to model the relationship between product price and
# sales, and evaluate with Mean Squared Error on both training and testing data.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_csv('data.csv')

# Write your code below

# Step 3: Prepare the features and target
# Keep X as a DataFrame so it is 2D, as sklearn expects.
X = df[['Product Price']]
y = df['Sales']

# Step 4: Split the data (80:20, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Step 5: Fit the Linear Regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Step 6: Make predictions for training and testing data
y_pred_train = lr.predict(X_train)
y_pred_test = lr.predict(X_test)

# Step 7: Compute MSE for training and testing data
mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)
print(mse_train, mse_test)
