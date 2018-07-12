import time, csv
from pprint import pprint
tic=time.time()

#%% 
rootDir= 'D:\Skata\Sreekanth_pc'
path= rootDir+ '\messung'
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

#for cols
daten=[[0 for i in range(len(header))] for j in range(0,numofrow-1)]
prevList= []
def existDictFn():
    for i in range(0,numofrow-1):
        for j in range(len(header)):  
            daten[i][j]= data_[i+1][0].split(";")[j] 
            fdict = {}   #Initialize empty dictionary
    
            def funWrite():
            #create all the header-value dict list       
                
                ind = header.index('date')
                da_te= []
                if(j==ind):                
                    for i in range(0,len(daten)):
                        da_te.append(daten[i][ind]) 
                        da_te = da_te[:numofrow]                    
                    count = 0
                    count +=1
                    if (da_te[-1] and count==1):                        
                              da_te =( ', '.join( repr(e) for e in da_te ))                          
#                              print da_te                    
                              fdict = {'date':da_te}        
                              return fdict
                    
                if(header.index('time')):    
                    ind = header.index('time')            
                    ti_me= []
                    if(j==ind):
                        for i in range(0,len(daten)):
                            ti_me.append(daten[i][ind])                         
                            ti_me = ti_me[:numofrow]
                        if(ti_me[-1]):
                            ti_me =( ", ".join( repr(e) for e in ti_me ))                            
    #                        print ti_me
                            fdict = {'ti_me':ti_me}      
                            return fdict     
                        
                if(header.index('file_name')):    
                    ind = header.index('file_name')            
                    f_name= []
                    if(j==ind):
                        for i in range(0,len(daten)):
                            f_name.append(daten[i][ind]) 
                            f_name = f_name[:numofrow]
                        if(f_name[-1]):
                            f_name =( ", ".join( repr(e) for e in f_name ))
#                            print f_name
                            fdict = {'file_name':f_name}      
                            return fdict                     
                    
                    if(header.index('file_path')):     
                        ind = ind = header.index('file_path')
                        f_path= []
                        if(j==ind):                        
                            for i in range(0,len(daten)):
                                f_path.append(daten[i][ind]) 
                                f_path = f_path[:numofrow]
                            if(f_path[-1]):
                                f_path =( ", ".join( repr(e) for e in f_path ))
        #                        print f_path
                                fdict = {'file_path':f_path}        
                                return fdict
                            
                    if(header.index('Measurement')):            
                        ind = header.index('Measurement')
                        measr = []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                measr.append(daten[i][ind]) 
                                measr = measr[:numofrow]
                            if(measr[-1]):
                                measr =( ", ".join( repr(e) for e in measr ))
        #                        print measr
                                fdict = {'Measurement':measr}        
                                return fdict
                            
                    if(header.index('SR')): 
                        ind = header.index('SR')
                        s_r= []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                s_r.append(daten[i][ind])
                                s_r = s_r[:numofrow]
                            if(s_r[-1]):
                                s_r =( ", ".join( repr(e) for e in s_r ))
        #                        print s_r
                                fdict = {'SR':s_r}        
                                return fdict
                            
                    if(header.index('rpm')):
                        ind = header.index('rpm')
                        r_pm = []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                r_pm.append(daten[i][ind]) 
                                r_pm = r_pm[:numofrow]
                            if(r_pm[-1]):
                                r_pm =( ", ".join( repr(e) for e in r_pm ))
        #                        print r_pm 
                                fdict = {'rpm':r_pm}        
                                return fdict
                                
                    if(header.index('fuel')):  
                        ind = header.index('fuel')
                        f_uel= []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                f_uel.append(daten[i][ind]) 
                                f_uel = f_uel[:numofrow]
                            if(f_uel[-1]):
                                f_uel =( ", ".join( repr(e) for e in f_uel ))
        #                        print f_uel
                                fdict = {'fuel':f_uel}        
                                return fdict
                            
                    if(header.index('OPP')):
                        ind = header.index('OPP')
                        o_pp= []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                o_pp.append(daten[i][ind]) 
                                o_pp = o_pp[:numofrow]
                            if(o_pp[-1]):
                                o_pp =( ", ".join( repr(e) for e in o_pp ))
        #                        print o_pp 
                                fdict = {'OPP':o_pp}        
                                return fdict                           
            
            fdict = funWrite()       
            # call the existing dictionary fun               
            if funWrite()!=None:     
                    if 'date' in fdict:             prevList.append(fdict)
                    if 'time' in fdict:             prevList.append(fdict)
                    if 'file_name' in fdict:        prevList.append(fdict)  
                    if 'file_path' in fdict:        prevList.append(fdict)
                    if 'Measurement' in fdict:      prevList.append(fdict)
                    if 'SR' in fdict:               prevList.append(fdict)
                    if 'rpm' in fdict:              prevList.append(fdict)
                    if 'fuel' in fdict:             prevList.append(fdict)
                    if 'OPP' in fdict:              prevList.append(fdict)
    
    return prevList           
print existDictFn()    
#%%                  
fr.close()
print('\n')        
toc=time.time()
pprint(str("%.2f" %(toc-tic)) + ' seconds elapsed')  
