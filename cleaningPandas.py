'''
First attempt at cleaning data with pandas library
Romeo 01/09/18
'''

# import analysis and wrangling
import numpy as np
import pandas as pd
import random as rnd
import re

# import datetime
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
dataset = pd.read_csv('report_Section_I_-_Demographic_Information_f6911ac7_2018.01.09.csv')

# remove column heading spaces
cols = dataset.columns
cols = cols.map(lambda x: x.replace(' ', '_') if isinstance(x, str) else x)
dataset.columns = cols
print(dataset.columns)

# column of interest
birth = 'Date_of_birth_(use_calendar_to_select_or_enter_as_MM/DD/YYYY)_(BirthDate)'

# regex expression
pattern = '[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]'

def is_21_yrs(date):
    '''helper: checks if a date is at least 21 years old'''
    now = datetime.datetime.now() # current time
    year,month,day = int(date[:4]),int(date[5:7]),int(date[8:])
    birthdate = datetime.date(year, month, day)

    # in case of a leap year!
    try: birthdate = datetime.datetime(year+21, month, day)
    except: birthdate = datetime.datetime(year+21,3,1)

    return birthdate <= now

print(' ')
print('------------------------------------------------------------------------------------------')
print('Errors in: '+birth)
print(' ')
print('Owner ID : input')
print(' ')
# searches through one column. Pythonic way
total_errors = 0
for ind, val in dataset[birth].iteritems():
    if type(val) != str or not(bool(re.match(pattern,val))) or not is_21_yrs(val):
        # replace with ID instead of ind. Maybe a hash table. Maybe run zip with IDs. Maybe write ind + 2 to indicate row #
        print(dataset.iloc[ind]['Owner_ID'], ':', val)
        total_errors += 1
print(' ')
print('Total errors found: '+ str(total_errors))
print(' ')


# To-Do's:
# read general file through command line
# email about:
# we wrote script to identify birthdate errors. How do you want us to report errors? where does data go?, where is it visualized?, what other errors have you found? What data analysis have you already run on data - trends and/or machine learning?
# write extra exception for invalid months and days
# write read-me for how to use file
