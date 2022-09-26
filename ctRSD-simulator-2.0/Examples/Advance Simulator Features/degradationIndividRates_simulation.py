# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:02:34 2022

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

kssd = [0,.001,.001,0,0] # single stranded degradation
kdsd = [0,.001,0,.001,0] # double stranded degradation
kdrd = [0,.001,0,0,.001] # RNA:DNA hybrid degradation

t_sim = np.linspace(0,6,1001)*3600 # seconds

color = ['aqua','orange','blue','red','pink']
linestyle = ['-','--','--','--','--']

model1 = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reactioon
model1.molecular_species('I{1}',DNA_con=IN_temp)
model1.molecular_species('G{1,2}',DNA_con=25)
model1.molecular_species('R{2}',ic=500)

for n in range(len(kssd)):
    
    model1.global_rate_constants(kssd=kssd[n],kdsd=kdsd[n],kdrd=kdrd[n]) #globally changes degradation rates
    
    # simulate the model (input is simulation time)
    model1.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model1.output_concentration('S{2}')
    I1 = model1.output_concentration('I{1}')
    G12 = model1.output_concentration('G{1,2}')
    O12 = model1.output_concentration('O{1,2}')
    
    
    plt.subplot(2,4,1)
    plt.plot(model1.t/60,I1,color=color[n],linewidth=2,linestyle=linestyle[n])   
    fs = 12
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.ylabel('Concentration (nM)',fontsize=fs)
    plt.xlabel('Time (min)',fontsize=fs)
    plt.legend(['None','All','kssd','kdsd','kdrd'],frameon=False,fontsize=10)
    plt.title('Input')
    
    plt.subplot(2,4,2)
    plt.plot(model1.t/60,G12,color=color[n],linewidth=2,linestyle=linestyle[n])   
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    plt.legend(['None','All','kssd','kdsd','kdrd'],frameon=False,fontsize=10)
    plt.title('Gate')
    
    plt.subplot(2,4,3)
    plt.plot(model1.t/60,O12,color=color[n],linewidth=2,linestyle=linestyle[n])   
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    plt.legend(['None','All','kssd','kdsd','kdrd'],frameon=False,fontsize=10)
    plt.title('Output')
    
    plt.subplot(2,4,4)
    plt.plot(model1.t/60,S2,color=color[n],linewidth=2,linestyle=linestyle[n])   
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    plt.legend(['None','All','kssd','kdsd','kdrd'],frameon=False,fontsize=10)
    plt.title('Reporter')
    