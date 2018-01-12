'''
First attempt at cleaning data with pandas library
Romeo 01/09/18
'''

# import analysis and wrangling
import numpy as np
import pandas as pd
import random as rnd
import re

#import current day
import datetime 

# import machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

# need to decide on data location
dataset = pd.read_csv('/Users/romeoflores/Documents/code-for-good-local/data/report_Section_I_-_Demographic_Information_f6911ac7_2018.01.09.csv')

# column of interest
birth = 'Date of birth (use calendar to select or enter as MM/DD/YYYY) (BirthDate)'

# regex expression
pattern = '[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]'

def is_21_yrs(date):
    '''checks if a date is at least 21 years old'''
    now = datetime.datetime.now() # current time
    year,month,day = int(date[:4]),int(date[5:7]),int(date[8:])
    birthdate = datetime.date(year, month, day)

    # in case of a leap year!
    try: birthdate = datetime.datetime(year+21, month, day)
    except: birthdate = datetime.datetime(year+21,3,1)

    return birthdate <= now

print(' ')
print('Invalid birthdates:')
print(' ')
print('ID : input')
print(' ')
# searches through one column. Pythonic way
for ind, val in dataset[birth].iteritems():
    #include is_21_yrs fxn
    if type(val) != str or not(bool(re.match(pattern,val))) or not is_21_yrs(val):
        # replace with ID instead of ind. Maybe a hash table. Maybe run zip with IDs. Maybe write ind + 2 to indicate row #
        print(ind, ':', val)
print(' ')

# pandas to extract all incorrectly formatted items
#.str.extract(pat, flags=0, expand=None)[source]

