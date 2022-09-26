# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:43:57 2022

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
    


##############################################################################
#Simulations
##############################################################################


IN_temp = 25 #input template

REP_con = 500 #reporter concentration

deg = [0,.00025,.0005,.001] #degradation rate

t_sim = np.linspace(0,6,1001)*3600 # seconds

color = ['aqua','blue','yellow','green']

model1 = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reactioon
model1.molecular_species('I{1}',DNA_con=IN_temp)
model1.molecular_species('G{1,2}',DNA_con=25)
model1.molecular_species('R{2}',ic=500)

for n in range(len(deg)):
    
    model1.global_rate_constants(kdeg=deg[n]) #globally changes all degradation rates
    
    # simulate the model (input is simulation time)
    model1.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model1.output_concentration('S{2}')
    
    
    plt.subplot(2,4,1)
    plt.plot(model1.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='--')   
fs = 12
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
#plt.ylim(-10,2000)
plt.xlim(0,180)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.xlabel('Time(min)',fontsize=fs)
plt.title('Degradation Simulation')
plt.legend(['kdeg=0','kdeg=.00025','kdeg=.0005','kdeg=.001'],frameon=False,fontsize=8)