# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:26:36 2022

@author: tnm12
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

import sys
sys.path.insert(1,'filepath to simulator location on local computer')
import ctRSD_simulator_200 as RSDs #import simulator version 2.0.0
    
'''
##############################################################################
Simulations
##############################################################################
'''


# create the model instance
model = RSDs.RSD_sim(8) # increasing # of domains to match highest index in system

model.global_rate_constants(ktxn=0.02) # changing the global transcription rate constant

# specify species involved in the system
model.molecular_species('O{4,3}',DNA_con=25)
model.molecular_species('G{3,8}',DNA_con=15)
model.molecular_species('G{3,5}',DNA_con=15,krsd=5e-6) # changing krsd{3,5} 
model.molecular_species('G{8,2}',DNA_con=10,krev=1e-8) # changing krev{8,2}
model.molecular_species('G{5,2}',DNA_con=10,krsd=3e-6,krev=1e-8) # changing krsd{5,2} and krev{5,2} 
model.molecular_species('R{2}',ic=500)

# simulating the model
t_sim = np.linspace(0,6,1001)*3600 # seconds
model.simulate(t_sim) # simulate the model

# pull out the species from the model solution to plot
S2 = model.output_concentration('S{2}')

    
fs = 12    
plt.subplot(3,5,1)
plt.plot(model.t/60,(S2/model.R_ic[1])*100,color=[1,0,0],linewidth=2,linestyle='--')
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


