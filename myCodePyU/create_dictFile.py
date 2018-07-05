import csv, time, pickle
#from os.path import join#, basename
#from os import walk, chdir#, listdir, getcwd

tic=time.time()

rootDir = 'D:\Skata\Sreekanth_pc'
path = rootDir + '\messung'
temp_path = path + '\\temp_daten3.csv'
fname = path + '\M996_20171110_150822_A_KH_1200_SK_SR26917_OPP3-2_IND'+'\M996_20171110_150822_A_KH_1200_SK_SR26917_OPP3-2_IND.xls'
i=count=0

f = open(fname)
r = csv.reader(f)
data = list(r)
#            print(data)              
header=data[1][0].split("\t")
#unit=data[2][0].split("\t") #print(unit)  #print(len(header))
#print(header)      #print("HeaderCount: %s"%len(header))  #print('\n')

#for rows
for i in range(0,len(data)):
    if [len(j) for j in [s.replace('\t', '') for s in data[i]]][0]:
        numofrow=i
#       print(numofrow) # count= count+1
        

daten=[[0 for i in range(len(header))] for j in range(0,numofrow-2)]
myList = []
def funTest():
    for i in range(0,numofrow-2):
        for j in range(len(header)):  
            daten[i][j]=data[i+3][0].split("\t")[j]
            ndict = {}          #Initialize empty dictionary
            
            #function to create dictionary key-value pairs
            def funReturn():
                #create all the header-value list        
                if(header.index('N_M')):
                    N_M_val = []
                    ind = header.index('N_M')
                    if(j==ind):
                        for i in range(0,len(daten)):
                            N_M_val.append(daten[i][ind])                      
                        if(N_M_val[-1]):
                            N_M_val= (", ".join(repr(e) for e in N_M_val))       #convert list values to str
    #                        print N_M_val
                            ndict = {'N_M':N_M_val}    #create dictionary by adding header-values
                            return ndict
    #                                                 
                if(header.index('AS_MFF_STND_CYL_0_PLS_1_M')):
                    ind = header.index('AS_MFF_STND_CYL_0_PLS_1_M')            
                    mass_cyl0_pls1 = []
                    if(j==ind):
                        for i in range(0,len(daten)):
                            mass_cyl0_pls1.append(daten[i][ind])
                        if(mass_cyl0_pls1[-1]):
                            mass_cyl0_pls1= (", ".join(repr(e) for e in mass_cyl0_pls1))                          
    #                        print mass_cyl0_pls1
                            ndict = {'AS_MFF_STND_CYL_0_PLS_1_M':mass_cyl0_pls1} 
                            return ndict         
                     
                if(header.index('AS_MFF_STND_CYL_0_PLS_2_M')):
                    ind = header.index('AS_MFF_STND_CYL_0_PLS_2_M')
                    mass_cyl0_pls2 = []
                    if(j==ind):
                        for i in range(0,len(daten)):
                            mass_cyl0_pls2.append(daten[i][ind])
                        if(mass_cyl0_pls2[-1]):
                            mass_cyl0_pls2= (", ".join(repr(e) for e in mass_cyl0_pls2))                        
    #                        print mass_cyl0_pls2
                            ndict = {'AS_MFF_STND_CYL_0_PLS_2_M':mass_cyl0_pls2} 
                            return ndict
                        
                    if(header.index('AS_MFF_STND_CYL_0_PLS_3_M')):
                        ind = header.index('AS_MFF_STND_CYL_0_PLS_3_M')
                        mass_cyl0_pls3 = []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                mass_cyl0_pls3.append(daten[i][ind])  
                            if(mass_cyl0_pls3[-1]):
                                mass_cyl0_pls3= (", ".join(repr(e) for e in mass_cyl0_pls3))  
        #                         print mass_cyl0_pls3
                                ndict = {'AS_MFF_STND_CYL_0_PLS_3_M':mass_cyl0_pls3}
                                return ndict
                             
                    if(header.index('AS_MFF_STND_CYL_0_PLS_4_M')):
                        ind = header.index('AS_MFF_STND_CYL_0_PLS_4_M')
                        mass_cyl0_pls4 = []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                mass_cyl0_pls4.append(daten[i][ind])  
                            if(mass_cyl0_pls4[-1]):
                                mass_cyl0_pls4= (", ".join(repr(e) for e in mass_cyl0_pls4))  
        #                         print mass_cyl0_pls4
                                ndict = {'AS_MFF_STND_CYL_0_PLS_4_M':mass_cyl0_pls4} 
                                return ndict
                             
                    if(header.index('AS_MFF_STND_CYL_1_PLS_1_M')):        
                        ind=header.index('AS_MFF_STND_CYL_1_PLS_1_M')
                        mass_cyl1_pls1=[]
                        if(j==ind):
                            for i in range(0,len(daten)):
                                mass_cyl1_pls1.append((daten[i][ind]))
                            if(mass_cyl1_pls1[-1]):
                                mass_cyl1_pls1= (", ".join(repr(e) for e in mass_cyl1_pls1))  
            #                         print mass_cyl1_pls1
                                ndict = {'AS_MFF_STND_CYL_1_PLS_1_M':mass_cyl1_pls1} 
                                return ndict
                                 
                    if(header.index('AS_MFF_STND_CYL_1_PLS_2_M')):
                        ind=header.index('AS_MFF_STND_CYL_1_PLS_2_M')       
                        mass_cyl1_pls2=[]
                        if(j==ind):
                            for i in range(0,len(daten)):
                                mass_cyl1_pls2.append((daten[i][ind]))
                            if(mass_cyl1_pls2[-1]):
                                mass_cyl1_pls2= (", ".join(repr(e) for e in mass_cyl1_pls2))
        #                         print mass_cyl1_pls2
                                ndict = {'AS_MFF_STND_CYL_1_PLS_2_M':mass_cyl1_pls2} 
                                return ndict
                        
                    if(header.index('AS_MFF_STND_CYL_1_PLS_3_M')):
                        ind=header.index('AS_MFF_STND_CYL_1_PLS_3_M')
                        mass_cyl1_pls3=[]
                        if(j==ind):
                            for i in range(0,len(daten)):
                                mass_cyl1_pls3.append((daten[i][ind]))
                            if(mass_cyl1_pls3[-1]):
                                mass_cyl1_pls3= (", ".join(repr(e) for e in mass_cyl1_pls3))  
        #                         print mass_cyl1_pls3
                                ndict = {'AS_MFF_STND_CYL_1_PLS_3_M':mass_cyl1_pls3} 
                                return ndict
                        
                    if(header.index('AS_MFF_STND_CYL_1_PLS_4_M')):
                        ind=header.index('AS_MFF_STND_CYL_1_PLS_4_M')
                        mass_cyl1_pls4=[]
                        if(j==ind):
                            for i in range(0,len(daten)):
                                mass_cyl1_pls4.append((daten[i][ind]))
                            if(mass_cyl1_pls4[-1]):
                                mass_cyl1_pls4= (", ".join(repr(e) for e in mass_cyl1_pls4))  
        #                         print mass_cyl1_pls4
                                ndict = {'AS_MFF_STND_CYL_1_PLS_4_M':mass_cyl1_pls4} 
                                return ndict
                    
                    if(header.index('AS_MFF_STND_CYL_2_PLS_1_M')):
                        ind = header.index('AS_MFF_STND_CYL_2_PLS_1_M')
                        mass_cyl2_pls1 = []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                mass_cyl2_pls1.append(daten[i][ind]) 
                            if(mass_cyl2_pls1[-1]):
                                mass_cyl2_pls1= (", ".join(repr(e) for e in mass_cyl2_pls1))  
        #                        print mass_cyl2_pls1
                                ndict = {'AS_MFF_STND_CYL_2_PLS_1_M':mass_cyl2_pls1} 
                                return ndict
                       
                    if(header.index('AS_MFF_STND_CYL_2_PLS_2_M')):
                        ind = header.index('AS_MFF_STND_CYL_2_PLS_2_M')
                        mass_cyl2_pls2 = []
                        if(j==ind):                
                            for i in range(0,len(daten)):
                                mass_cyl2_pls2.append(daten[i][ind]) 
                            if(mass_cyl2_pls2[-1]):
                                mass_cyl2_pls2= (", ".join(repr(e) for e in mass_cyl2_pls2))  
        #                        print mass_cyl2_pls2
                                ndict = {'AS_MFF_STND_CYL_2_PLS_2_M':mass_cyl2_pls2} 
                                return ndict
                    
                    if(header.index('AS_MFF_STND_CYL_2_PLS_3_M')):
                        ind = header.index('AS_MFF_STND_CYL_2_PLS_3_M')
                        mass_cyl2_pls3 = []
                        if(j==ind):                
                            for i in range(0,len(daten)):
                                mass_cyl2_pls3.append(daten[i][ind])
                            if(mass_cyl2_pls3[-1]):
                                mass_cyl2_pls3= (", ".join(repr(e) for e in mass_cyl2_pls3))  
        #                        print mass_cyl2_pls3
                                ndict = {'AS_MFF_STND_CYL_2_PLS_3_M':mass_cyl2_pls3}
                                return ndict
        #            
                    if(header.index('AS_MFF_STND_CYL_2_PLS_4_M')):
                        ind = header.index('AS_MFF_STND_CYL_2_PLS_4_M')
                        mass_cyl2_pls4 = []
                        if(j==ind):               
                            for i in range(0,len(daten)):
                                mass_cyl2_pls4.append(daten[i][ind]) 
                            if(mass_cyl2_pls4[-1]):
                                mass_cyl2_pls4= (", ".join(repr(e) for e in mass_cyl2_pls4))  
        #                        print mass_cyl2_pls4
                                ndict = {'AS_MFF_STND_CYL_2_PLS_4_M':mass_cyl2_pls4} 
                                return ndict
                                
                    if(header.index('AS_MFF_STND_CYL_3_PLS_1_M')):
                        ind = header.index('AS_MFF_STND_CYL_3_PLS_1_M')
                        mass_cyl3_pls1 = []
                        if(j==ind):                
                            for i in range(0,len(daten)):
                                mass_cyl3_pls1.append(daten[i][ind]) 
                            if(mass_cyl3_pls1[-1]):
                                mass_cyl3_pls1= (", ".join(repr(e) for e in mass_cyl3_pls1))  
        #                        print mass_cyl3_pls1
                                ndict = {'AS_MFF_STND_CYL_3_PLS_1_M':mass_cyl3_pls1}
                                return ndict
                    
                    if(header.index('AS_MFF_STND_CYL_3_PLS_2_M')):
                        ind = header.index('AS_MFF_STND_CYL_3_PLS_2_M')
                        mass_cyl3_pls2 = []
                        if(j==ind):                
                            for i in range(0,len(daten)):
                                mass_cyl3_pls2.append(daten[i][ind])
                            if(mass_cyl3_pls2[-1]):
                                mass_cyl3_pls2= (", ".join(repr(e) for e in mass_cyl3_pls2))  
        #                        print mass_cyl3_pls2
                                ndict = {'AS_MFF_STND_CYL_3_PLS_2_M':mass_cyl3_pls2}
                                return ndict
                    
                    if(header.index('AS_MFF_STND_CYL_3_PLS_3_M')):
                        ind = header.index('AS_MFF_STND_CYL_3_PLS_3_M')
                        mass_cyl3_pls3 = []
                        if(j==ind):                
                            for i in range(0,len(daten)):
                                mass_cyl3_pls3.append(daten[i][ind])
                            if(mass_cyl3_pls3[-1]):
                                mass_cyl3_pls3= (", ".join(repr(e) for e in mass_cyl3_pls3))  
        #                        print mass_cyl3_pls3
                                ndict = {'AS_MFF_STND_CYL_3_PLS_3_M':mass_cyl3_pls3} 
                                return ndict
        #            
                    if(header.index('AS_MFF_STND_CYL_3_PLS_4_M')):
                        ind = header.index('AS_MFF_STND_CYL_3_PLS_4_M')
                        mass_cyl3_pls4 = []
                        if(j==ind):                
                            for i in range(0,len(daten)):
                                mass_cyl3_pls4.append(daten[i][ind]) 
                            if(mass_cyl3_pls4[-1]):
                                mass_cyl3_pls4= (", ".join(repr(e) for e in mass_cyl3_pls4))  
        #                        print mass_cyl3_pls4
                                ndict = {'AS_MFF_STND_CYL_3_PLS_4_M':mass_cyl3_pls4}
                                return ndict
                          
                    if(header.index('AS_MFF_SP_HOM_MV_M')):
                        ind = header.index('AS_MFF_SP_HOM_MV_M')
                        masssp = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                masssp.append(daten[i][ind]) 
                            if(masssp[-1]):
                                masssp= (", ".join(repr(e) for e in masssp))  
        #                        print masssp
                                ndict = {'AS_MFF_SP_HOM_MV_M':masssp} 
                                return ndict
                 
                    if(header.index('AS_IGA_AV_MV_M')):
                        ind = header.index('AS_IGA_AV_MV_M')
                        soiia = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soiia.append(daten[i][ind])
                            if(soiia[-1]):
                                soiia= (", ".join(repr(e) for e in soiia))  
        #                        print soiia
                                ndict = {'AS_IGA_AV_MV_M':soiia} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M')):       # soi 1. injection
                        ind = header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M')
                        soi1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi1.append(daten[i][ind])  
                            if(soi1[-1]):
                                soi1= (", ".join(repr(e) for e in soi1))  
        #                        print soi1
                                ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_1_M':soi1} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M')  # soi 2. injection
                        soi2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi2.append(daten[i][ind])
                            if(soi2[-1]):
                                soi2= (", ".join(repr(e) for e in soi2))  
        #                        print soi2
                                ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_0_M':soi2} 
                                return ndict
        #            
                    if(header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M')):       # soi 3. injection
                        ind = header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M')
                        soi3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi3.append(daten[i][ind]) 
                            if(soi3[-1]):
                                soi3= (", ".join(repr(e) for e in soi3))  
        #                        print soi3
                                ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_1_M':soi3} 
                                return ndict
                    
                    if(header.index('ISY_PI_V')):
                        ind = header.index('ISY_PI_V')
                        CoV = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                CoV.append(daten[i][ind])  
                            if(CoV[-1]):
                                CoV= (", ".join(repr(e) for e in CoV))  
        #                        print CoV
                                ndict = {'ISY_PI_V':CoV} 
                                return ndict
                         
                    if(header.index('C_CNS_06_M')):
                        ind = header.index('C_CNS_06_M')
                        BSFC = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                BSFC.append(daten[i][ind])
                            if(BSFC[-1]):
                                BSFC= (", ".join(repr(e) for e in BSFC))  
        #                        print BSFC
                                ndict = {'C_CNS_06_M':BSFC} 
                                return ndict
                    
                    if(header.index('PAC1_DL_CONC_49_M')):
                        ind = header.index('PAC1_DL_CONC_49_M')
                        PN = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                PN.append(daten[i][ind])  
                            if(PN[-1]):
                                PN= (", ".join(repr(e) for e in PN))  
        #                        print PN
                                ndict = {'PAC1_DL_CONC_49_M':PN} 
                                return ndict
                    
                    if(header.index('EG1_CO_15_M')):
                        ind = header.index('EG1_CO_15_M')
                        CO = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                CO.append(daten[i][ind])  
                            if(CO[-1]):
                                CO= (", ".join(repr(e) for e in CO))  
        #                        print CO
                                ndict = {'EG1_CO_15_M':CO} 
                                return ndict
                    
                    if(header.index('EG1_NOX_16_M')):
                        ind = header.index('EG1_NOX_16_M')
                        NOx = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                NOx.append(daten[i][ind])
                            if(NOx[-1]):
                                NOx= (", ".join(repr(e) for e in NOx))  
        #                        print NOx
                                ndict = {'EG1_NOX_16_M':NOx} 
                                return ndict
                    
                    if(header.index('AS_LAMB_LS_UP_M')):
                        ind = header.index('AS_LAMB_LS_UP_M')
                        lambdav = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                lambdav.append(daten[i][ind])
                            if(lambdav[-1]):
                                lambdav= (", ".join(repr(e) for e in lambdav))  
        #                        print lambdav
                                ndict = {'AS_LAMB_LS_UP_M':lambdav} 
                                return ndict
                    
                    if(header.index('EG1_THC_16_M')):
                        ind = header.index('EG1_THC_16_M')
                        HC = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                HC.append(daten[i][ind]) 
                            if(HC[-1]):
                                HC= (", ".join(repr(e) for e in HC))  
        #                        print HC
                                ndict = {'EG1_THC_16_M':HC} 
                                return ndict
                    
                    if(header.index('T_B1CAT1B1_M')):
                        ind = header.index('T_B1CAT1B1_M')
                        TKAT = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                TKAT.append(daten[i][ind])
                            if(TKAT[-1]):
                                TKAT= (", ".join(repr(e) for e in TKAT))  
        #                        print TKAT
                                ndict = {'T_B1CAT1B1_M':TKAT} 
                                return ndict
                                
                    if(header.index('ISY_PI_S')):
                        ind = header.index('ISY_PI_S')
                        std = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                std.append(daten[i][ind]) 
                            if(std[-1]):
                                std= (", ".join(repr(e) for e in std))  
        #                        print std
                                ndict = {'ISY_PI_S':std} #
                                return ndict
                     
                    if(header.index('ISY_PI_M')):
                        ind = header.index('ISY_PI_M')
                        mitt = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                mitt.append(daten[i][ind])  
                            if(mitt[-1]):
                                mitt= (", ".join(repr(e) for e in mitt))  
        #                        print mitt
                                ndict = {'ISY_PI_M':mitt} 
                                return ndict
                    
                    if(header.index('ISY_PI_V')):
                        ind = header.index('ISY_PI_V')
                        cov = []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                cov.append(daten[i][ind])
                            if(cov[-1]):
                                cov= (", ".join(repr(e) for e in cov))  
        #                        print cov
                                ndict = {'ISY_PI_V':cov} 
                                return ndict
                    
                    if(header.index('ISY_PI1_S')):
                        ind = header.index('ISY_PI1_S')
                        std1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                std1.append(daten[i][ind]) 
                            if(std1[-1]):
                                std1= (", ".join(repr(e) for e in std1))  
        #                        print std1
                                ndict = {'ISY_PI1_S':std1} 
                                return ndict
                    
                    if(header.index('ISY_PI2_S')):
                        ind = header.index('ISY_PI2_S')
                        std2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                std2.append(daten[i][ind]) 
                            if(std2[-1]):
                                std2= (", ".join(repr(e) for e in std2))  
        #                        print std2
                                ndict = {'ISY_PI2_S':std2} 
                                return ndict
                
                    if(header.index('ISY_PI3_S')):
                        ind = header.index('ISY_PI3_S')
                        std3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                std3.append(daten[i][ind])
                            if(std3[-1]):
                                std3= (", ".join(repr(e) for e in std3))  
        #                        print std3
                                ndict = {'ISY_PI3_S':std3} 
                                return ndict
                    
                    if(header.index('ISY_PI4_S')):
                       ind=header.index('ISY_PI4_S')
                       std4=[]
                       if(j==ind): 
                           for i in range(0,len(daten)):
                               std4.append((daten[i][ind]))
                           if(std4[-1]):
                               std4= (", ".join(repr(e) for e in std4))  
        #                       print std4
                               ndict = {'ISY_PI4_S':std4}       
                               return ndict
                               
                    if(header.index('ISY_PI1_M')):
                        ind = header.index('ISY_PI1_M')
                        mitt1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                mitt1.append(daten[i][ind]) 
                            if(mitt1[-1]):
                                mitt1= (", ".join(repr(e) for e in mitt1))  
        #                        print mitt1
                                ndict = {'ISY_PI1_M':mitt1}
                                return ndict
                    
                    if(header.index('ISY_PI2_M')):
                        ind = header.index('ISY_PI2_M')
                        mitt2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                mitt2.append(daten[i][ind]) 
                            if(mitt2[-1]):
                                mitt2= (", ".join(repr(e) for e in mitt2))  
        #                        print mitt2
                                ndict = {'ISY_PI2_M':mitt2} 
                                return ndict
                     
                    if(header.index('ISY_PI3_M')):
                        ind = header.index('ISY_PI3_M')
                        mitt3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                mitt3.append(daten[i][ind])
                            if(mitt3[-1]):
                                mitt3= (", ".join(repr(e) for e in mitt3))  
        #                        print mitt3
                                ndict = {'ISY_PI3_M':mitt3}
                                return ndict
                    
                    if(header.index('ISY_PI4_M')):
                        ind = header.index('ISY_PI4_M')
                        mitt4 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                mitt4.append(daten[i][ind]) 
                            if(mitt4[-1]):
                                mitt4= (", ".join(repr(e) for e in mitt4))  
        #                        print mitt4
                                ndict = {'ISY_PI4_M':mitt4} 
                                return ndict
        #            
                    if(header.index('ISY_PI1_V')):
                        ind = header.index('ISY_PI1_V')
                        cov1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                cov1.append(daten[i][ind])
                            if(cov1[-1]):
                                cov1= (", ".join(repr(e) for e in cov1))  
        #                        print cov1
                                ndict = {'ISY_PI1_V':cov1} 
                                return ndict
                     
                    if(header.index('ISY_PI2_V')):
                        ind = header.index('ISY_PI2_V')
                        cov2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                cov2.append(daten[i][ind])
                            if(cov2[-1]):
                                cov2= (", ".join(repr(e) for e in cov2))  
        #                        print cov2
                                ndict = {'ISY_PI2_V':cov2} 
                                return ndict
                    
                    if(header.index('ISY_PI3_V')):
                        ind = header.index('ISY_PI3_V')
                        cov3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                cov3.append(daten[i][ind])
                            if(cov3[-1]):
                                cov3= (", ".join(repr(e) for e in cov3))  
        #                        print cov3
                                ndict = {'ISY_PI3_V':cov3} 
                                return ndict
                    
                    if(header.index('ISY_PI4_V')):
                        ind = header.index('ISY_PI4_V')
                        cov4 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                cov4.append(daten[i][ind])  
                            if(cov4[-1]):
                                cov4= (", ".join(repr(e) for e in cov4))  
        #                        print cov4
                                ndict = {'ISY_PI4_V':cov4} 
                                return ndict
                           
                    if(header.index('AS_MAF0_03_M')):
                        ind = header.index('AS_MAF0_03_M')
                        mafm = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                mafm.append(daten[i][ind]) 
                            if(mafm[-1]):
                                mafm= (", ".join(repr(e) for e in mafm))  
        #                        print mafm
                                ndict = {'AS_MAF0_03_M':mafm} 
                                return ndict
                    
                    if(header.index('AS_MAF0_03_S')):
                        ind = header.index('AS_MAF0_03_S')
                        mafs = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                mafs.append(daten[i][ind]) 
                            if(mafs[-1]):
                                mafs= (", ".join(repr(e) for e in mafs))  
        #                        print mafs
                                ndict = {'AS_MAF0_03_S':mafs} 
                                return ndict
        
                    if(header.index('AS_TI_MES_4_PLS_1_CYL_0_M')):
                        ind = header.index('AS_TI_MES_4_PLS_1_CYL_0_M')
                        ti_pls1_cyl0 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls1_cyl0.append(daten[i][ind]) 
                            if(ti_pls1_cyl0[-1]):
                                ti_pls1_cyl0= (", ".join(repr(e) for e in ti_pls1_cyl0))  
        #                        print ti_pls1_cyl0
                                ndict = {'AS_TI_MES_4_PLS_1_CYL_0_M':ti_pls1_cyl0} 
                                return ndict
                              
                    if(header.index('AS_TI_MES_4_PLS_2_CYL_0_M')):
                        ind = header.index('AS_TI_MES_4_PLS_2_CYL_0_M')
                        ti_pls2_cyl0 = []
                        if(j==ind):
                            for i in range(0,len(daten)):
                                ti_pls2_cyl0.append(daten[i][ind]) 
                            if(ti_pls2_cyl0[-1]):
                                ti_pls2_cyl0= (", ".join(repr(e) for e in ti_pls2_cyl0))  
        #                        print ti_pls2_cyl0
                                ndict = {'AS_TI_MES_4_PLS_2_CYL_0_M':ti_pls2_cyl0} 
                                return ndict
        
                    if(header.index('AS_TI_MES_4_PLS_3_CYL_0_M')):
                        ind=header.index('AS_TI_MES_4_PLS_3_CYL_0_M')
                        ti_pls3_cyl0=[]
                        if(j==ind):
                            for i in range(0,len(daten)):
                                ti_pls3_cyl0.append(daten[i][ind])
                            if(ti_pls3_cyl0[-1]):
                                ti_pls3_cyl0= (", ".join(repr(e) for e in ti_pls3_cyl0))  
        #                        print ti_pls3_cyl0
                                ndict = {'AS_TI_MES_4_PLS_3_CYL_0_M':ti_pls3_cyl0} 
                                return ndict
                                
                    if(header.index('AS_TI_MES_4_PLS_4_CYL_0_M')):
                        ind = header.index('AS_TI_MES_4_PLS_4_CYL_0_M')
                        ti_pls4_cyl0 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls4_cyl0.append(daten[i][ind])
                            if(ti_pls4_cyl0[-1]):
                                ti_pls4_cyl0= (", ".join(repr(e) for e in ti_pls4_cyl0))  
        #                        print ti_pls4_cyl0
                                ndict = {'AS_TI_MES_4_PLS_4_CYL_0_M':ti_pls4_cyl0}
                                return ndict
        
                    if(header.index('AS_TI_MES_4_PLS_1_CYL_1_M')):
                        ind = header.index('AS_TI_MES_4_PLS_1_CYL_1_M')
                        ti_pls1_cyl1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls1_cyl1.append(daten[i][ind]) 
                            if(ti_pls1_cyl1[-1]):
                                ti_pls1_cyl1= (", ".join(repr(e) for e in ti_pls1_cyl1))  
        #                        print ti_pls1_cyl1
                                ndict = {'AS_TI_MES_4_PLS_1_CYL_1_M':ti_pls1_cyl1} 
                                return ndict
                   
                    if(header.index('AS_TI_MES_4_PLS_2_CYL_1_M')):
                        ind = header.index('AS_TI_MES_4_PLS_2_CYL_1_M')
                        ti_pls2_cyl1 = []
                        if(j==ind):                           
                            for i in range(0,len(daten)):
                                ti_pls2_cyl1.append(daten[i][ind]) 
                            if(ti_pls2_cyl1[-1]):
                                ti_pls2_cyl1= (", ".join(repr(e) for e in ti_pls2_cyl1))
        #                        print ti_pls2_cyl1
                                ndict = {'AS_TI_MES_4_PLS_2_CYL_1_M':ti_pls2_cyl1} 
                                return ndict
                    
                    if(header.index('AS_TI_MES_4_PLS_3_CYL_1_M')):
                        ind = header.index('AS_TI_MES_4_PLS_3_CYL_1_M')
                        ti_pls3_cyl1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls3_cyl1.append(daten[i][ind])  
                            if(ti_pls3_cyl1[-1]):
                                ti_pls3_cyl1= (", ".join(repr(e) for e in ti_pls3_cyl1)) 
        #                        print ti_pls3_cyl1
                                ndict = {'AS_TI_MES_4_PLS_3_CYL_1_M':ti_pls3_cyl1}
                                return ndict
                    
                    if(header.index('AS_TI_MES_4_PLS_4_CYL_1_M')):
                        ind = header.index('AS_TI_MES_4_PLS_4_CYL_1_M')
                        ti_pls4_cyl1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls4_cyl1.append(daten[i][ind]) 
                            if(ti_pls4_cyl1[-1]):
                                ti_pls4_cyl1= (", ".join(repr(e) for e in ti_pls4_cyl1))  
        #                        print ti_pls4_cyl1
                                ndict = {'AS_TI_MES_4_PLS_4_CYL_1_M':ti_pls4_cyl1} 
                                return ndict
                    
                    if(header.index('AS_TI_MES_4_PLS_1_CYL_2_M')):
                        ind = header.index('AS_TI_MES_4_PLS_1_CYL_2_M')
                        ti_pls1_cyl2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls1_cyl2.append(daten[i][ind])  
                            if(ti_pls1_cyl2[-1]):
                                ti_pls1_cyl2= (", ".join(repr(e) for e in ti_pls1_cyl2))  
        #                        print ti_pls1_cyl2
                                ndict = {'AS_TI_MES_4_PLS_1_CYL_2_M':ti_pls1_cyl2} 
                                return ndict
                        
                    if(header.index('AS_TI_MES_4_PLS_2_CYL_2_M')):
                        ind = header.index('AS_TI_MES_4_PLS_2_CYL_2_M')
                        ti_pls2_cyl2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls2_cyl2.append(daten[i][ind]) 
                            if(ti_pls2_cyl2[-1]):
                                ti_pls2_cyl2= (", ".join(repr(e) for e in ti_pls2_cyl2))  
        #                        print ti_pls2_cyl2
                                ndict = {'AS_TI_MES_4_PLS_2_CYL_2_M':ti_pls2_cyl2}
                                return ndict
                            
                    if(header.index('AS_TI_MES_4_PLS_3_CYL_2_M')):
                        ind = header.index('AS_TI_MES_4_PLS_3_CYL_2_M')
                        ti_pls3_cyl2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls3_cyl2.append(daten[i][ind])  
                            if(ti_pls3_cyl2[-1]):
                                ti_pls3_cyl2= (", ".join(repr(e) for e in ti_pls3_cyl2))  
        #                        print ti_pls3_cyl2
                                ndict = {'AS_TI_MES_4_PLS_3_CYL_2_M':ti_pls3_cyl2}
                                return ndict
                    
                    if(header.index('AS_TI_MES_4_PLS_4_CYL_2_M')):
                        ind = header.index('AS_TI_MES_4_PLS_4_CYL_2_M')
                        ti_pls4_cyl2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls4_cyl2.append(daten[i][ind]) 
                            if(ti_pls4_cyl2[-1]):
                                ti_pls4_cyl2= (", ".join(repr(e) for e in ti_pls4_cyl2))  
        #                        print ti_pls4_cyl2
                                ndict = {'AS_TI_MES_4_PLS_4_CYL_2_M':ti_pls4_cyl2} 
                                return ndict
                    
                    if(header.index('AS_TI_MES_4_PLS_1_CYL_3_M')):
                        ind = header.index('AS_TI_MES_4_PLS_1_CYL_3_M')
                        ti_pls1_cyl3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls1_cyl3.append(daten[i][ind])  
                            if(ti_pls1_cyl3[-1]):
                                ti_pls1_cyl3= (", ".join(repr(e) for e in ti_pls1_cyl3))  
        #                        print ti_pls1_cyl3
                                ndict = {'AS_TI_MES_4_PLS_1_CYL_3_M':ti_pls1_cyl3} 
                                return ndict
                              
                    if(header.index('AS_TI_MES_4_PLS_2_CYL_3_M')):
                        ind = header.index('AS_TI_MES_4_PLS_2_CYL_3_M')
                        ti_pls2_cyl3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls2_cyl3.append(daten[i][ind]) 
                            if(ti_pls2_cyl3[-1]):
                                ti_pls2_cyl3= (", ".join(repr(e) for e in ti_pls2_cyl3))  
        #                        print ti_pls2_cyl3
                                ndict = {'AS_TI_MES_4_PLS_2_CYL_3_M':ti_pls2_cyl3}
                                return ndict
                    
                    if(header.index('AS_TI_MES_4_PLS_3_CYL_3_M')):
                        ind = header.index('AS_TI_MES_4_PLS_3_CYL_3_M')
                        ti_pls3_cyl3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls3_cyl3.append(daten[i][ind]) 
                            if(ti_pls3_cyl3[-1]):
                                ti_pls3_cyl3= (", ".join(repr(e) for e in ti_pls3_cyl3))  
        #                        print ti_pls3_cyl3
                                ndict = {'AS_TI_MES_4_PLS_3_CYL_3_M':ti_pls3_cyl3}
                                return ndict
                    
                    if(header.index('AS_TI_MES_4_PLS_4_CYL_3_M')):
                        ind = header.index('AS_TI_MES_4_PLS_4_CYL_3_M')
                        ti_pls4_cyl3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ti_pls4_cyl3.append(daten[i][ind]) 
                            if(ti_pls4_cyl3[-1]):
                                ti_pls4_cyl3= (", ".join(repr(e) for e in ti_pls4_cyl3))  
        #                        print ti_pls4_cyl3
                                ndict = {'AS_TI_MES_4_PLS_4_CYL_3_M':ti_pls4_cyl3}
                                return ndict
                  
                    if(header.index('AS_SOI_MES_CUS_PLS_1_CYL_0_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_1_CYL_0_M')
                        soi_pls1_cyl0 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls1_cyl0.append(daten[i][ind]) 
                            if(soi_pls1_cyl0[-1]):
                                soi_pls1_cyl0= (", ".join(repr(e) for e in soi_pls1_cyl0))  
        #                        print soi_pls1_cyl0
                                ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_0_M':soi_pls1_cyl0}
                                return ndict
                        
                    if(header.index('AS_SOI_MES_CUS_PLS_2_CYL_0_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_2_CYL_0_M')
                        soi_pls2_cyl0 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls2_cyl0.append(daten[i][ind])  
                            if(soi_pls2_cyl0[-1]):
                                soi_pls2_cyl0= (", ".join(repr(e) for e in soi_pls2_cyl0))  
        #                        print soi_pls2_cyl0
                                ndict = {'AS_SOI_MES_CUS_PLS_2_CYL_0_M':soi_pls2_cyl0} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M')
                        if(j==ind):
                            soi_pls3_cyl0 = []
                            for i in range(0,len(daten)):
                                soi_pls3_cyl0.append(daten[i][ind]) 
                            if(soi_pls3_cyl0[-1]):
                                soi_pls3_cyl0= (", ".join(repr(e) for e in soi_pls3_cyl0))  
        #                         print soi_pls3_cyl0
                                ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_0_M':soi_pls3_cyl0} 
                                return ndict
               
                    if(header.index('AS_SOI_MES_CUS_PLS_4_CYL_0_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_4_CYL_0_M')
                        soi_pls4_cyl0 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls4_cyl0.append(daten[i][ind]) 
                            if(soi_pls4_cyl0[-1]):                            
                                soi_pls4_cyl0= (", ".join(repr(e) for e in soi_pls4_cyl0))  
        #                        print soi_pls4_cyl0
                                ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_0_M':soi_pls4_cyl0} 
                                return ndict
                  
                    if(header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M')
                        soi_pls1_cyl1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls1_cyl1.append(daten[i][ind]) 
                            if(soi_pls1_cyl1[-1]):
                                soi_pls1_cyl1= (", ".join(repr(e) for e in soi_pls1_cyl1))                            
        #                        print soi_pls1_cyl1
                                ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_1_M':soi_pls1_cyl1} 
                                return ndict
                       
                    if(header.index('AS_SOI_MES_CUS_PLS_2_CYL_1_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_2_CYL_1_M')
                        soi_pls2_cyl1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls2_cyl1.append(daten[i][ind]) 
                            if(soi_pls2_cyl1[-1]):
                                soi_pls2_cyl1= (", ".join(repr(e) for e in soi_pls2_cyl1))  
        #                        print soi_pls2_cyl1
                                ndict = {'AS_SOI_MES_CUS_PLS_2_CYL_1_M':soi_pls2_cyl1} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_3_CYL_1_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_3_CYL_1_M')
                        soi_pls3_cyl1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls3_cyl1.append(daten[i][ind]) 
                            if(soi_pls3_cyl1[-1]):                            
                                soi_pls3_cyl1= (", ".join(repr(e) for e in soi_pls3_cyl1))  
        #                        print soi_pls3_cyl1
                                ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_1_M':soi_pls3_cyl1} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M')
                        soi_pls4_cyl1 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls4_cyl1.append(daten[i][ind]) 
                            if(soi_pls4_cyl1[-1]):
                                soi_pls4_cyl1= (", ".join(repr(e) for e in soi_pls4_cyl1))  
        #                        print soi_pls4_cyl1
                                ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_1_M':soi_pls4_cyl1} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_1_CYL_2_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_1_CYL_2_M')
                        soi_pls1_cyl2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls1_cyl2.append(daten[i][ind]) 
                            if(soi_pls1_cyl2[-1]):
                                soi_pls1_cyl2= (", ".join(repr(e) for e in soi_pls1_cyl2))  
        #                        print soi_pls1_cyl2
                                ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_2_M':soi_pls1_cyl2} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_2_CYL_2_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_2_CYL_2_M')
                        soi_pls2_cyl2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls2_cyl2.append(daten[i][ind])  
                            if(soi_pls2_cyl2[-1]):
                                soi_pls2_cyl2= (", ".join(repr(e) for e in soi_pls2_cyl2))  
        #                        print soi_pls2_cyl2
                                ndict = {'AS_SOI_MES_CUS_PLS_2_CYL_2_M':soi_pls2_cyl2}
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_3_CYL_2_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_3_CYL_2_M')
                        soi_pls3_cyl2 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls3_cyl2.append(daten[i][ind]) 
                            if(soi_pls3_cyl2[-1]):
                                soi_pls3_cyl2= (", ".join(repr(e) for e in soi_pls3_cyl2))  
        #                        print soi_pls3_cyl2
                                ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_2_M':soi_pls3_cyl2} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_4_CYL_2_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_4_CYL_2_M')
                        soi_pls4_cyl2 = [] 
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls4_cyl2.append(daten[i][ind])  
                            if(soi_pls4_cyl2[-1]):
                                soi_pls4_cyl2= (", ".join(repr(e) for e in soi_pls4_cyl2))  
        #                        print soi_pls4_cyl2
                                ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_2_M':soi_pls4_cyl2} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_1_CYL_3_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_1_CYL_3_M')
                        soi_pls1_cyl3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls1_cyl3.append(daten[i][ind])  
                            if(soi_pls1_cyl3[-1]):
                                soi_pls1_cyl3= (", ".join(repr(e) for e in soi_pls1_cyl3))  
        #                        print soi_pls1_cyl3
                                ndict = {'AS_SOI_MES_CUS_PLS_1_CYL_3_M':soi_pls1_cyl3} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_2_CYL_3_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_2_CYL_3_M')
                        soi_pls2_cyl3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls2_cyl3.append(daten[i][ind])  
                            if(soi_pls2_cyl3[-1]):
                                soi_pls2_cyl3= (", ".join(repr(e) for e in soi_pls2_cyl3))  
        #                        print soi_pls2_cyl3
                                ndict = {'AS_SOI_MES_CUS_PLS_2_CYL_3_M':soi_pls2_cyl3} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_3_CYL_3_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_3_CYL_3_M')
                        soi_pls3_cyl3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls3_cyl3.append(daten[i][ind]) 
                            if(soi_pls3_cyl3[-1]):
                                soi_pls3_cyl3= (", ".join(repr(e) for e in soi_pls3_cyl3))  
        #                        print soi_pls3_cyl3
                                ndict = {'AS_SOI_MES_CUS_PLS_3_CYL_3_M':soi_pls3_cyl3} 
                                return ndict
                    
                    if(header.index('AS_SOI_MES_CUS_PLS_4_CYL_3_M')):
                        ind = header.index('AS_SOI_MES_CUS_PLS_4_CYL_3_M')
                        soi_pls4_cyl3 = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                soi_pls4_cyl3.append(daten[i][ind]) 
                            if(soi_pls4_cyl3[-1]):
                                soi_pls4_cyl3= (", ".join(repr(e) for e in soi_pls4_cyl3))  
        #                        print soi_pls4_cyl3
                                ndict = {'AS_SOI_MES_CUS_PLS_4_CYL_3_M':soi_pls4_cyl3} 
                                return ndict
                        
                    if(header.index('ISY_STRING_IFILE_NAME')):
                        ind = header.index('ISY_STRING_IFILE_NAME')
                        ifile = []
                        if(j==ind):                    
                            for i in range(0,len(daten)):
                                ifile.append(daten[i][ind])  
                            if(ifile[-1]):
                                ifile= (", ".join(repr(e) for e in ifile))  
        #                        print ifile
                                ndict = {'ISY_STRING_IFILE_NAME':ifile} 
                                return ndict
                  
                     
                
            ndict = funReturn()       # call the dictionary function
            if ndict!=None:                            
                if 'N_M' in ndict:                             myList.append(ndict)     
                if 'AS_MFF_STND_CYL_0_PLS_1_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_0_PLS_3_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_0_PLS_4_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_1_PLS_1_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_1_PLS_2_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_1_PLS_3_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_1_PLS_4_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_2_PLS_1_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_2_PLS_2_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_2_PLS_3_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_2_PLS_4_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_3_PLS_1_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_3_PLS_2_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_3_PLS_3_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_STND_CYL_3_PLS_4_M' in ndict:       myList.append(ndict)
                if 'AS_MFF_SP_HOM_MV_M' in ndict:              myList.append(ndict)
                if 'AS_IGA_AV_MV_M' in ndict:                  myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_1_CYL_1_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_3_CYL_0_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_4_CYL_1_M' in ndict:    myList.append(ndict)
                if 'ISY_PI_V' in ndict:                        myList.append(ndict)
                if 'C_CNS_06_M' in ndict:                      myList.append(ndict)
                if 'PAC1_DL_CONC_49_M' in ndict:               myList.append(ndict)
                if 'EG1_CO_15_M' in ndict:                     myList.append(ndict)
                if 'EG1_NOX_16_M' in ndict:                    myList.append(ndict)
                if 'AS_LAMB_LS_UP_M' in ndict:                 myList.append(ndict)
                if 'EG1_THC_16_M' in ndict:                    myList.append(ndict)
                if 'T_B1CAT1B1_M' in ndict:                    myList.append(ndict)
                if 'ISY_PI_S' in ndict:                        myList.append(ndict)
                if 'ISY_PI_M' in ndict:                        myList.append(ndict)
                if 'ISY_PI_V' in ndict:                        myList.append(ndict)
                if 'ISY_PI1_S' in ndict:                       myList.append(ndict)
                if 'ISY_PI2_S' in ndict:                       myList.append(ndict)
                if 'ISY_PI4_S' in ndict:                       myList.append(ndict)
                if 'ISY_PI1_M' in ndict:                       myList.append(ndict)
                if 'ISY_PI2_M' in ndict:                       myList.append(ndict)
                if 'ISY_PI3_M' in ndict:                       myList.append(ndict)
                if 'ISY_PI1_V' in ndict:                       myList.append(ndict)
                if 'ISY_PI2_V' in ndict:                       myList.append(ndict)
                if 'ISY_PI3_V' in ndict:                       myList.append(ndict)
                if 'ISY_PI4_V' in ndict:                       myList.append(ndict)
                if 'AS_MAF0_03_M' in ndict:                    myList.append(ndict)
                if 'AS_MAF0_03_S' in ndict:                    myList.append(ndict)
                if 'AS_TI_MES_4_PLS_1_CYL_0_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_2_CYL_0_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_3_CYL_0_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_4_CYL_0_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_1_CYL_1_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_2_CYL_1_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_3_CYL_1_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_4_CYL_1_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_1_CYL_2_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_2_CYL_2_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_3_CYL_2_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_4_CYL_2_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_1_CYL_3_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_2_CYL_3_M' in ndict:       myList.append(ndict)
                if 'AS_TI_MES_4_PLS_3_CL_3_M' in ndict:        myList.append(ndict)
                if 'AS_TI_MES_4_PLS_4_CYL_3_M' in ndict:       myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_1_CYL_0_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_2_CYL_0_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_3_CYL_0_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_4_CYL_0_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_1_CYL_1_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_2_CYL_1_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_3_CYL_1_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_4_CYL_1_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_1_CYL_2_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_2_CYL_2_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_3_CYL_2_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_4_CYL_2_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_1_CYL_3_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_2_CYL_3_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_3_CYL_3_M' in ndict:    myList.append(ndict)
                if 'AS_SOI_MES_CUS_PLS_4_CYL_3_M' in ndict:    myList.append(ndict)
                if 'ISY_STRING_IFILE_NAME' in ndict:	        myList.append(ndict)
    
#    print myList
    pickle.dump(myList, open("save.p", "wb"))    #returns single_list of all dictionaries


## call the main function list of dict that have to added
#funTest()
#ndict_ = pickle.load(open("save.p", "rb"))  

f.close()
print('\n')        
print(count)        
toc=time.time()
print(str("%.2f" %(toc-tic)) + ' seconds elapsed')    