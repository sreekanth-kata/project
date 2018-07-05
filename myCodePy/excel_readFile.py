import csv, time
from os.path import join
from os import walk, chdir#, listdir, getcwd

tic=time.time()
rootDir = 'D:\Skata\Sreekanth_pc'
xlsname='M996_20171110_150822_A_KH_1200_SK_SR26917_OPP3-3_IND.xls'
i=count=0
#numMeas=len(xlsname) 

path = rootDir + '\messung'
for dirName, subDir, fList in walk(path):
    for fname in fList:
        if fname.endswith('.xls'):
            print('\nFound dir: %s\nFound File: %s' %(dirName, fname))
            
            fullpath = join(path, dirName)
            chdir(fullpath)
#            print('Curdir is:%s'%getcwd()) 
                                                           
            f = open(fname)
            r = csv.reader(f)
            data = list(r)
#            print(data)              print('\n')
            header=data[1][0].split("\t")
#            unit=data[2][0].split("\t") #print(unit) #print(unit) #print(len(header))
            print(header)
            
            for i in range(0,len(data)):
                if [len(j) for j in [s.replace('\t', '') for s in data[i]]][0]:
                    numofrow=i
#                    print(numofrow) # count= count+1
        
            daten=[[0 for i in range(len(header))] for j in range(0,numofrow-2)]
            for i in range(0,numofrow-2):
                for j in range(len(header)):                    
                    daten[i][j]=data[i+3][0].split("\t")[j]
#                    print(daten[i][j])
                    
#                print ('-*'*40)   #                print('\n')

break            
print('\n')        
print(count)        
toc=time.time()
print(str("%.2f" %(toc-tic)) + ' seconds elapsed')    
