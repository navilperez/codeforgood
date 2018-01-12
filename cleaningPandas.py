'''
First attempt at cleaning data with pandas library
Romeo 01/09/18
'''
# pylint: disable=invalid-name


########################### Imports ###############################

# interaction with the terminal
import sys

# regular expressions (regex)
import re

# working with dates
import datetime

# analysis and wrangling
import random as rnd
import numpy as np
import pandas as pd

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

########################### Helper Functions ###############################

def column_formatting():
    '''helper: fixes column formatting so pandas can easily parse it'''

    # remove column heading spaces
    cols = df_survey.columns
    cols = cols.map(lambda x: x.replace(' ', '_') if isinstance(x, str) else x)
    df_survey.columns = cols

    # idea: remove special characters such as '/'

def is_21_yrs(date):
    '''helper: checks if a date is at least 21 years old'''
    now = datetime.datetime.now() # current time
    year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])
    birthdate = datetime.date(year, month, day)

    # in case of a leap year!
    # incorrectly addresses invalid months and days. Pls Fix :(
    try: birthdate = datetime.datetime(year+21, month, day)
    except: birthdate = datetime.datetime(year+21, 3, 1)

    return birthdate <= now

########################### Script ##############################

# import file from terminal argument
try:
    df_survey = pd.read_csv(sys.argv[1]) # creates pandas dataframe
except IndexError:
    print('')
    print('ERROR! : ')
    print('No file found. Please select a file in the following format in terminal:')
    print('>python3 cleaningPandas.py filepath/filename.csv')
    print('')
    print('Please note: Filepath can be relative or absolute.')
    print('')
    sys.exit()

column_formatting()

# column of interest. can generalize by indexing dataframe and iterating
birth = 'Date_of_birth_(use_calendar_to_select_or_enter_as_MM/DD/YYYY)_(BirthDate)'

# regex expression for dates https://regex101.com/
pattern = '[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]'

print(' ')
print('-----------------------------------------------------------------')
print('Errors in: '+birth)
print(' ')
print('Owner ID : input')
print(' ')
# searches through one column. Pythonic way w/ help of pandas
total_errors = 0
for ind, val in df_survey[birth].iteritems():
    if not isinstance(val, str) or not bool(re.match(pattern, val)) or not is_21_yrs(val):
        print(df_survey.iloc[ind]['Owner_ID'], ':', val)
        total_errors += 1
print(' ')
print('Total errors found: '+ str(total_errors))
print(' ')

# To-Do's:
# generalize
# write extra exception for invalid months and days
# write read-me for how to use file
# create dictionary that maps conditions to check for to functions such as is_21_yrs() and isintance(), patternMatch, etc.
# create dictionary with entries for each column header and the necessary conditions and constants (such as required regex)
