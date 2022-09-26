# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:48:55 2022

@author: tnm12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
sys.path.insert(1,'filepath to simulator location on local computer')
import ctRSD_simulator_200 as RSDs #import simulator version 2.0.0

fs = 12



csl2 = [[255/255,170/255,170/255],
       [0.5,0,0],      
       [170/255,238/255,255/255],  
       [0/255,125/255,150/255],       
       [204/255,170/255,255/255],
       [100/255,42/255,150/255], 
       [255/255,204/255,170/255],      
       [1,0.25,0]]      


'''
##############################################################################
Simulations
##############################################################################
'''

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.0075 #transcription rate

REP_con = 500

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reaction

'''
For this simulation, gates with u-th inputs have default forward rate, gates \
with v-th inputs have a forward rate of 5e3/1e9 1/nM-s

Note the lowercase letters before and after the component indices are ignored in the simulation
these are only added here to keep track of components
'''

model.molecular_species('G{v1,u2r}',DNA_con=25,krsd=5e3/1e9) 
model.molecular_species('R{u2}',ic=REP_con)

model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates

IN1 = [0,50,0,0,0,0,0,0]
IN4 = [0,0,0,0,0,50,0,0]
                        #input templates
IN5 = [0,0,0,50,0,0,0,0]
IN3 = [0,0,0,0,0,0,0,50]

i = 0

plt.subplot(2,4,1)
for n in range(len(IN1)):
    
    model.molecular_species('I{v1}',DNA_con=IN1[n])
    model.molecular_species('I{v4}',DNA_con=IN4[n])
    model.molecular_species('I{u5}',DNA_con=IN5[n])
    model.molecular_species('I{u3}',DNA_con=IN3[n])
    
    if n > 1:
        model.molecular_species('G{u5,v1}',DNA_con=25) 
    if n > 3:
        model.molecular_species('G{v4,u5}',DNA_con=25,krsd=5e3/1e9) 
    if n > 5: 
        model.molecular_species('G{u3,v4}',DNA_con=25) 

    
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,100*(S2/REP_con),color=csl2[n],linewidth=2,linestyle='--')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,200)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('Two Toehold Simulation')