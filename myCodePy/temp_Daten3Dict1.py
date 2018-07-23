import time, csv
from pprint import pprint
tic=time.time()

#%% 
rootDir= 'Z:\MESSDATEN'
fname_= rootDir+ '\\temp_daten3.csv'

fr= open(fname_)
reader= csv.reader(fr)
data_= list(reader)
header= data_[0][0].split(";")    #print(header) 

i=0
#for rows
for i in range(0,len(data_)):
    if [len(j) for j in [s.replace(';', '') for s in data_[i]]][0]:
        numofrow= i              #print(numofrow) 


da_te=[]; ti_me=[]; f_name=[]; f_path=[]; measr=[]; s_r=[]; r_pm=[]; fu_el=[]; o_pp=[];
#for cols 
daten=[[0 for i in range(len(header))] for j in range(0,numofrow-1)]
prevList= []
def existDictFn():
    for i in range(0,numofrow-1):
        for j in range(len(header)):  
            daten[i][j]= data_[i+1][0].split(";")[j]     	
#            fdict = {}   #Initialize empty dictionary
    
            def funWrite():
            #create all the header-value dict list    
                 if(j==header.index('date')): 
                      da_te.append(daten[i][header.index('date')])
                      if i==numofrow-3:
#                           print da_te 
                           date= (", ".join(repr(e) for e in da_te)) 
                           ndict = {'date':date}   
                           return ndict
                      
                 if(j==header.index('time')): 
                      ti_me.append(daten[i][header.index('time')])
                      if i==numofrow-3:
#                           print ti_me 
                           time= (", ".join(repr(e) for e in ti_me)) 
                           ndict = {'time':time}   
                           return ndict
                 if(j==header.index('file_name')): 
                      f_name.append(daten[i][header.index('file_name')])
                      if i==numofrow-3:
#                           print f_name 
                           file_name= (", ".join(repr(e) for e in f_name)) 
                           ndict = {'file_name':file_name}   
                           return ndict
                 if(j==header.index('file_path')): 
                      f_path.append(daten[i][header.index('file_path')])
                      if i==numofrow-3:
#                           print f_path 
                           file_path= (", ".join(repr(e) for e in f_path)) 
                           ndict = {'file_path':file_path}  
                           return ndict
                 if(j==header.index('Measurement')): 
                      measr.append(daten[i][header.index('Measurement')])
                      if i==numofrow-3:
#                           print measr 
                           Measurement= (", ".join(repr(e) for e in measr)) 
                           ndict = {'Measurement':Measurement}   
                           return ndict
                 if(j==header.index('SR')): 
                      s_r.append(daten[i][header.index('SR')])
                      if i==numofrow-3:
#                           print s_r 
                           SR = (", ".join(repr(e) for e in s_r)) 
                           ndict = {'Measurement':SR}    
                           return ndict
                 if(j==header.index('rpm')): 
                      r_pm.append(daten[i][header.index('rpm')])
                      if i==numofrow-3:
#                           print r_pm 
                           rpm= (", ".join(repr(e) for e in r_pm)) 
                           ndict = {'rpm':rpm}    #create dictionary by adding header-values
                           return ndict
                 if(j==header.index('fuel')): 
                      fu_el.append(daten[i][header.index('fuel')])
                      if i==numofrow-3:
#                           print fu_el 
                           fuel= (", ".join(repr(e) for e in fu_el)) 
                           ndict = {'fuel':fuel}  
                           return ndict
                 if(j==header.index('OPP')): 
                      o_pp.append(daten[i][header.index('OPP')])
                      if i==numofrow-3:
#                           print o_pp 
                           OPP= (", ".join(repr(e) for e in o_pp)) 
                           ndict = {'OPP':OPP}    
                           return ndict
                     
#                 
#            fdict = funWrite()       
#            # call the existing dictionary fun               
#            if funWrite()!=None:     
#                 if 'date' in fdict:             prevList.append(fdict)
#                 if 'time' in fdict:             prevList.append(fdict)
#                 if 'file_name' in fdict:        prevList.append(fdict)  
#                 if 'file_path' in fdict:        prevList.append(fdict)
#                 if 'Measurement' in fdict:      prevList.append(fdict)
#                 if 'SR' in fdict:               prevList.append(fdict)
#                 if 'rpm' in fdict:              prevList.append(fdict)
#                 if 'fuel' in fdict:             prevList.append(fdict)
#                 if 'OPP' in fdict:              prevList.append(fdict)
#    
#    return prevList          
#print existDictFn()    
#%%                  
fr.close()
print('\n')        
toc=time.time()
pprint(str("%.2f" %(toc-tic)) + ' seconds elapsed')  
