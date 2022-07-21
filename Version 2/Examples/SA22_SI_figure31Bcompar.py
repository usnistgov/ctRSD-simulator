# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 10:34:01 2022

@author: tnm12
"""

import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

import sys
import Simulator1 as RSDs #import first version of simulator

esp = np.linspace(0,1,4+1)
csl = [cm.summer(x) for x in esp]

fs = 12

# Modeling

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = [0.015,0.009,0.006,0.0045]

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('output','O2',temp_con=25) # thresholding gate
model.DNA_species('reporter','REP2',temp_con=500)
 
plt.subplot(2,4,1)
for n in range(len(k_txn)):

    model.simulate(t_sim,1,k_txn[n])
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
   
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl[n],linewidth=2,linestyle='-')

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
    
k_txn2 = [0.02,0.0065]
p = [0,3]

plt.subplot(2,4,3)
for n in range(len(k_txn2)):

    model.simulate(t_sim,1,k_txn2[n])
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl[n],linewidth=2,linestyle='-')

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



import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator

color = ['aqua','red','orange','yellow']

fs = 12

# Modeling

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = [0.015,0.009,0.006,0.0045] #transcription rates

REP_con = 500

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify DNA txn templates and reporters and concentrations
model.molecular_species('O{1,2}',DNA_con=25) # thresholding gate
model.molecular_species('REP{2}',DNA_con=REP_con)
 
plt.subplot(2,4,1)
for n in range(len(k_txn)):
    model.global_rate_constants(ktxn=k_txn[n]) #globally changes transcription rates
    
    # run simulaton (input is simulaton time)
    model.simulate(t_sim,smethod='LSODA') #RK45 method has slight instability
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
   
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='--')

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
    
k_txn2 = [0.02,0.0065] #transcription rates
p = [0,3]

plt.subplot(2,4,3)
for n in range(len(k_txn2)):
    model.global_rate_constants(ktxn=k_txn2[n]) #globally changes transcription rates
    
    # run simulation (input is simulation time)
    model.simulate(t_sim,smethod='LSODA') #RK45 method has slight instability
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n+2],linewidth=2,linestyle='--')

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

plt.suptitle('SA22_SI_figure31B Comparison')