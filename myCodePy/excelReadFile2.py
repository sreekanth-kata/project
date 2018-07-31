import time, csv
import temp_DatenFDict
from os import walk, chdir#, getcwd
from os.path import join, basename#, listdir, 

rootDir = 'Z:\MESSDATEN'
path = rootDir+'\Dai'
fname_= path+ '\\temp_daten3.csv'
tic=time.time()
i=count=0; oneRowCt=0; RowCt=0; NotinFile=0

for dirName, subDir, fList in walk(path):    
    for fname in fList:
        if fname.endswith('.xls') and basename(dirName) == fname.split(".x")[0]:  
#            if count>2:
#                 break
            fullpath = join(path, dirName)
            chdir(fullpath) #print ('-'*80)       
           
            print('\nMoved to CurDir: %s\nFound File:%d --> %s' %(dirName, count, fname)) 
            
            count +=1            #print('Curdir is:%s'%getcwd                
            
            if 'OPP' in fname:                
                 f = open(fname)
                 r = csv.reader(f)
                 data = list(r)          #print(data) #print('\n')
                 header=data[1][0].split("\t")       #print(len(header))#print(header)  #unit=data[2][0].split("\t") #print(unit) #print(unit) 
                           
                 for i in range(0,len(data)):    #for rows
                      if [len(j) for j in [s.replace('\t', '') for s in data[i]]][0]:
                         numofrow=i      #print(numofrow)    
                            
                 daten=[[0 for i in range(len(header))] for j in range(0,numofrow-2)]         
                 myListT = []
                 N_M_val=[]; mass_cyl0_pls1=[]; mass_cyl0_pls2=[]; mass_cyl0_pls3=[]; mass_cyl0_pls4=[]; mass_cyl1_pls1=[]; mass_cyl1_pls2=[]; mass_cyl1_pls3=[]; mass_cyl1_pls4=[]; mass_cyl2_pls1=[]; mass_cyl2_pls2=[]; mass_cyl2_pls3=[]; mass_cyl2_pls4=[]; 
                 mass_cyl3_pls1=[]; mass_cyl3_pls2=[]; mass_cyl3_pls3=[]; mass_cyl3_pls4=[]; masssp=[]; soiia=[]; soi1=[]; soi2=[]; soi3=[]; CoV=[]; BSFC=[]; PN=[]; CO=[]; NOx=[]; lambdav=[]; HC=[]; TKAT=[]; std=[]; mitt=[]; cov=[]; std1=[]; std2=[]; std3=[]; std4=[]; 
                 mitt1=[]; mitt2=[]; mitt3=[]; mitt4=[]; cov1=[]; cov2=[]; cov3=[]; cov4=[]; mafm=[]; mafs=[]; ti_pls1_cyl0=[]; ti_pls2_cyl0=[]; ti_pls3_cyl0=[]; ti_pls4_cyl0=[]; ti_pls1_cyl1=[]; ti_pls2_cyl1=[]; ti_pls3_cyl1=[]; ti_pls4_cyl1=[]; 
                 ti_pls1_cyl2=[]; ti_pls2_cyl2=[]; ti_pls3_cyl2=[]; ti_pls4_cyl2=[]; ti_pls1_cyl3=[]; ti_pls2_cyl3=[]; ti_pls3_cyl3=[]; ti_pls4_cyl3=[]; soi_pls1_cyl0=[]; soi_pls2_cyl0=[]; soi_pls3_cyl0=[]; soi_pls4_cyl0=[]; soi_pls1_cyl1=[]; soi_pls2_cyl1=[]; soi_pls3_cyl1=[]; soi_pls4_cyl1=[]; 
                 soi_pls1_cyl2=[]; soi_pls2_cyl2=[]; soi_pls3_cyl2=[]; soi_pls4_cyl2=[]; soi_pls1_cyl3=[]; soi_pls2_cyl3=[]; soi_pls3_cyl3=[]; soi_pls4_cyl3=[]; ifile=[];
               
                 for i in range(0,numofrow-2):    #for cols
                      for j in range(len(header)):                    
                           daten[i][j]=data[i+3][0].split("\t")[j]     #print(daten[i][j])                   
                           ndict = {}   #Initialize empty dictionary  
                        
                           def funReturn():
               #           function to create dictionary key-value pairs with header-value dict-list
                                if(j==header.index('N_M')): 
                                     N_M_val.append(daten[i][header.index('N_M')])
                                     if i==numofrow-3:
                    #                                     print N_M_val 
                                          N_M= (", ".join(repr(e) for e in N_M_val)) 
                                          ndict = {'N_M':N_M}    #create dictionary by adding header-values
                                          return ndict
                                 
                                if(j==header.index('AS_MFF_STND_CYL_0_PLS_1_M')):                   
                                   mass_cyl0_pls1.append(daten[i][header.index('AS_MFF_STND_CYL_0_PLS_1_M')])
                                   if i==numofrow-3:
                    #                                     print mass_cyl0_pls1                         
                                        AS_MFF_STND_CYL_0_PLS_1_M= (", ".join(repr(e) for e in mass_cyl0_pls1)) 
                                        ndict = {'AS_MFF_STND_CYL_0_PLS_1_M':AS_MFF_STND_CYL_0_PLS_1_M} 
                                        return ndict         
                                        
                                if(j==header.index('AS_MFF_STND_CYL_0_PLS_2_M')):
                                   mass_cyl0_pls2.append(daten[i][header.index('AS_MFF_STND_CYL_0_PLS_2_M')])
                                   if i==numofrow-3:                       
                    #                                     print mass_cyl0_pls2
                                        AS_MFF_STND_CYL_0_PLS_2_M= (", ".join(repr(e) for e in mass_cyl0_pls2))                        
                                        ndict = {'AS_MFF_STND_CYL_0_PLS_2_M':AS_MFF_STND_CYL_0_PLS_2_M} 
                                        return ndict
                                   
                                if(j== header.index('AS_MFF_STND_CYL_0_PLS_3_M')):     
                                     mass_cyl0_pls3.append(daten[i][header.index('AS_MFF_STND_CYL_0_PLS_3_M')])  
                                     if i==numofrow-3:                        
                    #                                     print mass_cyl0_spls3
                                          AS_MFF_STND_CYL_0_PLS_3_M= (", ".join(repr(e) for e in mass_cyl0_pls3))  
                                          ndict = {'AS_MFF_STND_CYL_0_PLS_3_M':AS_MFF_STND_CYL_0_PLS_3_M}
                                          return ndict
                                          
                                if(j==header.index('AS_MFF_STND_CYL_0_PLS_4_M')):
                                     mass_cyl0_pls4.append(daten[i][header.index('AS_MFF_STND_CYL_0_PLS_4_M')])
                                     if i==numofrow-3:                        
                    #                                     print mass_cyl0_pls4
                                          AS_MFF_STND_CYL_0_PLS_4_M= (", ".join(repr(e) for e in mass_cyl0_pls4))  
                                          ndict = {'AS_MFF_STND_CYL_0_PLS_4_M':AS_MFF_STND_CYL_0_PLS_4_M} 
                                          return ndict
                                          
                                if(j==header.index('AS_MFF_STND_CYL_1_PLS_1_M')):
                                     mass_cyl1_pls1.append(daten[i][header.index('AS_MFF_STND_CYL_1_PLS_1_M')])
                                     if i==numofrow-3:                        
                    #                                     print mass_cyl1_pls1
                                          AS_MFF_STND_CYL_1_PLS_1_M= (", ".join(repr(e) for e in mass_cyl1_pls1))  
                                          ndict = {'AS_MFF_STND_CYL_1_PLS_1_M':AS_MFF_STND_CYL_1_PLS_1_M} 
                                          return ndict
                                              
                                if(j==header.index('AS_MFF_STND_CYL_1_PLS_2_M')):
                                     mass_cyl1_pls2.append(daten[i][header.index('AS_MFF_STND_CYL_1_PLS_2_M')])
                                     if i==numofrow-3:                        
                    #                                     print mass_cyl1_pls2
                                          AS_MFF_STND_CYL_1_PLS_2_M= (", ".join(repr(e) for e in mass_cyl1_pls2))
                                          ndict = {'AS_MFF_STND_CYL_1_PLS_2_M':AS_MFF_STND_CYL_1_PLS_2_M} 
                                          return ndict
                                     
                                if(j==header.index('AS_MFF_STND_CYL_1_PLS_3_M')):
                                     mass_cyl1_pls3.append(daten[i][header.index('AS_MFF_STND_CYL_1_PLS_3_M')])
                                     if i==numofrow-3:
                    #                                     print mass_cyl1_pls3
                                          AS_MFF_STND_CYL_1_PLS_3_M= (", ".join(repr(e) for e in mass_cyl1_pls3))  
                                          ndict = {'AS_MFF_STND_CYL_1_PLS_3_M':AS_MFF_STND_CYL_1_PLS_3_M} 
                                          return ndict
                                     
                                if(j==header.index('AS_MFF_STND_CYL_1_PLS_4_M')):
                                     mass_cyl1_pls4.append(daten[i][header.index('AS_MFF_STND_CYL_1_PLS_4_M')])
                                     if i==numofrow-3:
                    #                                     print mass_cyl1_pls4
                                          AS_MFF_STND_CYL_1_PLS_4_M= (", ".join(repr(e) for e in mass_cyl1_pls4))  
                                          ndict = {'AS_MFF_STND_CYL_1_PLS_4_M':AS_MFF_STND_CYL_1_PLS_4_M} 
                                          return ndict
                                                
                                if(j==header.index('AS_MFF_STND_CYL_2_PLS_1_M')):
                                     mass_cyl2_pls1.append(daten[i][header.index('AS_MFF_STND_CYL_2_PLS_1_M')])
                                     if i==numofrow-3:                        
                    #                                     print mass_cyl2_pls1
                                          AS_MFF_STND_CYL_2_PLS_1_M= (", ".join(repr(e) for e in mass_cyl2_pls1))  
                                          ndict = {'AS_MFF_STND_CYL_2_PLS_1_M':AS_MFF_STND_CYL_2_PLS_1_M} 
                                          return ndict
                                    
                                if(j==header.index('AS_MFF_STND_CYL_2_PLS_2_M')):
                                     mass_cyl2_pls2.append(daten[i][header.index('AS_MFF_STND_CYL_2_PLS_2_M')]) 
                                     if i==numofrow-3:                     
                    #                                     print mass_cyl2_pls2
                                          AS_MFF_STND_CYL_2_PLS_2_M= (", ".join(repr(e) for e in mass_cyl2_pls2))  
                                          ndict = {'AS_MFF_STND_CYL_2_PLS_2_M':AS_MFF_STND_CYL_2_PLS_2_M} 
                                          return ndict
                            
                                if(j==header.index('AS_MFF_STND_CYL_2_PLS_3_M')):
                                     mass_cyl2_pls3.append(daten[i][header.index('AS_MFF_STND_CYL_2_PLS_3_M')])
                                     if i==numofrow-3:                  
                    #                                     print mass_cyl2_pls3
                                          AS_MFF_STND_CYL_2_PLS_3_M= (", ".join(repr(e) for e in mass_cyl2_pls3))  
                                          ndict = {'AS_MFF_STND_CYL_2_PLS_3_M':AS_MFF_STND_CYL_2_PLS_3_M}
                                          return ndict
                            
                                if(j==header.index('AS_MFF_STND_CYL_2_PLS_4_M')):
                                     mass_cyl2_pls4.append(daten[i][header.index('AS_MFF_STND_CYL_2_PLS_4_M')]) 
                                     if i==numofrow-3:                   
                    #                                     print mass_cyl2_pls4
                                          AS_MFF_STND_CYL_2_PLS_4_M= (", ".join(repr(e) for e in mass_cyl2_pls4))  
                                          ndict = {'AS_MFF_STND_CYL_2_PLS_4_M':AS_MFF_STND_CYL_2_PLS_4_M} 
                                          return ndict
                                             
                                if(j==header.index('AS_MFF_STND_CYL_3_PLS_1_M')):                      
                                     mass_cyl3_pls1.append(daten[i][header.index('AS_MFF_STND_CYL_3_PLS_1_M')])
                                     if i==numofrow-3:                        
                    #                                     print mass_cyl3_pls1
                                          AS_MFF_STND_CYL_3_PLS_1_M= (", ".join(repr(e) for e in mass_cyl3_pls1))  
                                          ndict = {'AS_MFF_STND_CYL_3_PLS_1_M':AS_MFF_STND_CYL_3_PLS_1_M}
                                          return ndict
                                 
                                if(j==header.index('AS_MFF_STND_CYL_3_PLS_2_M')):
                                     mass_cyl3_pls2.append(daten[i][header.index('AS_MFF_STND_CYL_3_PLS_2_M')])
                                     if i==numofrow-3:                        
                    #                                     print mass_cyl3_pls2
                                          AS_MFF_STND_CYL_3_PLS_2_M= (", ".join(repr(e) for e in mass_cyl3_pls2))  
                                          ndict = {'AS_MFF_STND_CYL_3_PLS_2_M':AS_MFF_STND_CYL_3_PLS_2_M}
                                          return ndict
                                 
                                if(j==header.index('AS_MFF_STND_CYL_3_PLS_3_M')):
                                     mass_cyl3_pls3.append(daten[i][header.index('AS_MFF_STND_CYL_3_PLS_3_M')])
                                     if i==numofrow-3:                   
                    #                                     print mass_cyl3_pls3
                                          AS_MFF_STND_CYL_3_PLS_3_M= (", ".join(repr(e) for e in mass_cyl3_pls3))  
                                          ndict = {'AS_MFF_STND_CYL_3_PLS_3_M':AS_MFF_STND_CYL_3_PLS_3_M} 
                                          return ndict
                                 
                                if(j==header.index('AS_MFF_STND_CYL_3_PLS_4_M')):
                                     mass_cyl3_pls4.append(daten[i][header.index('AS_MFF_STND_CYL_3_PLS_4_M')]) 
                                     if i==numofrow-3:                       
                    #                                     print mass_cyl3_pls4
                                          AS_MFF_STND_CYL_3_PLS_4_M= (", ".join(repr(e) for e in mass_cyl3_pls4))  
                                          ndict = {'AS_MFF_STND_CYL_3_PLS_4_M':AS_MFF_STND_CYL_3_PLS_4_M}
                                          return ndict
                                       
                                if(j==header.index('AS_MFF_SP_HOM_MV_M')):                    
                                     masssp.append(daten[i][header.index('AS_MFF_SP_HOM_MV_M')]) 
                                     if i==numofrow-3:                   
                    #                                     print masssp
                                          AS_MFF_SP_HOM_MV_M= (", ".join(repr(e) for e in masssp))  
                                          ndict = {'AS_MFF_SP_HOM_MV_M':AS_MFF_SP_HOM_MV_M} 
                                          return ndict
                              
                                if(j==header.index('AS_IGA_AV_MV_M')):
                                     soiia.append(daten[i][header.index('AS_IGA_AV_MV_M')])
                                     if i==numofrow-3:                        
                    #                                     print soiia
                                          AS_IGA_AV_MV_M= (", ".join(repr(e) for e in soiia))  
                                          ndict = {'AS_IGA_AV_MV_M':AS_IGA_AV_MV_M} 
                                          return ndict
                                 
                                if(j==header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M')):       # soi 1. injection
                                     soi1.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M')])  
                                     if i==numofrow-3:                        
                    #                                     print soi1
                                          AS_SOI_MES_CUS_PLS_1_CYL_1_M= (", ".join(repr(e) for e in soi1))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_1_M':AS_SOI_MES_CUS_PLS_1_CYL_1_M} 
                                          return ndict
                            
                                if(j==header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M')):       # soi 2. injection
                                     soi2.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M')])
                                     if i==numofrow-3:
                    #                                     print soi2
                                          AS_SOI_MES_CUS_PLS_3_CYL_0_M= (", ".join(repr(e) for e in soi2))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_0_M':AS_SOI_MES_CUS_PLS_3_CYL_0_M} 
                                          return ndict
                                 
                                if(j==header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M')):       # soi 3. injection
                                     soi3.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print soi3
                                          AS_SOI_MES_CUS_PLS_4_CYL_1_M= (", ".join(repr(e) for e in soi3))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_1_M':AS_SOI_MES_CUS_PLS_4_CYL_1_M} 
                                          return ndict
                                 
                                if(j==header.index('ISY_PI_V')):
                                     CoV.append(daten[i][header.index('ISY_PI_V')])  
                                     if i==numofrow-3:                        
                    #                                     print CoV
                                          ISY_PI_V= (", ".join(repr(e) for e in CoV))  
                                          ndict = {'ISY_PI_V':ISY_PI_V} 
                                          return ndict
                                      
                                if(j==header.index('C_CNS_06_M')):
                                     BSFC.append(daten[i][header.index('C_CNS_06_M')])
                                     if i==numofrow-3:                        
                    #                                     print BSFC
                                          C_CNS_06_M= (", ".join(repr(e) for e in BSFC))  
                                          ndict = {'C_CNS_06_M':C_CNS_06_M} 
                                          return ndict
                                 
                                if(j==header.index('PAC1_DL_CONC_49_M')):
                                     PN.append(daten[i][header.index('PAC1_DL_CONC_49_M')])  
                                     if i==numofrow-3:
                    #                                     print PN
                                          PAC1_DL_CONC_49_M= (", ".join(repr(e) for e in PN))  
                                          ndict = {'PAC1_DL_CONC_49_M':PAC1_DL_CONC_49_M} 
                                          return ndict
                                 
                                if(j==header.index('EG1_CO_15_M')):
                                     CO.append(daten[i][header.index('EG1_CO_15_M')])  
                                     if i==numofrow-3:                        
                    #                                     print CO
                                          EG1_CO_15_M= (", ".join(repr(e) for e in CO))  
                                          ndict = {'EG1_CO_15_M':EG1_CO_15_M} 
                                          return ndict
                             
                                if(j==header.index('EG1_NOX_16_M')):
                                     NOx.append(daten[i][header.index('EG1_NOX_16_M')])
                                     if i==numofrow-3:                        
                    #                                     print NOx
                                          EG1_NOX_16_M= (", ".join(repr(e) for e in NOx))  
                                          ndict = {'EG1_NOX_16_M':EG1_NOX_16_M}                          
                                          return ndict
                             
                                if(j==header.index('AS_LAMB_LS_UP_M')):
                                     lambdav.append(daten[i][header.index('AS_LAMB_LS_UP_M')])
                                     if i==numofrow-3:                        
                    #                                     print lambdav
                                          AS_LAMB_LS_UP_M= (", ".join(repr(e) for e in lambdav))  
                                          ndict = {'AS_LAMB_LS_UP_M':AS_LAMB_LS_UP_M}                          
                                          return ndict
                             
                                if(j==header.index('EG1_THC_16_M')):
                                     HC.append(daten[i][header.index('EG1_THC_16_M')]) 
                                     if i==numofrow-3:
                    #                                     print HC
                                          EG1_THC_16_M= (", ".join(repr(e) for e in HC))  
                                          ndict = {'EG1_THC_16_M':EG1_THC_16_M} 
                                          return ndict
                             
                                if(j==header.index('T_B1CAT1B1_M')):
                                     TKAT.append(daten[i][header.index('T_B1CAT1B1_M')])
                                     if i==numofrow-3:                        
                    #                                     print TKAT
                                          T_B1CAT1B1_M= (", ".join(repr(e) for e in TKAT))  
                                          ndict = {'T_B1CAT1B1_M':T_B1CAT1B1_M} 
                                          return ndict
                                         
                                if(j==header.index('ISY_PI_S')):
                                     std.append(daten[i][header.index('ISY_PI_S')]) 
                                     if i==numofrow-3:                        
                    #                                     print std
                                          ISY_PI_S= (", ".join(repr(e) for e in std))  
                                          ndict = {'ISY_PI_S':ISY_PI_S} 
                                          return ndict
                              
                                if(j==header.index('ISY_PI_M')):
                                     mitt.append(daten[i][header.index('ISY_PI_M')])  
                                     if i==numofrow-3:                        
                    #                                     print mitt
                                          ISY_PI_M= (", ".join(repr(e) for e in mitt))  
                                          ndict = {'ISY_PI_M':ISY_PI_M} 
                                          return ndict
                             
                                if(j==header.index('ISY_PI_V')):
                                     cov.append(daten[i][header.index('ISY_PI_V')])
                                     if i==numofrow-3:                        
                    #                                     print cov
                                          ISY_PI_V= (", ".join(repr(e) for e in cov))  
                                          ndict = {'ISY_PI_V':ISY_PI_V} 
                                          return ndict
                             
                                if(j==header.index('ISY_PI1_S')):
                                     std1.append(daten[i][header.index('ISY_PI1_S')]) 
                                     if i==numofrow-3:                        
                    #                                     print std1
                                          ISY_PI1_S= (", ".join(repr(e) for e in std1))  
                                          ndict = {'ISY_PI1_S':ISY_PI1_S} 
                                          return ndict
                             
                                if(j==header.index('ISY_PI2_S')):
                                     std2.append(daten[i][header.index('ISY_PI2_S')]) 
                                     if i==numofrow-3:                        
                    #                                     print std2
                                          ISY_PI2_S= (", ".join(repr(e) for e in std2))  
                                          ndict = {'ISY_PI2_S':ISY_PI2_S} 
                                          return ndict
                         
                                if(j==header.index('ISY_PI3_S')):
                                     std3.append(daten[i][header.index('ISY_PI3_S')])
                                     if i==numofrow-3:                        
                    #                                     print std3
                                          ISY_PI3_S= (", ".join(repr(e) for e in std3))  
                                          ndict = {'ISY_PI3_S':ISY_PI3_S} 
                                          return ndict
                             
                                if(j==header.index('ISY_PI4_S')):
                                     std4.append((daten[i][header.index('ISY_PI4_S')]))
                                     if i==numofrow-3:                        
                    #                                     print std4
                                          ISY_PI4_S= (", ".join(repr(e) for e in std4))  
                                          ndict = {'ISY_PI4_S':ISY_PI4_S}       
                                          return ndict
                                        
                                if(j==header.index('ISY_PI1_M')):
                                     mitt1.append(daten[i][header.index('ISY_PI1_M')]) 
                                     if i==numofrow-3:                   
                    #                                     print mitt1
                                          ISY_PI1_M= (", ".join(repr(e) for e in mitt1))  
                                          ndict = {'ISY_PI1_M':ISY_PI1_M}
                                          return ndict
                             
                                if(j==header.index('ISY_PI2_M')): 
                                     mitt2.append(daten[i][header.index('ISY_PI2_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print mitt2
                                          ISY_PI2_M= (", ".join(repr(e) for e in mitt2))  
                                          ndict = {'ISY_PI2_M':ISY_PI2_M} 
                                          return ndict
                              
                                if(j==header.index('ISY_PI3_M')): 
                                     mitt3.append(daten[i][header.index('ISY_PI3_M')])
                                     if i==numofrow-3:                        
                    #                                     print mitt3
                                          ISY_PI3_M= (", ".join(repr(e) for e in mitt3))  
                                          ndict = {'ISY_PI3_M':ISY_PI3_M}
                                          return ndict
                             
                                if(j==header.index('ISY_PI4_M')): 
                                     mitt4.append(daten[i][header.index('ISY_PI4_M')]) 
                                     if i==numofrow-3:                      
                    #                                     print mitt4
                                          ISY_PI4_M= (", ".join(repr(e) for e in mitt4))  
                                          ndict = {'ISY_PI4_M':ISY_PI4_M} 
                                          return ndict
                             
                                if(j==header.index('ISY_PI1_V')):
                                     cov1.append(daten[i][header.index('ISY_PI1_V')])
                                     if i==numofrow-3:                      
                    #                                     print cov1
                                          ISY_PI1_V= (", ".join(repr(e) for e in cov1))  
                                          ndict = {'ISY_PI1_V':ISY_PI1_V} 
                                          return ndict
                              
                                if(j==header.index('ISY_PI2_V')):
                                     cov2.append(daten[i][header.index('ISY_PI2_V')])
                                     if i==numofrow-3:                        
                    #                                     print cov2
                                          ISY_PI2_V= (", ".join(repr(e) for e in cov2))  
                                          ndict = {'ISY_PI2_V':ISY_PI2_V} 
                                          return ndict
                             
                                if(j==header.index('ISY_PI3_V')):
                                     cov3.append(daten[i][header.index('ISY_PI3_V')])
                                     if i==numofrow-3:                        
                    #                                     print cov3
                                          ISY_PI3_V= (", ".join(repr(e) for e in cov3))  
                                          ndict = {'ISY_PI3_V':ISY_PI3_V} 
                                          return ndict
                             
                                if(j==header.index('ISY_PI4_V')):
                                     cov4.append(daten[i][header.index('ISY_PI4_V')])  
                                     if i==numofrow-3:                        
                    #                                     print cov4
                                          ISY_PI4_V= (", ".join(repr(e) for e in cov4))  
                                          ndict = {'ISY_PI4_V':ISY_PI4_V} 
                                          return ndict
                                    
                                if(j==header.index('AS_MAF0_03_M')):
                                     mafm.append(daten[i][header.index('AS_MAF0_03_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print mafm
                                          AS_MAF0_03_M= (", ".join(repr(e) for e in mafm))  
                                          ndict = {'AS_MAF0_03_M':AS_MAF0_03_M} 
                                          return ndict
                             
                                if(j==header.index('AS_MAF0_03_S')):
                                     mafs.append(daten[i][header.index('AS_MAF0_03_S')]) 
                                     if i==numofrow-3: 
                    #                                     print mafs
                                          AS_MAF0_03_S= (", ".join(repr(e) for e in mafs))  
                                          ndict = {'AS_MAF0_03_S':AS_MAF0_03_S} 
                                          return ndict
                      
                                if(j==header.index('AS_TI_MES_4_PLS_1_CYL_0_M')):
                                     ti_pls1_cyl0.append(daten[i][header.index('AS_TI_MES_4_PLS_1_CYL_0_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls1_cyl0
                                          AS_TI_MES_4_PLS_1_CYL_0_M= (", ".join(repr(e) for e in ti_pls1_cyl0))  
                                          ndict = {'AS_TI_MES_4_PLS_1_CYL_0_M':AS_TI_MES_4_PLS_1_CYL_0_M} 
                                          return ndict
                                  
                                if(j==header.index('AS_TI_MES_4_PLS_2_CYL_0_M')):
                                     ti_pls2_cyl0.append(daten[i][header.index('AS_TI_MES_4_PLS_2_CYL_0_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls2_cyl0
                                          AS_TI_MES_4_PLS_2_CYL_0_M= (", ".join(repr(e) for e in ti_pls2_cyl0))  
                                          ndict = {'AS_TI_MES_4_PLS_2_CYL_0_M':AS_TI_MES_4_PLS_2_CYL_0_M} 
                                          return ndict
                      
                                if(j==header.index('AS_TI_MES_4_PLS_3_CYL_0_M')):
                                     ti_pls3_cyl0.append(daten[i][header.index('AS_TI_MES_4_PLS_3_CYL_0_M')])
                                     if i==numofrow-3:                        
                    #                                     print ti_pls3_cyl0
                                          AS_TI_MES_4_PLS_3_CYL_0_M= (", ".join(repr(e) for e in ti_pls3_cyl0))  
                                          ndict = {'AS_TI_MES_4_PLS_3_CYL_0_M':AS_TI_MES_4_PLS_3_CYL_0_M} 
                                          return ndict
                                                 
                                if(j==header.index('AS_TI_MES_4_PLS_4_CYL_0_M')):
                                     ti_pls4_cyl0.append(daten[i][header.index('AS_TI_MES_4_PLS_4_CYL_0_M')])
                                     if i==numofrow-3:                        
                    #                                     print ti_pls4_cyl0
                                          AS_TI_MES_4_PLS_4_CYL_0_M= (", ".join(repr(e) for e in ti_pls4_cyl0))  
                                          ndict = {'AS_TI_MES_4_PLS_4_CYL_0_M':AS_TI_MES_4_PLS_4_CYL_0_M}
                                          return ndict
                      
                                if(j==header.index('AS_TI_MES_4_PLS_1_CYL_1_M')):
                                     ti_pls1_cyl1.append(daten[i][header.index('AS_TI_MES_4_PLS_1_CYL_1_M')]) 
                                     if i==numofrow-3:                      
                    #                                     print ti_pls1_cyl1
                                          AS_TI_MES_4_PLS_1_CYL_1_M= (", ".join(repr(e) for e in ti_pls1_cyl1))  
                                          ndict = {'AS_TI_MES_4_PLS_1_CYL_1_M':AS_TI_MES_4_PLS_1_CYL_1_M} 
                                          return ndict
                            
                                if(j==header.index('AS_TI_MES_4_PLS_2_CYL_1_M')):
                                     ti_pls2_cyl1.append(daten[i][header.index('AS_TI_MES_4_PLS_2_CYL_1_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls2_cyl1
                                          AS_TI_MES_4_PLS_2_CYL_1_M= (", ".join(repr(e) for e in ti_pls2_cyl1))
                                          ndict = {'AS_TI_MES_4_PLS_2_CYL_1_M':AS_TI_MES_4_PLS_2_CYL_1_M} 
                                          return ndict
                             
                                if(j==header.index('AS_TI_MES_4_PLS_3_CYL_1_M')):
                                     ti_pls3_cyl1.append(daten[i][header.index('AS_TI_MES_4_PLS_3_CYL_1_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls3_cyl1
                                          AS_TI_MES_4_PLS_3_CYL_1_M= (", ".join(repr(e) for e in ti_pls3_cyl1)) 
                                          ndict = {'AS_TI_MES_4_PLS_3_CYL_1_M':AS_TI_MES_4_PLS_3_CYL_1_M}
                                          return ndict
                             
                                if(j==header.index('AS_TI_MES_4_PLS_4_CYL_1_M')):
                                     ti_pls4_cyl1.append(daten[i][header.index('AS_TI_MES_4_PLS_4_CYL_1_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls4_cyl1
                                          AS_TI_MES_4_PLS_4_CYL_1_M= (", ".join(repr(e) for e in ti_pls4_cyl1))  
                                          ndict = {'AS_TI_MES_4_PLS_4_CYL_1_M':AS_TI_MES_4_PLS_4_CYL_1_M} 
                                          return ndict
                             
                                if(j==header.index('AS_TI_MES_4_PLS_1_CYL_2_M')):
                                     ti_pls1_cyl2.append(daten[i][header.index('AS_TI_MES_4_PLS_1_CYL_2_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls1_cyl2
                                          AS_TI_MES_4_PLS_1_CYL_2_M= (", ".join(repr(e) for e in ti_pls1_cyl2))  
                                          ndict = {'AS_TI_MES_4_PLS_1_CYL_2_M':AS_TI_MES_4_PLS_1_CYL_2_M} 
                                          return ndict
                                 
                                if(j==header.index('AS_TI_MES_4_PLS_2_CYL_2_M')):
                                     ti_pls2_cyl2.append(daten[i][header.index('AS_TI_MES_4_PLS_2_CYL_2_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls2_cyl2
                                          AS_TI_MES_4_PLS_2_CYL_2_M= (", ".join(repr(e) for e in ti_pls2_cyl2))  
                                          ndict = {'AS_TI_MES_4_PLS_2_CYL_2_M':AS_TI_MES_4_PLS_2_CYL_2_M}
                                          return ndict
                                    
                                if(j==header.index('AS_TI_MES_4_PLS_3_CYL_2_M')):
                                     ti_pls3_cyl2.append(daten[i][header.index('AS_TI_MES_4_PLS_3_CYL_2_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls3_cyl2
                                          AS_TI_MES_4_PLS_3_CYL_2_M= (", ".join(repr(e) for e in ti_pls3_cyl2))  
                                          ndict = {'AS_TI_MES_4_PLS_3_CYL_2_M':AS_TI_MES_4_PLS_3_CYL_2_M}
                                          return ndict
                             
                                if(j==header.index('AS_TI_MES_4_PLS_4_CYL_2_M')):
                                     ti_pls4_cyl2.append(daten[i][header.index('AS_TI_MES_4_PLS_4_CYL_2_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls4_cyl2
                                          AS_TI_MES_4_PLS_4_CYL_2_M= (", ".join(repr(e) for e in ti_pls4_cyl2))  
                                          ndict = {'AS_TI_MES_4_PLS_4_CYL_2_M':AS_TI_MES_4_PLS_4_CYL_2_M} 
                                          return ndict
                             
                                if(j==header.index('AS_TI_MES_4_PLS_1_CYL_3_M')):
                                     ti_pls1_cyl3.append(daten[i][header.index('AS_TI_MES_4_PLS_1_CYL_3_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls1_cyl3
                                          AS_TI_MES_4_PLS_1_CYL_3_M= (", ".join(repr(e) for e in ti_pls1_cyl3))  
                                          ndict = {'AS_TI_MES_4_PLS_1_CYL_3_M':AS_TI_MES_4_PLS_1_CYL_3_M} 
                                          return ndict
                                       
                                if(j==header.index('AS_TI_MES_4_PLS_2_CYL_3_M')):
                                     ti_pls2_cyl3.append(daten[i][header.index('AS_TI_MES_4_PLS_2_CYL_3_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls2_cyl3
                                          AS_TI_MES_4_PLS_2_CYL_3_M= (", ".join(repr(e) for e in ti_pls2_cyl3))  
                                          ndict = {'AS_TI_MES_4_PLS_2_CYL_3_M':AS_TI_MES_4_PLS_2_CYL_3_M}
                                          return ndict
                             
                                if(j==header.index('AS_TI_MES_4_PLS_3_CYL_3_M')):
                                     ti_pls3_cyl3.append(daten[i][header.index('AS_TI_MES_4_PLS_3_CYL_3_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls3_cyl3
                                          AS_TI_MES_4_PLS_3_CYL_3_M= (", ".join(repr(e) for e in ti_pls3_cyl3))  
                                          ndict = {'AS_TI_MES_4_PLS_3_CYL_3_M':AS_TI_MES_4_PLS_3_CYL_3_M}
                                          return ndict
                             
                                if(j==header.index('AS_TI_MES_4_PLS_4_CYL_3_M')):
                                     ti_pls4_cyl3.append(daten[i][header.index('AS_TI_MES_4_PLS_4_CYL_3_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print ti_pls4_cyl3
                                          AS_TI_MES_4_PLS_4_CYL_3_M= (", ".join(repr(e) for e in ti_pls4_cyl3))  
                                          ndict = {'AS_TI_MES_4_PLS_4_CYL_3_M':AS_TI_MES_4_PLS_4_CYL_3_M}
                                          return ndict
                           
                                if(j==header.index('AS_SOI_MES_CUS_PLS_1_CYL_0_M')):
                                     soi_pls1_cyl0.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_1_CYL_0_M')])
                                     if i==numofrow-3:                        
                    #                                     print soi_pls1_cyl0
                                          AS_SOI_MES_CUS_PLS_1_CYL_0_M= (", ".join(repr(e) for e in soi_pls1_cyl0))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_0_M':AS_SOI_MES_CUS_PLS_1_CYL_0_M}
                                          return ndict
                                 
                                if(j==header.index('AS_SOI_MES_CUS_PLS_2_CYL_0_M')):
                                     soi_pls2_cyl0.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_2_CYL_0_M')])  
                                     if i==numofrow-3:                        
                    #                                     print soi_pls2_cyl0
                                          AS_SOI_MES_CUS_PLS_2_CYL_0_M= (", ".join(repr(e) for e in soi_pls2_cyl0))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_2_CYL_0_M':AS_SOI_MES_CUS_PLS_2_CYL_0_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M')):
                                     soi_pls3_cyl0.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print soi_pls3_cyl0
                                          AS_SOI_MES_CUS_PLS_3_CYL_0_M= (", ".join(repr(e) for e in soi_pls3_cyl0))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_0_M':AS_SOI_MES_CUS_PLS_3_CYL_0_M} 
                                          return ndict
                        
                                if(j==header.index('AS_SOI_MES_CUS_PLS_4_CYL_0_M')):
                                     soi_pls4_cyl0.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_4_CYL_0_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print soi_pls4_cyl0
                                          AS_SOI_MES_CUS_PLS_4_CYL_0_M= (", ".join(repr(e) for e in soi_pls4_cyl0))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_0_M':AS_SOI_MES_CUS_PLS_4_CYL_0_M} 
                                          return ndict
                           
                                if(j==header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M')):
                                     soi_pls1_cyl1.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print soi_pls1_cyl1
                                          AS_SOI_MES_CUS_PLS_1_CYL_1_M= (", ".join(repr(e) for e in soi_pls1_cyl1))                            
                                          ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_1_M':AS_SOI_MES_CUS_PLS_1_CYL_1_M} 
                                          return ndict
                           
                                if(j==header.index('AS_SOI_MES_CUS_PLS_2_CYL_1_M')):
                                     soi_pls2_cyl1.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_2_CYL_1_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print soi_pls2_cyl1
                                          AS_SOI_MES_CUS_PLS_2_CYL_1_M= (", ".join(repr(e) for e in soi_pls2_cyl1))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_2_CYL_1_M':AS_SOI_MES_CUS_PLS_2_CYL_1_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_3_CYL_1_M')):
                                     soi_pls3_cyl1.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_3_CYL_1_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print soi_pls3_cyl1
                                          AS_SOI_MES_CUS_PLS_3_CYL_1_M= (", ".join(repr(e) for e in soi_pls3_cyl1))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_1_M':AS_SOI_MES_CUS_PLS_3_CYL_1_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M')):
                                     soi_pls4_cyl1.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print soi_pls4_cyl1
                                          AS_SOI_MES_CUS_PLS_4_CYL_1_M= (", ".join(repr(e) for e in soi_pls4_cyl1))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_1_M':AS_SOI_MES_CUS_PLS_4_CYL_1_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_1_CYL_2_M')):
                                     soi_pls1_cyl2.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_1_CYL_2_M')]) 
                                     if i==numofrow-3:
                    #                                     print soi_pls1_cyl2
                                          AS_SOI_MES_CUS_PLS_1_CYL_2_M= (", ".join(repr(e) for e in soi_pls1_cyl2))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_2_M':AS_SOI_MES_CUS_PLS_1_CYL_2_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_2_CYL_2_M')):
                                     soi_pls2_cyl2.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_2_CYL_2_M')]) 
                                     if i==numofrow-3:                        
                    #                                     print soi_pls2_cyl2
                                          AS_SOI_MES_CUS_PLS_2_CYL_2_M= (", ".join(repr(e) for e in soi_pls2_cyl2))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_2_CYL_2_M':AS_SOI_MES_CUS_PLS_2_CYL_2_M}
                                          return ndict
                        
                                if(j==header.index('AS_SOI_MES_CUS_PLS_3_CYL_2_M')):
                                     soi_pls3_cyl2.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_3_CYL_2_M')])
                                     if i==numofrow-3:                    
                    #                                   print soi_pls3_cyl2
                                          AS_SOI_MES_CUS_PLS_3_CYL_2_M= (", ".join(repr(e) for e in soi_pls3_cyl2))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_2_M':AS_SOI_MES_CUS_PLS_3_CYL_2_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_4_CYL_2_M')):
                                     soi_pls4_cyl2.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_4_CYL_2_M')]) 
                                     if i==numofrow-3:                    
                    #                                     print soi_pls4_cyl2
                                          AS_SOI_MES_CUS_PLS_4_CYL_2_M= (", ".join(repr(e) for e in soi_pls4_cyl2))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_2_M':AS_SOI_MES_CUS_PLS_4_CYL_2_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_1_CYL_3_M')):
                                     soi_pls1_cyl3.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_1_CYL_3_M')])  
                                     if i==numofrow-3:                    
                    #                                     print soi_pls1_cyl3
                                          AS_SOI_MES_CUS_PLS_1_CYL_3_M= (", ".join(repr(e) for e in soi_pls1_cyl3))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_3_M':AS_SOI_MES_CUS_PLS_1_CYL_3_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_2_CYL_3_M')):                            
                                     soi_pls2_cyl3.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_2_CYL_3_M')])  
                                     if i==numofrow-3:
                    #                                     print soi_pls2_cyl3
                                          AS_SOI_MES_CUS_PLS_2_CYL_3_M= (", ".join(repr(e) for e in soi_pls2_cyl3))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_2_CYL_3_M':AS_SOI_MES_CUS_PLS_2_CYL_3_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_3_CYL_3_M')):
                                     soi_pls3_cyl3.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_3_CYL_3_M')]) 
                                     if i==numofrow-3:                    
                    #                                   print soi_pls3_cyl3
                                          AS_SOI_MES_CUS_PLS_3_CYL_3_M= (", ".join(repr(e) for e in soi_pls3_cyl3))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_3_M':AS_SOI_MES_CUS_PLS_3_CYL_3_M} 
                                          return ndict
                             
                                if(j==header.index('AS_SOI_MES_CUS_PLS_4_CYL_3_M')):        
                                     soi_pls4_cyl3.append(daten[i][header.index('AS_SOI_MES_CUS_PLS_4_CYL_3_M')]) 
                                     if i==numofrow-3:                    
                    #                                     print soi_pls4_cyl3
                                          AS_SOI_MES_CUS_PLS_4_CYL_3_M= (", ".join(repr(e) for e in soi_pls4_cyl3))  
                                          ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_3_M':AS_SOI_MES_CUS_PLS_4_CYL_3_M} 
                                          return ndict
                                 
                                if(j==header.index('ISY_STRING_IFILE_NAME')):                            
                                     ifile.append(daten[i][header.index('ISY_STRING_IFILE_NAME')])  
                                     if i==numofrow-3:                  
                    #                                     print ifile
                                          ISY_STRING_IFILE_NAME= (", ".join(repr(e) for e in ifile))  
                                          ndict = {'ISY_STRING_IFILE_NAME':ISY_STRING_IFILE_NAME} 
                                          return ndict                    
                                       
                           ndict = funReturn()      #call the dictionary function    
                           if ndict!=None:                            
                                if 'N_M' in ndict:                             myListT.append(ndict)     
                                if 'AS_MFF_STND_CYL_0_PLS_1_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_0_PLS_2_M' in ndict:       myListT.append(ndict)                           
                                if 'AS_MFF_STND_CYL_0_PLS_3_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_0_PLS_4_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_1_PLS_1_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_1_PLS_2_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_1_PLS_3_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_1_PLS_4_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_2_PLS_1_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_2_PLS_2_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_2_PLS_3_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_2_PLS_4_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_3_PLS_1_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_3_PLS_2_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_3_PLS_3_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_STND_CYL_3_PLS_4_M' in ndict:       myListT.append(ndict)
                                if 'AS_MFF_SP_HOM_MV_M' in ndict:              myListT.append(ndict)
                                if 'AS_IGA_AV_MV_M' in ndict:                  myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_1_CYL_1_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_3_CYL_0_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_4_CYL_1_M' in ndict:    myListT.append(ndict)
                                if 'ISY_PI_V' in ndict:                        myListT.append(ndict)
                                if 'C_CNS_06_M' in ndict:                      myListT.append(ndict)
                                if 'PAC1_DL_CONC_49_M' in ndict:               myListT.append(ndict)
                                if 'EG1_CO_15_M' in ndict:                     myListT.append(ndict)
                                if 'EG1_NOX_16_M' in ndict:                    myListT.append(ndict)
                                if 'AS_LAMB_LS_UP_M' in ndict:                 myListT.append(ndict)
                                if 'EG1_THC_16_M' in ndict:                    myListT.append(ndict)
                                if 'T_B1CAT1B1_M' in ndict:                    myListT.append(ndict)
                                if 'ISY_PI_S' in ndict:                        myListT.append(ndict)
                                if 'ISY_PI_M' in ndict:                        myListT.append(ndict)
                                if 'ISY_PI_V' in ndict:                        myListT.append(ndict)
                                if 'ISY_PI1_S' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI2_S' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI3_S' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI4_S' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI1_M' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI2_M' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI3_M' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI4_M' in ndict:                       myListT.append(ndict)                           
                                if 'ISY_PI1_V' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI2_V' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI3_V' in ndict:                       myListT.append(ndict)
                                if 'ISY_PI4_V' in ndict:                       myListT.append(ndict)
                                if 'AS_MAF0_03_M' in ndict:                    myListT.append(ndict)
                                if 'AS_MAF0_03_S' in ndict:                    myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_1_CYL_0_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_2_CYL_0_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_3_CYL_0_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_4_CYL_0_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_1_CYL_1_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_2_CYL_1_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_3_CYL_1_M' in ndict:       myListT.append(ndict)                           
                                if 'AS_TI_MES_4_PLS_4_CYL_1_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_1_CYL_2_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_2_CYL_2_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_3_CYL_2_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_4_CYL_2_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_1_CYL_3_M' in ndict:       myListT.append(ndict)
                                if 'AS_TI_MES_4_PLS_2_CYL_3_M' in ndict:       myListT.append(ndict)                         
                                if 'AS_TI_MES_4_PLS_3_CYL_3_M' in ndict:       myListT.append(ndict)                           
                                if 'AS_TI_MES_4_PLS_4_CYL_3_M' in ndict:       myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_1_CYL_0_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_2_CYL_0_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_3_CYL_0_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_4_CYL_0_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_1_CYL_1_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_2_CYL_1_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_3_CYL_1_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_4_CYL_1_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_1_CYL_2_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_2_CYL_2_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_3_CYL_2_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_4_CYL_2_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_1_CYL_3_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_2_CYL_3_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_3_CYL_3_M' in ndict:    myListT.append(ndict)
                                if 'AS_SOI_MES_CUS_PLS_4_CYL_3_M' in ndict:    myListT.append(ndict)
                                if 'ISY_STRING_IFILE_NAME' in ndict:	         myListT.append(ndict)
                           
                 f.close()
#                 print myListT
#%%                        
                 ndict_= sorted(myListT)
                 dnct = dict(map(str.strip,x) for d in ndict_ for x in d.items())
                 
                 def nklen():
                 #get the key length to know the nr. of rows in file               
                      for key in sorted(dnct):
                           nklen = len((dnct[key].replace("'", "")).split(','))                      
                      return nklen
                 nklen = nklen()
                           
                 #Already existing header-values retrieval                             
                 fdict = temp_DatenFDict.existDictFn(fname)
                 #print fdict
               
                 if count== 1:
                      with open(fname_, "wb") as fw:     #To write keys; needs atleast one file to be written in 1st count
                           print 'Writing Keys Once..'
                           writer= csv.writer(fw, delimiter= ';')
                           ks = fdict.keys()+sorted(dnct.keys())
                           writer.writerow(ks)
      
                 dfctL = []; dnctRa = []                 
                 dnctR = [[] for x in range(nklen)]       
                 for key in fdict:
                      dfctL.append(fdict[key])   
#%%   
                 for key in sorted(dnct):                  
                      if nklen is 1:    #for single new values no repeat required              
                           dnctRa.append(dnct[key].replace("'", ""))
                           if nklen is 1:
                                dfnLRA = dfctL+dnctRa                               
                 if nklen is 1:                 
                      print 'Writing only 1-Row found..'
                      oneRowCt+=nklen        #  print dfnLRA      #print len(dfnLRA)                 
                      with open(fname_, "ab") as fw:    #append rows of data
                           writer= csv.writer(fw, delimiter= ';')
                           writer.writerow(dfnLRA)
                           
                 for key in sorted(dnct):          
                      if nklen is not 1:     #but here, repeat the old values to nklen count
                           dfnLR = [[] for x in range(nklen)]
                           for i in range(nklen):
                                dnctR[i].append(dnct[key].replace("'", "").split(',')[i])
                                dnctR[i] = [item.strip() for item in dnctR[i]]
                                dfnLR[i] = dfctL+dnctR[i]            
                 if nklen is not 1:
                      print 'Writing %s-Rows found..'%(nklen)
                      RowCt+=nklen
                      for i in range(nklen):    #print dfnLR[i]      #print len(dfnLR[i])                      
                           with open(fname_, "ab") as fw:    #append rows of data
                                writer= csv.writer(fw, delimiter= ';')
#                                writer.writerow(dfnLR[i])   
#%%             
            else: 
                 print 'File "{}" is not in required format'.format(fname)
                 with open(path+"\\fileNot.txt","ab") as fN:
                      fN.write(fname+'\r\n')
                 NotinFile+=1     
#%%    
print 'Files-Count: {}\nOne-Row-TCount:{}\nRepeated-Rows-TCount: {}'.format(count, oneRowCt, RowCt)
print '\tFiles-Not-in-Required-Format-TCount: {}'.format(NotinFile)
toc=time.time()
print(str("%.2f" %(toc-tic)) + ' seconds elapsed')    
