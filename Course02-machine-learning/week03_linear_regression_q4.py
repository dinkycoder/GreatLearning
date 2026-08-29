# Week 3: Basic Linear Regression - Practice Assessment (Question 4)
#
# Problem Statement:
# Build a linear regression model to predict the credit amount based on the
# applicant's age. After fitting, evaluate performance using the R-squared
# score to see how well age explains the variability in credit amount.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('data.csv')

# Write your code here:

# Step 3: Prepare the features and target
# 'Age' is the feature (kept as a DataFrame so X is 2D, as sklearn expects);
# 'Credit amount' is the target.
X = df[['Age']]
y = df['Credit amount']

# Step 4: Fit the Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Step 5: Compute the R2 Score
predictions = model.predict(X)
r2 = r2_score(y, predictions)
print(r2)
