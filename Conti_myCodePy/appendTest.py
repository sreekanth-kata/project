import csv, time, pickle
from pprint import pprint
#write csv data to exist excel and save the filename
#open temp_Daten3.csv write fields to file and close the file
tic=time.time()
import temp_Daten3Dict, create_dictFile
rootDir = 'D:\Skata\Sreekanth_pc'
path = rootDir + '\messung'
temp_path = path + '\\temp_daten3.csv'
fname = path + '\M996_20171110_150822_A_KH_1200_SK_SR26917_OPP3-2_IND'+'\M996_20171110_150822_A_KH_1200_SK_SR26917_OPP3-2_IND.xls'
i=count=0

gotList1 = temp_Daten3Dict.existDictFn()   
gotList2 = create_dictFile.funTest()   
fdict_ = pickle.load(open("savef.p", "rb"))
ndict_ = pickle.load(open("save.p", "rb"))

#list3 = fdict_+ndict_
head_new = []
for x in ndict_:
    head_new.append(x.keys())
head_new_ = map(';'.join, head_new)
#print head_new             #ndict_.keys(); header to be added(appended)
head_new = str(head_new_)
head_new = ';'.join(i for i in head_new.split(','))
head_new = head_new.replace("'","")

#write to excel code
with open(temp_path, "rb") as fr, open(temp_path, "ab") as fw:
    reader= csv.reader(fr)
    data_= list(reader)
    header= data_[0][0].split(";")
#    print(header)     #header has to be dictionaries
#    headList = header+head_new_ #Contains all the headerList including the ones to be added    
    
    writer= csv.DictWriter(fw, fieldnames=[head_new])    
    writer.writeheader()

    
print('\n')        
print(count)        
toc=time.time()
pprint(str("%.2f" %(toc-tic)) + ' seconds elapsed')  
