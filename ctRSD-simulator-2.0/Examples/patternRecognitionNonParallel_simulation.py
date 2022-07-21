# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:26:28 2022

@author: tnm12
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import sys
import Simulatorv2021 as RSDs
import time
from multiprocessing import Pool

tic= time.time()


'''
###############################################################################
Defining the patterns
###############################################################################
'''
# THE WINNER TAKE ALL DOMAINS
wta = '6_7' 

in_con = 10 # concentrations of all the inputs
gate_con = 5 # concentrations of all the gates
REP_con = 500

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.015
 
tpt = 240 # plotting time

# MODEL INITIATION
model = RSDs.RSD_sim(13) # define the model instance

# FIXED SPECIES
# specify DNA txn templates and reporters and concentrations
model.molecular_species('g{6,1}',DNA_con=15)
model.molecular_species('g{7,2}',DNA_con=15)
model.molecular_species('CG{6,7}',DNA_con=45)
model.molecular_species('REP{1}',DNA_con=500)
model.molecular_species('REP{2}',DNA_con=500)

model.global_rate_constants(krsdCG=5e5/1e9,ktxn=k_txn)


# layout of which inputs correspond to which pixels in the patterns
gate_layout = np.array([[3, 8, 11],
               [4, 9, 12],
               [5, 10, 13]])

# the two memories for the patterns - these map which gates are present in the system
pattern1 = np.array([[1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]])

pattern2 = np.array([[1, 0, 1],
            [1, 0, 1],
            [0, 1, 0]])

# Defining the gates present based on the patterns

for r in range(pattern1.shape[0]):
    for c in range(pattern1.shape[1]):
        
        if pattern1[r][c] != 0:
           model.molecular_species('g{'+str(gate_layout[r][c])+',6}',DNA_con=gate_con) 
           
        if pattern2[r][c] != 0:
           model.molecular_species('g{'+str(gate_layout[r][c])+',7}',DNA_con=gate_con) 
           

'''
###############################################################################
WTA simulations and plots
###############################################################################
'''

# the inputs that are proved for a given experiment

# Pattern 1 inputs
ip1 = np.array([[1, 0, 1],
       [0, 1, 0],
       [1, 0, 1]])

ip2 = np.array([[1, 0, 1],
       [0, 0, 0],
       [1, 0, 1]])

ip3 = np.array([[1, 0, 1],
       [0, 1, 0],
       [1, 1, 1]])

ip4 = np.array([[0, 0, 0],
       [0, 1, 0],
       [1, 0, 1]])

ip5 = np.array([[0, 0, 1],
       [1, 1, 0],
       [1, 0, 1]])

ip6 = np.array([[1, 0, 1],
       [1, 1, 1],
       [1, 0, 1]])

# Pattern 2 inputs

ip7 = np.array([[1, 0, 1],
       [1, 0, 1],
       [0, 1, 0]])


ip8 = np.array([[1, 0, 1],
       [1, 0, 1],
       [0, 0, 0]])


ip9 = np.array([[1, 0, 1],
       [1, 0, 0],
       [0, 1, 0]])


ip10 = np.array([[0, 0, 0],
       [1, 0, 1],
       [0, 1, 0]])


ip11 = np.array([[1, 0, 1],
        [1, 1, 1],
        [0, 1, 0]])

ip12 = np.array([[1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]])

all_ip = [ip1,ip2,ip3,ip4,ip5,ip6,ip7,ip8,ip9,ip10,ip11,ip12] # list of all patterns

spp = [1,2,3,4,5,6,13,14,15,16,17,18] # where the patterns should be plotted

outputs = []

i = 0
for input_pattern in all_ip:  
    for r in range(input_pattern.shape[0]):
        for c in range(input_pattern.shape[1]):
            
            if input_pattern[r][c] != 0:
               model.molecular_species('IN{'+str(gate_layout[r][c])+'}',DNA_con=in_con) 
            else:
                # need to erase any inputs from previous patterns
               model.molecular_species('IN{'+str(gate_layout[r][c])+'}',DNA_con=0) 
    
    # simulate the model
    model.simulate(t_sim,smethod='BDF')
    
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    S1 = model.output_concentration('S{1}')
    
    outputs.append([S1,S2])
    
    
    
fs = 12
plt.figure(1)

for i in range(len(outputs)):
    S1 = outputs[i][0]
    S2 = outputs[i][1]
    
    plt.subplot(4,6,spp[i]+6)
    plt.plot(model.t/60,(S1/REP_con)*100,color=[0,0,1],linewidth=1.5,linestyle='--')
    plt.fill_between(model.t/60,(S1/REP_con)*100,color=[0,0,1],alpha=0.1)
    plt.plot(model.t/60,(S2/REP_con)*100,color=[1,0,0],linewidth=1.5,linestyle='--')
    plt.fill_between(model.t/60,(S2/REP_con)*100,color=[1,0,0],alpha=0.1)
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.ylim(-10,110)
    plt.xlim(0,tpt)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    if i>5:
        plt.xlabel('Time (min)',fontsize=fs)
    else:
        ax1.xaxis.set_ticklabels([])
    if i == 0 or i == 6:
        plt.ylabel('Reacted reporter (%)',fontsize=fs)
    else:
        ax1.yaxis.set_ticklabels([])
    
    '''
    ###############################################################################
    Input pattern grids
    ###############################################################################
    '''
    
    plt.subplot(4,6,spp[i])
    plt.imshow(-1*np.array(all_ip[i]),cmap='gray')
    plt.show()
    ax1 = plt.gca()
    ax1.xaxis.set_ticklabels([])
    ax1.yaxis.set_ticklabels([])
    


toc = time.time()
time_elapsed = toc - tic
    
    
