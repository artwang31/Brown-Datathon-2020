# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 08:41:47 2020

@author: hariz
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

y = pd.read_csv('1996-2003.csv')

#X['Date'] = X['Date'].astype('datetime64[ns]')
y['Date'] = y['Date'].astype('datetime64[ns]')

X = pd.read_csv('training.csv')
X['Date_'] = X['Date_'].astype('datetime64[ns]')

joined = X.set_index('Date_').join(y.set_index('Date'))

countries = ['UK','China','Japan','Korea','Brazil','Australia']
currencies = ['U.K. Pound Sterling','Chinese Yuan','Japanese Yen','Korean Won','Brazilian Real','Australian Dollar']

y = joined[countries]
X = joined[currencies]

X = X.reset_index()
X['month'] = X['Date_'].dt.month
X['year'] = X['Date_'].dt.year

X = pd.melt(frame=X,id_vars=['month','year','Date_'], var_name="currency", value_name="rate")
X = X[['currency','rate','month','year']]

y = y.reset_index()
y = pd.melt(frame=y,id_vars=['Date_'], var_name="country", value_name="arrival")
y = y['arrival']
y = y.convert_objects(convert_numeric=True)


from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

scaler = StandardScaler()
X['rate'] = scaler.fit_transform(X['rate'])

le = LabelEncoder()
X['currency'] = le.fit_transform(X['currency'])
X['month'] = le.fit_transform(X['month'])
X['year'] = le.fit_transform(X['year'])

linreg = LinearRegression()
linreg.fit(X,y)
linreg.coef_


