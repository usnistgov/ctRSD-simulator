# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:57:51 2022

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

color = ['red','pink','aqua','orange']

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reaction
model.molecular_species('ag{3.1,2}',DNA_con=25) # 3 AND 1 -> 2
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
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='-')
    
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




import Simulator1 as RSDs #import first version of simulator
    
'''
##############################################################################
Simulations
##############################################################################
'''

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.009 #transcription rate

IN1 = [0,50,0,50]
IN3 = [0,0,50,50]

csl = [[0.4,0.4,0.4],
       [0.4,0,0],
       [0.8,0.3,0],
       [0,0,0.5]]

# model with inputs
model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','3&1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)


fs = 12

plt.subplot(2,4,1)
for n in range(len(IN1)):
    model.DNA_species('input','I1',temp_con=IN1[n])
    model.DNA_species('input','I3',temp_con=IN3[n])
    
    # simulate the model
    model.simulate(t_sim,1,k_txn)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl[n],linewidth=2,linestyle='--')
    
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
plt.title('Figure 4F Comparison')
plt.legend(['o','1','3','1,3'],frameon=False)



