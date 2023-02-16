# -*- coding: utf-8 -*-
"""pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/atharvthakur17/eb9428adb98611c4fce3d0cfe84de6bb/pandas.ipynb
"""

import pandas as pd
iris=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(type(iris))

df=iris.copy()
df.head()

print(df.shape)
df.columns=["a","b","c","d","type"]
print(df.head())

df.head()

df.describe()

print(df.c)
df.isnull().sum()

print(df.iloc[1:4,2:3])    #particular data
print(df.head())

print(df.head())
df.drop(0,inplace=True)
df.head()

df.drop(1,inplace=True)
df.drop(df.index[0],inplace=True)
df.head()

df[df.a>6]

df.loc[7]
df.loc[0]=[1,8,9,88,"typenew"]
print(df.head())
df.loc[1]=[1,8,9,88,"typenew"]
df.tail()