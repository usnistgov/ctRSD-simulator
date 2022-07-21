

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:29:40 2022

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

color = ['blue', 'aqua']
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
    plt.plot(model1.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='-')
    plt.xlabel('Time(min)',fontsize=fs)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.xlim(0,180)



import Simulator1 as RSDs #import first version of simulator
    


##############################################################################
#Simulations
##############################################################################


IN_temp = 25 #input template

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.013 #transcription rate

thresh_con = [0,50] #threshold concentration

color = ['orange','red']

model2 = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model2.DNA_species('gate','1_2',temp_con=25)
model2.DNA_species('reporter','REP2',temp_con=500)
model2.DNA_species('input','I1',temp_con=IN_temp)


for n in range(len(thresh_con)):
    
    model2.DNA_species('threshold','TH1',temp_con=thresh_con[n])

    # simulate the model
    model2.simulate(t_sim,1,k_txn)
    
    
    # pull out the species from the model solution to plot
    REP = model2.output_concentration['REP2']
    
    
    fs = 12
    
    plt.subplot(2,4,1)
    plt.plot(model2.sol.t/60,(1-REP/REP_con)*100,color=color[n],linewidth=2,linestyle='--')
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
    plt.title('Threshold Simulation Comparison')
    plt.legend(['Th=0v2','Th=50v2','Th=0v1','Th=50v1'],frameon=False)