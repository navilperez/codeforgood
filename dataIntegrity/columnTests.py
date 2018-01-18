import pandas as pd
import datetime

'''DI TESTS'''
'''Any additional tests need to be put here with these and then added to the dictionary below the tests.'''
'''A return of True means the test is passed, False means an error that needs to be recorded'''

def is_string(x):
    '''checks if x is string'''
    try:
        return isinstance(x, str)
    except:
        return False

def is_valid_date(x):
    '''checks if date is valid format'''
    try:
        datetime.datetime.strptime(x,'%Y-%m-%d')
        return True
    except:
        return False

def is_21_yrs_old(x):
    '''checks if a date is at least 21 years old'''
    '''note: does not check when entry was made, only from today's date'''
    try:
        today = datetime.datetime.today()
        birthdate = datetime.datetime.strptime(x, '%Y-%m-%d')
        return today - birthdate >= datetime.timedelta(days=7665) #21 years
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

'''Here are the tests for each column for each of the excel docouments. Make the key exactly the value
of the column header in excel as string (without any newline at the end), and map it to a LIST of whichever
DI test functions above should be applied'''

columnTests = {
    'Owner ID':
        [is_string],
    'Instance ID':
        [],
    'Date of birth (use calendar to select or enter as MM/DD/YYYY) (BirthDate)':
        [is_string, is_valid_date, is_21_yrs_old],
    'Sex (PatientSex)':
        [is_string],
    'Height - please select unit (HeightMeasure)':
        [is_string],
    'Height (PatientHeight)':
        [is_positive],
    'Weight (PatienWeight)':
        [is_positive],
    'Weight measure (WeightMeasure)':
        [is_string],
    'Dominant hand (Domhand)':
        [is_string],
    'Education - number of years completed (including kindergarten, elementary school, middle school, high school, and all post-high school education) (Yearsofeducation)':
        [is_atleast_zero],
    'Highest level of education (HighEducLevel)':
        [is_string],
    'Current marital status (MaritalStatus)':
        [is_string],
    'Employment status - select one (EmployStatus)':
        [is_string],
    'Please indicate age when disabled (DisableAge)':
        [is_positive],  
    'Please indicate age when retired (RetiredAge)':
        [is_positive],
    'Do you live with other people or in a group setting? (LiveWithOtherPeople)':
        [is_string],
    'What type(s) of health insurance do you have? Please check all that apply. (HealthInsurance)':
        [is_string],
    'What is the name of your insurer? (NameofInsurer)':
        [],
    'If other, please specify. (OtherInsurance)':
        [],
    'Please indicate which of the following categories best represents your household income: (Household income)':
        [is_number],
    '[DomesticStatus1]:Living with spouse/partner (LivingwithSpouse)':
        [is_Y_or_N],
    '[DomesticStatus1]:Living with sibling (LivingwithSibling)':
        [is_Y_or_N],
    '[DomesticStatus1]:Living with children (LivingwithChildren)':
        [is_Y_or_N],
    '[DomesticStatus1]:Living with parent (LivingwithParent)':
        [is_Y_or_N],
    '[DomesticStatus1]:Living with other relative (LivingwithOtherRelative)':
        [is_Y_or_N],
    '[DomesticStatus1]:Living with friend/companion (LivingwithFriend)':
        [is_Y_or_N],
    '[DomesticStatus1]:Living with domestic help (LivingwithDomesticHelp)':
        [is_Y_or_N]
}


"""
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

def is_21_yrs(date):
    '''helper: checks if a date is at least 21 years old'''
    today = datetime.datetime.today()
    age = datetime.timedelta(years=21)
    year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])
    birthdate = datetime.date(year, month, day)

    return today - birthdate >= age
"""