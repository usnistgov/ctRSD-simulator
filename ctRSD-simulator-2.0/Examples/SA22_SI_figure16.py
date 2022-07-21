# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:58:34 2022

@author: tnm12
"""
import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator
    
'''
##############################################################################
Simulations
##############################################################################
'''


k_txn = 0.024 #transcirption rate

txn_time = [0.5,1,2]

REP_con = 500 #reporter concentration


color = ['orange','aqua','pink'] # colors for plotting

title = ['0.5 h Transcription','1 h Transcription','2 h Transcription']



for n in range(len(txn_time)):
    
    model1 = RSDs.RSD_sim(5) # define the model instance and # of domains
    
    #input species involved in reaction
    model1.molecular_species('g{1,2}',DNA_con=50,krev=5/1e9) #changed corresponding reverse rate
    model1.molecular_species('in{3}',DNA_con=100)
   
    t_sim = np.linspace(0,txn_time[n],1001)*3600 # seconds
    
    model1.global_rate_constants(ktxn=k_txn) #changes all transcription rates to .024
    
    # simulate the model
    model1.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    gate_produced = model1.output_concentration('g{1,2}')[-1]
    in_produced = model1.output_concentration('in{3}')[-1]
    
    model1 = RSDs.RSD_sim(5) # define the model instance and # of domains

    #input species involved in reaction
    model1.molecular_species('g{1,2}',DNA_con=0,ic=gate_produced/2,krev=5/1e9) #changed corresponding reverse rate
    model1.molecular_species('in{1}',DNA_con=0,ic=in_produced/2)
    model1.molecular_species('r{2}',DNA_con=REP_con)
    
    t_sim = np.linspace(0,3,1001)*3600 # seconds
    
    model1.global_rate_constants(ktxn=k_txn) #changes all transcription rates to .024
    
    # simulate the model
    model1.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model1.output_concentration('S{2}')

    fs = 12
    
    plt.subplot(2,3,n+1)
    plt.plot(model1.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='--')
    plt.legend(['S2'],frameon=False)
    plt.title(title[n])
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.ylim(-10,110)
    plt.xlim(0,180)
    ax1 = plt.gca()
    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
    #ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
    plt.xlabel('Time (min)',fontsize=fs)
    if n == 0:
        plt.ylabel('Reacted Reporter (%)',fontsize=fs)
        
    plt.suptitle('SA22_SI_figure16')