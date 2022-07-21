# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 10:51:49 2022

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

tic = time.time()
    
##############################################################################
#Simulations
##############################################################################

IN_temp1 = [0,2.5,5,7.5,10,12.5,15]
                                    #input templates
IN_temp2 = [0,2.5,5,7.5,10,12.5,15]

REP_con = 500 #reporter concentration

t_sim = np.linspace(0,6,1001)*3600 # seconds


model1 = RSDs.RSD_sim(7) # define the model instance and # of domains

#specify species invovled in the reaction
model1.molecular_species('CG{6,7}',DNA_con=45)
model1.molecular_species('g{6,2}',DNA_con=15)
model1.molecular_species('g{7,1}',DNA_con=15)
model1.molecular_species('REP{1}',DNA_con=REP_con)
model1.molecular_species('REP{2}',DNA_con=REP_con)

model1.global_rate_constants(krsdCG=5e5/1e9)

outputs = np.empty((len(IN_temp1),len(IN_temp2)),dtype=object)



for i in range(len(IN_temp1)):
    for j in range(len(IN_temp2)):

        model1.molecular_species('IN{6}',DNA_con=IN_temp1[i])
        model1.molecular_species('IN{7}',DNA_con=IN_temp2[j])
        
        
        # simulate the model
        model1.simulate(t_sim,smethod='BDF') #BDF method is used because of varying time scales
        
    
        # pull out the species from the model solution to plot
        S1 = model1.output_concentration('S{1}')
        S2 = model1.output_concentration('S{2}')
        
        outputs[i][j] = [S1,S2]
        
for i in range(len(IN_temp1)):
    for j in range(len(IN_temp2)): 
        
        S1 = outputs[i][j][0]
        S2 = outputs[i][j][1]
                          
        plt.subplot(len(IN_temp1),len(IN_temp2),i*len(IN_temp1)+(j+1))
        if i == j:
            plt.plot(model1.t/60,(S1/REP_con)*100,color='red',linewidth=2,linestyle='-')
        else:
            plt.plot(model1.t/60,(S1/REP_con)*100,color='red',linewidth=2,linestyle='--')
        plt.plot(model1.t/60,(S2/REP_con)*100,color='blue',linewidth=2,linestyle='--')
        
        fs = 12
        plt.xticks(fontsize=fs)
        plt.yticks(fontsize=fs)
        plt.ylim(-10,110)
        plt.xlim(0,240)
        ax1 = plt.gca()
        ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
        ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
        if i != 6:
            ax1.get_xaxis().set_visible(False)
        if j != 0:
            ax1.get_yaxis().set_visible(False)
        if i == 6 and j == 3:
            plt.xlabel('Time (min)',fontsize=fs)
        if i == 3 and j == 0:
            plt.ylabel('Reacted reporter (%)',fontsize=fs)
         
        if S1[-1] > S2[-1] and (i!=j):
            plt.fill_between(model1.t/60, (S1/REP_con)*100, (S2/REP_con)*100, color='red',alpha=0.2)
            plt.fill_between(model1.t/60, (S2/REP_con)*100, color='blue',alpha=0.2)
        elif S1[-1] < S2[-1] and (i!=j):
            plt.fill_between(model1.t/60, (S1/REP_con)*100, (S2/REP_con)*100, color='blue',alpha=0.2)
            plt.fill_between(model1.t/60, (S1/REP_con)*100, color='red',alpha=0.2)

toc = time.time()
time_elapsed = toc - tic