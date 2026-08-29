# Week 3: Basic Linear Regression - Practice Assessment (Question 3)
#
# Problem Statement:
# Build a linear regression model to predict the credit amount an individual is
# applying for, using their age as the input feature. Train the model, generate
# predictions, and evaluate performance using Mean Squared Error (MSE).

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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

# Step 6: Calculate Mean Squared Error
mse = mean_squared_error(y, predictions)
print(mse)
