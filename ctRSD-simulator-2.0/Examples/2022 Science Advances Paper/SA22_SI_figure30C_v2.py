# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 10:24:16 2022

@author: tnm12
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
sys.path.insert(1,'filepath to simulator location on local computer')
import ctRSD_simulator_200 as RSDs #import simulator version 2.0.0
    

'''
##############################################################################
Simulations
##############################################################################
'''
k_txn = 0.019 #transcription rate

ksd1 = [1e1/1e9,1e2/1e9,1e3/1e9,1e4/1e9,1e5/1e9,1e6/1e9,1e7/1e9] # 1/nM-s

t_sim = np.linspace(0,8,1001)*3600 # seconds

color =[[0,0,0.25],
        [0,0,0.5],
        [0,0,0.75],
        [0,0,1],
        [0,0.33,1],
        [0,0.66,1],
        [0,0.86,1],
        [0,1,1]]

REP_con=150 #reportet concentration

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involved in the reaction
model.molecular_species('I{1}',DNA_con=5)
model.molecular_species('R{2}',ic=REP_con)



i = 0

plt.subplot(2,4,1)
for n in range(len(ksd1)):
    
    model.molecular_species('G{1,2}',DNA_con=5,krev=5/1e9,krsd=ksd1[n]) # thresholding gate
    
    model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='--')
    
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,180)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('SA22_figure30C')

