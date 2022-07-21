# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:10:21 2022

@author: tnm12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator
    
'''
##############################################################################
Simulations
##############################################################################
'''

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.009 #transcription rate

IN1 = [0,50,0,50]
                #input templates
IN3 = [0,0,50,50]

REP_con = 500 #reporter concentration

color = ['black','aqua','orange','red']

plotType = ['-','--','-.','--']

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reaction
model.molecular_species('ag{3&1,2}',DNA_con=25) # 3 AND 1 -> 2
model.molecular_species('reporter{2}',DNA_con=REP_con)

model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates


fs = 12

plt.subplot(2,4,1)
for n in range(len(IN1)):
    model.molecular_species('input{1}',DNA_con=IN1[n])
    model.molecular_species('input{3}',DNA_con=IN3[n])
    
    # simulate the model
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    
    
   
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle=plotType[n])
    
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
plt.title('Figure 4F')
plt.legend(['o','1','3','1,3'],frameon=False)