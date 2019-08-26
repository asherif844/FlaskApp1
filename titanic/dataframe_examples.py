import csv
import pandas as pd
import numpy as np

def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""
    percent = np.divide(val, total)

    return percent


titanic_df = pd.read_csv("titanic/static/data/train.csv")
survived = titanic_df[(titanic_df['Survived']==1) & (titanic_df["Age"].notnull())]

pclass_percent = calculate_percentage(survived.groupby('Pclass').size().values, survived['PassengerId'].count())*100

print(pclass_percent)


class_labels = ['Class I', 'Class II', 'Class III']
pclass_percent = calculate_percentage(survived.groupby('Pclass').size().values, survived['PassengerId'].count())*100

pieChartData = []
for index, item in enumerate(pclass_percent):
    eachData = {}
    eachData['category'] = class_labels[index]
    eachData['measure'] =  round(item,1)
    pieChartData.append(eachData)

age_labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
survived["age_group"] = pd.cut(survived.Age, range(0, 81, 10), right=False, labels=age_labels)