# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:40:33 2022

@author: tnm12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
sys.path.insert(1,'filepath to simulator location on local computer')
import ctRSD_simulator_200 as RSDs #import simulator version 2.0.0
    
fs = 12

color = ['grey','grey','grey','orange','grey','grey','grey','orange','grey','grey','grey','orange','orange','orange','orange','blue']

'''
##############################################################################
Simulations
##############################################################################
'''

t_sim = np.linspace(0,4,1001)*3600 # seconds

k_txn = 0.0075 #transcription rate

REP_con=500
      #0 0 0 1 0 0 0 1  0  0  0  1  1  1  1  1 (creates reporter)
I1 = [0,0,0,0,0,0,0,0,25,25,25,25,25,25,25,25]
I3 = [0,0,0,0,25,25,25,25,0,0,0,0,25,25,25,25]
I4 = [0,0,25,25,0,0,25,25,0,0,25,25,0,0,25,25] #input template
I5 = [0,25,0,25,0,25,0,25,0,25,0,25,0,25,0,25]


model = RSDs.RSD_sim() # define the model instance

model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates

# specify species involved in the reaction
model.molecular_species('AG{5.4,2}',DNA_con=25)
model.molecular_species('AG{3.1,2}',DNA_con=25)
model.molecular_species('R{2}',ic=REP_con)

plt.subplot(2,4,1)
for n in range(len(I1)):
    model.molecular_species('I{1}',DNA_con=I1[n])
    model.molecular_species('I{3}',DNA_con=I3[n])
    model.molecular_species('I{4}',DNA_con=I4[n])
    model.molecular_species('I{5}',DNA_con=I5[n])
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    

    # printing the conditions for which outputs are released    
    if (S2[-1] >= REP_con*.9):
        print("S{2} Created for Inputs=["+str(I1[n])+','+str(I3[n])+','+str(I4[n])+','+str(I5[n])+']')
       
    fs = 12
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
plt.title('AG{3.1,2} + AG{5.4,2}')