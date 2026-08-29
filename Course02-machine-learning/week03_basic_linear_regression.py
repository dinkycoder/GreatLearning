# Week 3: Basic Linear Regression - Practice Assessment
#
# Problem Statement:
# Use linear regression to predict the annual expenditure of individuals based
# on their annual income and evaluate the model's performance using R-squared.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('data.csv')

# Write your code below

# Step 3: Preparing the Data
# Select 'annual_income_in_usd' as the feature X (kept as a DataFrame so it is
# 2D, as scikit-learn expects) and 'annual_expenditure' as the target y.
X = df[['annual_income_in_usd']]
y = df['annual_expenditure']

# Step 4: Splitting the Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Training the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Making Predictions
y_pred = model.predict(X_test)

# Step 7: Evaluating the Model
r_squared = r2_score(y_test, y_pred)
print(r_squared)
