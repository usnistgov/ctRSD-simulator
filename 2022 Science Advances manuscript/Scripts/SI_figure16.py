# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:08:52 2021

@author: sws5
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
sys.path.insert(1,'C:\\Users\\sws5\\OneDrive - National Institute of Standards and Technology (NIST)\\Research\\Code\\General RSD simulator')
import RSD_simulator as RSDs
    
'''
##############################################################################
Simulations
##############################################################################
'''

csl = [[0,0,0.5],[0,0,1],[0,0.5,1]]

k_txn = 0.024

txn_time = [0.5,1,2]


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

rte=[[k_txn],[ksd,ksd,ksd,ksd,ksd],[kfsd],[krev,5/1e9,krev,krev,krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]


for n in range(len(txn_time)):
    
    model = RSDs.RSD_sim() # define the model instance
    
    # specify DNA txn templates and reporters and concentrations
    model.DNA_species('gate','1_2',temp_con=50)
    model.DNA_species('input','IN3',temp_con=100)
   
    t_sim = np.linspace(0,txn_time[n],1001)*3600 # seconds
    
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    gate_produced = model.output_concentration['RSDg1'][-1]
    in_produced = model.output_concentration['IN3'][-1]
    
    model = RSDs.RSD_sim() # define the model instance

    # specify DNA txn templates and reporters and concentrations
    model.DNA_species('gate','1_2',temp_con=0,ic=gate_produced/2)
    model.DNA_species('input','IN1',temp_con=0,ic=in_produced/2)
    model.DNA_species('reporter','REP2',temp_con=500)
    
    t_sim = np.linspace(0,3,1001)*3600 # seconds
    
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP2 = model.output_concentration['REP2']

    fs = 12
    
    plt.subplot(3,6,n+1)
    plt.plot(model.sol.t/60,(1-REP2/model.REP_con[1])*100,color=csl[n],linewidth=1.5,linestyle='--')
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.ylim(-10,110)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    #ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    if n == 0:
        plt.ylabel('Reacted Reporter (%)',fontsize=fs)
