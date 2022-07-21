# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:09:30 2022

@author: tnm12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
import Simulator1 as RSDs #import first version of Simulator

'''
##############################################################################
Simulations (xRz reactions)
##############################################################################
'''

'''
Fast reverse reaction with xRz  gate
'''

ksd = 1e3/1e9 # 1/nM-s
kfsd = 1e3/1e9 # 1/nM-s
krev = 270/1e9 # 1/nM-s
kf_rep = 1e4/1e9 # 1/nM-s
kr_rep = 0*1e2/1e9 # 1/nM-s
kf_wta = 1e5/1e9 # 1/nM-s
kr_wta = 0.4 # 1/s
kRz = 0.25/60 # 1/s
kth = 1e5/1e9 # 1/nM-s
kd = 0

k_txn = 0.015

rte=[[k_txn],[ksd,ksd,ksd,ksd,ksd],[kfsd],[krev,5/1e9*2e5,krev,krev,krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]

t_sim = np.linspace(0,6,1001)*3600 # seconds

IN = [0,25]

csl1 = [[0.2,0.2,0.2],
       [0,0,0.5]]

csl2 = [[0.2,0.2,0.2],
       [0.5,0,0]]

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)


for n in range(len(IN)):
    model.DNA_species('input','I1',temp_con=IN[n])
    
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.subplot(2,4,1+n)
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color='blue',linewidth=2,linestyle='-')
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.ylim(-10,110)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    #ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    
    
'''
Slow forward reaction with xRz gate
'''
    
ksd = 1e1/1e9 # 1/nM-s
kfsd = 1e3/1e9 # 1/nM-s
krev = 270/1e9 # 1/nM-s
kf_rep = 1e4/1e9 # 1/nM-s
kr_rep = 0*1e2/1e9 # 1/nM-s
kf_wta = 1e5/1e9 # 1/nM-s
kr_wta = 0.4 # 1/s
kRz = 0.25/60 # 1/s
kth = 1e5/1e9 # 1/nM-s
kd = 0

k_txn = 0.015

rte=[[k_txn],[ksd,ksd,ksd,ksd,ksd],[kfsd],[krev,5/1e9,krev,krev,krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]

t_sim = np.linspace(0,6,1001)*3600 # seconds

IN = [0,25]

csl1 = [[0.2,0.2,0.2],
       [0,0,0.5]]

csl2 = [[0.2,0.2,0.2],
       [0.5,0,0]]

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)


for n in range(len(IN)):
    model.DNA_species('input','I1',temp_con=IN[n])
    
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    
    plt.subplot(2,4,1+n) 
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color='red',linewidth=2,linestyle='-')
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.ylim(-10,110)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    #ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    



'''
Version 2.0.2.1 Simulator
'''

import Simulatorv2021 as RSDs #import version 2.0.2.1 of Simulator


k_txn = 0.015 #transcription rate


t_sim = np.linspace(0,6,1001)*3600 # seconds

IN = [0,25]

REP_con = 500


model1 = RSDs.RSD_sim(5) # define the model instance

# specify DNA txn templates and reporters and concentrations
model1.molecular_species('g{1,2}',DNA_con=25,krev=5/1e9*2e5) #changes corresponding reverse rate
model1.molecular_species('r{2}',DNA_con=REP_con)

model1.global_rate_constants(ktxn=k_txn) #changed transcription rates


for n in range(len(IN)):
    model1.molecular_species('I{1}',DNA_con=IN[n])
    
    # simulate the model
    model1.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model1.output_concentration('s{2}')
    
    fs = 12
    
    
    plt.subplot(2,4,1+n)
    plt.plot(model1.t/60,(S2/REP_con)*100,color='orange',linewidth=2,linestyle='--')
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.ylim(-10,110)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    #ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    
    
'''
Slow forward reaction with xRz gate
'''
    

k_txn = 0.015 #transcirption rate


t_sim = np.linspace(0,6,1001)*3600 # seconds


model2 = RSDs.RSD_sim(5) # define the model instance

# specify DNA txn templates and reporters and concentrations
model2.molecular_species('g{1,2}',DNA_con=25,krev=5/1e9) #changes corresponding reverse rate
model2.molecular_species('r{2}',DNA_con=REP_con)
model2.global_rate_constants(ktxn=k_txn,krsd=1e1/1e9) #changed transcription/forward rates


for n in range(len(IN)):
    model2.molecular_species('I{1}',DNA_con=IN[n])
    
    # simulate the model
    model2.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    s2 = model2.output_concentration('s{2}')
    
    fs = 12
    
    plt.subplot(2,4,1+n)  
    plt.plot(model2.t/60,(s2/REP_con)*100,color='aqua',linewidth=2,linestyle='--')
    plt.legend(['S2v1 Fast','S2v1 Slow','S2v2 Fast','S2v2 Slow'],frameon=False)
    if n == 0:
        plt.title('Input Concentration  0 nM')
        plt.ylabel('Reacted reporter (%)',fontsize=fs)
    else:
        plt.title('Input Concentration 25 nM')
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.ylim(-10,110)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    #ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    
    
    
plt.suptitle('SA22_SI_figure18 Comparison')   