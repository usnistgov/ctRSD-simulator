# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:25:45 2022

@author: tnm12
"""
import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import Simulatorv2021 as RSDs #imoort version 2021 of the simulator
    
'''
##############################################################################
Simulations
In this example, the 1_2 gate is initially transcribed for an hour in the
absence of the I1 template. After the first hour, the I1 template is added and
the reaction is resumed for another 3 hours
##############################################################################
'''


REP_con = 500 #reporter concentration

k_txn = 0.01 #transcription rate

    
t_sim = np.linspace(0,1,1001)*3600 # seconds

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify DNA txn templates and reporters and concentrations

model.molecular_species('gate{1,2}',DNA_con=25)
model.molecular_species('reporter{2}',DNA_con=REP_con)
model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates

# simulate the model (before addition of the input template)
model.simulate(t_sim)

# updating the simulation time for the second phase of the simulation
t_sim2 = np.linspace(t_sim[-1]/3600,4,1001)*3600 # seconds

# adding the I1 template to the model
model.molecular_species('input{1}',DNA_con=25)

# simulate the model (after addition of the input template)
model.simulate(t_sim2,iteration=2) #must specify it is second iteration

# pulling out the reporter concentration for plotting
S2 = model.output_concentration('S{2}')

fs = 12
plt.subplot(2,4,1)
plt.plot(model.t/60,(S2/REP_con)*100,'blue',linewidth=2,linestyle='--')
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,240)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.legend(['S2v2'],frameon=False)
plt.title('Discontinuous Simulation')