# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 13:36:00 2022

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

# without fuel
###############################################################################

t_sim = np.linspace(0,12,1001)*3600 # seconds

k_txn = 0.01 #transcription rate

IN1 = [2.5,1.25] #input template

REP_con = 500 #reporter concentration

color = [[0,0,1],
       [0,0.5,1]]

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reaction
model.molecular_species('G{1,2}',DNA_con=25,krev=5/1e9)
model.molecular_species('R{2}',ic=REP_con)

model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates

plt.subplot(2,4,1)
for n in range(len(IN1)):
    model.molecular_species('I{1}',DNA_con=IN1[n])
    
    # simulate the model (input os simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle=':')

# with fuel
###############################################################################
    
IN1 = [2.5,1.25] #input template


model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reaction
model.molecular_species('G{1,2}',DNA_con=25,krev=5/1e9)
model.molecular_species('R{2}',ic=REP_con)
model.molecular_species('F{1}',DNA_con=25)

model.global_rate_constants(ktxn=k_txn)

plt.subplot(2,4,1)
for n in range(len(IN1)):
    model.molecular_species('I{1}',DNA_con=IN1[n])
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='--')
    
    
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,360)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('Figure 4H')
plt.legend(['I=2.5 nM -F','I=1.25 nM -F','I=2.5 nM +F','I=1.25 nM +F'],frameon=False)