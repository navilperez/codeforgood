import pandas as pd
import datetime
import numpy as np
import os

__DIR_PATH = os.path.dirname(os.path.realpath(__file__))
__EXCEL_FILE = __DIR_PATH+"/TestSettings.xlsx"

'''DI TESTS'''
'''Any additional tests need to be put here with these and then added to the dictionary below the tests.'''
'''A return of True means the test is passed, False means an error that needs to be recorded'''

def is_string(x):
    '''checks if x is string'''
    try:
        return isinstance(x, str)
    except:
        return False

def is_valid_birthdate(x):
    '''checks if date is valid format and somewhat reasonable'''
    try:
        bdate = datetime.datetime.strptime(x,'%Y-%m-%d')
        today = datetime.datetime.today()
        return (today - bdate < datetime.timedelta(days = 54750)) and (today - bdate >= datetime.timedelta(days=7665)) #no one over 150 years old or under 21
    except:
        return False

def is_positive(x):
    '''checks if x is number-like object and greater than 0'''
    try:
        if x>0:
            return True
        else:
            return False
    except:
        return False

def is_number(x):
    '''checks if x is number-like object'''
    try:
        return (isinstance(x, float) or isinstance(x, int))
    except:
        return False

def is_Y_or_N(x):
    '''checks if x is "Y" or "N" '''
    try:
        return (str(x) == 'Y' or str(x) == 'N')
    except:
        return False

def is_atleast_zero(x):
    '''checks if x is atleast 0 as float'''
    try:
        return float(x)>=0
    except:
        return False

'''Here are the mappings from the excel file to test functions they represent'''
TEST_MAPPING = {
    'Is a string of characters (not a plain number)': is_string,
    'Is a number': is_number,
    'Is a number atleast zero': is_atleast_zero,
    'Is a positive number': is_positive,
    'Is a valid birthdate (over 21, under 150)': is_valid_birthdate,
    "Is 'Y' or 'N'": is_Y_or_N
}

def makeTestSchedule():
    '''Make Test Schedule
    
    Reads excel file of test settings,
    and then makes a dictionary of which
    tests apply to which column
    
    Returns:
        dict -- maps column names (str) to lists of test functions
    '''
    df = pd.read_excel(__EXCEL_FILE)
    df = df.replace(np.nan, '', regex=True)
    fieldTests = readSettingSpreadsheet(df)
    return fieldTests
    

def readSettingSpreadsheet(df):
    '''Read Settings Spreadsheet
    
    Does the nitty gritty of reading the spreadsheet,
    in which cells that have values signify a test for a
    column, and empty cells do not.
    
    Arguments:
        df {DataFrame} -- Created by makeTestSchedule
    
    Returns:
        dict -- maps column names (str) to lists of test functions
    '''
    fieldTests = {}
    for rind, row in df.iterrows():
        fieldTests[rind] = []
        for cind, col in row.iteritems():
            if col!='':
                try:
                    fieldTests[rind].append(TEST_MAPPING[cind])
                except:
                    print("PROBLEM!! Tests don't line up with the spreadsheet")
    return fieldTests


FIELD_TESTS = makeTestSchedule()





def test(FIELD_TESTS):
    #Just a test function for seeing what happened in reading spreadsheet
    for key in FIELD_TESTS:
        print(key)
        for x in FIELD_TESTS[key]:
            print(len(FIELD_TESTS[key]))
            print(x.__name__)

if __name__ == '__main__':
    test(FIELD_TESTS)