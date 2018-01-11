# First attempt at cleaning data with pandas library
# Romeo 01/09/18

# import analysis and wrangling
import numpy as np
import pandas as pd
import random as rnd

# import machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv('../data/report_Section_I_-_Demographic_Information_f6911ac7_2018.01.09.csv')

print(dataset.columns.values)