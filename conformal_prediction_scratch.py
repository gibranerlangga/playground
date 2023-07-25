import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from nonconformist.cp import IcpRegressor
from nonconformist.nc import RegressorNc, AbsErrorErrFunc


# Load Boston housing data
housing = fetch_california_housing()
X, y = housing.data, housing.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=123)

# Train OLS regressor
ols = LinearRegression()
ols.fit(X_train, y_train)

# Get predictions for test set
ols_prediction = ols.predict(X_test)

# Create nonconformity function and conformal predictor
nc = RegressorNc(ols, AbsErrorErrFunc())
icp = IcpRegressor(nc)

# Calibrate ICP using training data and obtain predictions for test set
icp.fit(X_train, y_train)

# Calibrate ICP using training data and obtain predictions for test set
icp.calibrate(X_test, y_test)

# Produce predictions for test set and obtain indices of inliers
icp_prediction = icp.predict(X_test)

print(ols_prediction)
print(icp_prediction)