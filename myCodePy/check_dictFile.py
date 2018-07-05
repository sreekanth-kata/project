import csv, time
from os.path import join, basename
from os import walk, chdir,rename, listdir, getcwd

tic=time.time()
rootDir = 'D:\Skata\Sreekanth_pc'
i=count=0
#numMeas=len(xlsname) 
path = rootDir + '\messung'
fname = path + '\M996_20171110_150822_A_KH_1200_SK_SR26917_OPP3-2_IND'+'\M996_20171110_150822_A_KH_1200_SK_SR26917_OPP3-2_IND.xls'

f = open(fname)
r = csv.reader(f)
data = list(r)
#            print(data)              print('\n')
header=data[1][0].split("\t")
#unit=data[2][0].split("\t") #print(unit) #print(unit) #print(len(header))
#print(header)      #print("HederCount: %s"%len(header))        #print('\n')

#for rows
for i in range(0,len(data)):
    if [len(j) for j in [s.replace('\t', '') for s in data[i]]][0]:
        numofrow=i
#                    print(numofrow) # count= count+1

#for cols
daten=[[0 for i in range(len(header))] for j in range(0,numofrow-2)]
#print(len(header))
for i in range(0,numofrow-2):
    for j in range(len(header)):  
        daten[i][j]=data[i+3][0].split("\t")[j]
#        if(daten[i][j]==daten[i][0]):
#            print(daten[i][0])   

        if(header.index('N_M')):
            ind = header.index('N_M')
            if(j==ind):
                N_M_val = []
                for i in range(0,len(daten)):
                    N_M_val.append(daten[i][ind])  
#                                                      
        if(header.index('TQ_M')):
            ind = header.index('TQ_M')
            if(j==ind):
                TQ_M_val = daten[i][ind]
                
               
        if(j == ind):                
            ndict = {'N_M':N_M_val}
            print(ndict['N_M'])
                
                
#            print(ndict['TQ_M'])
#                print('x'*40)
            
        
           
print('\n')        
print(count)        
toc=time.time()
print(str("%.2f" %(toc-tic)) + ' seconds elapsed')    


#*************************************************************************
#copy_csvFile
import csv, time#, shutil
from os.path import join, basename
from os import walk, chdir,rename, listdir, getcwd

tic=time.time()
rootDir = 'D:\Skata\Sreekanth_pc'
i=count=0
#numMeas=len(xlsname) 
csvLoc = rootDir+ '\\temp_daten3.csv'
path = rootDir + '\messung'


for dirName, subDir, fList in walk(path):
    for fname in fList:
        if fname.endswith('.xls'):
#            print('\nFound dir: %s\nFound File: %s' %(dirName, fname))
            
            fullpath = join(path, dirName)
            chdir(fullpath)
#            print('Curdir is:%s'%getcwd()) 
#            shutil.copy(csvLoc, fullpath)     # copy csv format file into dir
            
            # rename the csv format file
        if(fname.endswith('daten3.csv')):
            print(fname)
            name = basename(dirName)
            print(rename(fname,name))
            
            
#    break           
print('\n')        
print(count)        
toc=time.time()
print(str("%.2f" %(toc-tic)) + ' seconds elapsed')    
