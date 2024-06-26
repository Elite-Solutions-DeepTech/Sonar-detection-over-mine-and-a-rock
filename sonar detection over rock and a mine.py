# -*- coding: utf-8 -*-
"""Copy of Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15JuC-OLK5CuATyr6iTGsmXkwr8cKoKJw
"""

import numpy as np
import pandas as pd

df=pd.read_csv('/content/sonar.all-data-uci.csv')

df

y=df.Label

y

x = df[['Freq_1','Freq_2','Freq_3','Freq_4','Freq_5','Freq_6','Freq_7','Freq_8','Freq_9','Freq_10','Freq_11','Freq_12','Freq_13','Freq_14','Freq_15','Freq_16','Freq_17','Freq_18','Freq_19','Freq_20','Freq_21','Freq_22','Freq_23','Freq_24','Freq_25','Freq_26','Freq_27','Freq_28','Freq_29','Freq_30','Freq_31','Freq_32','Freq_33','Freq_34','Freq_35','Freq_36','Freq_37','Freq_38','Freq_39','Freq_40','Freq_41','Freq_42','Freq_43','Freq_44','Freq_45','Freq_46','Freq_47','Freq_48','Freq_49','Freq_50','Freq_51','Freq_52','Freq_53','Freq_54','Freq_55','Freq_56','Freq_57','Freq_58','Freq_59','Freq_60']]

x

from sklearn import model_selection
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LogisticRegression
alg1=LogisticRegression()

alg1.fit(x_train,y_train)

y_pred=alg1.predict(x_test)
accuracy=alg1.score(x_test,y_test)
print(accuracy)

accuracy2=alg1.score(x_test,y_test)
print(accuracy2)

from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()

dtc.fit(x_train,y_train)

y_pred=dtc.predict(x_test)
accuracy=dtc.score(x_test,y_test)
print(accuracy)

accuracy2=dtc.score(x_test,y_test)

print(accuracy2)

import matplotlib.pyplot as plt

plt.scatter(y_test,y_pred,color='red')
plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],color='black',linewidth=3)
plt.show

plt.scatter(y_test,y_pred,color='red')
plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],color='grey',linewidth=3)
plt.xlabel('actual')
plt.ylabel('predicted')
plt.title('actual vs predicted sonar rock over a mine detection')
plt.grid(True)
plt.show()