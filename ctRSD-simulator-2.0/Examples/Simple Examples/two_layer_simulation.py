# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:26:36 2022

@author: tnm12
"""

# auxiliary packages needed in the script below, e.g., plotting
import numpy as np
import matplotlib.pyplot as plt

# importing the simulator
import sys
sys.path.insert(1,'filepath to simulator location on local computer')
import ctRSD_simulator_200 as RSDs #import simulator version 2.0.0
    
'''
##############################################################################
Simulations
##############################################################################
'''

# create the model instance
model = RSDs.RSD_sim() # default # of domains (5 domains)

model.global_rate_constants(ktxn=0.02) # changing the global transcription rate constant

# specify species involved in the system
model.molecular_species('I{3}',DNA_con=25)
model.molecular_species('G{3,2}',DNA_con=25)
model.molecular_species('G{1,2}',DNA_con=10)
model.molecular_species('R{2}',ic=500)

# simulating the model
t_sim = np.linspace(0,3,1001)*3600 # simulating from 0 to 3 hours with 1000 increments (*3600 converts to seconds)
model.simulate(t_sim) # simulate the model

# pull out the species from the model solution to plot
S2 = model.output_concentration('S{2}') # S{2} is the output of a reacted reporter (R{2})
I3 = model.output_concentration('I{3}') # concentration of I{3} as a function of time
G12 = model.output_concentration('G{1,2}') # concentration of G{1,2} as a function of time
# etc...

# simple plotting code
plt.plot(t_sim,S2)
plt.plot(t_sim,I3,color='red')
plt.plot(t_sim,G12,color='green')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (nM)')


# plotting code that mirrors plots in ctRSD publications
plt.figure(2)
fs = 12    
# converting time to minutes, normalzing reacted reporter from 0 to 100%
plt.plot(t_sim/60,(S2/model.R_ic[1])*100,color=[0,0,1],linewidth=2,linestyle='--')
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

