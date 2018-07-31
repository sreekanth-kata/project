
import time
from collections import OrderedDict

tic=time.time()
rootDir = 'Z:\MESSDATEN'
#%%
def existDictFn(fname):   
     if ('\xb0' or '\xef\xbf\xbd') not in fname:          
          fList = fname.split('_') 
#          if fList[5]!='1000rpm':
          try:
               KH_indx = fList.index('KH')   #test 'KH' as index
               
               da_te = fList[KH_indx-3]     
               ti_me = fList[KH_indx-2]                         
               r_pm = fList[KH_indx+1]      
               if r_pm == '1000rpm':
                    r_pm = r_pm.split('r')[0]
               
               if fList[KH_indx+2] is 'SK' or 'RON95' or 'NK' or 'E10':
                    f_uel = fList[KH_indx+2]
               else: 
                    print 'Fuel Type unknown in path {}'.format(fname)                         
                    
               sr = fList[KH_indx+3]          
               opp = fList[KH_indx+4]                      
               
          except:
               A_indx = fList.index('A')     #test 'A' as index, when 'KH' fails
               
               da_te = fList[A_indx-2]     
               ti_me = fList[A_indx-1]         
               
               r_pm = fList[A_indx+1].strip('KH')                  
               if fList[A_indx+2] is 'SK' or 'RON95' or 'NK' or 'E10':
                    f_uel = fList[A_indx+2]
               else: 
                    print 'Fuel Type unknown in path {}'.format(fname)    
                    
               sr = fList[A_indx+3]          
               opp = fList[A_indx+4]   
          
          finally:        
               measr = 'catalyst heating'                       
               fdict = OrderedDict((zip(('date','time','file_name','filepath','Measurement','rpm','fuel','SR','OPP'), 
                                 (da_te, ti_me, fname, rootDir, measr, r_pm, f_uel, sr, opp))))               
               return fdict  
          
     else:     #2 types of degree exists; one of them is with extraNumber after fuel
          degree = u"\u00b0"
          if '\xb0' in fname:     
               fN = fname.split('\xb0')              
          if '\xef\xbf\xbd' in fname:
               fN = fname.split('\xef\xbf\xbd')             
          
          fN.insert(1, degree)
          fnameNew = ''.join(fN)
          print 'File name in Degree Format='
          print fnameNew          
          fList = fnameNew.split('_')          
          KH_indx = fList.index('KH')
          
          if ('\xb0' in fname and '180' not in fname) or '\xef\xbf\xbd' in fname:
                    sr = fList[KH_indx+4].encode('ascii', 'ignore')
                    opp = fList[KH_indx+5].encode('ascii', 'ignore')
          else:
               if '\xb0' in fname:      #Only 180, NO 10,20 degrees
                    sr = fList[KH_indx+3].encode('ascii', 'ignore')
                    opp = fList[KH_indx+6].encode('ascii', 'ignore')
               
          if fList[KH_indx+2] is 'SK' or 'RON95' or 'NK' or 'E10':
               f_uel = fList[KH_indx+2].encode('ascii', 'ignore')
          else: 
               print 'Fuel Type unknown in FILE path.'        
          
          da_te = fList[KH_indx-3].encode('ascii', 'ignore')
          ti_me = fList[KH_indx-2].encode('ascii', 'ignore')          
          r_pm = fList[KH_indx+1].encode('ascii', 'ignore')           
          
          measr = 'catalyst heating'
          
          fdict = OrderedDict((zip(('date','time','file_name','filepath','Measurement','rpm','fuel','SR','OPP'), 
                            (da_te, ti_me, fnameNew.encode('ascii', 'ignore'), rootDir, measr, r_pm, f_uel, sr, opp))))     
          return fdict
    
#fdict =  existDictFn(fname)
#print fdict
#%%
toc=time.time()
print(str("%.2f" %(toc-tic)) + ' seconds elapsed')         
     
