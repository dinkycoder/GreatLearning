# Week 3: Basic Linear Regression - Practice Assessment (Question 2)
#
# Problem Statement:
# Use simple linear regression to model the relationship between an individual's
# age and the credit amount they apply for. Fit the model, generate predictions,
# and evaluate accuracy using Mean Absolute Error (MAE).

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('data.csv')

# Write your code below:

# Step 3: Prepare the features and target
# 'Age' is the predictor (kept as a DataFrame so X is 2D, as sklearn expects);
# 'Credit amount' is the target.
X = df[['Age']]
y = df['Credit amount']

# Step 4: Fit the Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Step 5: Predict the values
predictions = model.predict(X)

# Step 6: Calculate Mean Absolute Error
mae = mean_absolute_error(y, predictions)
print(mae)
