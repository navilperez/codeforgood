import pandas as pd
import datetime
import numpy as np

__EXCEL_FILE = "TestSettings.xlsx"

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

def is_atleast_zero(x):
    '''checks if x is atleast 0 as float'''
    try:
        return float(x)>=0
    except:
        return False

def is_zipcode(x):
    return True

def is_int_in_range(x, start, end):
    '''checks if x is number in provided range'''
    try:
        return int(x) in range(start, end + 1)
    except: 
        return False

def is_1_or_2(x):
    '''checks if x is number in range 1 -> 2'''
    
    return is_int_in_range(x, 1, 2)
    
def is_1_to_5(x):
    '''checks if x is number in range 1 -> 5'''
    
    return are_valid_Numbers(x, range(1,6))

def is_1_to_3(x):
    '''checks if x is number in range 1 -> 3'''
    
    return is_int_in_range(x, 1, 3)

def is_0_to_2(x):
    '''checks if x is number in range 0 -> 2'''
    
    return is_int_in_range(x, 0, 2)

def is_0_to_10(x):
    '''checks if x is number in range 1 -> 10'''
    
    return is_int_in_range(x, 0, 10)

def is_0_to_4(x):
    '''checks if x is number in range 0 -> 4'''
    
    return is_int_in_range(x, 0, 4)

def is_in_Choices(x, choices):
    '''checks if x is in list of possible choices'''
    
    return str(x) in choices

def is_Yes_or_No(x):

    return is_in_Choices(x, ["Yes", "No"]);


def is_WellnessActivities_choice(x):

    return is_in_Choices(x, ["ActivitiesUsed", "ActivitiesHelpful"])

def is_VitaminsMinerals_choice(x):

    return is_in_Choices(x, ["VitMinUsed", "VitMinHelpful"])

def is_Supplements_choice(x):

    return is_in_Choices(x, ["SupplementsUsed",  "SupplementHelpful"])

def is_Diet_choice(x):
    
    return is_in_Choices(x, ["DietUsed", "DietHelpful"])

def is_high_cholesterol_drug(x):

    hcDrugs = ["Alirocumab", "Atorvastatin", "Cholestyramine", "Colesevelam", "Colestipol", "Evolocumab", "Ezetimibe", "Fenofibrate", "Fluvastatin", "Gemfibrozil", "Lovastatin", "Niacin", "Pitavastatin", "Pravastatin", "Rosuvastatin", "Simvastatin", "Other"]

    return are_valid_Choices(x, hcDrugs)
    

def is_Yes_No_DontKnow(x):

    return is_in_Choices(x, ["Yes", "No", "DontKnow"])

def is_HasMSChoice(x):
    return is_in_Choices(x, ["ProbablyHaveMS", "NotSureHaveMS", "DontHaveMS"])

def is_form_of_MS(x):
    return is_in_Choices(x, ["CIS", "rrms", "spms","ppms", "ris", "99"])

def is_Yes_No_DontKnow_NA(x):
    return is_in_Choices(x, ["Yes", "No", "IDontKnow", "Notapplicable"])

def is_MS_Diagnostic_Test(x):
    
   
    print(tests)

    return are_valid_Choices(x, ["HeadMRI", "SpinalcordMRI", "SpinalFluidTest", "BloodTest", "DiagnosticEvoked", "NeurologicalExamination", "Other", "NoTest", "NotSure"])

def are_valid_Numbers(inputString, choices):

    print("inputString", inputString)
    print("choices", choices)

    try: 
        if int(inputString) in choices:
            return True
    except: 
        try: 
            inputArray = [int(elt) for elt in inputString.split(',')]
            print(inputArray)
            for elt in inputArray:
                if elt not in choices:
                    return False
            return True
        except:
            return False

def are_valid_Choices(inputString, choices):
    

    inputArray = [elt.strip() for elt in inputString.split(',')]
    for elt in inputArray:
        if elt not in choices:
            return False
    return True

def is_HowDidPersonHelp_choice(x):
    return is_in_Choices(x, ["ReadOrEntered", "Answered", "OtherHelp"])

def is_date(x):########################
    return True
def is_email(x):##########################
    return True

'''Here are the mappings from the excel file to test functions they represent'''
TEST_MAPPING = {
    'Is a string of characters (not a plain number)': is_string,
    'Is a number': is_number,
    'Is a number atleast zero': is_atleast_zero,
    'Is a positive number': is_positive,
    'Is a valid birthdate (over 21, under 150)': is_valid_birthdate,
    "Is 'Y' or 'N'": is_Y_or_N,
    "Is an integer between 1 to 2": is_1_or_2,
    "Is an integer between 1 to 5": is_1_to_5,
    "Is an integer between 1 to 3": is_1_to_3,
    "Is an integer between 0 to 2": is_0_to_2,
    "Is an integer between 0 to 10": is_0_to_10,
    "Is an integer between 0 to 4": is_0_to_4,
    "is 'Yes' or 'No'": is_Yes_or_No,
    "Is WellnessActivities Choice": is_WellnessActivities_choice,
    "Is VitaminsMinerals Choice":is_VitaminsMinerals_choice,
    "Is Supplements Choice":is_Supplements_choice,
    "Is Diet Choice":is_Diet_choice,
    "Is High Cholesterol Drug": is_high_cholesterol_drug,
    "Is Yes, No, Don't Know": is_Yes_No_DontKnow,
    "Is HasMSChoice": is_HasMSChoice,
    "Is Form of MS": is_form_of_MS,
    "Is Yes, No, Not Applicable, Don't Know": is_Yes_No_DontKnow_NA,
    "Is MS Diagnostic Test": is_MS_Diagnostic_Test,
    "Is HowDidPersonHelp Choice": is_HowDidPersonHelp_choice,
    "is date": is_date,
    "is email":is_email
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