#!/usr/bin/env python
# coding: utf-8

# In[11]:


""" Import data from csv file """

import pandas as pd
import numpy as np

# Import data from csv file
df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')


# display data with plot
# df_with_nan = df[df.isna().any(axis=1)]
# df_with_nan.head(10)
# drop data with too many NaN

train_df = df.sample(frac=0.8, random_state=101)
validate_df = df.drop(train_df.index)

train_df_original = train_df.copy()
validate_df_original = validate_df.copy()
test_df_original = test_df.copy()


# In[12]:


""" Process with data """
# getting correlation between each column

train_df_corr = train_df.corr(numeric_only=True)
corr_result = train_df_corr['SalePrice']

tags_to_use = []
tags_to_drop = []
size = corr_result.size

for i in range(size):
    if ((abs(corr_result[i]) >= 0.27)):
        if corr_result.index[i] != "SalePrice":
            tags_to_use.append(corr_result.index[i])

for i in train_df.columns:
    if i == "SalePrice":
        continue

    if i not in tags_to_use:
        tags_to_drop.append(i)
    else:
        # Replace NaN with mean value
        train_df[i] = train_df[i].fillna(train_df[i].mean())
        validate_df[i] = test_df[i].fillna(test_df[i].mean())
        test_df[i] = test_df[i].fillna(test_df[i].mean())


# train data
tags_to_drop_with_saleprice = tags_to_drop.copy() + ["SalePrice"]

print(tags_to_use)
print(tags_to_drop)
print(tags_to_drop_with_saleprice)

y_train_df = train_df["SalePrice"]
train_df = train_df.drop(columns=(tags_to_drop_with_saleprice))
y_validate_df = validate_df["SalePrice"]
validate_df = validate_df.drop(columns=(tags_to_drop_with_saleprice))

# test data
test_df = test_df.drop(columns=tags_to_drop)

# Standardize data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
train_df = scaler.fit_transform(train_df)
validate_df = scaler.transform(validate_df)
test_df = scaler.transform(test_df)


# In[13]:


""" Train model """
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(train_df, y_train_df)
validate_df_predict = regressor.predict(validate_df)

""" Evaluate model """
# w_0 = regressor.intercept_
# w_1 = regressor.coef_
# print("w_0: ", w_0)
# print("w_1: ", w_1)

mean_square = mean_squared_error(y_validate_df, validate_df_predict)
print("root mean square: ", mean_square)


# In[14]:


""" Predict """
test_df_predict = regressor.predict(test_df)
print(test_df_predict)
print(test_df)
# save the result to csv file
dataframe_result = pd.DataFrame({'Id': test_df_original.Id, 'SalePrice': test_df_predict})
dataframe_result.to_csv('result.csv', index=False)


# In[15]:


""" Visualize """
import matplotlib.pyplot as plt
# visualize the training set results
plt.scatter(train_df["1stFlrSF"], y_train_df, color = 'red')
plt.plot(train_df["1stFlrSF"], regressor.predict(train_df), color = 'blue')
plt.title('Environment vs SalesPrice (trainning set)')
plt.xlabel("Environment")
plt.ylabel("Sales Price")
plt.show()

# visualize the test set results
plt.scatter(test_df["1stFlrSF"], y_test_df, color = 'red')
plt.plot(test_df["1stFlrSF"], regressor.predict(test_df), color = 'blue')
plt.title('Environment vs SalesPrice (test set)')
plt.xlabel("Environment")
plt.ylabel("Sales Price")
plt.show()

