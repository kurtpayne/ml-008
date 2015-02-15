#!/usr/local/bin/python

# Imports
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

# Load data
df_adv = pd.read_csv('./input.csv', index_col=False)
X = df_adv[['Square_Feet', 'Bedrooms']]
y = df_adv['Sales_Price']
df_adv.head()

Square_Feet = [ 4478, 1268, 2300, 7000 ]
Bedrooms = [ 5, 3, 4, 7 ]

d = {
	'Square_Feet' : Square_Feet,
	'Bedrooms'    : Bedrooms
}
Z = pd.DataFrame(data = d);

print Z

# formula: response ~ predictor + predictor
results = smf.ols(formula='Sales_Price ~ Square_Feet + Bedrooms', data=df_adv).fit()
predictions = results.predict(Z)
print predictions