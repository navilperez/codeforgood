import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

df = pd.read_csv('/Users/navilcoding/visualization/diagnoses.csv')

df.set_index('Owner ID', inplace=True)



table1 = pd.crosstab(df["type"],df["exas"],margins=True)

def percConvert(ser):
  return ser/float(ser[-1])

table2 = pd.crosstab(df["type"],df["exas"],margins=True).apply(percConvert, axis=1)

dg = pd.read_csv('/Users/navilcoding/visualization/practicedata2.csv')
dg.set_index('Owner ID', inplace=True)
result = pd.concat([df, dg], axis=1, join='inner')
print (result)

table2 = pd.crosstab(result["type"],result["exas"],margins=True).apply(percConvert, axis=1)
print (table2)

# load and merge all files into the data frame
paths = []
# paths.append(os.getcwd()+'/survey-data/baseline data/demographics/')
# paths.append(os.getcwd()+'/survey-data/baseline data/MS History/')
# paths.append(os.getcwd()+'/survey-data/baseline data/demographics/')
# paths.append(os.getcwd()+'/survey-data/baseline data/other conditions/')
# paths.append(os.getcwd()+'/survey-data/baseline data/overall health/')
# paths.append(os.getcwd()+'/survey-data/baseline data/physical activity/')
# paths.append(os.getcwd()+'/survey-data/baseline data/QoL/')
# paths.append(os.getcwd()+'/survey-data/baseline data/Wellness and Data/')
#
# files = []
# for path in paths:
#     temp_files = os.listdir(path)
#     for f in temp_files:
#         files.append(path+f)
#
# files_csv = [f for f in files if f[-3:] =='csv']
# print (files_csv)
# df = pd.DataFrame()
# template = pd.read_csv(files_csv[0])
# template.set_index('Owner ID', inplace=True)
#
# df = pd.concat([df, template],axis=1)
#
#
# for f in files_csv[1:]:
#     data = pd.read_csv(f)
#     data.set_index('Owner ID', inplace=True)
#     df = pd.concat([df,data],axis=1)
