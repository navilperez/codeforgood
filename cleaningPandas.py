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

########################### Conditions and Constants ###############################

# maps column names to list of conditions that need to be checked.
# Can outsource this by importing excel file
columns_to_conditions = {

    'Date_of_birth_(use_calendar_to_select_or_enter_as_MM/DD/YYYY)_(BirthDate)' :
        ['is_string', 'matches_pattern', 'is_21_yrs']

}

# maps condition names to functions
# args = [column_name, arg1, arg2, arg3,...]
conditions_to_functions = {

    'is_string': lambda args: isinstance(args[1],str),
    'is_21_yrs': lambda args: is_21_yrs(args[1]),
    'matches_pattern': lambda args: bool(re.match(Constants[args[0]]['pattern'], args[1]))

}

# connects columns and constants. Hmmm... dict of dicts?
Constants = {

    'Date_of_birth_(use_calendar_to_select_or_enter_as_MM/DD/YYYY)_(BirthDate)' :
        {
            'pattern':
            '[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]'
        }
}

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

def find_errors(column_names):
    '''iterates through every entry value in every column and prints errors'''
    total_errors = 0

    # iterate through each column
    for column_name in column_names:
        print_new_column(column_name)
        column_errors = 0

        # iterate through every entry in column
        for ind, val in df_survey[birth].iteritems():

            # iterate through each condition that has to be met
            for condition in columns_to_conditions[column_name]:

                # check each condition. Short-circuits if error is found
                if not conditions_to_functions[condition]((column_name, val)):
                    print(df_survey.iloc[ind]['Owner_ID'], ':', val)
                    column_errors += 1
                    total_errors += 1
                    break

        print(' ')
        print('Column errors found: '+ str(column_errors))

    print(' ')
    print('Total errors found: '+ str(total_errors))
    print(' ')

def export_to_csv():
    '''exports to csv file'''
    pass

def print_new_column(col):
    '''prints messages to terminal'''
    print('')
    print('-----------------------------------------------------------------')
    print('Errors in: '+ col)
    print('')
    print('Owner ID : cell number : input')
    print('')
    print('running...')
    print('')

def print_terminal_error():
    '''prints if error in reading terminal input'''
    print('')
    print('ERROR!: ')
    print('No file found. Please select a file in the following format in terminal:')
    print('>python3 cleaningPandas.py filepath/filename.csv')
    print('')
    print('Please note: filepath can be relative or absolute.')
    print('')

########################### Script ##############################

# import file from terminal argument
try: df_survey = pd.read_csv(sys.argv[1]) # creates pandas dataframe
except IndexError:
    print_terminal_error()
    sys.exit()

# current column of interest. can generalize by indexing dataframe and iterating
birth = 'Date_of_birth_(use_calendar_to_select_or_enter_as_MM/DD/YYYY)_(BirthDate)'

# update when we identify the mistakes of new columns
column_names = [birth]

#fix column formatting
column_formatting()

# find errors
find_errors(column_names)

# export errors to csv file

# To-Do's:
# write extra exception for invalid months and days
# write read-me for how to use file
# allow for conditions and constants to be read from csv file (kind of like a UI for the script!)
# write key/rules for formatting of conditions and parameters
