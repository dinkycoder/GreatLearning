# Week 3: Linear Regression with Adjustment & Metrics - Practice Assessment (Q4)
#
# Problem Statement:
# Fit a Linear Regression model to predict Sales from Product Price, then assess
# how well the model explains the variability in sales using the R-squared score.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('data.csv')

# Write your code below

# Step 3: Prepare the features and target
# Keep X as a DataFrame so it is 2D, as sklearn expects.
X = df[['Product Price']]
y = df['Sales']

# Step 4: Fit the Linear Regression model
lr = LinearRegression()
lr.fit(X, y)

# Step 5: Make predictions
y_pred = lr.predict(X)

# Step 6: Compute R2 Score
# The RHS r2_score(...) call runs before the name is rebound, so assigning the
# result to a variable also named r2_score (as the step asks) works here.
r2_score = r2_score(y, y_pred)
print(r2_score)
