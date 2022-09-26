# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:27:34 2022

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


t_sim = np.linspace(0,6,1001)*3600 # seconds

REP_con = 500 #reporter concentration

fuel_con = [0,50] #fuel concentration

color = ['red','blue']

linestyle = ['--','--']

# model with inputs
model1 = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reaction
model1.molecular_species('AG{3.1,2}',DNA_con=25)
model1.molecular_species('R{2}',ic=REP_con)
model1.molecular_species('O{4,1}',DNA_con=1.25)
model1.molecular_species('I{3}',DNA_con=25)


for n in range(len(fuel_con)):
    model1.molecular_species('F{1}',DNA_con=fuel_con[n])
    
    # simulate the model (input is simulation time)
    model1.simulate(t_sim)
    
    
    # pull out the species from the model solution to plot
    S2 = model1.output_concentration('S{2}')
    
    fs = 12
    
    plt.subplot(2,4,1)
    plt.plot(model1.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle=linestyle[n])
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.xlim(0,180)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.xlabel('Time(min)',fontsize=fs)
plt.title('AND Gate Fuel Sim')
plt.legend(['S{2} w/o F','S{2} w/ F'],frameon=False)

