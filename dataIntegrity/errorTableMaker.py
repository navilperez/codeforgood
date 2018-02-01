import pandas as pd
import datetime
import columnTests
import numpy as np
import os

'''Things that need to be added to python for this to work:

pandas
datetime
numpy 
matplotlib (eventually)
openpyxl (just in case of dependencies)
xlrd (just in case of dependencies)
xlwt (just in case of dependencies)
xlsxwriter (just in case of dependencies)
'''
#TODO make a .bat to install the above to python3
#using command 'python -m pip install [library]'
#and make sure to write instructions for installing python 3
#including making sure to check 'add to path' during installation

'''We need to ask some questions to Sara, and also write a readme 
saying they have to re-save the xls files, as pandas thinks they are corrupted

Note to self, make custom error reminding that this needs to be done.
Maybe add a logger too
'''




#Here's where the files are set for now
#Later we can make it iterate through a directory or take some other input
#such as command line argument, depending on usage needs
__DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = __DIR_PATH+"/exampleData/dem_info.xls"
OUTPUT = __DIR_PATH+"/testErrorTable/dem_info_errors.xlsx"



def makeDataFrameFromExcel(excel_file):
	'''Make Data Frame From Excel
	
	Makes a pandas DataFrame from an excel file
	containing only the first sheet of said file.
	Removes default Nan values
	
	Arguments:
		excel_file {string} -- filepath to excel file
	
	Returns:
		pandas DataFrame -- DataFrame with '' instead of default NaN
	'''
	frame = pd.read_excel(excel_file)
	frame = frame.replace(np.nan, '', regex=True)
	return frame

def makeErrorTable(data):
	'''Make Error Table
	
	Makes Excel file of errors.

	The file has the structure of the original dataa
	with one additional column containing columns in
	error for each row.
	
	Arguments:
		data {DataFrame} -- The raw data to test
	
	Returns:
		bool -- True
	'''
	dataCopy = data.copy(deep=True)
	errorFrame = runTests(dataCopy)
	errorFrame = errorFrame[errorFrame.error_columns != '']
	makeOutputExcel(errorFrame)
	return True

def makeOutputExcel(df):
	'''Make Output Excel
	
	Writes a DataFrame to an Excel file.
	Makes header row bold.
	
	Arguments:
		df {DataFrame} -- DataFrame to write
	
	Returns:
		bool -- True
	'''
	outputFileName = makeOutputFilename()
	writer = pd.ExcelWriter(outputFileName, engine='xlsxwriter')
	df.to_excel(writer, index=False, sheet_name="Errors")
	workbook = writer.book
	worksheet = writer.sheets['Errors']
	header_fmt = workbook.add_format({'bold': True})
	worksheet.set_row(0, None, header_fmt)
	writer.save()
	return True

def makeOutputFilename():
	#Until I get around to this, it just returns the default
	#eventually it will be a function of the input file name
	return OUTPUT

def testAllCols(row):
	'''Test All Columns
	
	Tests all the column fields for a particular row,
	using the DATA DataFrame initialized with this .py file
	
	Arguments:
		row {ndarray} -- row from DataFrame, raw form
	
	Returns:
		string -- headers of all columns in error for row
	'''
	errorColumns = []
	for cind, column in row.iteritems():
		if column!="":
			tests = getTests(cind)
			for test in tests:
				if not test(column):
					errorColumns.append(cind)
					break
	errorColumnsString = ", ".join(errorColumns)
	return errorColumnsString

def runTests(df):
	'''Run Tests
	
	Applies testAllCols to each row in df,
	saving result in a new column: error_columns
	
	Arguments:
		df {DataFrame} -- copy of initial DATA
	
	Returns:
		DataFrame -- df with a new column detailing errors
	'''
	df['error_columns'] = df.apply(testAllCols, axis=1, raw=False)
	return df

def getTests(col):
	'''Get Tests
	
	Retrieves all tests for a particular field
	by checking columnTests file
	
	Arguments:
		col {str} -- column title from DATA
	
	Returns:
		list -- list of functions returning True if passed, False otherwise
	'''
	return columnTests.FIELD_TESTS[col]

#Global original DataFrame
DATA = makeDataFrameFromExcel(FILENAME)	

if __name__ == '__main__':
	makeErrorTable(DATA)