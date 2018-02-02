############## CODE FOR GOOD IAP 2018 DATA CLEANER README ######################

Made by Friederike Buck, Navil Perez, Romeo Florez, and Ben Gruber

This readme details how the data cleaning script works.


First, this script requires an installation of Python 3. It also requires a few
additional libraries. The .bat file titled 'install_libraries.bat' will do this
for you on Windows if the term 'python' in cmd defaults to Python 3 on your
machine. If you want to do it manually, you can see a list of the libraries by
opening the .bat file as a text file.


All the necessary files are currently (as I write this) in a folder called
'dataIntegrity'. The name of this folder doesn't matter, but the structure of
the directory DOES matter. Within this folder, there needs to be a folder called
'surveyData', the python files 'columnTests.py' and 'errorTableMaker.py', and
the Excel workbook 'TestSettings.xlsx'.


The folder 'surveyData' is where raw data goes in AND where error information
comes out. Put excel files of survey info here, and once the script is run,
there will be new excel files with the names of the original files plus '_errors'
detailing the possibly erroneous rows.

							***IMPORTANT***
The code thinks that the raw data as we originally received it is corrupt!
You MUST open the raw data in Excel and click 'save as' and save a new copy
of it to fix this! I recommend taking the original data and saving it to the 
'surveyData' folder with a shorter, more descriptive name. ONLY these new
copies 

'columnTests.py' contains all the functions that are used to test data fields
from the raw survey excel files. To add tests, there are a few simple steps:
1. Create your test function along with the other functions (this location matters,
you shouldn't put it later down in the file). Make sure that it takes in one
argument and returns True or False. Note that with pandas, the data library
used for this tool, pandas will guess the type of the field that it finds in the
raw data, (i.e. a cell with '13' will by default be a float, but the cell 'kssdf'
will be a string). This affects the input type of the function, and can be used
to your advantage.
2. Add your test to the dictionary 'TEST_MAPPING' later down in the file, mapping
a title for your test as a string to the name of your function.
3. Using the key that you made in (2), add a column with that exact title to the
'TestSettings.xlsx' file (and check the rows for that column accordingly to use 
the test).

'errorTableMaker.py' actually reads the raw data and creates the excel file(s) with errors.
It relies on the pandas library to do this. It doesn't need to be edited much,
unless if you want to change the name of the file 'surveyData', in which case you
have to change the variable 'FOLDER_NAME' accordingly. It will read any excel files
in the folder 'surveyData' that are Excel workbooks that don't end in '_errors'.
It can handle multiple flies at once, it doens't need to be one at a time in
'surveyData'.
							***IMPORTANT***
To run the data cleaner, you just run 'errorTableMaker.py'.

'TestSettings.xlsx' is read in order to determine which tests are applied to which
columns. Every survey field being tested should be in this file! If not, it will
throw an exception (which is caught and just printed to console). Any non-empty
cell will be read to mean that that row's field should undergo that column's test.
Any empty cell will be ignored.