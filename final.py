#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 孫書恆 PYTHON_3 HW2
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np


train_data = pd.read_csv('train_2.csv')
test_data = pd.read_csv('test_2.csv')


X_train = train_data[['MSSubClass', 'LotArea', 'OverallQual', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold','OverallCond','YearBuilt','YearRemodAdd','BsmtFinSF1','BsmtUnfSF','TotalBsmtSF','1stFlrSF','2ndFlrSF','GrLivArea','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr']]
y_train = train_data['SalePrice']
X_test = test_data[['MSSubClass', 'LotArea', 'OverallQual', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold','OverallCond','YearBuilt','YearRemodAdd','BsmtFinSF1','BsmtUnfSF','TotalBsmtSF','1stFlrSF','2ndFlrSF','GrLivArea','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr']]
from sklearn.impute import SimpleImputer


imputer = SimpleImputer(strategy='mean')
imputer.fit(X_train)
X_test = imputer.transform(X_test)


rf_regressor = RandomForestRegressor()
rf_regressor.fit(X_train, y_train)
y_pred = rf_regressor.predict(X_test)


result_df = pd.DataFrame({'Id': range(1461, 2920), 'SalePrice': y_pred})


result_df.to_csv('predicted_hw2_孫書恆.csv', index=False)


# In[ ]:




