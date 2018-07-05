# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 16:47:41 2018

@author: uid18326
"""
import Tkinter as tk
import numpy as np
import struct
import operator 
from math import cos, sin, asin, degrees
from scipy.optimize import fsolve
import os.path

def indi_read_all_new_20180307(ifile,channel_masks):
    datatrans,datainfo,signalname,signalunit,calc_val=indi_read_ifile(ifile,channel_masks)   
    for k in range(0,len(datatrans['kalfak1'])):      
        if not np.isnan(datatrans['kalfak1'][k]):
            datatrans['value'][k]=np.array(datatrans['value'][k])*datatrans['kalfak1'][k]+datatrans['kalfak0'][k]
    
#    import matplotlib.pyplot as plt
#    fig12=plt.figure(1)
#    for i in range(0,50):    
#        plt.plot(datatrans['angle'][0],datatrans['value'][0][i])
#        plt.hold(True)

    return(datatrans,datainfo,signalname,signalunit,calc_val)

#function fseek_and_check(varargin)
def fseek_and_check(*varargin):
    varargin[0].seek(0,2)
    fp_end=varargin[0].tell()    
    varargin[0].seek(varargin[1],varargin[2])
    fp_cur=varargin[0].tell()
    if fp_cur>fp_end-256:
        popup=tk.Tk()    
        popup.geometry('800x100+800+300')
        popup.wm_title('Warning')
        label=tk.Label(popup, text='Tried to access an address which is larger than length of file - iFile probably corrupted!', font=('Helvetica', 10))
        label.pack(side='top', fill='x', pady=10)
        B1=tk.Button(popup, text='Ok', font=('Helvetica','10'), width=7, command = popup.destroy)
        B1.pack()
        popup.focus_set()
        popup.grab_set()
        popup.wait_window()
        popup.mainloop()

#function dg=get_data_group_info(fid,start_adr)
def get_data_group_info(f,start_adr):
################################################### Data Group Description (DGB) ############################
    f.seek(start_adr,0)
    
    dg_datart_bin=f.read(2)
    dg_datart_decoded=struct.unpack('h',dg_datart_bin)
    dg_datart=dg_datart_decoded[0]
   
    f.seek(2,1)
    f.seek(10,1)

    dg_dltphi_bin=f.read(8)
    dg_dltphi_decoded=struct.unpack('d',dg_dltphi_bin)
    dg_dltphi=dg_dltphi_decoded[0]

    dg_dltzei_bin=f.read(8)
    dg_dltzei_decoded=struct.unpack('d',dg_dltzei_bin)
    dg_dltzei=dg_dltzei_decoded[0]
    if dg_dltzei==0:
        dg_dltzei=0.01
    
    dg_kananz_bin=f.read(2)
    dg_kananz_decoded=struct.unpack('h',dg_kananz_bin)
    dg_kananz=dg_kananz_decoded[0]

    f.seek(8,1)
    dg_fortyp=struct.unpack('h',f.read(2))[0]
    dg_beranz=struct.unpack('h',f.read(2))[0]
    f.seek(2,1)    
    dg_zykanz=struct.unpack('l',f.read(4))[0]   
    f.seek(20,1)
    dg_datfor=struct.unpack('h',f.read(2))[0]   
    f.seek(6,1)
    dg_diradr=struct.unpack('i',f.read(4))[0]   
    f.seek(4,1)
    dg_mpladr=struct.unpack('i',f.read(4))[0]  
    f.seek(4,1)
    dg_rztadr=struct.unpack('i',f.read(4))[0]  
    f.seek(8,1)
    dg_thekx1=struct.unpack('d',f.read(8))[0]
    dg_thekx2=struct.unpack('d',f.read(8))[0]
    dg_polexp=struct.unpack('d',f.read(8))[0]

####################### Data Content Directory (Dateninhaltsverzeichnis) ####################################
    fseek_and_check(f,dg_diradr,0)

    for i in range(0,dg_kananz):
        signame_bin=struct.unpack('10s',f.read(10))[0].strip('\x00').replace('_',' ') 
        f.seek(118,1)
        if i==0:        
            signame_list=[signame_bin]
        else:
            signame_list.append(signame_bin)

    fseek_and_check(f,dg_diradr+10,0)
    
    for i in range(0,dg_kananz):
        signaleinheit_bin=struct.unpack('10s',f.read(10))[0].strip('\x00').replace('_',' ') 
        f.seek(118,1)
        if i==0:        
            signalunit_list=[signaleinheit_bin]
        else:
            signalunit_list.append(signaleinheit_bin)

    fseek_and_check(f,dg_diradr+50,0)

    for i in range(0,dg_kananz):
        abskor_bin=struct.unpack('l',f.read(4))[0]
        f.seek(124,1)        
        if i==0: 
            abskor_list=[abskor_bin]
        else:
            abskor_list.append(abskor_bin)

    fseek_and_check(f,dg_diradr+54,0)

    for i in range(0,dg_kananz):
        desori_bin=struct.unpack('h',f.read(2))[0]
        f.seek(126,1)        
        if i==0: 
            desori_list=[desori_bin]
        else:
            desori_list.append(desori_bin)
    
    fseek_and_check(f,dg_diradr+56,0)

    for i in range(0,dg_kananz):
        zykofs_bin=struct.unpack('l',f.read(4))[0]
        f.seek(124,1)        
        if i==0: 
            zykofs_list=[zykofs_bin]
        else:
            zykofs_list.append(zykofs_bin)    

    fseek_and_check(f,dg_diradr+62,0)

    for i in range(0,dg_kananz):
        nultyp_bin=struct.unpack('h',f.read(2))[0]
        f.seek(126,1)        
        if i==0: 
            nultyp_list=[nultyp_bin]
        else:
            nultyp_list.append(nultyp_bin)  

    fseek_and_check(f,dg_diradr+80,0)
      
    for i in range(0,dg_kananz):
        kalfak0_bin=struct.unpack('d',f.read(8))[0]
        f.seek(120,1)        
        if i==0: 
            kalfak0_list=[kalfak0_bin]
        else:
            kalfak0_list.append(kalfak0_bin)  

    fseek_and_check(f,dg_diradr+88,0)
    
#      dg.data_content_dir.kalfak1=fread(fid,dg.kananz,'double',120)';
    for i in range(0,dg_kananz):
        kalfak1_bin=struct.unpack('d',f.read(8))[0]
        f.seek(120,1)        
        if i==0: 
            kalfak1_list=[kalfak1_bin]
        else:
            kalfak1_list.append(kalfak1_bin)  

############################## Channel Content Table (Datenbereich) #########################################
    fseek_and_check(f,dg_mpladr,0)

    for i in range(0,dg_kananz*dg_beranz):
        for j in range(0,5):
            tmp_bin=struct.unpack('l',f.read(4))[0]
            if i==0 and j==0: 
                tmp_list=[[tmp_bin]]
            elif not i==0 and j==0:
                tmp_list.append([tmp_bin])
            else:
                tmp_list[i].append(tmp_bin)  
    for n in range(0,len(tmp_list)):
        if n==0:        
            beranf_list=[tmp_list[n][0]]
            wrtanz_list=[tmp_list[n][1]]
            absint_list=[tmp_list[n][2]]
            beradr_list=[tmp_list[n][3]]
            adrint_list=[tmp_list[n][4]]
        else:
            beranf_list.append(tmp_list[n][0])
            wrtanz_list.append(tmp_list[n][1])
            absint_list.append(tmp_list[n][2])
            beradr_list.append(tmp_list[n][3])
            adrint_list.append(tmp_list[n][4])

################################################ Calculate Values ###########################################
    deltaphi=list(map(lambda x: x*dg_dltphi, absint_list))
    startangle=list(map(lambda x: x*dg_dltphi, beranf_list))
#    import operator    
    endangle=list(map(operator.sub,map(operator.add,[a*b for a,b in zip(wrtanz_list,deltaphi)],startangle),deltaphi))

    startangleproK_list=np.reshape(startangle,(dg_kananz,dg_beranz)).tolist()
    endangleproK_list=np.reshape(endangle,(dg_kananz,dg_beranz)).tolist()
    berardrmat_list=np.reshape(beradr_list,(dg_kananz,dg_beranz)).tolist()
    deltaphiresh_list=np.reshape(deltaphi,(dg_kananz,dg_beranz)).tolist()
    wrtanzproK_list=np.reshape(wrtanz_list,(dg_kananz,dg_beranz)).tolist()
    
    lv_valid_list1=[map(lambda x:(x!=0)*1, x) for x in wrtanzproK_list]
    lv_valid_list21=map(lambda x: (x!=0)*1, adrint_list)
    lv_valid_list22=map(lambda x: (x!=0)*1, absint_list)
    lv_valid_list2=np.reshape([a*b for a,b in zip(lv_valid_list21,lv_valid_list22)],(dg_kananz,dg_beranz)).tolist()
    lv_valid_list=[[lv_valid_list1[i1][j1]*lv_valid_list2[i2][j2] for j1,j2 in zip(range(len(lv_valid_list1[i1])),range(len(lv_valid_list2[i2])))] for i1,i2 in zip(range(len(lv_valid_list1)),range(len(lv_valid_list2)))]
    
    return(dg_datart,dg_dltphi,dg_dltzei,dg_kananz,dg_fortyp,dg_beranz,dg_zykanz,
           dg_datfor,dg_diradr,dg_mpladr,dg_rztadr,dg_thekx1,dg_thekx2,dg_polexp,
           signame_list,signalunit_list,abskor_list,desori_list,zykofs_list,
           nultyp_list,kalfak0_list,kalfak1_list,beranf_list,wrtanz_list,absint_list,
           beradr_list,adrint_list,startangleproK_list,endangleproK_list,berardrmat_list,
           deltaphiresh_list,wrtanzproK_list,lv_valid_list)


#function tmp_datatrans=get_channel_data(dg,DATA,fid,desaxi,desaxi2)
#def get_channel_data(dg,ind_dg_crk,DATA,f,desaxi,desaxi2):
#    dt_sz_string=dg['datfor'][ind_dg_crk]*8
#    if dg['fortyp'][ind_dg_crk]==0:
#        dt_string='int';
#        dest_dt_sz_string=[dt_string + str(dt_sz_string)]
#        #tempDATA=int(0)
#        tempDATA=[]
#    elif dg['fortyp'][ind_dg_crk]==1:
#        dt_string='float';
#        dest_dt_sz_string=[dt_string + str(dt_sz_string)]  
#        #tempDATA=float(0)
#        tempDATA=[]
#    else:
#        print('ERROR3! Hmmm! Unknown fortyp value!')
#    #dt_sz_string1=[dt_string + str(dt_sz_string)]
#    tmpANGLE=[]   
#    valid_beranz=[index for index, value in enumerate(dg['chan_content_tab']['lv_valid'][0][DATA]) if value==1]
#    for z in (valid_beranz):
#        sa=(dg['chan_content_tab']['startangleproK'][ind_dg_crk][DATA][z])
#        da=(dg['chan_content_tab']['deltaphiresh'][ind_dg_crk][DATA][z])
#        ea=(dg['chan_content_tab']['endangleproK'][ind_dg_crk][DATA][z])
#        tmpANGLE=tmpANGLE+[(x*da)+sa for x in range(int(abs((sa-ea)/da))+1)]
#        
#        fseek_and_check(f,dg['chan_content_tab']['berardrmat'][ind_dg_crk][DATA][z],0)
#
#        # In Data postprocessing Results sometimes datfor = 0 -> use no_skip_bytes only where necessary
#        if dg['datfor'][ind_dg_crk]>0 and dg['data_content_dir']['zykofs'][ind_dg_crk][DATA]>0:
#            nsb1=dg['data_content_dir']['zykofs'][ind_dg_crk][DATA]*dg['datfor'][ind_dg_crk]      
#            nsb2=dg['datfor'][ind_dg_crk]*dg['chan_content_tab']['wrtanzproK'][ind_dg_crk][DATA][z] 
#            no_skip_bytes=[nsb1-nsb2]
#        else:
#            no_skip_bytes=[]
#
#        for i in range(0,dg['zykanz'][ind_dg_crk]):
#            for j in range(0,dg['chan_content_tab']['wrtanzproK'][ind_dg_crk][DATA][z]):            
#                tmp1_bin=struct.unpack('h',f.read(2))[0]
#                if j==0:        
#                    tmp1=[tmp1_bin]
#                else:
#                    tmp1.append(tmp1_bin)
#            if z==valid_beranz[0]:
#                tempDATA.append(tmp1)
#            else:
#                tempDATA[i]=tempDATA[i]+tmp1   
#            f.seek(no_skip_bytes[0],1)
#            
#    if dest_dt_sz_string=='double':
#        tempDATA=(np.array(tempDATA)*dg['data_content_dir']['kalfak1'][ind_dg_crk][DATA]+dg['data_content_dir']['kalfak0'][ind_dg_crk][DATA]).tolist()
#        kalfak0=None
#        kalfak1=None
#    else:
#        kalfak0=dg['data_content_dir']['kalfak0'][ind_dg_crk][DATA]
#        kalfak1=dg['data_content_dir']['kalfak1'][ind_dg_crk][DATA]
#    
#    sign=lambda a: (a>0)-(a<0)
#    if dg['data_content_dir']['desori'][ind_dg_crk][DATA]==-1 or dg['data_content_dir']['desori'][ind_dg_crk][DATA]==0 or dg['data_content_dir']['desori'][ind_dg_crk][DATA]==1:
#        desaxis=desaxi*sign(dg['data_content_dir']['desori'][ind_dg_crk][DATA])
#    elif dg['data_content_dir']['desori'][ind_dg_crk][DATA]==-2 or dg['data_content_dir']['desori'][ind_dg_crk][DATA]==2:
#        desaxis=desaxi2*sign(dg['data_content_dir']['desori'][ind_dg_crk][DATA])
#    else:
#        print('Unknown value for desori!')
#       
#    tmp_datatrans={'label':dg['data_content_dir']['signalname'][ind_dg_crk][DATA],
#                   'unit':dg['data_content_dir']['signalunit'][ind_dg_crk][DATA],
#                   'angle':tmpANGLE,
#                   'value':tempDATA,
#                   'kalfak0':kalfak0,
#                   'kalfak1':kalfak1,
#                   'tdc_ofs':dg['data_content_dir']['abskor'][ind_dg_crk][DATA]*dg['dltphi'][ind_dg_crk],
#                   'corr_type':'',
#                   'p_offset':0,
#                   'lv_cor':0,
#                   'desaxis':desaxis}
                   
#    if DATA==6:
#        print((tmp_datatrans['angle'])) 
#        print(len(tmp_datatrans['value'])) 
#        print(len(tmp_datatrans['value'][0]))            
#        import matplotlib.pyplot as plt
#        for i in range(len(tmp_datatrans['value'])):       
#            plt.plot(tmp_datatrans['angle'],tmp_datatrans['value'][i],label=str(i))
#            plt.hold(True)
#            leg4=plt.legend(loc='best', numpoints=1, fontsize=18, borderpad=0.6, labelspacing=0.2)
#            if leg4:
#                leg4.draggable()    

    return(tmp_datatrans)

#function tmp_datatrans=get_channel_data(dg,DATA,fid,desaxi,desaxi2)
def new_get_channel_data(dg_tmp,DATA,f,desaxi,desaxi2):
    dt_sz_string=dg_tmp['datfor']*8
    if dg_tmp['fortyp']==0:
        dt_string='int';
        dest_dt_sz_string=[dt_string + str(dt_sz_string)]
        tempDATA=[]
    elif dg_tmp['fortyp']==1:
        dt_string='float'
        dest_dt_sz_string='double'  
        tempDATA=[]
    else:
        print('ERROR3! Hmmm! Unknown fortyp value!')
#    dt_sz_string1=[dt_string + str(dt_sz_string)]
    tmpANGLE=[]   
    valid_beranz=[index for index, value in enumerate(dg_tmp['chan_content_tab']['lv_valid'][DATA]) if value==1]   
    for z in (valid_beranz):
        sa=(dg_tmp['chan_content_tab']['startangleproK'][DATA][z])
        da=(dg_tmp['chan_content_tab']['deltaphiresh'][DATA][z])
        ea=(dg_tmp['chan_content_tab']['endangleproK'][DATA][z])
        tmpANGLE=tmpANGLE+[(x*da)+sa for x in range(int(abs((sa-ea)/da))+1)]
        
        fseek_and_check(f,dg_tmp['chan_content_tab']['berardrmat'][DATA][z],0)

        # In Data postprocessing Results sometimes datfor = 0 -> use no_skip_bytes only where necessary
        if dg_tmp['datfor']>0 and dg_tmp['data_content_dir']['zykofs'][DATA]>0:
            nsb1=dg_tmp['data_content_dir']['zykofs'][DATA]*dg_tmp['datfor']     
            nsb2=dg_tmp['datfor']*dg_tmp['chan_content_tab']['wrtanzproK'][DATA][z] 
            no_skip_bytes=[nsb1-nsb2]
        else:
            no_skip_bytes=[]
        for i in range(0,dg_tmp['zykanz']):
            for j in range(0,dg_tmp['chan_content_tab']['wrtanzproK'][DATA][z]):            
                if dest_dt_sz_string=='double':
                    tmp1_bin=struct.unpack('f',f.read(4))[0]
                else:
                    tmp1_bin=struct.unpack('h',f.read(2))[0]
                if j==0:        
                    tmp1=[tmp1_bin]
                else:
                    tmp1.append(tmp1_bin)
                        
            if z==valid_beranz[0]:# and dest_dt_sz_string!='double':
                tempDATA.append(tmp1)
#            elif z==valid_beranz[0] and dest_dt_sz_string=='double':
#                tempDATA=tmp1
            else:
                tempDATA[i]=tempDATA[i]+tmp1   
            if no_skip_bytes:
                f.seek(no_skip_bytes[0],1)
                
    if dest_dt_sz_string=='double':
####################################   
        tempDATA=(np.array(tempDATA)*dg_tmp['data_content_dir']['kalfak1'][DATA]+dg_tmp['data_content_dir']['kalfak0'][DATA]).tolist()
        kalfak0='None'
        kalfak1='None'
    else:
        kalfak0=dg_tmp['data_content_dir']['kalfak0'][DATA]
        kalfak1=dg_tmp['data_content_dir']['kalfak1'][DATA]
    
    sign=lambda a: (a>0)-(a<0)
    if dg_tmp['data_content_dir']['desori'][DATA]==-1 or dg_tmp['data_content_dir']['desori'][DATA]==0 or dg_tmp['data_content_dir']['desori'][DATA]==1:
        desaxis=desaxi*sign(dg_tmp['data_content_dir']['desori'][DATA])
    elif dg_tmp['data_content_dir']['desori'][DATA]==-2 or dg_tmp['data_content_dir']['desori'][DATA]==2:
        desaxis=desaxi2*sign(dg_tmp['data_content_dir']['desori'][DATA])
    else:
        print('Unknown value for desori!')
       
    tmp_datatrans={'label':dg_tmp['data_content_dir']['signalname'][DATA],
                   'unit':dg_tmp['data_content_dir']['signalunit'][DATA],
                   'angle':tmpANGLE,
                   'value':tempDATA,
                   'kalfak0':kalfak0,
                   'kalfak1':kalfak1,
                   'tdc_ofs':dg_tmp['data_content_dir']['abskor'][DATA]*dg_tmp['dltphi'],
                   'corr_type':'',
                   'p_offset':0,
                   'lv_cor':0,
                   'desaxis':desaxis}
#    print(tempDATA)              
#    if DATA==0:
#        print(len(tempDATA))
#        print(dg_tmp['data_content_dir']['kalfak1'][DATA])
#        print(dg_tmp['data_content_dir']['kalfak0'][DATA])
##        print((tmp_datatrans['angle'])) 
##        print(len(tmp_datatrans['value'])) 
##        print(len(tmp_datatrans['value'][0]))            
#        import matplotlib.pyplot as plt
#        for i in range(len(tmp_datatrans['value'])):       
#            plt.plot(tmp_datatrans['angle'],tmp_datatrans['value'][i],label=str(i))
#            plt.hold(True)
#            leg4=plt.legend(loc='best', numpoints=1, fontsize=18, borderpad=0.6, labelspacing=0.2)
#            if leg4:
#                leg4.draggable()    

    return(tmp_datatrans)


#function [ v_rel, theta_deg_bdc, r_lc_ratio] = f_cyl_vol_rel_20180307( theta_deg, compression_ratio, s_lc_ratio, y_lc_ratio )
def f_cyl_vol_rel_20180307(theta_deg,compression_ratio,s_lc_ratio,y_lc_ratio):
    f_true_stroke_rel=lambda r_lc_rat,y_lc_rat: ((1+r_lc_rat)**2-y_lc_rat**2 )**0.5-((1-r_lc_rat)**2-y_lc_rat**2)**0.5
    f_zero_fun=lambda r_lc_ratio0: f_true_stroke_rel(r_lc_ratio0,y_lc_ratio)-s_lc_ratio
#    from scipy.optimize import fsolve    
    r_lc_ratio=fsolve(f_zero_fun, s_lc_ratio/2)
    y_r_ratio=y_lc_ratio/r_lc_ratio

#    from math import cos, sin, asin, degrees
    
    f_cyl_position=lambda theta_deg: r_lc_ratio*((1+((1/r_lc_ratio)**2-y_r_ratio**2)**0.5)-((cos(theta_deg*np.pi/180))+((1/r_lc_ratio)**2-((sin(theta_deg*np.pi/180))-y_r_ratio)**2)**0.5))

    f_cyl_position2=lambda theta_deg: r_lc_ratio*((1+((1/r_lc_ratio)**2-y_r_ratio**2)**0.5)-([(cos(i*np.pi/180)) for i in theta_deg]+((1/r_lc_ratio)**2-([(sin(i*np.pi/180)) for i in theta_deg]-y_r_ratio)**2)**0.5))
   
    theta_piston_TDC=degrees(asin(y_r_ratio/(1/r_lc_ratio+1)))
    theta_piston_BDC=degrees(asin(y_r_ratio/(1/r_lc_ratio-1)))+180
    theta_deg_bdc=theta_piston_BDC-theta_piston_TDC; # norm: 0 deg = TDC(piston)

    cyl_position_piston_TDC=f_cyl_position(theta_piston_TDC)
    #cyl_position_piston_BDC=f_cyl_position(theta_piston_BDC)

    delta_cyl_position_piston_TDC=f_cyl_position2([theta_piston_TDC+i for i in theta_deg])-cyl_position_piston_TDC

#    import matplotlib.pyplot as plt    
#    plt.plot(delta_cyl_position_piston_TDC)
#    plt.hold(True)

    v_rel=(compression_ratio-1)*delta_cyl_position_piston_TDC/s_lc_ratio+1

    #return(v_rel,theta_deg_bdc,r_lc_ratio)
    return(v_rel,theta_deg_bdc)
    
    
#function [ v_rel, ang_bdc ] = calc_vol_rel_comb_chamber_new_20180307( ang, compression, s_lc_ratio, y_lc_ratio )
def calc_vol_rel_comb_chamber_new_20180307(ang,compression,s_lc_ratio,y_lc_ratio):
    if y_lc_ratio!=0:
        v_rel,ang_bdc=f_cyl_vol_rel_20180307(ang,compression,s_lc_ratio,y_lc_ratio)
    else:
        from math import cos, sin
        r_lc_ratio=0.5*s_lc_ratio
        v_rel=[1+0.5*(compression-1)*((1-(cos(i*np.pi/180)))+1/r_lc_ratio*(1-(1-(r_lc_ratio**2)*(sin(i*np.pi/180))**2)**0.5)) for i in ang]
        ang_bdc=180
    return(v_rel,ang_bdc)
    

def indi_read_ifile(ifile,channel_masks):
    #datart_type=('Crank synchronous','Time synchronous','Real Time Processing Results','Data postprocessing Results','Asynchronous UTC Data','Unknown');
    #name_dlg_not_supported_data_taype='Not supported data type found in i-file ...';
    #supported_datart=[1,3,4];
    
    #import os.path
    #import Tkinter as tk
    #import struct
    
    if not os.path.isfile(ifile):
        popup=tk.Toplevel()
        popup.geometry('900x100+800+300')
        popup.wm_title('Warning')
        label=tk.Label(popup, text='File: ' + str(ifile) + ' does not exist!', font=('Helvetica', 10))
        label.pack(side='top', fill='x', pady=10)
        B1=tk.Button(popup, text='Ok', font=('Helvetica','10'), width=7, command = popup.destroy)
        B1.pack()
        popup.focus_set()
        popup.grab_set()
        popup.wait_window()
        popup.mainloop()
    
    ################################# General parameter block (APB) #############################################
    with open(ifile,'rb') as f:
        #data=f.read()
        
        f.seek(0)
        parlng_bin=f.read(2)
        parlng_decoded=struct.unpack('h',parlng_bin)
        parlng=parlng_decoded[0]
        
        grpanz_bin=f.read(2)
        grpanz_decoded=struct.unpack('h',grpanz_bin)
        grpanz=grpanz_decoded[0]
        
        filkom_bin=f.read(80)
        filkom_decoded=struct.unpack('80s',filkom_bin)
        filkom=filkom_decoded[0].strip('\x00')
        
        mesdat_bin=f.read(24)
        mesdat_decoded=struct.unpack('24s',mesdat_bin)
        mesdat_stripped=mesdat_decoded[0].strip('\x00')
        mesdat_replaced=mesdat_stripped.replace(' ','0')     
        mesdat=mesdat_replaced
        
        if len(mesdat)==14:
            try:
                mesdat=str(mesdat[6:8] + '-' + mesdat[4:6] + '-' + mesdat[0:4] + '   ' + mesdat[8:10] + ':' + mesdat[10:12] + ':' + mesdat[12:14])
            except:
                pass
    
        parfil_bin=f.read(18)
        parfil_decoded=struct.unpack('18s',parfil_bin)
        parfil=parfil_decoded[0].strip('\x00')
    
        f.seek(18,1)
        f.seek(10,1)
    
        motnam_bin=f.read(18)
        motnam_decoded=struct.unpack('18s',motnam_bin)
        motnam=motnam_decoded[0].strip('\x00')    
    
        mottyp_bin=f.read(2)
        mottyp_decoded=struct.unpack('h',mottyp_bin)
        mottyp=mottyp_decoded[0]
        if mottyp==0:
            motortype='Diesel'
        else:
            motortype='Gasoline'
    
        tktanz_bin=f.read(2)
        tktanz_decoded=struct.unpack('h',tktanz_bin)
        tktanz=tktanz_decoded[0]
        if tktanz==0:
            stroketype=4
        else:
            stroketype=2
        
        geoein_bin=f.read(2)
        geoein_decoded=struct.unpack('h',geoein_bin)
        geoein=geoein_decoded[0]
        if geoein==0:
            units='mm'
        else:
            units='inch'
        
        hublng_bin=f.read(8)
        hublng_decoded=struct.unpack('d',hublng_bin)
        hublng=hublng_decoded[0]
        
        pleuel_bin=f.read(8)
        pleuel_decoded=struct.unpack('d',pleuel_bin)
        pleuel=pleuel_decoded[0]   
        
        bohrng_bin=f.read(8)
        bohrng_decoded=struct.unpack('d',bohrng_bin)
        bohrng=bohrng_decoded[0]
    
        kompre_bin=f.read(8)
        kompre_decoded=struct.unpack('d',kompre_bin)
        kompre=kompre_decoded[0]
        
        desaxi_bin=f.read(8)
        desaxi_decoded=struct.unpack('d',desaxi_bin)
        desaxi=desaxi_decoded[0]
        
        f.seek(8,1)
    
        version_bin=f.read(2)
        version_decoded=struct.unpack('h',version_bin)
        version=version_decoded[0]
    
        desaxi2_bin=f.read(8)
        desaxi2_decoded=struct.unpack('d',desaxi2_bin)
        desaxi2=desaxi2_decoded[0]
    
        f.seek(12,1)
    
        bpar_bin=f.read(28)
        bpar_decoded=struct.unpack('28s',bpar_bin)
        bpar=bpar_decoded[0].strip('\x00')
    
    ################################################### Data Group Descriptions (DGBs) ##########################
        dg={}
        for k in range(1,grpanz+1):
            dg_datart,dg_dltphi,dg_dltzei,dg_kananz,dg_fortyp,dg_beranz,dg_zykanz,dg_datfor,dg_diradr,dg_mpladr,dg_rztadr,dg_thekx1,dg_thekx2,dg_polexp,signame_list,signalunit_list,abskor_list,desori_list,zykofs_list,nultyp_list,kalfak0_list,kalfak1_list,beranf_list,wrtanz_list,absint_list,beradr_list,adrint_list,startangleproK_list,endangleproK_list,berardrmat_list,deltaphiresh_list,wrtanzproK_list,lv_valid_list=get_data_group_info(f,parlng+(k-1)*256)
    
            if k==1:        
                dg['datart']=[dg_datart] #a={'b':{'c':[1, 2, 3], 'd':['sddsa', 'sdsadqwwq']}} 
                dg['dltphi']=[dg_dltphi]
                dg['dltzei']=[dg_dltzei]
                dg['kananz']=[dg_kananz]
                dg['fortyp']=[dg_fortyp]
                dg['beranz']=[dg_beranz] 
                dg['zykanz']=[dg_zykanz]
                dg['datfor']=[dg_datfor]
                dg['diradr']=[dg_diradr]
                dg['mpladr']=[dg_mpladr]
                dg['rztadr']=[dg_rztadr]
                dg['thekx1']=[dg_thekx1]
                dg['thekx2']=[dg_thekx2]
                dg['polexp']=[dg_polexp]
                dg['data_content_dir']={'signalname':[signame_list]}
                dg['data_content_dir'].update({'signalunit':[signalunit_list]})
                dg['data_content_dir'].update({'abskor':[abskor_list]})
                dg['data_content_dir'].update({'desori':[desori_list]})
                dg['data_content_dir'].update({'zykofs':[zykofs_list]})
                dg['data_content_dir'].update({'nultyp':[nultyp_list]})
                dg['data_content_dir'].update({'kalfak0':[kalfak0_list]})
                dg['data_content_dir'].update({'kalfak1':[kalfak1_list]})
                dg['chan_content_tab']={'beranf':[beranf_list]}
                dg['chan_content_tab'].update({'wrtanz':[wrtanz_list]})
                dg['chan_content_tab'].update({'absint':[absint_list]})
                dg['chan_content_tab'].update({'beradr':[beradr_list]})
                dg['chan_content_tab'].update({'adrint':[adrint_list]})
                dg['chan_content_tab'].update({'startangleproK':[startangleproK_list]})
                dg['chan_content_tab'].update({'endangleproK':[endangleproK_list]})
                dg['chan_content_tab'].update({'berardrmat':[berardrmat_list]})
                dg['chan_content_tab'].update({'deltaphiresh':[deltaphiresh_list]})
                dg['chan_content_tab'].update({'wrtanzproK':[wrtanzproK_list]})
                dg['chan_content_tab'].update({'lv_valid':[lv_valid_list]})
            else:
                dg['datart'].append(dg_datart)
                dg['dltphi'].append(dg_dltphi)
                dg['dltzei'].append(dg_dltzei)
                dg['kananz'].append(dg_kananz)
                dg['fortyp'].append(dg_fortyp)
                dg['beranz'].append(dg_beranz)
                dg['zykanz'].append(dg_zykanz)
                dg['datfor'].append(dg_datfor)
                dg['diradr'].append(dg_diradr)
                dg['mpladr'].append(dg_mpladr)
                dg['rztadr'].append(dg_rztadr)
                dg['thekx1'].append(dg_thekx1)
                dg['thekx2'].append(dg_thekx2)
                dg['polexp'].append(dg_polexp)            
                dg['data_content_dir']['signalname'].append(signame_list)
                dg['data_content_dir']['signalunit'].append(signalunit_list)
                dg['data_content_dir']['abskor'].append(abskor_list)
                dg['data_content_dir']['desori'].append(desori_list)
                dg['data_content_dir']['zykofs'].append(zykofs_list)
                dg['data_content_dir']['nultyp'].append(nultyp_list)
                dg['data_content_dir']['kalfak0'].append(kalfak0_list)
                dg['data_content_dir']['kalfak1'].append(kalfak1_list)
                dg['chan_content_tab']['beranf'].append(beranf_list)
                dg['chan_content_tab']['wrtanz'].append(wrtanz_list)
                dg['chan_content_tab']['absint'].append(absint_list)
                dg['chan_content_tab']['beradr'].append(beradr_list)
                dg['chan_content_tab']['adrint'].append(adrint_list)
                dg['chan_content_tab']['startangleproK'].append(startangleproK_list)
                dg['chan_content_tab']['endangleproK'].append(endangleproK_list)
                dg['chan_content_tab']['berardrmat'].append(berardrmat_list)
                dg['chan_content_tab']['deltaphiresh'].append(deltaphiresh_list)
                dg['chan_content_tab']['wrtanzproK'].append(wrtanzproK_list)
                dg['chan_content_tab']['lv_valid'].append(lv_valid_list)
         
    #-------------------------------------------- check found data groups ---------------------------------------
        #not_supported_datart=list(set(dg['datart'])-set(supported_datart))
        ind_dg_crk=[index for index, value in enumerate(dg['datart']) if value==1]
        signalname=dg['data_content_dir']['signalname'][ind_dg_crk[0]]
        signalunit=dg['data_content_dir']['signalunit'][ind_dg_crk[0]]
      
    ####################################### Relative Time Table (RZT) ###########################################
        if dg['rztadr'][ind_dg_crk[0]]!=0:
            print('Hmmmm, rpm should be calculated, but in python not implemented as this case do not valid!')
            #        fseek_and_check(f,dg['rztadr'][ind_dg_crk[0]],0)
            #        for i in range(0,dg_zykanz):
            #            rzt_bin=struct.unpack('h',f.read(2))[0]       
            #            if i==0: 
            #                rzt_list=[rzt_bin]
            #            else:
            #                rzt_list.append(rzt_bin)         
            #        if rzt==0:
            #            rzt=0.01
            #            print('ERROR1! Hmmm!')
            #        rpm=stroketype*30000/dg['dltzei'][ind_dg_crk[0]]/rzt
            #        count_rpm_error=0
            #        for CYCLENR in range(0,dg['zykanz'][ind_dg_crk[0]]):
            #            if rzt[CYCLENR]==0 and rzt[CYCLENR+1]!=0:
            #                rpm[CYCLENR]=rpm[CYCLENR+1]
            #                count_rpm_error=count_rpm_error+1
            #            elif rzt[CYCLENR]==0 and rzt[CYCLENR+1]==0:
            #                print('ERROR2! Hmmm!')
        else:
            rpm=None
            count_rpm_error=None
    
    ###################################### Data Structure #######################################################
    #--------------- get calculated values -------------------------------
        channel_masks='^' + channel_masks.replace('*','.*') + '$'
        datatrans={'label':[],'unit':[],'angle':[],'value':[],'kalfak0':[],'kalfak1':[],'tdc_ofs':[],'corr_type':[],'p_offset':[],'lv_cor':[],'desaxis':[]}
        
        dg_tmp1={'datart':[],'dltphi':[],'dltzei':[],'kananz':[],'fortyp':[],'beranz':[],'zykanz':[],
        'datfor':[],'diradr':[],'mpladr':[],'rztadr':[],'thekx1':[],'thekx2':[],'polexp':[],
        'data_content_dir':{'signalname':[],'signalname':[],'signalunit':[],'abskor':[],'desori':[],'zykofs':[],'nultyp':[],'kalfak0':[],'kalfak1':[]},
        'chan_content_tab':{'beranf':[],'wrtanz':[],'absint':[],'beradr':[],'adrint':[],'startangleproK':[],'endangleproK':[],'berardrmat':[],'deltaphiresh':[],'wrtanzproK':[],'lv_valid':[]}}        
        dg_tmp1['datart']=dg['datart'][ind_dg_crk[0]]
        dg_tmp1['dltphi']=dg['dltphi'][ind_dg_crk[0]]
        dg_tmp1['dltzei']=dg['dltzei'][ind_dg_crk[0]]
        dg_tmp1['kananz']=dg['kananz'][ind_dg_crk[0]]
        dg_tmp1['fortyp']=dg['fortyp'][ind_dg_crk[0]]
        dg_tmp1['beranz']=dg['beranz'][ind_dg_crk[0]]
        dg_tmp1['zykanz']=dg['zykanz'][ind_dg_crk[0]]
        dg_tmp1['datfor']=dg['datfor'][ind_dg_crk[0]]
        dg_tmp1['diradr']=dg['diradr'][ind_dg_crk[0]]
        dg_tmp1['mpladr']=dg['mpladr'][ind_dg_crk[0]]
        dg_tmp1['rztadr']=dg['rztadr'][ind_dg_crk[0]]
        dg_tmp1['thekx1']=dg['thekx1'][ind_dg_crk[0]]
        dg_tmp1['thekx2']=dg['thekx2'][ind_dg_crk[0]]
        dg_tmp1['polexp']=dg['polexp'][ind_dg_crk[0]]
        dg_tmp1['data_content_dir']['signalname']=dg['data_content_dir']['signalname'][ind_dg_crk[0]]
        dg_tmp1['data_content_dir']['signalunit']=dg['data_content_dir']['signalunit'][ind_dg_crk[0]]
        dg_tmp1['data_content_dir']['abskor']=dg['data_content_dir']['abskor'][ind_dg_crk[0]]
        dg_tmp1['data_content_dir']['desori']=dg['data_content_dir']['desori'][ind_dg_crk[0]]
        dg_tmp1['data_content_dir']['zykofs']=dg['data_content_dir']['zykofs'][ind_dg_crk[0]]
        dg_tmp1['data_content_dir']['nultyp']=dg['data_content_dir']['nultyp'][ind_dg_crk[0]]
        dg_tmp1['data_content_dir']['kalfak0']=dg['data_content_dir']['kalfak0'][ind_dg_crk[0]]
        dg_tmp1['data_content_dir']['kalfak1']=dg['data_content_dir']['kalfak1'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['beranf']=dg['chan_content_tab']['beranf'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['wrtanz']=dg['chan_content_tab']['wrtanz'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['absint']=dg['chan_content_tab']['absint'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['beradr']=dg['chan_content_tab']['beradr'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['adrint']=dg['chan_content_tab']['adrint'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['startangleproK']=dg['chan_content_tab']['startangleproK'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['endangleproK']=dg['chan_content_tab']['endangleproK'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['berardrmat']=dg['chan_content_tab']['berardrmat'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['deltaphiresh']=dg['chan_content_tab']['deltaphiresh'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['wrtanzproK']=dg['chan_content_tab']['wrtanzproK'][ind_dg_crk[0]]
        dg_tmp1['chan_content_tab']['lv_valid']=dg['chan_content_tab']['lv_valid'][ind_dg_crk[0]]         
        
        for DATA in range(0,dg['kananz'][ind_dg_crk[0]]):
            if dg['data_content_dir']['signalname'][ind_dg_crk[0]][DATA]:
                tmp_datatrans=new_get_channel_data(dg_tmp1,DATA,f,desaxi,desaxi2)
                for dn in datatrans.keys():
                    datatrans[dn].append(tmp_datatrans[dn])

#            if DATA==0:
#        #        print((tmp_datatrans['angle'])) 
#        #        print(len(tmp_datatrans['value'])) 
#        #        print(len(tmp_datatrans['value'][0]))            
#                import matplotlib.pyplot as plt
#                for i in range(len(datatrans['value'][DATA])):
#                    plt.plot(np.array(datatrans['angle'][DATA]),np.array(datatrans['value'][DATA][i]))
##                    plt.plot(np.array(datatrans['angle'][DATA]),np.array(datatrans['value'][DATA][i])*datatrans['kalfak1'][DATA]+datatrans['kalfak0'][DATA])
#                    plt.hold(True)
##                    leg4=plt.legend(loc='best', numpoints=1, fontsize=18, borderpad=0.6, labelspacing=0.2)
##                    if leg4:
##                        leg4.draggable() 
                    
    #--------------- get calculated values -------------------------------
        ind_dg_rtp_pp=[dg['datart'].index(3)]
        ind_dg_rtp_pp.append(dg['datart'].index(4))
        data_calc={'label':[],'unit':[],'angle':[],'value':[],'kalfak0':[],'kalfak1':[],'tdc_ofs':[],'corr_type':[],'p_offset':[],'lv_cor':[],'desaxis':[]}
        for this_ind_dg in ind_dg_rtp_pp:
            dg_tmp2={'datart':[],'dltphi':[],'dltzei':[],'kananz':[],'fortyp':[],'beranz':[],'zykanz':[],
            'datfor':[],'diradr':[],'mpladr':[],'rztadr':[],'thekx1':[],'thekx2':[],'polexp':[],
            'data_content_dir':{'signalname':[],'signalname':[],'signalunit':[],'abskor':[],'desori':[],'zykofs':[],'nultyp':[],'kalfak0':[],'kalfak1':[]},
            'chan_content_tab':{'beranf':[],'wrtanz':[],'absint':[],'beradr':[],'adrint':[],'startangleproK':[],'endangleproK':[],'berardrmat':[],'deltaphiresh':[],'wrtanzproK':[],'lv_valid':[]}}        
            dg_tmp2['datart']=dg['datart'][this_ind_dg]
            dg_tmp2['dltphi']=dg['dltphi'][this_ind_dg]
            dg_tmp2['dltzei']=dg['dltzei'][this_ind_dg]
            dg_tmp2['kananz']=dg['kananz'][this_ind_dg]
            dg_tmp2['fortyp']=dg['fortyp'][this_ind_dg]
            dg_tmp2['beranz']=dg['beranz'][this_ind_dg]
            dg_tmp2['zykanz']=dg['zykanz'][this_ind_dg]
            dg_tmp2['datfor']=dg['datfor'][this_ind_dg]
            dg_tmp2['diradr']=dg['diradr'][this_ind_dg]
            dg_tmp2['mpladr']=dg['mpladr'][this_ind_dg]
            dg_tmp2['rztadr']=dg['rztadr'][this_ind_dg]
            dg_tmp2['thekx1']=dg['thekx1'][this_ind_dg]
            dg_tmp2['thekx2']=dg['thekx2'][this_ind_dg]
            dg_tmp2['polexp']=dg['polexp'][this_ind_dg]
            dg_tmp2['data_content_dir']['signalname']=dg['data_content_dir']['signalname'][this_ind_dg]
            dg_tmp2['data_content_dir']['signalunit']=dg['data_content_dir']['signalunit'][this_ind_dg]
            dg_tmp2['data_content_dir']['abskor']=dg['data_content_dir']['abskor'][this_ind_dg]
            dg_tmp2['data_content_dir']['desori']=dg['data_content_dir']['desori'][this_ind_dg]
            dg_tmp2['data_content_dir']['zykofs']=dg['data_content_dir']['zykofs'][this_ind_dg]
            dg_tmp2['data_content_dir']['nultyp']=dg['data_content_dir']['nultyp'][this_ind_dg]
            dg_tmp2['data_content_dir']['kalfak0']=dg['data_content_dir']['kalfak0'][this_ind_dg]
            dg_tmp2['data_content_dir']['kalfak1']=dg['data_content_dir']['kalfak1'][this_ind_dg]
            dg_tmp2['chan_content_tab']['beranf']=dg['chan_content_tab']['beranf'][this_ind_dg]
            dg_tmp2['chan_content_tab']['wrtanz']=dg['chan_content_tab']['wrtanz'][this_ind_dg]
            dg_tmp2['chan_content_tab']['absint']=dg['chan_content_tab']['absint'][this_ind_dg]
            dg_tmp2['chan_content_tab']['beradr']=dg['chan_content_tab']['beradr'][this_ind_dg]
            dg_tmp2['chan_content_tab']['adrint']=dg['chan_content_tab']['adrint'][this_ind_dg]
            dg_tmp2['chan_content_tab']['startangleproK']=dg['chan_content_tab']['startangleproK'][this_ind_dg]
            dg_tmp2['chan_content_tab']['endangleproK']=dg['chan_content_tab']['endangleproK'][this_ind_dg]
            dg_tmp2['chan_content_tab']['berardrmat']=dg['chan_content_tab']['berardrmat'][this_ind_dg]
            dg_tmp2['chan_content_tab']['deltaphiresh']=dg['chan_content_tab']['deltaphiresh'][this_ind_dg]
            dg_tmp2['chan_content_tab']['wrtanzproK']=dg['chan_content_tab']['wrtanzproK'][this_ind_dg]
            dg_tmp2['chan_content_tab']['lv_valid']=dg['chan_content_tab']['lv_valid'][this_ind_dg]        
            for DATA in range(0,dg['kananz'][this_ind_dg]):
                tmp_data_calc=new_get_channel_data(dg_tmp2,DATA,f,desaxi,desaxi2)
                for dn in data_calc.keys():
                    data_calc[dn].append(tmp_data_calc[dn]) 
                
#                if DATA==0:
#    #                print(data_calc['value'])
#                #        print((tmp_datatrans['angle'])) 
#                #        print(len(tmp_datatrans['value'])) 
#                #        print(len(tmp_datatrans['value'][0]))            
#                    import matplotlib.pyplot as plt
#                    for i in range(len(data_calc['value'])):       
#                        plt.plot(data_calc['angle'][i],data_calc['value'][i][0],label=str(i))
#                        plt.hold(True)
#                        leg4=plt.legend(loc='best', numpoints=1, fontsize=18, borderpad=0.6, labelspacing=0.2)
#                        if leg4:
#                            leg4.draggable() 
                                
             
                
        if data_calc['label']==[]:
            calc_val={'label':[], 'unit':[], 'value':[]}
    
        else:
            for i in range(len(data_calc['angle'])):       
                if i==0:
                    no_cycles=[len(data_calc['value'][i][0])]
                else:
                    no_cycles.append(len(data_calc['value'][i][0]))          
                
            no_cycles_max=dg['zykanz'][ind_dg_crk[0]]
            
            index1=[i for i,x in enumerate(no_cycles) if x==1]
            for k in index1:
                data_calc['value'][k][0]=no_cycles_max*data_calc['value'][k][0]
    
            index2=[i for i,x in enumerate(no_cycles) if x>1 and enumerate(no_cycles) if x<no_cycles_max]
            for k in index2:
                for l in range(len(data_calc['value'][k][0]),no_cycles_max):
                    data_calc['value'][k][0].append(None)
    
            lv_get_calc_val=[(i<=no_cycles_max)*1 for i in no_cycles]
    
            calc_label=[]
            calc_unit=[]
            calc_value=[]
            for j in [i for i,x in enumerate(lv_get_calc_val) if x==1]:
                calc_label.append(data_calc['label'][j].replace(' ','_'))
                calc_unit.append(data_calc['unit'][j])
                calc_value.append(data_calc['value'][j][0])
    
            if not any(calc_value):
                    calc_value=[]
    
            calc_val={'label':calc_label, 'unit':calc_unit, 'value':calc_value}
    
    ######################################## close file and create structure "datainfo" #########################
        datainfo={'filecomment':filkom,
                    'aquisitiondate':mesdat,
                    'parameterfile':parfil,
                    'motorname':motnam,
                    'motortype':motortype,
                    'stroketype':stroketype,
                    'units':units,
                    'stroke':hublng,
                    'conrod':pleuel,
                    'bore':bohrng,
                    'compression':kompre,
                    'desaxis':desaxi,
                    'desaxis2':desaxi2,
                    'version':version,
                    'nultyp':dg['data_content_dir']['nultyp'][ind_dg_crk[0]],
                    'number_of_channels':dg['kananz'][ind_dg_crk[0]],
                    'number_of_cycles':dg['zykanz'][ind_dg_crk[0]],
                    'cycle_length':dg['data_content_dir']['zykofs'][ind_dg_crk[0]],
                    'thekx1':dg['thekx1'][ind_dg_crk[0]],
                    'thekx2':dg['thekx2'][ind_dg_crk[0]],
                    'polexp':dg['polexp'][ind_dg_crk[0]],
                    'rpm':rpm,
                    'count_rpm_error':count_rpm_error,
                    'bpar':bpar}
    
    ############################## thermodynamic presssure offset correction ####################################
    #    if ~isempty(datatrans)
        if not datatrans['label']==[]:
    #----volume at crank and mean(value) calculation (value=uncorrected)-----------------------------------------
            Ak=np.pi*datainfo['bore']**2*0.25 # piston surface
            Vh=Ak*datainfo['stroke'] # cylinder capacity
            Vc=Vh/(datainfo['compression']-1) # compression volume
            #lp=datainfo['conrod'] # conrod
            #r=datainfo['stroke']*0.5 # crank radius
            #lam_s=r/lp # crank radius / conrod
            thekx1=datainfo['thekx1'] # reference angle 1 for thermod. correction
            thekx2=datainfo['thekx2'] # reference angle 2 for thermod. correction
            polexp=datainfo['polexp'] # polytrop exponent
    #----thermodynamic correction--------------------------------------------------------------------------------
            corr_type=2 # manual setting (Hohenberg=1, Polytrop=2)
            CHC=len(datainfo['nultyp']) # channel_masks with defined correction
            #haziness_crk=0
            for CH in range(0,CHC):
                try:
                    ind_ch=datatrans['label'].index(signalname[CH])
                except:
                    ind_ch=[]
                if ind_ch!=[]:
                    if datainfo['nultyp'][CH]==2 or datainfo['nultyp'][CH]==512:
                        phi=datatrans['angle'][ind_ch]
                        v_rel=[]
                        ang_bdc=[]
                        v_rel,ang_bdc=calc_vol_rel_comb_chamber_new_20180307(phi,datainfo['compression'],datainfo['stroke']/datainfo['conrod'],datatrans['desaxis'][ind_ch]/datainfo['conrod'])
                        V_angle=Vc*v_rel
    
                        anglist1=([abs(i-thekx1) for i in datatrans['angle'][ind_ch]])
                        min_dev=min(anglist1)
                        indthekx1=anglist1.index(min_dev)
                        
                        anglist2=([abs(i-thekx2) for i in datatrans['angle'][ind_ch]])
                        min_dev=min(anglist2)
                        indthekx2=anglist2.index(min_dev)                    
    
                        if corr_type==1: # thermod. corr. according to "Hohenberg"
                            datatrans['corr_type'][ind_ch]='Hohenberg'
                          
                            VatC=V_angle[indthekx1:indthekx2+1] # volume at crank
                            frac_V=(VatC[0:-1]/VatC[1:])**polexp 
                            matrix=np.ones((len(datatrans['value'][ind_ch]),indthekx2-indthekx1)) #50vertical x 70horizontal
                            frac_V=np.transpose(np.dot(matrix,np.diag(frac_V)))
                            Vi_pl_1=np.transpose(np.dot(matrix,np.diag(VatC[1:])))
                            val1_double=[datatrans['value'][ind_ch][0][indthekx1+1:indthekx2+1]]
                            for i in range(1,len(datatrans['value'][ind_ch])): # 50
                                val1_double.append(datatrans['value'][ind_ch][i][indthekx1+1:indthekx2+1])
                            
                            val2_double=[datatrans['value'][ind_ch][0][indthekx1:indthekx2]]
                            for i in range(1,len(datatrans['value'][ind_ch])): # 50
                                val2_double.append(datatrans['value'][ind_ch][i][indthekx1:indthekx2])
    
                            if not datatrans['kalfak1'][ind_ch]==None:
                                val1_double=np.array(val1_double)*datatrans['kalfak1'][ind_ch]+datatrans['kalfak0'][ind_ch]
                                val2_double=np.array(val2_double)*datatrans['kalfak1'][ind_ch]+datatrans['kalfak0'][ind_ch]
    
                            numerator=np.transpose(Vi_pl_1)*(val1_double-(val2_double*np.transpose(frac_V)))
                            numerator=-sum(np.transpose(numerator)) # numerator of fraction ("Hohenberg")
                            denominator=np.transpose(Vi_pl_1)*np.transpose((1-frac_V))
                            denominator=sum(np.transpose(denominator)) # denominator of fraction ("Hohenberg")
                         
                            p_offset=numerator/denominator
                    
                        elif corr_type==2:
                            pass
                            datatrans['corr_type'][ind_ch]='polytrop method'
                            V1=np.mean(V_angle[indthekx1-1:indthekx1+1+1]) # V1 at reference angle 1
                            V2=np.mean(V_angle[indthekx2-1:indthekx2+1+1]) # V2 at reference angle 2
                            
                            val1_double=[datatrans['value'][ind_ch][0][indthekx1]]                         
                            for i in range(1,len(datatrans['value'][ind_ch])): # 50                     
                                val1_double.append(datatrans['value'][ind_ch][i][indthekx1])                       
    
                            val2_double=[datatrans['value'][ind_ch][0][indthekx2]]                         
                            for i in range(1,len(datatrans['value'][ind_ch])): # 50                     
                                val2_double.append(datatrans['value'][ind_ch][i][indthekx2])                       
    
                            if not datatrans['kalfak1'][ind_ch]==None:
                                val1_double=np.array(val1_double)*datatrans['kalfak1'][ind_ch]+datatrans['kalfak0'][ind_ch]
                                val2_double=np.array(val2_double)*datatrans['kalfak1'][ind_ch]+datatrans['kalfak0'][ind_ch]
                    
                            p2_abs=np.dot((val2_double-val1_double),(V1**polexp/(V1**polexp-V2**polexp)))
                            p_offset=p2_abs-val2_double                        
    
                    else:
                        datatrans['corr_type'][ind_ch]='no correction'
                        p_offset=[0]*len(datatrans['value'][ind_ch])
                    
    
                    datatrans['p_offset'][ind_ch]=p_offset
                    datatrans['lv_cor'][ind_ch]=(datainfo['nultyp'][CH]==2 or datainfo['nultyp'][CH]==512)*1
                    datatrans['angle'][ind_ch]=np.float32(datatrans['angle'][ind_ch])
                    
    return(datatrans,datainfo,signalname,signalunit,calc_val)

#ifile='d:\\Data\\projects\\Motorpruefstand\\Datenbank\\20180118_05h00_1200rpm_MAP_800hPa.2303'
#channel_masks='*'   
#datatrans,datainfo,signalname,signalunit,calc_val=indi_read_all_new_20180307(ifile,channel_masks)   
