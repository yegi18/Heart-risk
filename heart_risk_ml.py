# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 01:54:19 2023

@author: HP
"""

import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from matplotlib import pyplot as plt
data=pd.read_csv("D:\\new_downloads\\Heart Attack Data Set.csv")

data=data.loc[:, data.columns != 'cp']
data=data.loc[:, data.columns != 'chol']
data=data.loc[:, data.columns != 'fbs']
data=data.loc[:, data.columns != 'exang']
data=data.loc[:, data.columns != 'ca']
data=data.loc[:, data.columns != 'thal']
x1=data.loc[:, data.columns != 'target']
y1=data=data.loc[:,"target"]
x,y = shuffle(x1,y1,random_state=42)
x_train , x_test , y_train ,y_test = train_test_split(x, y, train_size=0.8)
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
clf = SVC(kernel='linear', probability=True)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
a=accuracy_score(y_test,y_pred) 
b=recall_score(y_test,y_pred)
print(a)
print(b)