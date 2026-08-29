# Week 3: Basic Linear Regression - Practice Assessment (Question 5)
#
# Problem Statement:
# Build a simple Linear Regression model to predict the Credit amount based
# solely on the individual's Age, to see whether age alone is a reasonable
# predictor of credit demand.

import pandas as pd
from sklearn.linear_model import LinearRegression

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
