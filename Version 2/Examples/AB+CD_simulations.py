# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:40:33 2022

@author: tnm12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator
    
fs = 12

color = ['grey','grey','grey','orange','grey','grey','grey','orange','grey','grey','grey','orange','orange','orange','orange','red']

'''
##############################################################################
Simulations
##############################################################################
'''

t_sim = np.linspace(0,4,1001)*3600 # seconds

k_txn = 0.0075 #transcription rate

REP_con=500
      #0 0 0 1 0 0 0 1  0  0  0  1  1  1  1  1 (creates reporter)
IN1 = [0,0,0,0,0,0,0,0,25,25,25,25,25,25,25,25]
IN3 = [0,0,0,0,25,25,25,25,0,0,0,0,25,25,25,25]
IN4 = [0,0,25,25,0,0,25,25,0,0,25,25,0,0,25,25] #input template
IN5 = [0,25,0,25,0,25,0,25,0,25,0,25,0,25,0,25]


model = RSDs.RSD_sim() # define the model instance

# specify species involved in the reaction
model.molecular_species('gate{5.4,2}',DNA_con=25)
model.molecular_species('gate{3.1,2}',DNA_con=25)
model.molecular_species('reporter{2}',DNA_con=REP_con)

model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates

plt.subplot(2,4,1)
for n in range(len(IN1)):
    model.molecular_species('input{1}',DNA_con=IN1[n])
    model.molecular_species('input{3}',DNA_con=IN3[n])
    model.molecular_species('input{4}',DNA_con=IN4[n])
    model.molecular_species('input{5}',DNA_con=IN5[n])
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    if (S2[-1] >= REP_con*.9):
        print("S2 Created for Inputs=["+str(IN1[n])+','+str(IN3[n])+','+str(IN4[n])+','+str(IN5[n])+']')
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='--')

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
plt.title('AB + CD Simulation')