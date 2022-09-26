# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:55:40 2022

@author: tnm12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
sys.path.insert(1,'filepath to simulator location on local computer')
import ctRSD_simulator_200 as RSDs #import simulator version 2.0.0

fs = 12

csl = [[0.4,0.4,0.4],  # Io
       [1,0.5,0],      # IN
       [147/255,42/255,255/255], # I4
       [0,0.75,0.9],  # IN
       [1,0.5,1],      # I3/IN
       [0,0.9,0.9],  # I3/I5
       [0,0,0.5],      # I4/I5
       [0,0,1]]        # I3/I4/I5

'''
##############################################################################
Simulations
##############################################################################
'''

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.0075 #transcription rate

REP_con=500

IN3 = [0,25, 0, 0,25,25, 0,25]
IN4 = [0, 0,25, 0,25, 0,25,25] #input template
IN5 = [0, 0, 0,25, 0,25,25,25]

plotType = ['-','--','-.',':','-','--',':','--']

model = RSDs.RSD_sim() # define the model instance

# specify species involved in the reaction
model.molecular_species('AG{5.4,1}',DNA_con=25)
model.molecular_species('AG{3.1,2}',DNA_con=25,krev=5/1e9)
#model.molecular_species('AG{5&4,1}',DNA_con=25) # this nomenclature also works
#model.molecular_species('AG{3&1,2}',DNA_con=25) # this nomenclature also works
model.molecular_species('R{2}',ic=REP_con)

model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates

plt.subplot(2,4,1)
for n in range(len(IN3)):
    model.molecular_species('I{3}',DNA_con=IN3[n])
    model.molecular_species('I{4}',DNA_con=IN4[n])
    model.molecular_species('I{5}',DNA_con=IN5[n])
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=csl[n],linewidth=2,linestyle=plotType[n])

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,200)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('Figure 5D')