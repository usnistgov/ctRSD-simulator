# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:14:49 2022

@author: tnm12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import openpyxl as opxl
import xlrd
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True
import scipy.integrate as spi

import sys
sys.path.insert(1,'C:\\Users\\sws5\\OneDrive - National Institute of Standards and Technology (NIST)\\ctRSD simulator and documentation\\ctRSD-simulator\\ctRSD-simulator-2.0')
import ctRSD_simulator_200 as RSDs

'''
##############################################################################
Loading data 
##############################################################################
'''

save_loc = 'C:\\Users\\sws5\\OneDrive - National Institute of Standards and Technology (NIST)\\Presentations and write ups\\Papers\\RSD technical note\\Data upload files\\'
save_name = 'Supporting File S3'

wb = xlrd.open_workbook(save_loc+save_name+'.xlsx')

ws = wb.sheet_by_name('Figure S4')

t = np.zeros(ws.nrows-3)
for r in range(3,ws.nrows):
    t[r-3] = ws.cell_value(r,0)
    
DDn = np.zeros([ws.nrows-3,int(ws.ncols/2)-1])

for c in range(1,int(ws.ncols/2)):
    for r in range(3,ws.nrows):
        DDn[r-3,c-1] = ws.cell_value(r,c)

'''
###############################################################################
PLOTTING DATA
###############################################################################
'''

clpm = plt.cm.copper(np.linspace(0,1,5))

clp2 = [[1,0,0],
       [0.75,0.75,0.75],
       [0.5,0.5,0.5],
       [0.2,0.2,0.2],
       [1,0.7812,0.4975],
       [0.9301,0.5882,0.375],
       [0.6201,0.3921,0.2497]]
       

fs = 12
ts = 0

# fluorescence plots
plt.figure(1)

# PANEL A
plt.subplot(3,5,6)
plt.plot(t-ts,DDn[:,1]*100,color=[0.5,0,0],linewidth=2)
plt.plot(t-ts,DDn[:,2]*100,color=[1,0,0],linewidth=2)
plt.plot(t-ts,DDn[:,3]*100,color=[1,0.5,0.5],linewidth=2)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,120)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)

plt.subplot(3,5,8)
plt.plot(t-ts,DDn[:,4]*100,color=[0.75,0.25,0],linewidth=2)
plt.plot(t-ts,DDn[:,5]*100,color=[1,0.5,0],linewidth=2)
plt.plot(t-ts,DDn[:,6]*100,color=[1,0.75,0],linewidth=2)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,120)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)

plt.subplot(3,5,10)
plt.plot(t-ts,DDn[:,7]*100,color=[0,0.4,0],linewidth=2)
plt.plot(t-ts,DDn[:,8]*100,color=[0,0.6,0],linewidth=2)
plt.plot(t-ts,DDn[:,9]*100,color=[0,0.8,0],linewidth=2)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,120)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)

# PANEL B
plt.subplot(3,5,11)
plt.plot(t-ts,DDn[:,1]*100,color=[1,0,0],linewidth=2)
plt.plot(t-ts,DDn[:,4]*100,color=[1,0.5,0],linewidth=2)
plt.plot(t-ts,DDn[:,7]*100,color=[0,0.6,0],linewidth=2)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,120)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)

plt.subplot(3,5,13)
plt.plot(t-ts,DDn[:,2]*100,color=[1,0,0],linewidth=2)
plt.plot(t-ts,DDn[:,5]*100,color=[1,0.5,0],linewidth=2)
plt.plot(t-ts,DDn[:,8]*100,color=[0,0.6,0],linewidth=2)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,120)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)

plt.subplot(3,5,15)
plt.plot(t-ts,DDn[:,3]*100,color=[1,0,0],linewidth=2)
plt.plot(t-ts,DDn[:,6]*100,color=[1,0.5,0],linewidth=2)
plt.plot(t-ts,DDn[:,9]*100,color=[0,0.6,0],linewidth=2)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,120)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)

'''
##############################################################################
Simulations 
##############################################################################
'''

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.024

IN = [25,12.5,6.25]
REP_con = 500

r = 3
krsd = [1e3/r/1e9,1e3/1e9,r*1e3/1e9] # 1/nM-s


REP2 = np.array([])
REP2_l = np.array([])
REP2_h = np.array([])

for x in range(len(krsd)):
        
    for n in range(len(IN)):
        

        model = RSDs.RSD_sim() # define the model instance
        
        model.global_rate_constants(ktxn=k_txn)
        
        # specify molecular txn DNAlates and reporters and concentrations
        model.molecular_species('G{1,2}',DNA_con=25,krsd=krsd[x])
        model.molecular_species('R{2}',DNA_con=REP_con)
       
        model.molecular_species('I{1}',DNA_con=IN[n])
        
        # simulate the model
        model.simulate(t_sim)
        
        if x == 0:
            # pull out the species from the model solution to plot
            if len(REP2_l) == 0:
                REP2_l = model.output_concentration('S{2}')
            else:
                REP2_l = np.vstack([REP2_l,model.output_concentration('S{2}')])
        elif x == 1:
            if len(REP2) == 0:
                REP2 = model.output_concentration('S{2}')
            else:
                REP2 = np.vstack([REP2,model.output_concentration('S{2}')])
        elif x == 2:
            if len(REP2_h) == 0:
                REP2_h = model.output_concentration('S{2}')
            else:
                REP2_h = np.vstack([REP2_h,model.output_concentration('S{2}')])
     
plt.figure(1)

plt.subplot(3,5,6)
plt.plot(model.t/60,(REP2[0]/REP_con)*100,color=[0,0,0.5],linewidth=1,linestyle='--')
plt.plot(model.t/60,(REP2[1]/REP_con)*100,color=[0,0,1],linewidth=1,linestyle='--')
plt.plot(model.t/60,(REP2[2]/REP_con)*100,color=[0,0.5,1],linewidth=1,linestyle='--')

plt.subplot(3,5,8)
plt.plot(model.t/60,(REP2[0]/REP_con)*100,color=[0,0,0.5],linewidth=1,linestyle='--')
plt.plot(model.t/60,(REP2[1]/REP_con)*100,color=[0,0,1],linewidth=1,linestyle='--')
plt.plot(model.t/60,(REP2[2]/REP_con)*100,color=[0,0.5,1],linewidth=1,linestyle='--')

plt.subplot(3,5,10)
plt.plot(model.t/60,(REP2[0]/REP_con)*100,color=[0,0,0.5],linewidth=1,linestyle='--')
plt.plot(model.t/60,(REP2[1]/REP_con)*100,color=[0,0,1],linewidth=1,linestyle='--')
plt.plot(model.t/60,(REP2[2]/REP_con)*100,color=[0,0.5,1],linewidth=1,linestyle='--')

i = 0     
plt.subplot(3,5,11)
plt.plot(model.t/60,(REP2[i]/REP_con)*100,color=[0,0,0.75],linewidth=1,linestyle='--')
plt.plot(model.t/60,(REP2_l[i]/REP_con)*100,color=[0,0,0.75],linewidth=.75,linestyle=':',zorder=0)
plt.plot(model.t/60,(REP2_h[i]/REP_con)*100,color=[0,0,0.75],linewidth=.75,linestyle=':',zorder=0)
plt.fill_between(model.t/60,(REP2_h[i]/REP_con)*100,(REP2_l[i]/REP_con)*100,color=[0,0,1],alpha=0.05,zorder=0)

i = 1     
plt.subplot(3,5,13)
plt.plot(model.t/60,(REP2[i]/REP_con)*100,color=[0,0,0.75],linewidth=1,linestyle='--')
plt.plot(model.t/60,(REP2_l[i]/REP_con)*100,color=[0,0,0.75],linewidth=.75,linestyle=':',zorder=0)
plt.plot(model.t/60,(REP2_h[i]/REP_con)*100,color=[0,0,0.75],linewidth=.75,linestyle=':',zorder=0)
plt.fill_between(model.t/60,(REP2_h[i]/REP_con)*100,(REP2_l[i]/REP_con)*100,color=[0,0,1],alpha=0.05,zorder=0)

i = 2     
plt.subplot(3,5,15)
plt.plot(model.t/60,(REP2[i]/REP_con)*100,color=[0,0,0.75],linewidth=1,linestyle='--')
plt.plot(model.t/60,(REP2_l[i]/REP_con)*100,color=[0,0,0.75],linewidth=.75,linestyle=':',zorder=0)
plt.plot(model.t/60,(REP2_h[i]/REP_con)*100,color=[0,0,0.75],linewidth=.75,linestyle=':',zorder=0)
plt.fill_between(model.t/60,(REP2_h[i]/REP_con)*100,(REP2_l[i]/REP_con)*100,color=[0,0,1],alpha=0.05,zorder=0)