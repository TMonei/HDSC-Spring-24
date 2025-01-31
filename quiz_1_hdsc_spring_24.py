# -*- coding: utf-8 -*-
"""Quiz 1 HDSC Spring 24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UC7xA_KVmhaUha87nP6BqMDnoPqL_ceI
"""

from google.colab import files
uploaded = files.upload()

import io
import pandas as pd

df = pd.read_csv("FoodBalanceSheets_E_Africa_NOFLAG.csv",encoding = 'latin-1')
df.head()

#Question 1
my_tuppy = (1,2,5,8)
my_tuppy[2] = 6
#the code gives a type error

#Question 2
df.groupby('Element').Y2017.sum()

#Question 3
area = df.groupby('Area').Y2017.sum()
area.sort_values()
#Guinea-Bissau has the 7th Lowest Sum

#Question 4
df.isnull().sum()
#1589/60943 * 100 = 2.6%

#Question 5
lst = [[35,'Portugal',94],[33,'Argentina',93],[30,'Brazil',92]]
col = ['Age','Nationality','Overall']
pd.DataFrame(lst,columns = col, index = [i for i in range(1,4)] )

#Question 6
y = [(2,4),(7,8),(1,5,9)]

y[1][1]
y[1][-2]
y[1][-1]
y[2][-1]

#Question 7
df.Y2017.describe()

#Question 8
area1 = df.groupby('Area').Y2017.sum()
area1.sort_values()

#Question 9
df.groupby('Item').Y2015.sum()
df.groupby('Item').Y2018.sum()

#Question 10
df.groupby('Element').Y2017.sum()

#Question 12
S = [['him', 'sell'], [90, 28, 43]]
S[0][1][1]

#Question 16
df.groupby('Element').sum()

#Question 17
countries = df.groupby('Area').count()
countries.shape

#Question 18
df.groupby(['Area','Element']).Y2015.sum()

#Question 19
array = ([[94,89,63],
          [93,92,48],
          [92,94,56]])
array[:2,0:]
array[:1,1:]
array[1:,:]
array[:1,1:]
array[:2,1:]
#TypeError

#Question 20
df.shape