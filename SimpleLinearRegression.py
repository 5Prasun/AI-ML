# Simple Linear Regression in Machine Learning

import numpy as np
import pandas as pd
import matplotlib .pyplot as plt

#Importing the dataset
dataset=pd.read_csv('Salary_Data.csv')

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
print(x)
print(y)