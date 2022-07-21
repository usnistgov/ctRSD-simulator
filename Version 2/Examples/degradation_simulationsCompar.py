# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:03:23 2022

@author: tnm12
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

import sys
import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator
    


##############################################################################
#Simulations
##############################################################################


IN_temp = 25 #input template

REP_con = 500 #reporter concentration

deg = [0,.00025,.0005,.001] #degradation rate

t_sim = np.linspace(0,6,1001)*3600 # seconds

color = ['aqua','blue','yellow','green']

model1 = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reactioon
model1.molecular_species('I{1}',DNA_con=IN_temp)
model1.molecular_species('G{1,2}',DNA_con=25)
model1.molecular_species('REP{2}',DNA_con=500)

for n in range(len(deg)):
    
    model1.global_rate_constants(kdeg=deg[n]) #globally changes degradation rates
    
    # simulate the model (input is simulation time)
    model1.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model1.output_concentration('S{2}')
    
    
    plt.subplot(2,4,1)
    plt.plot(model1.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='-')   
fs = 12
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
#plt.ylim(-10,2000)
plt.xlim(0,180)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.xlabel('Time(min)',fontsize=fs)
    
    
    

import Simulator1 as RSDs
    


##############################################################################
#Simulations
##############################################################################



IN_temp = 25 #input template
REP_con = 500 #reporter concentration

t_sim = np.linspace(0,6,1001)*3600 # seconds

color2 = ['red','orange','black','pink']

ksd = 1e3/1e9
kfsd = 1e3/1e9
krev = 270/1e9
kf_rep = 1e4/1e9
kr_rep = 0*1e2/1e9
kf_wta = 1e5/1e9
kr_wta = 0.4
kRz = 0.25/60
kth = 1e5/1e9
k_txn = 0.013

deg = [0,.00025,.0005,.001] #degradation rate

model2 = RSDs.RSD_sim() # define the model instance

# specify species invovled in the reaction
model2.DNA_species('gate','1_2',temp_con=25)
model2.DNA_species('reporter','REP2',temp_con=500)
model2.DNA_species('input','I1',temp_con=IN_temp)
    
    
    
for n in range(len(deg)):  
    
    rte=[[k_txn],[ksd],[kfsd],[krev,krev,krev,krev,krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[deg[n]]]

    # simulate the model
    model2.simulate(t_sim,1,k_txn,rate_constants=rte)

    # pull out the species from the model solution to plot
    REP = model2.output_concentration['REP2']
    
    
    plt.subplot(2,4,1)
    plt.plot(model2.sol.t/60,(1-REP/REP_con)*100,color=color2[n],linewidth=2,linestyle='--')
fs = 12
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,240)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('Degradation Simulation Comparison')
plt.legend(['0','.00025','.0005','.001'],frameon=False,fontsize=8,bbox_to_anchor=(.62,.62))



