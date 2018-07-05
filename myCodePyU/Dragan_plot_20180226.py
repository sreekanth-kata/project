# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:43:20 2018

@author: uid18326
"""
def cov_dp(docid_dp):
    #DRAGAN PLOT
    #path="D:/Data/projects/Motorpruefstand/Datenbank/work/M996_20171111_033420_A_KH_1300_SK_SR26917_OPP3-3_IND.xls"
    #xlsname='M996_20171111_033420_A_KH_1300_SK_SR26917_OPP3-3_IND.xls'
    #inj_text='SR26917'
    #rpm_text='1300'
    #fuel_text='SK'
    #numMeas=1
    
    import csv
    import pylab
    import time
    import matplotlib
    import matplotlib.pyplot as plt
    
    tic=time.time()
      
    plt.close("all")
    
    plt.figure(1,figsize=(10,7),facecolor='whitesmoke')
    plt.figure(2,figsize=(10,7),facecolor='whitesmoke')
    plt.figure(3,figsize=(23,13),facecolor='whitesmoke')
    plt.figure(4,figsize=(23,13),facecolor='whitesmoke')
    
    symboltype=['o', 's', 'd', '^', 'v', 'p', 'h', '>', '<', '+', '*', 'x', 's', 'd', '^', 'v', 'p', 'h', '>', '<', '+', '*', 'x','o', 's', 'd', '^', 'v', 'p', 'h', '>', '<', '+', '*', 'x', 's', 'd', '^', 'v', 'p', 'h', '>', '<', '+', '*', 'x']
    #linetype  =['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.']
#    ms        =[ 10,   3,   3,   3,   3,   3,   3,   3,   3,   5,   5,   5,   3,   3,   3,   3,   3,   3,   3,   3,   5]
    colors    =['r', 'b', 'g', 'm', 'k', 'c', 'y', 'r', 'b', 'g', 'm', 'k', 'c', 'y', 'r', 'b', 'g', 'm', 'k', 'c', 'y', 'r', 'b', 'g', 'm', 'k', 'c', 'y', 'r', 'b', 'g', 'm', 'k', 'c', 'y', 'r', 'b', 'g', 'm', 'k', 'c', 'y', 'r', 'b', 'g', 'm', 'k', 'c', 'y']
    
#    xlsname=[]
#    xlsname.append('M996_20180124_224231_A_KH_1300_SK_SR33217_OPP1-1_IND.xls')
#    xlsname.append('M996_20180124_224425_A_KH_1300_SK_SR33217_OPP1-2_IND.xls')
#    xlsname.append('M996_20180124_225755_A_KH_1300_SK_SR33217_OPP2-1_IND.xls')
#    xlsname.append('M996_20180124_233100_A_KH_1300_SK_SR33217_OPP2-2_IND.xls')
#    xlsname.append('M996_20180125_000409_A_KH_1300_SK_SR33217_OPP3-1_IND.xls')
#    xlsname.append('M996_20180125_003140_A_KH_1300_SK_SR33217_OPP3-2_IND.xls')
#    xlsname.append('M996_20180125_004524_A_KH_1300_SK_SR33217_OPP3-3_IND.xls')
#    xlsname.append('M996_20180125_011257_A_KH_1300_SK_SR33217_OPP2-ZK_IND.xls')
#    xlsname.append('M996_20180125_031307_A_KH_1300_SK_SR33217_OPP2-3_IND.xls')
#    xlsname.append('M996_20180125_033042_A_KH_1300_SK_SR33217_OPP3-4_IND.xls')
#    xlsname.append('M996_20180125_035818_A_KH_1300_SK_SR33217_OPP3-5_IND.xls')
#    xlsname.append('M996_20180125_042559_A_KH_1300_SK_SR33217_OPP3-ZK_IND.xls')
#    xlsname.append('M996_20180125_051128_A_KH_1300_SK_SR33217_OPP3-6_IND.xls')
#    xlsname.append('M996_20180125_052716_A_KH_1300_SK_SR33217_OPP4-1_IND.xls')
#    xlsname.append('M996_20180125_054511_A_KH_1300_SK_SR33217_OPP4-ZK_IND.xls')
#    
#    strat_text=[]
#    strat_text.append('OPP1-1')
#    strat_text.append('OPP1-2')
#    strat_text.append('OPP2-1')
#    strat_text.append('OPP2-2')
#    strat_text.append('OPP3-1')
#    strat_text.append('OPP3-2')
#    strat_text.append('OPP3-3')
#    strat_text.append('OPP2-ZK')
#    strat_text.append('OPP2-3')
#    strat_text.append('OPP3-4')
#    strat_text.append('OPP3-5')
#    strat_text.append('OPP3-ZK')
#    strat_text.append('OPP3-6')
#    strat_text.append('OPP4-1')
#    strat_text.append('OPP4-ZK')
#    
#    path=[]
#    inj_text=[]
#    rpm_text=[]
#    fuel_text=[]
#    
#    numMeas=len(xlsname)
    
    
    numMeas=len(list(docid_dp))
    xlsname=[]
    strat_text=[]
    path=[]
    inj_text=[]
    rpm_text=[]
    fuel_text=[]
    date_text=[]
    
    
    for nM in range(0,numMeas):
        
#        path.append('D:\\Data\\projects\\Motorpruefstand\\Dai\\' + xlsname[nM][0:-4] )
#        inj_text.append('SR33217')
#        rpm_text.append('1300')
#        fuel_text.append('SK')
        
            xlsname.append(docid_dp[nM]['file_name'])
            path.append(docid_dp[0]['file_path'] + '\\' + xlsname[nM][0:-4])

        try:
            strat_text.append(docid_dp[nM]['OPP'])
        except:
            strat_text.append('-')
         
        try: 
            inj_text.append(docid_dp[nM]['SR'])
        except:
            inj_text.append('-')    
                
        try:
            rpm_text.append(docid_dp[nM]['rpm'])
        except:
            rpm_text.append('-')
            
        try:
            fuel_text.append(docid_dp[nM]['fuel'])
        except:
            fuel_text.append('-')            
            
        try:
            date_text.append(docid_dp[nM]['date'])
        except:
            date_text.append('-')
        
        f=open(path[nM] + '\\' + xlsname[nM])
        r=csv.reader(f)
        data=list(r)
        header=data[1][0].split("\t")
        #unit=data[2][0].split("\t")
        
        for i in range(0,len(data)):
            if [len(j) for j in [s.replace('\t', '') for s in data[i]]][0]:
                numofrow=i
        
        daten=[[0 for i in range(len(header))] for j in range(0,numofrow-2)]
        for i in range(0,numofrow-2):
            for j in range(len(header)):
                daten[i][j]=data[i+3][0].split("\t")[j]
                
                #for i in range(0,numofrow-3):
                #    print(daten[i][1])        
        
    #    try:  
            rpm=[]
            ind=header.index('N_M')
            for i in range(0,len(daten)):
                rpm.append(float(daten[i][ind]))
        #print(rpm)    
        
        mass_cyl0_pls1=[]
        ind=header.index('AS_MFF_STND_CYL_0_PLS_1_M')
        for i in range(0,len(daten)):
            mass_cyl0_pls1.append(float(daten[i][ind]))
        #print(mass_cyl0_pls1) 
        
        mass_cyl0_pls2=[]
        ind=header.index('AS_MFF_STND_CYL_0_PLS_2_M')
        for i in range(0,len(daten)):
            mass_cyl0_pls2.append(float(daten[i][ind]))
        #print(mass_cyl0_pls2) 
        
        mass_cyl0_pls3=[]
        ind=header.index('AS_MFF_STND_CYL_0_PLS_3_M')
        for i in range(0,len(daten)):
            mass_cyl0_pls3.append(float(daten[i][ind]))
        #print(mass_cyl0_pls3) 
        
        mass_cyl0_pls4=[]
        ind=header.index('AS_MFF_STND_CYL_0_PLS_4_M')
        for i in range(0,len(daten)):
            mass_cyl0_pls4.append(float(daten[i][ind]))
        #print(mass_cyl0_pls4)
        
        mass_cyl1_pls1=[]
        ind=header.index('AS_MFF_STND_CYL_1_PLS_1_M')
        for i in range(0,len(daten)):
            mass_cyl1_pls1.append(float(daten[i][ind]))
        #print(mass_cyl1_pls1) 
        
        mass_cyl1_pls2=[]
        ind=header.index('AS_MFF_STND_CYL_1_PLS_2_M')
        for i in range(0,len(daten)):
            mass_cyl1_pls2.append(float(daten[i][ind]))
        #print(mass_cyl1_pls2) 
        
        mass_cyl1_pls3=[]
        ind=header.index('AS_MFF_STND_CYL_1_PLS_3_M')
        for i in range(0,len(daten)):
            mass_cyl1_pls3.append(float(daten[i][ind]))
        #print(mass_cyl1_pls3) 
        
        mass_cyl1_pls4=[]
        ind=header.index('AS_MFF_STND_CYL_1_PLS_4_M')
        for i in range(0,len(daten)):
            mass_cyl1_pls4.append(float(daten[i][ind]))
        #print(mass_cyl1_pls4)
        
        mass_cyl2_pls1=[]
        ind=header.index('AS_MFF_STND_CYL_2_PLS_1_M')
        for i in range(0,len(daten)):
            mass_cyl2_pls1.append(float(daten[i][ind]))
        #print(mass_cyl2_pls1) 
        
        mass_cyl2_pls2=[]
        ind=header.index('AS_MFF_STND_CYL_2_PLS_2_M')
        for i in range(0,len(daten)):
            mass_cyl2_pls2.append(float(daten[i][ind]))
        #print(mass_cyl2_pls2) 
        
        mass_cyl2_pls3=[]
        ind=header.index('AS_MFF_STND_CYL_2_PLS_3_M')
        for i in range(0,len(daten)):
            mass_cyl2_pls3.append(float(daten[i][ind]))
        #print(mass_cyl2_pls3) 
        
        mass_cyl2_pls4=[]
        ind=header.index('AS_MFF_STND_CYL_2_PLS_4_M')
        for i in range(0,len(daten)):
            mass_cyl2_pls4.append(float(daten[i][ind]))
        #print(mass_cyl2_pls4)
            
        mass_cyl3_pls1=[]
        ind=header.index('AS_MFF_STND_CYL_3_PLS_1_M')
        for i in range(0,len(daten)):
            mass_cyl3_pls1.append(float(daten[i][ind]))
        #print(mass_cyl3_pls1) 
        
        mass_cyl3_pls2=[]
        ind=header.index('AS_MFF_STND_CYL_3_PLS_2_M')
        for i in range(0,len(daten)):
            mass_cyl3_pls2.append(float(daten[i][ind]))
        #print(mass_cyl3_pls2) 
        
        mass_cyl3_pls3=[]
        ind=header.index('AS_MFF_STND_CYL_3_PLS_3_M')
        for i in range(0,len(daten)):
            mass_cyl3_pls3.append(float(daten[i][ind]))
        #print(mass_cyl3_pls3) 
        
        mass_cyl3_pls4=[]
        ind=header.index('AS_MFF_STND_CYL_3_PLS_4_M')
        for i in range(0,len(daten)):
            mass_cyl3_pls4.append(float(daten[i][ind]))
        #print(mass_cyl3_pls4)
        
        masssp=[]
        ind=header.index('AS_MFF_SP_HOM_MV_M')
        for i in range(0,len(daten)):
            masssp.append(float(daten[i][ind]))
        #print(masssp)
        
        soiia=[]
        ind=header.index('AS_IGA_AV_MV_M')
        for i in range(0,len(daten)):
            soiia.append(float(daten[i][ind]))
        #print(soiia)
        
        soi1=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M') # soi 1. injection
        for i in range(0,len(daten)):
            soi1.append(float(daten[i][ind]))
        #print(soi1)
        
        soi2=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M') # soi 3. injection
        for i in range(0,len(daten)):
            soi2.append(float(daten[i][ind]))
        #print(soi2)
        
        soi3=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M') # soi 2. injection
        for i in range(0,len(daten)):
            soi3.append(float(daten[i][ind]))
        #print(soi3)
        
        CoV=[]
        ind=header.index('ISY_PI_V')
        for i in range(0,len(daten)):
            CoV.append(float(daten[i][ind]))
        #print(CoV)
        
        BSFC=[]
        ind=header.index('C_CNS_06_M')
        for i in range(0,len(daten)):
            BSFC.append(float(daten[i][ind]))
        #print(BSFC)
        
        PN=[]
        ind=header.index('PAC1_DL_CONC_49_M')
        for i in range(0,len(daten)):
            PN.append(float(daten[i][ind]))
        #print(PN)
        
        CO=[]
        ind=header.index('EG1_CO_15_M')
        for i in range(0,len(daten)):
            CO.append(float(daten[i][ind]))
        #print(CO)
        
        NOx=[]
        ind=header.index('EG1_NOX_16_M')
        for i in range(0,len(daten)):
            NOx.append(float(daten[i][ind]))
        #print(NOx)
        
        lambdav=[]
        ind=header.index('AS_LAMB_LS_UP_M')
        for i in range(0,len(daten)):
            lambdav.append(float(daten[i][ind]))
        #print(lambdav)
        
        HC=[]
        ind=header.index('EG1_THC_16_M')
        for i in range(0,len(daten)):
            HC.append(float(daten[i][ind]))
        #print(HC)
        
        TKAT=[]
        ind=header.index('T_B1CAT1B1_M')
        for i in range(0,len(daten)):
            TKAT.append(float(daten[i][ind]))
        #print(TKAT)
                    
        std=[]
        ind=header.index('ISY_PI_S')
        for i in range(0,len(daten)):
            std.append(float(daten[i][ind]))
        #print(std)                        
                                
        mitt=[]
        ind=header.index('ISY_PI_M')
        for i in range(0,len(daten)):
            mitt.append(float(daten[i][ind]))
        #print(mitt)
        
        cov=[]
        ind=header.index('ISY_PI_V')
        for i in range(0,len(daten)):
            cov.append(float(daten[i][ind]))
        #print(cov)
            
        std1=[]
        ind=header.index('ISY_PI1_S')
        for i in range(0,len(daten)):
            std1.append(float(daten[i][ind]))
        #print(std1)    
            
        std2=[]
        ind=header.index('ISY_PI2_S')
        for i in range(0,len(daten)):
            std2.append(float(daten[i][ind]))
        #print(std2)    
        
        std3=[]
        ind=header.index('ISY_PI3_S')
        for i in range(0,len(daten)):
            std3.append(float(daten[i][ind]))
        #print(std3)    
        
        std4=[]
        ind=header.index('ISY_PI4_S')
        for i in range(0,len(daten)):
            std4.append(float(daten[i][ind]))
        #print(std4)    
        
        mitt1=[]
        ind=header.index('ISY_PI1_M')
        for i in range(0,len(daten)):
            mitt1.append(float(daten[i][ind]))
        #print(mitt1)    
        
        mitt2=[]
        ind=header.index('ISY_PI2_M')
        for i in range(0,len(daten)):
            mitt2.append(float(daten[i][ind]))
        #print(mitt2)  
            
        mitt3=[]
        ind=header.index('ISY_PI3_M')
        for i in range(0,len(daten)):
            mitt3.append(float(daten[i][ind]))
        #print(mitt3)  
        
        mitt4=[]
        ind=header.index('ISY_PI4_M')
        for i in range(0,len(daten)):
            mitt4.append(float(daten[i][ind]))
        #print(mitt4)  
        
        cov1=[]
        ind=header.index('ISY_PI1_V')
        for i in range(0,len(daten)):
            cov1.append(float(daten[i][ind]))
        #print(cov1)  
            
        cov2=[]
        ind=header.index('ISY_PI2_V')
        for i in range(0,len(daten)):
            cov2.append(float(daten[i][ind]))
        #print(cov2)  
        
        cov3=[]
        ind=header.index('ISY_PI3_V')
        for i in range(0,len(daten)):
            cov3.append(float(daten[i][ind]))
        #print(cov3)  
        
        cov4=[]
        ind=header.index('ISY_PI4_V')
        for i in range(0,len(daten)):
            cov4.append(float(daten[i][ind]))
        #print(cov4)      
                           
        mafm=[]
        ind=header.index('AS_MAF0_03_M')
        for i in range(0,len(daten)):
            mafm.append(float(daten[i][ind]))
        #print(mafm)
            
        mafs=[]
        ind=header.index('AS_MAF0_03_S')
        for i in range(0,len(daten)):
            mafs.append(float(daten[i][ind]))
        #print(mafs)     
                                
        ti_pls1_cyl0=[]
        ind=header.index('AS_TI_MES_4_PLS_1_CYL_0_M')
        for i in range(0,len(daten)):
            ti_pls1_cyl0.append(float(daten[i][ind]))
        #print(ti_pls1_cyl0) 
            
        ti_pls2_cyl0=[]
        ind=header.index('AS_TI_MES_4_PLS_2_CYL_0_M')
        for i in range(0,len(daten)):   
            ti_pls2_cyl0.append(float(daten[i][ind]))
        #print(ti_pls2_cyl0)
        
        ti_pls3_cyl0=[]
        ind=header.index('AS_TI_MES_4_PLS_3_CYL_0_M')
        for i in range(0,len(daten)):
            ti_pls3_cyl0.append(float(daten[i][ind]))
        #print(ti_pls3_cyl0)
        
        ti_pls4_cyl0=[]
        ind=header.index('AS_TI_MES_4_PLS_4_CYL_0_M')
        for i in range(0,len(daten)):
            ti_pls4_cyl0.append(float(daten[i][ind]))
        #print(ti_pls4_cyl0)    
        
        ti_pls1_cyl1=[]
        ind=header.index('AS_TI_MES_4_PLS_1_CYL_1_M')
        for i in range(0,len(daten)):
            ti_pls1_cyl1.append(float(daten[i][ind]))
        #print(ti_pls1_cyl1) 
            
        ti_pls2_cyl1=[]
        ind=header.index('AS_TI_MES_4_PLS_2_CYL_1_M')
        for i in range(0,len(daten)):
            ti_pls2_cyl1.append(float(daten[i][ind]))
        #print(ti_pls2_cyl1)
        
        ti_pls3_cyl1=[]
        ind=header.index('AS_TI_MES_4_PLS_3_CYL_1_M')
        for i in range(0,len(daten)):
            ti_pls3_cyl1.append(float(daten[i][ind]))
        #print(ti_pls3_cyl1)
        
        ti_pls4_cyl1=[]
        ind=header.index('AS_TI_MES_4_PLS_4_CYL_1_M')
        for i in range(0,len(daten)):
            ti_pls4_cyl1.append(float(daten[i][ind]))
        #print(ti_pls4_cyl1) 
        
        ti_pls1_cyl2=[]
        ind=header.index('AS_TI_MES_4_PLS_1_CYL_2_M')
        for i in range(0,len(daten)):
            ti_pls1_cyl2.append(float(daten[i][ind]))
        #print(ti_pls1_cyl2) 
            
        ti_pls2_cyl2=[]
        ind=header.index('AS_TI_MES_4_PLS_2_CYL_2_M')
        for i in range(0,len(daten)):
            ti_pls2_cyl2.append(float(daten[i][ind]))
        #print(ti_pls2_cyl2)
        
        ti_pls3_cyl2=[]
        ind=header.index('AS_TI_MES_4_PLS_3_CYL_2_M')
        for i in range(0,len(daten)):
            ti_pls3_cyl2.append(float(daten[i][ind]))
        #print(ti_pls3_cyl2)
        
        ti_pls4_cyl2=[]
        ind=header.index('AS_TI_MES_4_PLS_4_CYL_2_M')
        for i in range(0,len(daten)):
            ti_pls4_cyl2.append(float(daten[i][ind]))
        #print(ti_pls4_cyl2) 
        
        ti_pls1_cyl3=[]
        ind=header.index('AS_TI_MES_4_PLS_1_CYL_3_M')
        for i in range(0,len(daten)):
            ti_pls1_cyl3.append(float(daten[i][ind]))
        #print(ti_pls1_cyl3) 
            
        ti_pls2_cyl3=[]
        ind=header.index('AS_TI_MES_4_PLS_2_CYL_3_M')
        for i in range(0,len(daten)):
            ti_pls2_cyl3.append(float(daten[i][ind]))
        #print(ti_pls2_cyl3)
        
        ti_pls3_cyl3=[]
        ind=header.index('AS_TI_MES_4_PLS_3_CYL_3_M')
        for i in range(0,len(daten)):
            ti_pls3_cyl3.append(float(daten[i][ind]))
        #print(ti_pls3_cyl3)
        
        ti_pls4_cyl3=[]
        ind=header.index('AS_TI_MES_4_PLS_4_CYL_3_M')
        for i in range(0,len(daten)):
            ti_pls4_cyl3.append(float(daten[i][ind]))
        #print(ti_pls4_cyl3) 
                                
        soi_pls1_cyl0=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_1_CYL_0_M')
        for i in range(0,len(daten)):
            soi_pls1_cyl0.append(float(daten[i][ind]))
        #print(soi_pls1_cyl0) 
        
        soi_pls2_cyl0=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_2_CYL_0_M')
        for i in range(0,len(daten)):
            soi_pls2_cyl0.append(float(daten[i][ind]))
        #print(soi_pls2_cyl0) 
        
        soi_pls3_cyl0=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_3_CYL_0_M')
        for i in range(0,len(daten)):
            soi_pls3_cyl0.append(float(daten[i][ind]))
        #print(soi_pls3_cyl0) 
        
        soi_pls4_cyl0=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_4_CYL_0_M')
        for i in range(0,len(daten)):
            soi_pls4_cyl0.append(float(daten[i][ind]))
        #print(soi_pls4_cyl0)     
        
        soi_pls1_cyl1=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_1_CYL_1_M')
        for i in range(0,len(daten)):
            soi_pls1_cyl1.append(float(daten[i][ind]))
        #print(soi_pls1_cyl1) 
        
        soi_pls2_cyl1=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_2_CYL_1_M')
        for i in range(0,len(daten)):
            soi_pls2_cyl1.append(float(daten[i][ind]))
        #print(soi_pls2_cyl1) 
        
        soi_pls3_cyl1=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_3_CYL_1_M')
        for i in range(0,len(daten)):
            soi_pls3_cyl1.append(float(daten[i][ind]))
        #print(soi_pls3_cyl1) 
        
        soi_pls4_cyl1=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_4_CYL_1_M')
        for i in range(0,len(daten)):
            soi_pls4_cyl1.append(float(daten[i][ind]))
        #print(soi_pls4_cyl1)  
        
        soi_pls1_cyl2=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_1_CYL_2_M')
        for i in range(0,len(daten)):
            soi_pls1_cyl2.append(float(daten[i][ind]))
        #print(soi_pls1_cyl2) 
        
        soi_pls2_cyl2=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_2_CYL_2_M')
        for i in range(0,len(daten)):
            soi_pls2_cyl2.append(float(daten[i][ind]))
        #print(soi_pls2_cyl2) 
        
        soi_pls3_cyl2=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_3_CYL_2_M')
        for i in range(0,len(daten)):
            soi_pls3_cyl2.append(float(daten[i][ind]))
        #print(soi_pls3_cyl2) 
        
        soi_pls4_cyl2=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_4_CYL_2_M')
        for i in range(0,len(daten)):
            soi_pls4_cyl2.append(float(daten[i][ind]))
        #print(soi_pls4_cyl2) 
        
        soi_pls1_cyl3=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_1_CYL_3_M')
        for i in range(0,len(daten)):
            soi_pls1_cyl3.append(float(daten[i][ind]))
        #print(soi_pls1_cyl3) 
        
        soi_pls2_cyl3=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_2_CYL_3_M')
        for i in range(0,len(daten)):
            soi_pls2_cyl3.append(float(daten[i][ind]))
        #print(soi_pls2_cyl3) 
        
        soi_pls3_cyl3=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_3_CYL_3_M')
        for i in range(0,len(daten)):
            soi_pls3_cyl3.append(float(daten[i][ind]))
        #print(soi_pls3_cyl3) 
        
        soi_pls4_cyl3=[]
        ind=header.index('AS_SOI_MES_CUS_PLS_4_CYL_3_M')
        for i in range(0,len(daten)):
            soi_pls4_cyl3.append(float(daten[i][ind]))
        #print(soi_pls4_cyl3) 
        
        ifile=[]
        ind=header.index('ISY_STRING_IFILE_NAME')
        for i in range(0,len(daten)):
            ifile.append((daten[i][ind]))
            #print(ifile) 
    #    except:
    #        print('Error at reading data!')
        
        
        matplotlib.rcParams['font.family']='Arial'
        matplotlib.rcParams['font.size']=18
        plt.rcParams['axes.axisbelow']=True
        
        title_text=(inj_text[nM] + '__' + rpm_text[nM] + '__' + fuel_text[nM])
        label_text=strat_text[nM] + '(' + date_text[nM] + ')'
        
        plt.figure(1)
        plt.plot(CoV,PN,symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=colors[nM], label=label_text)
        plt.hold(True)
        
        plt.figure(2)
        hom=[]
        stra=[]
        zk=[]
        for ie in range(0,len(soi1)):
            if soi1[ie]>=180 or soi3[ie]>=180 or soi2[ie]>=180: #homogen
                hom.append(1)
            else: #no homogen
                hom.append(0)
            if (soi1[ie]>0 and soi1[ie]<180) or (soi3[ie]>0 and soi3[ie]<180) or (soi2[ie]>0 and soi2[ie]<180): #stratified
                stra.append(1)
            else: #no stratified
                stra.append(0)
            if soi1[ie]<=0 or soi3[ie]<=0 or soi2[ie]<=0: #ZK
                zk.append(1)
            else: #no ZK
                zk.append(0)
            if hom[ie]==1 and stra[ie]==0 and zk[ie]==0: #homogen 
                col=(52.0/255,179.0/255,3.0/255)
            elif hom[ie]==1 and stra[ie]==1 and zk[ie]==0: #homogen + stratified   
                col=(239.0/255,166.0/255,4.0/255)
            elif hom[ie]==1 and stra[ie]==0 and zk[ie]==1: #homogen + zk
                col=(232.0/255,39.0/255,55.0/255)
            elif hom[ie]==1 and stra[ie]==1 and zk[ie]==1: #homogen + stratified + zk
                col=(20.0/255,22.0/255,138.0/255)
            else:
                col='black';
            plt.plot(CoV[ie],PN[ie],symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=col, label=label_text)
            plt.hold(True)
        
        plt.figure(3)
        plt.subplot(511)
        plt.plot(CoV,PN,symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=colors[nM], label=label_text)
        plt.xlim(0,45)
        plt.ylim(0,5e6)    
        plt.hold(True)
        plt.grid(True)
        plt.grid(b=True, which='minor', color='silver', linestyle=':')
        plt.minorticks_on()  
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
        plt.yticks([0, 5e6])
        plt.subplot(512)
        plt.plot(cov1,PN,symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=colors[nM], label=label_text)
        plt.xlim(0,45)
        plt.ylim(0,5e6)    
        plt.hold(True)
        plt.grid(True)
        plt.grid(b=True, which='minor', color='silver', linestyle=':')
        plt.minorticks_on()  
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
        plt.yticks([0, 5e6])
        plt.subplot(513)
        plt.plot(cov2,PN,symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=colors[nM], label=label_text)
        plt.xlim(0,45)
        plt.ylim(0,5e6)    
        plt.hold(True)
        plt.grid(True)
        plt.grid(b=True, which='minor', color='silver', linestyle=':')
        plt.minorticks_on()  
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
        plt.yticks([0, 5e6])
        plt.subplot(514)
        plt.plot(cov3,PN,symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=colors[nM], label=label_text)
        plt.xlim(0,45)
        plt.ylim(0,5e6)    
        plt.hold(True)
        plt.grid(True)
        plt.grid(b=True, which='minor', color='silver', linestyle=':')
        plt.minorticks_on()  
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
        plt.yticks([0, 5e6]) 
        plt.subplot(515)
        plt.plot(cov4,PN,symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=colors[nM], label=label_text)
        plt.xlim(0,45)
        plt.ylim(0,5e6)    
        plt.hold(True)
        plt.grid(True)
        plt.grid(b=True, which='minor', color='silver', linestyle=':')
        plt.minorticks_on()  
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
        plt.yticks([0, 5e6])
    
        plt.figure(4)
        for ie in range(0,len(soi1)):
            if soi1[ie]>=180 or soi3[ie]>=180 or soi2[ie]>=180: #homogen
                hom.append(1)
            else: #no homogen
                hom.append(0)
            if (soi1[ie]>0 and soi1[ie]<180) or (soi3[ie]>0 and soi3[ie]<180) or (soi2[ie]>0 and soi2[ie]<180): #stratified
                stra.append(1)
            else: #no stratified
                stra.append(0)
            if soi1[ie]<=0 or soi3[ie]<=0 or soi2[ie]<=0: #ZK
                zk.append(1)
            else: #no ZK
                zk.append(0)
            if hom[ie]==1 and stra[ie]==0 and zk[ie]==0: #homogen 
                col=(52.0/255,179.0/255,3.0/255)
            elif hom[ie]==1 and stra[ie]==1 and zk[ie]==0: #homogen + stratified   
                col=(239.0/255,166.0/255,4.0/255)
            elif hom[ie]==1 and stra[ie]==0 and zk[ie]==1: #homogen + zk
                col=(232.0/255,39.0/255,55.0/255)
            elif hom[ie]==1 and stra[ie]==1 and zk[ie]==1: #homogen + stratified + zk
                col=(20.0/255,22.0/255,138.0/255)
            else:
                col='black';        
            plt.subplot(511)
            plt.plot(CoV[ie],PN[ie],symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=col, label=label_text)
            plt.xlim(0,45)
            plt.ylim(0,5e6)    
            plt.hold(True)
            plt.grid(True)
            plt.grid(b=True, which='minor', color='silver', linestyle=':')
            plt.minorticks_on()  
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
            plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
            plt.yticks([0, 5e6])
            plt.subplot(512)
            plt.plot(cov1[ie],PN[ie],symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=col, label=label_text)
            plt.xlim(0,45)
            plt.ylim(0,5e6)    
            plt.hold(True)
            plt.grid(True)
            plt.grid(b=True, which='minor', color='silver', linestyle=':')
            plt.minorticks_on()  
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
            plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
            plt.yticks([0, 5e6])
            plt.subplot(513)
            plt.plot(cov2[ie],PN[ie],symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=col, label=label_text)
            plt.xlim(0,45)
            plt.ylim(0,5e6)    
            plt.hold(True)
            plt.grid(True)
            plt.grid(b=True, which='minor', color='silver', linestyle=':')
            plt.minorticks_on()  
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
            plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
            plt.yticks([0, 5e6])
            plt.subplot(514)
            plt.plot(cov3[ie],PN[ie],symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=col, label=label_text)
            plt.xlim(0,45)
            plt.ylim(0,5e6)    
            plt.hold(True)
            plt.grid(True)
            plt.grid(b=True, which='minor', color='silver', linestyle=':')
            plt.minorticks_on()  
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
            plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
            plt.yticks([0, 5e6]) 
            plt.subplot(515)
            plt.plot(cov4[ie],PN[ie],symboltype[nM], markersize=5, markerfacecolor='None',markeredgewidth=3, markeredgecolor=col, label=label_text)
            plt.xlim(0,45)
            plt.ylim(0,5e6)    
            plt.hold(True)
            plt.grid(True)
            plt.grid(b=True, which='minor', color='silver', linestyle=':')
            plt.minorticks_on()  
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
            plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
            plt.yticks([0, 5e6])
    
    
      
    plt.figure(1)
    plt.grid(True)
    plt.title(title_text, fontweight='bold', fontsize=18) 
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.xlim(0, 45)
    plt.ylim(0, 5e6)
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
    plt.yticks([0, 5e5, 1e6, 1.5e6, 2e6, 2.5e6, 3e6, 3.5e6, 4e6, 4.5e6, 5e6])
    plt.grid(b=True, which='minor', color='silver', linestyle=':')
    plt.minorticks_on()
    leg1=plt.legend(loc='best', numpoints=1, fontsize=16, handletextpad=0.0) 
    if leg1:
        leg1.draggable()
    plt.xlabel('CoV PMI [%]')
    plt.ylabel('Particle Number [#/ccm]')
    plt.show()
    
    plt.figure(2)
    plt.grid(True)
    plt.title(title_text, fontweight='bold', fontsize=18) 
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.xlim(0, 45)
    plt.ylim(0, 5e6)
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
    plt.yticks([0, 5e5, 1e6, 1.5e6, 2e6, 2.5e6, 3e6, 3.5e6, 4e6, 4.5e6, 5e6])
    plt.grid(b=True, which='minor', color='silver', linestyle=':')
    plt.minorticks_on()
    plt.xlabel('CoV PMI [%]')
    plt.ylabel('Particle Number [#/ccm]')
    plt.show()
    line1,=plt.plot(0,0,'-',color=(52.0/255,179.0/255,3.0/255),linewidth=15.0)
    line2,=plt.plot(0,0,'-',color=(239.0/255,166.0/255,4.0/255),linewidth=15.0)
    line3,=plt.plot(0,0,'-',color=(232.0/255,39.0/255,55.0/255),linewidth=15.0)
    line4,=plt.plot(0,0,'-',color=(20.0/255,22.0/255,138.0/255),linewidth=15.0)
    leg2=plt.legend((line1,line2,line3,line4),('homogen','homogen + stratified','homogen + ZK','homogen + stratified + ZK'),loc='best', numpoints=1, fontsize=18, borderpad=0.6, labelspacing=0.2)
    if leg2:
        leg2.draggable()
        
    plt.figure(3)
    plt.subplot(511)
    plt.title(title_text + '\nCOV mean', fontweight='bold', fontsize=18)
    plt.subplot(512)
    plt.title('COV cylinder 1', fontweight='bold', fontsize=18)
    plt.subplot(513)
    plt.title('COV cylinder 2', fontweight='bold', fontsize=18)
    plt.ylabel('Particle Number [#/ccm]')
    legend_y=0.75+nM/10.0
    leg3=plt.legend(loc='upper center', bbox_to_anchor=(1.08, legend_y), numpoints=1, handletextpad=0.0, fontsize=16)
    if leg3:
        leg3.draggable()    
    plt.subplot(514)
    plt.title('COV cylinder 3', fontweight='bold', fontsize=18)
    plt.subplot(515)
    plt.title('COV cylinder 4', fontweight='bold', fontsize=18)
    plt.xlabel('CoV PMI [%]')
    plt.tight_layout(pad=1, h_pad=0.0, rect=(0,0,0.88,1))
    
    plt.figure(4)
    plt.subplot(511)
    line1,=plt.plot(0,0,'-',color=(52.0/255,179.0/255,3.0/255),linewidth=15.0)
    line2,=plt.plot(0,0,'-',color=(239.0/255,166.0/255,4.0/255),linewidth=15.0)
    line3,=plt.plot(0,0,'-',color=(232.0/255,39.0/255,55.0/255),linewidth=15.0)
    line4,=plt.plot(0,0,'-',color=(20.0/255,22.0/255,138.0/255),linewidth=15.0)
    leg4=plt.legend((line1,line2,line3,line4),('homogen','homogen + stratified','homogen + ZK','homogen + stratified + ZK'),loc='best', numpoints=1, fontsize=18, borderpad=0.6, labelspacing=0.2)
    if leg4:
        leg4.draggable()    
    plt.title(title_text + '\nCOV mean', fontweight='bold', fontsize=18)
    plt.subplot(512)
    plt.title('COV cylinder 1', fontweight='bold', fontsize=18)
    plt.subplot(513)
    plt.title('COV cylinder 2', fontweight='bold', fontsize=18)
    plt.ylabel('Particle Number [#/ccm]')
    plt.subplot(514)
    plt.title('COV cylinder 3', fontweight='bold', fontsize=18)
    plt.subplot(515)
    plt.title('COV cylinder 4', fontweight='bold', fontsize=18)
    plt.xlabel('CoV PMI [%]')
    plt.tight_layout(pad=1, h_pad=0.0, rect=(0,0,0.88,1))
    
    toc=time.time()
    print(str("%.2f" %(toc-tic)) + ' seconds elapsed')    