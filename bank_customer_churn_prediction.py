# -*- coding: utf-8 -*-
"""Bank customer churn prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KZtu2Ou3cmpBY8_wD3NJXliXy8OlN9QW
"""

import pandas as pd
import numpy as np

data = pd.read_csv("/content/Churn_Modelling.csv")

data.head()

data.tail()

data.shape

print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])

data.info()

data.isnull().sum()

"""Overall statistics of the dataset

"""

data.describe()

data.describe(include ='all')

data.columns

data.drop(['RowNumber', 'CustomerId', 'Surname'],axis = 1)

data['Geography'].unique()

data = pd.get_dummies(data,drop_first=True)

data.head()

data['Exited'].value_counts()

import seaborn as sns

sns.countplot(data['Exited'])

"""Spliting the dataset into the training dataset and test dataset"""

# Assuming 'data' is your DataFrame and 'Exited' is the target variable
x = data.drop('Exited', axis=1)  # Features (all columns except 'Exited')
y = data['Exited']               # Target variable

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42, stratify=y)

"""Feature scalling"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler

from sklearn.preprocessing import StandardScaler

sc = StandardScaler() # Create an instance of the StandardScaler
x_train=sc.fit_transform(x_train)
x_test = sc.transform(x_test)

x_train

"""Logistic Regression"""

from sklearn.linear_model import LogisticRegression

log = LogisticRegression()

log.fit(x_train,y_train)

y_pred1 = log.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred1)

from sklearn.metrics import precision_score,recall_score,f1_score

precision_score(y_test,y_pred1)

recall_score(y_test,y_pred1)

f1_score(y_test,y_pred1)

"""Handling imbalaned data with SMOTE"""

from imblearn.over_sampling  import SMOTE

x_res,y_res = SMOTE().fit_resample(x,y)

x_res.value_counts()

y_res.value_counts()

"""Support  Vector Classifier (SVC)"""

from sklearn import svm

svm = svm.SVC()

svm.fit(x_train,y_train)

from sklearn import svm  # Import the svm module

# Create an instance of the SVC classifier
clf = svm.SVC()

# Use clf for fitting and prediction
clf.fit(x_train, y_train)
y_pred2 = clf.predict(x_test)

accuracy_score(y_test,y_pred2)

precision_score(y_test,y_pred2)

"""KNnighbours classifier"""

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(x_train,y_train)

y_pred3 = knn.predict(x_test)

accuracy_score(y_test,y_pred3)

precision_score(y_test,y_pred3)

"""Decision Tree Classifier"""

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()

dt.fit(x_train,y_train)

y_pred4 = dt.predict(x_test)

accuracy_score(y_test,y_pred4)

precision_score(y_test,y_pred4)

"""Random Forest Classofier"""

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()

rf.fit(x_train,y_train)

y_pred5 = rf.predict(x_test)

accuracy_score(y_test,y_pred5)

precision_score(y_test,y_pred5)

"""Gradient Boosting Classifier"""

from sklearn.ensemble import GradientBoostingClassifier

gbc = GradientBoostingClassifier()

gbc.fit(x_train,y_train)

y_pred6 = gbc.predict(x_test)

accuracy_score(y_test,y_pred6)

precision_score(y_test,y_pred6)

final_data=pd.DataFrame({'Models':['LR','SVC','KNN','DT','RF','GBC'],
                        'ACC':[accuracy_score(y_test,y_pred1),
                              accuracy_score(y_test,y_pred2),
                              accuracy_score(y_test,y_pred3),
                              accuracy_score(y_test,y_pred4),
                              accuracy_score(y_test,y_pred5),
                              accuracy_score(y_test,y_pred6)]})

final_data

import seaborn as sns

import seaborn as sns

# Use the 'data' parameter to pass the DataFrame
# and 'x' and 'y' to specify the columns for the plot
sns.barplot(data=final_data, x='Models', y='ACC')

final_data=pd.DataFrame({'Models':['LR','SVC','KNN','DT','RF','GBC'],
                        'PRE':[precision_score(y_test,y_pred1),
                              precision_score(y_test,y_pred2),
                              precision_score(y_test,y_pred3),
                              precision_score(y_test,y_pred4),
                              precision_score(y_test,y_pred5),
                              precision_score(y_test,y_pred6)]})

final_data

import seaborn as sns

# Use the 'data' parameter to pass the DataFrame
# and 'x' and 'y' to specify the columns for the plot
sns.barplot(data=final_data, x='Models', y='PRE')

"""Save the model"""

x_res=sc.fit_transform(x_res)

rf.fit(x_res,y_res)

import joblib

joblib.dump(rf,'churn_predict_model')

model = joblib.load('churn_predict_model')

data.columns

"""GUI"""

from tkinter import *
from sklearn.preprocessing import StandardScaler
import joblib

from sklearn.preprocessing import StandardScaler
import joblib

def predict_churn():
    p1 = int(input("Enter CreditScore: "))
    p2 = int(input("Enter Age: "))
    p3 = int(input("Enter Tenure: "))
    p4 = float(input("Enter Balance: "))
    p5 = int(input("Enter NumOfProducts: "))
    p6 = int(input("Enter HasCrCard (1 for Yes, 0 for No): "))
    p7 = int(input("Enter IsActiveMember (1 for Yes, 0 for No): "))
    p8 = float(input("Enter EstimatedSalary: "))
    p9 = int(input("Enter Geography (1 for Germany, 2 for Spain, 3 for France): "))
    if p9 == 1:
        Geography_Germany=1
        Geography_Spain=0
        Geography_France=0
    elif p9 == 2:
        Geography_Germany=0
        Geography_Spain=1
        Geography_France=0
    elif p9 == 3:
        Geography_Germany=0
        Geography_Spain=0
        Geography_France=1
    p10 = int(input("Enter Gender (1 for Male, 0 for Female): "))

    model = joblib.load('churn_model')  # Load your model here
    result = model.predict(sc.transform([[p1, p2, p3, p4, p5, p6, p7, p8, Geography_Germany, Geography_Spain, p10]]))

    if result == 0:
        print("No Exit")
    else:
        print("Exit")

if __name__ == "__main__":
    predict_churn()