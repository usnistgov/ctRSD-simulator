# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:03:45 2022

@author: tnm12
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

import sys
import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator
    


##############################################################################
#Simulations
##############################################################################


IN_temp = 25 #input template

REP_con = 500 #reporter concentration

t_sim = np.linspace(0,6,1001)*3600 # seconds

thresh_con = [0,50] #threshold concentration

color = ['blue', 'red']
model1 = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reaction
model1.molecular_species('G{1,2}',DNA_con=25)
model1.molecular_species('REP{2}',DNA_con=REP_con)
model1.molecular_species('I{1}',DNA_con=IN_temp)

for n in range(len(thresh_con)):
    model1.molecular_species('th{1}',DNA_con=thresh_con[n])

# simulate the model (input is simulation time)
    model1.simulate(t_sim)
    
    
    # pull out the species from the model solution to plot
    S2 = model1.output_concentration('S{2}')
    
    
    fs = 12 #font size
    
    plt.subplot(2,4,1)
    plt.plot(model1.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='--')
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.ylim(-10,110)
    plt.xlim(0,240)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    plt.ylabel('Reacted reporter (%)',fontsize=fs)
    plt.title('Threshold Simulation')
    plt.legend(['Th=0v2','Th=50v2'],frameon=False)