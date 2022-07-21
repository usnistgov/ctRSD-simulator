# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:31:56 2022

@author: tnm12
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
import time

import sys
sys.path.insert(1,'C:\\Users\\tnm12\\SURF')
import Simulatorv2021 as RSDs #import simulator version 2.0.2.1
    
##############################################################################
#Simulations
##############################################################################

IN_temp1 = [25,10]
                    #input templates
IN_temp2 = [10,25]

REP_con = 500 #reporter concentration

t_sim = np.linspace(0,6,1001)*3600 # seconds


model1 = RSDs.RSD_sim(10) # define the model instance and # of domains

#specify species invovled in the reaction
model1.molecular_species('CG{6,7}',DNA_con=45)
model1.molecular_species('g{6,2}',DNA_con=15)
model1.molecular_species('g{7,1}',DNA_con=15)
model1.molecular_species('REP{1}',DNA_con=REP_con)
model1.molecular_species('REP{2}',DNA_con=REP_con)


for n in range(len(IN_temp1)):

    model1.molecular_species('IN{6}',DNA_con=IN_temp1[n])
    model1.molecular_species('IN{7}',DNA_con=IN_temp2[n])
    
    
    # simulate the model
    model1.simulate(t_sim,smethod='BDF') #BDF method is used because of varying time scales
    

    # pull out the species from the model solution to plot
    S1 = model1.output_concentration('S{1}')
    S2 = model1.output_concentration('S{2}')
    
    
    plt.subplot(2,4,1+n*2)
    plt.plot(model1.t/60,(S1/REP_con)*100,color='red',linewidth=2,linestyle='-')
    plt.plot(model1.t/60,(S2/REP_con)*100,color='orange',linewidth=2,linestyle='-')
    
    fs = 12
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



sys.path.insert(1,'C:\\Users\\tnm12\\SURF')
import Simulator1 as RSDs #import version 1 of simulator
    


##############################################################################
#Simulations
##############################################################################


t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.013 #transcription rate


model2 = RSDs.RSD_sim(10) # define the model instance

# specify DNA txn templates and reporters and concentrations
model2.DNA_species('gate','6_7 wta',temp_con=45)

model2.DNA_species('gate','6_2',temp_con=15)
model2.DNA_species('gate','7_1',temp_con=15)

model2.DNA_species('reporter','REP1',temp_con=REP_con)
model2.DNA_species('reporter','REP2',temp_con=REP_con)


for n in range(len(IN_temp1)):
    
    model2.DNA_species('output','O6',temp_con=IN_temp1[n])
    model2.DNA_species('output','O7',temp_con=IN_temp2[n])
    
    # simulate the model
    model2.simulate(t_sim,1,k_txn)
    
    # pull out the species from the model solution to plot
    REP1 = model2.output_concentration['REP1']
    REP2 = model2.output_concentration['REP2']
    
    
    plt.subplot(2,4,1+n*2)
    plt.plot(model2.sol.t/60,(1-REP1/REP_con)*100,color='aqua',linewidth=2,linestyle='--')
    plt.plot(model2.sol.t/60,(1-REP2/REP_con)*100,color='blue',linewidth=2,linestyle='--')
    
    fs = 12
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
    if n == 0:
        plt.title('Input 6 Greater')
    else:
        plt.title('Input 7 Greater')
    plt.legend(['S1v2','S2v2','S1v1','S2v1'],frameon=False)

plt.suptitle('CG Simulation Comparison')
