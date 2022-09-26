# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:01:25 2022

@author: tnm12
"""

'''
Version 2.0.2.1 Simulator
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
sys.path.insert(1,'filepath to simulator location on local computer')
import ctRSD_simulator_200 as RSDs #import simulator version 2.0.0


k_txn = 0.015 #transcription rate

t_sim = np.linspace(0,6,1001)*3600 # seconds

IN = [0,25] #input concentration list

REP_con = 500 #reporter concentration

krevL = [5/1e9*2e5,5/1e9] #changing reverse rates
krsdL = [1e3/1e9,1e1/1e9] #changing forward rates

color1 = [[0.2,0.2,0.2],
          [0.5,0,0]]

color2 = [[0.2,0.2,0.2],
          [0.5,0,0]]

for i in range(len(krevL)):
    for j in range(len(IN)):
        model1 = RSDs.RSD_sim(5) # define the model instance
        
        #initiate species involved in the reaction
        model1.molecular_species('G{1,2}',DNA_con=25,krev=krevL[i]) #changes corresponding reverse rate
        model1.molecular_species('R{2}',ic=REP_con)
        model1.molecular_species('I{1}',DNA_con=IN[j])
        
        model1.global_rate_constants(ktxn=k_txn,krsd=krsdL[i]) #changed transcription/forward rates
        
        # simulate the model
        model1.simulate(t_sim)
        
        # pull out the species from the model solution to plot
        S2 = model1.output_concentration('S{2}')
        
        fs = 12
        
        plt.subplot(2,4,1)
        if i == 0:
            plt.plot(model1.t/60,(S2/REP_con)*100,color=color1[j],linewidth=2,linestyle='--')
        else:
            plt.plot(model1.t/60,(S2/REP_con)*100,color=color2[j],linewidth=2,linestyle=':')
        plt.legend(['S2 Fast I=0','S2 Fast I=25','S2 Slow I=0','S2 Slow I=25'],frameon=False)
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
        
plt.suptitle('SA22_SI_figure18')