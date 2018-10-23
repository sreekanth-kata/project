import time
from collections import OrderedDict

tic=time.time()
rootDir = 'Z:\MESSDATEN'
path = rootDir+'\Dai'
#%%
def existDictFn(fname):
     fList = fname.split('_')      
     measr = 'catalyst heating'  
     if ('\xb0' or '\xef\xbf\xbd') not in fname:                   
          try:
               KH_indx = fList.index('KH')    #test 'KH' as index    
               
               da_te = fList[KH_indx-3]
               ti_me = fList[KH_indx-2] 
               r_pm = fList[KH_indx+1]  
               sr = fList[KH_indx+3]
               if fList[KH_indx+2] is 'SK' or 'RON95' or 'NK' or 'E10':
                    f_uel = fList[KH_indx+2] 
               if r_pm == '1000rpm':
                    r_pm = r_pm.split('r')[0]  
                    
               opp = fList[KH_indx+4]  
               if fList[KH_indx+4] == 'SK': # 2 'SK' in fList, second one after sr
                    opp = fList[KH_indx+6]    
               if 'SR' not in sr or 'OPP' not in opp:                    
                    sr = fList[KH_indx+4]
                    opp = fList[KH_indx+5]  
               if 'Spacer' in fname:
                    opp = fList[KH_indx+5]    
               if 'Spacer_1mm' in fname:
                    opp = fList[KH_indx+6]  
               
          except:
               A_indx = fList.index('A')   #test 'A' as index, when 'KH' fails
               
               da_te = fList[A_indx-2]     
               ti_me = fList[A_indx-1]
               r_pm = fList[A_indx+1].strip('KH')  
               sr = fList[A_indx+3]   
               opp = fList[A_indx+4]      
                                              
               if fList[A_indx+2] is 'SK' or 'RON95' or 'NK' or 'E10':
                    f_uel = fList[A_indx+2]
                              
               if 'Spacer' in fname:
                    opp = fList[A_indx+5] 
               if 'Spacer_1mm' in fname:
                    opp = fList[A_indx+6]
                    
               if 'SR' not in sr or 'OPP' not in opp:
                    sr = fList[A_indx+4]
                    opp = fList[A_indx+5]  
          finally:                 
               if 'OPP' not in opp:
                    with open(path+"\\fNotOPP.txt","ab") as fN:
                      fN.write(fname+'\r\n')                      
               
               fdict = OrderedDict(zip(('date','time','file_name','filepath','Measurement','rpm','fuel','SR','OPP'), 
                                 (da_te, ti_me, fname, path, measr, r_pm, f_uel, sr, opp)))               
               return fdict  
          
     else:     #2 types of degree exists; one of them is with extraNumber after fuel
#          degree = u"\u00b0"
          KH_indx = fList.index('KH')    #test 'KH' as index  (for eg: KH is KH1000)
                  
               
          da_te = fList[KH_indx-3]
          ti_me = fList[KH_indx-2] 
          r_pm = fList[KH_indx+1]  
          sr = fList[KH_indx+3]
          if fList[KH_indx+2] is 'SK' or 'RON95' or 'NK' or 'E10':
               f_uel = fList[KH_indx+2]
          
          if ('\xb0' in fname and '180' not in fname) or '\xef\xbf\xbd' in fname:
                    sr = fList[KH_indx+4]
                    opp = fList[KH_indx+5]                  
          else:
               if '\xb0' in fname:      #Only 180, NO 10,20 degrees
                    sr = fList[KH_indx+3]
                    opp = fList[KH_indx+6]
                    if '1.5Spacer' not in fname:
                         opp = fList[KH_indx+5]
               
          if 'OPP' not in opp:
               with open(path+"\\fNotOPP.txt","ab") as fN:
                    fN.write(fname+'\r\n')
          
          fdict = OrderedDict(zip(('date','time','file_name','filepath','Measurement','rpm','fuel','SR','OPP'), 
                            (da_te, ti_me, fname, path, measr, r_pm, f_uel, sr, opp)))     
          return fdict
    
#fdict =  existDictFn(fpath)
#print fdict
#%%
toc=time.time()
print(str("%.2f" %(toc-tic)) + ' seconds elapsed')         
     
