'''
First attempt at cleaning data with pandas library
Romeo 01/09/18
'''
# pylint: disable=invalid-name

########################### Imports ###############################

# interaction with the terminal
import sys

# regular expressions (regex) https://regex101.com/
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
    'Owner_ID':
        ['is_string'],
    'Instance_ID':
        [],
    'Date_of_birth__use_calendar_to_select_or_enter_as_MM_DD_YYYY___BirthDate_':
        ['is_string', 'matches_pattern', 'is_21_yrs'],
    'Sex__PatientSex_':
        ['is_string'],
    'Height_-_please_select_unit__HeightMeasure_':
        ['is_string'],
    'Height__PatientHeight_':
        ['is_not_zero'],
    'Weight__PatienWeight_':
        ['is_not_zero'],
    'Weight_measure__WeightMeasure_':
        ['is_string'],
    'Dominant_hand__Domhand_':
        ['is_string'],
    'Education_-_number_of_years_completed__including_kindergarten,_elementary_school,_middle_school,_high_school,_and_all_post-high_school_education___Yearsofeducation_':
        ['is_number'],
    'Highest_level_of_education__HighEducLevel_':
        ['is_string'],
    'Current_marital_status__MaritalStatus_':
        ['is_string'],
    'Employment_status_-_select_one__EmployStatus_':
        ['is_string'],
    'Please_indicate_age_when_disabled__DisableAge_':
        ['is_number'],  
    'Please_indicate_age_when_retired__RetiredAge_':
        ['is_number'],
    'Do_you_live_with_other_people_or_in_a_group_setting?__LiveWithOtherPeople_':
        ['is_string'],
    'What_type_s__of_health_insurance_do_you_have?_Please_check_all_that_apply.__HealthInsurance_':
        ['is_string', 'value_separator_parsed'], # Note that commas did not parse well!
    'What_is_the_name_of_your_insurer?__NameofInsurer_':
        [],
    'If_other,_please_specify.__OtherInsurance_':
        [],
    'Please_indicate_which_of_the_following_categories_best_represents_your_household_income:__Household_income_':
        ['is_string'],
    '[DomesticStatus1]:Living_with_spouse_partner__LivingwithSpouse_':
        ['is_Y_or_N'],
    '[DomesticStatus1]:Living_with_sibling__LivingwithSibling_':
        ['is_Y_or_N'],
    '[DomesticStatus1]:Living_with_children__LivingwithChildren_':
        ['is_Y_or_N'],
    '[DomesticStatus1]:Living_with_parent__LivingwithParent_':
        ['is_Y_or_N'],
    '[DomesticStatus1]:Living_with_other_relative__LivingwithOtherRelative_':
        ['is_Y_or_N'],
    '[DomesticStatus1]:Living_with_friend_companion__LivingwithFriend_':
        ['is_Y_or_N'],
    '[DomesticStatus1]:Living_with_domestic_help__LivingwithDomesticHelp_':
        ['is_Y_or_N']
}

# maps condition names to functions
# args = [column_name, arg1, arg2, arg3,...]
conditions_to_functions = {

    'is_string': lambda args: isinstance(args[1], str),
    'is_21_yrs': lambda args: is_21_yrs(args[1]),
    'matches_pattern': lambda args: bool(re.match(Constants[args[0]]['pattern'], args[1])),
    'contains_pattern':lambda args: bool(re.search(Constants[args[0]]['pattern'], args[1])),
    'is_gender': lambda args: args[1] == 'M' or args[1] == 'F' or args[1] == 'PreferNotAnswer' or args[1] == 'Other',
    'height_units': lambda args: isinstance(args[1], str) and (args[1] == 'FeetInch' or args[1] == 'CM'),
    'is_not_zero': lambda args: isinstance(args[1], float) and args[1] > 0,
    'weight_units': lambda args: isinstance(args[1], str) and (args[1] == 'lb' or args[1] == 'kg'),
    'dominant_hand': lambda args: isinstance(args[1], str) and (args[1] == 'Right' or args[1] == 'Left' or args[1] == 'Ambidextrous' or args[1] == 'DontKnow'),
    'is_number': lambda args: isinstance(args[1], int) or isinstance(args[1], float),
    'is_Y_or_N': lambda args: isinstance(args[1], str) and (args[1] == 'Y' or args[1] == 'N'),
    'value_separator_parsed': lambda args: isinstance(args[1], str) and not conditions_to_functions['contains_pattern'](args)

}

# connects columns and constants. Hmmm... dict of dicts?
Constants = {
    'Owner_ID':
        {
            'pattern':
            '__VALUE_SEPARATOR'
        },
    'Date_of_birth__use_calendar_to_select_or_enter_as_MM_DD_YYYY___BirthDate_':
        {
            'pattern':
            '[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]'
        },
    'What_type_s__of_health_insurance_do_you_have?_Please_check_all_that_apply.__HealthInsurance_':
        {
            'pattern':
            '__VALUE_SEPARATOR'
        }
}

########################### Helper Functions ###############################

def column_formatting():
    '''helper: fixes column formatting so pandas can easily parse it'''

    # remove column heading spaces and special characters
    special_chars = [' ','/','(',')']
    cols = df_survey.columns
    for special_char in special_chars:
        cols = cols.map(lambda x: x.replace(special_char, '_') if isinstance(x, str) else x)
    df_survey.columns = cols
    #print(cols)

def is_21_yrs(date):
    '''helper: checks if a date is at least 21 years old'''
    today = datetime.datetime.today()
    age = datetime.timedelta(years=21)
    year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])
    birthdate = datetime.date(year, month, day)

    return today - birthdate >= age

def find_errors(column_names):
    '''iterates through every entry value in every column and prints errors'''
    all_errors = {} # every single error
    total_errors = 0
    total_fixed = 0
    bad_columns = set() # columns with more than 5% errors

    # iterate through each column
    for column_name in column_names:
        #print_new_column(column_name)
        column_errors = 0
        column_fixed = 0
        print('Column: ' + column_name)
        if column_name in columns_to_conditions: # just in case we haven't added a column yet
            # iterate through every entry in column
            for ind, val in df_survey[column_name].iteritems():
                #print(ind,val)
                # iterate through each condition that has to be met
                for condition in columns_to_conditions[column_name]:

                    # check each condition. Short-circuits if error is found
                    try:
                        if not conditions_to_functions[condition]((column_name, val)):
                            owner_id = df_survey.iloc[ind]['Owner_ID']
                            #print(str(owner_id) + ' : ' + str(val))
                            column_errors += 1
                            total_errors += 1
                            add_to_dict(all_errors, owner_id, column_name)
                            break
                    except:
                        print('Error: The condition ' + condition + ' cannot be applied to this column.')
                        sys.exit()

            # Ideas: fix data here. Complicated but definitely doable
                # distinguish blank entries from entries with incorrect formatting!!!
                # replace __VALUE_SEPARATOR with commas
                # remove columns with high percentage error > 90% error
                # remove individual bad datapoints to make them blank
                # try to guess datapoints using ML or something


            # calculate and print percentage of errors
            percent_clean = 1 - column_errors / df_survey[column_name].size 
            print(' ')
            print(str(column_errors) + ' column errors found, approximately ' + str(int(percent_clean*100)) + '% clean')
            print(' ')
            print(' ')

            if percent_clean < bad: bad_columns.update([column_name])
        
        # column not being checked
        else:           
            print('Not analyzed')
            print('')

    # calculates and prints percentage of errors
    print(' ')
    print(str(len(bad_columns)) + ' columns with more than ' + str(int(100*(1-bad))) + '% errors:')
    for col in bad_columns:
        print(col)
    print('')
    total_percent = 100 * (1 - total_errors / (len(df_survey) * len(column_names)))
    print('Total errors found: ' + str(total_errors) + ', approximately ' + str(int(total_percent)) + '% clean.')
    print('Please note: blank entries are also counted as errors (for now).')
    print('Total errors fixed: ' + str(int(total_fixed)))
    print(' ')

def add_to_dict(diction, key, val):
    '''adds element to list in dict entry'''
    if key in diction: diction[key].append(val)
    else: diction[key] = [val]

def export_to_csv():
    '''exports to csv file'''
    pass

def print_new_column(col):
    '''prints messages to terminal'''
    print('')
    print('-----------------------------------------------------------------')
    print('Errors in - ' + col)
    print('')
    print('OWNER ID                             : INPUT')

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

# sample column names
birth = 'Date_of_birth__use_calendar_to_select_or_enter_as_MM_DD_YYYY___BirthDate_'
sex = 'Sex__PatientSex_'
height_units = 'Height_-_please_select_unit__HeightMeasure_'
height = 'Height__PatientHeight_'

# update when we identify the mistakes of new columns
column_headings = [birth, sex, height]


#fix column formatting
column_formatting()
column_headings = list(df_survey.columns.values)
#column_headings = ['What_type_s__of_health_insurance_do_you_have?_Please_check_all_that_apply.__HealthInsurance_']

# find errors
bad = 0.95 # threshold percentage of errors for a column to be considered bad
print('')
print('running...')
find_errors(column_headings)


# export errors to csv file

# To-Do's:
# allow code to read all files in a directory depending on values input into command line
# write extra exception for invalid months and days
# write read-me for how to use file
# allow for conditions and constants to be read from csv file (kind of like a UI for the script!)
# write key/rules for formatting of conditions and parameters
