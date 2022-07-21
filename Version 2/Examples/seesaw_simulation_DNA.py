# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 12:48:27 2022

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

ic = 90

IN_temp1 = [0,ic,0,ic] #input template
IN_temp3 = [0,0,ic,ic] #input template

t_sim = np.linspace(0,6,1001)*3600 # seconds

fuel_con = [0,200] #fuel concentration

color = ['blue', 'red','aqua','orange']

linestyle = ['--','-','--','--']

model2 = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reaction
model2.molecular_species('G{1,2}',ic=100)
model2.molecular_species('G{3,2}',ic=100)
model2.molecular_species('G{2,4}',ic=200)
model2.molecular_species('REP{4}',ic=150)
model2.molecular_species('th{2}',ic=120)

model2.global_rate_constants(krsd=5e4/1e9,krsdF=5e4/1e9,kth=2e6/1e9,krep=5e4/1e9)

for j in range(len(fuel_con)):
    
    model2.molecular_species('f{2}',ic=fuel_con[j])

    for n in range(len(IN_temp1)):

        model2.molecular_species('I{1}',ic=IN_temp1[n])
        model2.molecular_species('I{3}',ic=IN_temp3[n])
    
    # simulate the model (input is simulation time)
        model2.simulate(t_sim)
        
        
        # pull out the species from the model solution to plot
        S4 = model2.output_concentration('S{4}')
        
        
        fs = 12 #font size
        
        plt.subplot(2,5,1+2*j)
        plt.plot(model2.t/60,(S4/150)*100,color=color[n],linewidth=2,linestyle=linestyle[n])
    
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.ylim(-10,110)
    plt.xlim(0,240)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    plt.ylabel('Reacted reporter (%)',fontsize=fs)
    if j == 0:
        plt.title('DNA Implementation w/o Fuel')
    else:
        plt.title('DNA Implementation w/ Fuel')
    plt.legend(['o','I1','I3','I1,I3'],frameon=False,fontsize=8)
