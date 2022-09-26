# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:25:45 2022

@author: tnm12
"""
import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt

# importing the simulator
import sys
sys.path.insert(1,'filepath to simulator location on local computer')
import ctRSD_simulator_200 as RSDs #import simulator version 2.0.0
    
'''
##############################################################################
Simulations
In this example, the G{1,2} is initially transcribed for 15 min by itself
and given different krz values. After 15 min, the G{1,2} template is set to 0 
and the cleavage profile of the gate is observed in the absence of transcription
##############################################################################
'''

csl =[[0,0,0.5],
      [0,0,1],
      [0,0.25,1],
      [0,0.5,1],
      [0,0.75,1]]

k_txn = 0.025 #transcription rate

t_sim = np.linspace(0,15/60,1001)*3600 # seconds

k_rz = [0.5/60,0.35/60,0.25/60,0.15/60,0.1/60] # per s

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

fs = 12
plt.subplot(2,3,2)
i = 0
for n in k_rz:
    # specify DNA txn templates and concentrations
    model.molecular_species('G{1,2}',DNA_con=25,krz=n)
    model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates
    
    # simulate the model (before addition of the input template)
    model.simulate(t_sim)
    
    # updating the simulation time for the second phase of the simulation
    t_sim2 = np.linspace(t_sim[-1]/3600,1,1001)*3600 # seconds
    
    # shutting off G{1,2} txn
    model.molecular_species('G{1,2}',DNA_con=0)
    
    # simulate the model (after addition of the input template)
    model.simulate(t_sim2,iteration=2) #must specify it is second iteration
    
    # pulling out the reporter concentration for plotting
    uG = model.output_concentration('uG{1,2}')
    G = model.output_concentration('G{1,2}')
    
    plt.plot(model.t/60,G/(uG+G),color=csl[i],linewidth=2,linestyle='--')
    i+=1


plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-0.1,1.1)
plt.xlim(0,45)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Fraction Cleaved',fontsize=fs)
