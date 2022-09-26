# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:36:41 2022

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

'''
G{1,2}
'''

color1 =[[0,0,0.5],[0.5,0,0]]

t_sim = np.linspace(0,8,1001)*3600 # seconds

k_txn = 0.01 #transcription rate

IN1 = 10 #input concentration
REP_con = 500 #reporter concentration

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# Initialize species involved in the reaction
model.molecular_species('G{1,2}',DNA_con=25,krev=5/1e9) #updtes corresponding reverse rate
model.molecular_species('R{2}',ic=REP_con)
model.molecular_species('I{1}',DNA_con=IN1)


ksd1 = [1e3/1e9,2e1/1e9] # 1/nM-s

i = 0

for n in range(len(ksd1)):
    
    
    model.global_rate_constants(ktxn=k_txn,krsd=ksd1[n]) #globally change needed rates
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim) 
    
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.subplot(2,4,1)
    plt.plot(model.t/60,(S2 / REP_con)*100,color=color1[n],linewidth=2,linestyle='--')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,400)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.legend(['Fast Fwd Rate','Slow Fwd Rate'],frameon=False)
plt.title('Gate{1,2}')

'''
AND gate
'''

IN1 = 10 #input concentration

t_sim = np.linspace(0,8,1001)*3600 # seconds

k_txn = 0.01 #transcription rate

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involved in the reaction
model.molecular_species('I{1}',DNA_con=IN1)
model.molecular_species('I{3}',DNA_con=25)
model.molecular_species('R{2}',ic=REP_con)

ksd1 = [1e3/1e9,0.5e1/1e9] # 1/nM-s



i = 0

for n in range(len(ksd1)):
      
    model.global_rate_constants(ktxn=k_txn) #globally changes needed rates
    model.molecular_species('I{1}',DNA_con=IN1)
    model.molecular_species('AG{3.1,2}',DNA_con=25,krev=5/1e9) #changes reverse rate for reaction
    model.molecular_species('AGOa{1,2}',krsdA=ksd1[n]) #changes rate for second gate in reaction
    
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.subplot(2,4,3)
    plt.plot(model.t/60,(S2 / REP_con)*100,color=color1[n],linewidth=2,linestyle='--')


plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,400)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.legend(['Fast Fwd Rate','Slow Fwd Rate'],frameon=False)
plt.title('Gate{3,2} AGOa{1,2}')

plt.suptitle('SA22_SIfigure26')