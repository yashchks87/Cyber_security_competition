# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:17:31 2019

@author: Tanvi
"""

import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt

#Import and data cleaning- removing the rows with atleast 1 null value-------------------

spamdf=pd.read_csv("C:/Users/kunal/OneDrive/Documents/Cal Poly Competition/Spam.csv")
#df=print (df.dropna(inplace = True))
#print (spamdf.isnull().values.any())
#print (spamdf.isnull().sum().sum())
cleaned = spamdf.dropna()
#print(cleaned.isnull().sum())
print(cleaned.isnull().values.any())

#---------------------------------------------------------------------------------
#Feature Importance - using Extra Tree Classifier
x = cleaned.iloc[:,0:78]
y = cleaned.iloc[:,-1]
from sklearn.ensemble import ExtraTreesClassifier
model=ExtraTreesClassifier()
model.fit(x,y)
print(model.feature_importances_)
feature_imp= pd.Series(model.feature_importances_,index=x.columns)
feature_imp.nlargest(10).plot(kind='barh')
plt.show()

#as per paper feature columns chose were
#Domain token count
#tld
#ldl getArg, 
#Number of Dots in URL
#delimiter path
#Symbol Count Domain

#------------------------------------------------------------------------------
#Implementing Basic Descision Forest
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=66)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(x_train,y_train)
rfc.predict = rfc.predict(y_test)


