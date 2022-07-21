# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:02:22 2022

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

t_sim = np.linspace(0,12,1001)*3600 # seconds

k_txn = 0.01 #transcription rate

IN1 = [2.5,1.25] #input template

REP_con = 500

color = ['red','orange']

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify DNA txn templates and reporters and concentrations
model.molecular_species('gate{1,2}',DNA_con=25)
model.molecular_species('reporter{2}',DNA_con=REP_con)

model.global_rate_constants(ktxn=k_txn)

plt.subplot(2,4,1)
for n in range(len(IN1)):
    model.molecular_species('input{1}',DNA_con=IN1[n])
    
    # simulate the model
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='-')
    
    
IN1 = [2.5,1.25] #input template

color = ['pink','purple']

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify DNA txn templates and reporters and concentrations
model.molecular_species('gate{1,2}',DNA_con=25)
model.molecular_species('reporter{2}',DNA_con=REP_con)
model.molecular_species('f{1}',DNA_con=25)

model.global_rate_constants(ktxn=k_txn)

plt.subplot(2,4,1)
for n in range(len(IN1)):
    model.molecular_species('input{1}',DNA_con=IN1[n])
    
    # simulate the model
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='-')
    
    
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


import Simulator1 as RSDs #import first version of simulator


'''
##############################################################################
Simulations
##############################################################################
'''

t_sim = np.linspace(0,12,1001)*3600 # seconds

k_txn = 0.01 #transcription rate

IN1 = [2.5,1.25] #input template

csl = ['blue','aqua']

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)

plt.subplot(2,4,1)
for n in range(len(IN1)):
    model.DNA_species('input','I1',temp_con=IN1[n])
    
    # simulate the model
    model.simulate(t_sim,1,k_txn)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl[n],linewidth=2,linestyle='--')
    
    
IN1 = [2.5,1.25]

csl = ['black','yellow']

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)
model.DNA_species('fuel','F1',temp_con=25)

plt.subplot(2,4,1)
for n in range(len(IN1)):
    model.DNA_species('input','I1',temp_con=IN1[n])
    
    # simulate the model
    model.simulate(t_sim,1,k_txn)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl[n],linewidth=2,linestyle='--')
    
    
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
plt.title('Figure 4H Comparison')
plt.legend(['In=2.5 NF','In=1.25 NF','In=2.5 F','In=1.25 F'],frameon=False)




