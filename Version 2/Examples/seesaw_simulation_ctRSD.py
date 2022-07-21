# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:25:30 2022

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


IN_temp1 = [0,25,0,25] #input template
IN_temp3 = [0,0,25,25] #input template

REP_con = 500 #reporter concentration

t_sim = np.linspace(0,6,1001)*3600 # seconds

fuel_con = [0,250] #fuel concentration

color = ['blue', 'red','aqua','orange']

linestyle = ['--','-','--','--']

model1 = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reaction
model1.molecular_species('G{1,2}',DNA_con=25)
model1.molecular_species('G{3,2}',DNA_con=25)
model1.molecular_species('G{2,4}',DNA_con=25)
model1.molecular_species('REP{4}',DNA_con=REP_con)
model1.molecular_species('th{2}',DNA_con=30)


for j in range(len(fuel_con)):
    
    model1.molecular_species('F{2}',DNA_con=fuel_con[j])
    
    for n in range(len(IN_temp1)):
    
        model1.molecular_species('I{1}',DNA_con=IN_temp1[n])
        model1.molecular_species('I{3}',DNA_con=IN_temp3[n])
    
    # simulate the model (input is simulation time)
        model1.simulate(t_sim)
        
        
        # pull out the species from the model solution to plot
        S4 = model1.output_concentration('S{4}')
        
        
        fs = 12 #font size
        
        plt.subplot(2,4,1+j*2)
        plt.plot(model1.t/60,(S4/REP_con)*100,color=color[n],linewidth=2,linestyle=linestyle[n])

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
        plt.title('Seesaw Sim w/o Fuel')
    else:
        plt.title('Seesaw Sim w/ Fuel')
    plt.legend(['o','I1','I3','I1,I3'],frameon=False,fontsize=8)
    
