Internship project contains two main programs in python:

excel_readFile.py: 
It searches through all 1000 folders in directory to find an excel file(xls) with its name matching to that of the directory name. 
Then its filters required keys from all the available headers and maps the data to these keys. 

temp_Daten3Dict.py: 
To split the pathName of the folder. 
Repeat them exactly to the available rows of data times(dynamically) of the excel file. 
The pathName is recursively split and combined to this formated data. 
The result is finally written to single excel file using python library.
