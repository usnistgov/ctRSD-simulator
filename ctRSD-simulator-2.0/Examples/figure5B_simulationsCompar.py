# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 13:49:49 2022

@author: tnm12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
import Simulator1 as RSDs #import first version of simulator

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

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25) 

model.DNA_species('reporter','REP2',temp_con=500)

IN1 = [0,50,0,0,0,0,0,0]
IN4 = [0,0,0,0,0,50,0,0]
                        #input templates
IN5 = [0,0,0,50,0,0,0,0]
IN3 = [0,0,0,0,0,0,0,50]

i = 0

plt.subplot(2,4,1)
for n in range(len(IN1)):
    
    model.DNA_species('input','I1',temp_con=IN1[n])
    model.DNA_species('input','I4',temp_con=IN4[n])
    model.DNA_species('input','I5',temp_con=IN5[n])
    model.DNA_species('input','I3',temp_con=IN3[n])
    if n > 1:
        model.DNA_species('gate','5_1',temp_con=25) # output gate
    if n > 3:
        model.DNA_species('gate','4_5',temp_con=25) # output gate
    if n > 5: 
        model.DNA_species('gate','3_4',temp_con=25) # output gate
    
    
    # simulate the model
    model.simulate(t_sim,1,k_txn)
    
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,100*(1-REP/model.REP_con[1]),color=csl2[n],linewidth=2,linestyle='-')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,200)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)




import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator

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
model.molecular_species('gate{1,2}',DNA_con=25) 
model.molecular_species('reporter{2}',DNA_con=REP_con)

model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates

IN1 = [0,50,0,0,0,0,0,0]
IN4 = [0,0,0,0,0,50,0,0]
                        #input templates
IN5 = [0,0,0,50,0,0,0,0]
IN3 = [0,0,0,0,0,0,0,50]

i = 0

plt.subplot(2,4,1)
for n in range(len(IN1)):
    
    model.molecular_species('input{1}',DNA_con=IN1[n])
    model.molecular_species('input{4}',DNA_con=IN4[n])
    model.molecular_species('input{5}',DNA_con=IN5[n])
    model.molecular_species('input{3}',DNA_con=IN3[n])
    
    if n > 1:
        model.molecular_species('gate{5,1}',DNA_con=25) # output gate
    if n > 3:
        model.molecular_species('gate{4,5}',DNA_con=25) # output gate
    if n > 5: 
        model.molecular_species('gate{3,4}',DNA_con=25) # output gate
    
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,100*(S2/REP_con),color='orange',linewidth=2,linestyle='--')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,200)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('Figure 5B Comparison')