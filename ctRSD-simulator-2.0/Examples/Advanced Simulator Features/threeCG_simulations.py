# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 09:33:22 2022

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


IN_temp1 = [50,20,20]
IN_temp2 = [30,50,30] #input templates
IN_temp3 = [20,30,50]

REP_con = 500 #reporter concentration

t_sim = np.linspace(0,6,1001)*3600 # seconds

model1 = RSDs.RSD_sim(7) # define the model instance and # of domains

model1.global_rate_constants(krsdCG=5e5/1e9)

# specify species involved in the reaction
model1.molecular_species('CG{6,7}',DNA_con=45)
model1.molecular_species('CG{7,4}',DNA_con=45)
model1.molecular_species('CG{4,6}',DNA_con=45)
model1.molecular_species('G{6,2}',DNA_con=15)
model1.molecular_species('G{7,1}',DNA_con=15)
model1.molecular_species('G{4,3}',DNA_con=15)
model1.molecular_species('R{1}',ic=REP_con)
model1.molecular_species('R{2}',ic=REP_con)
model1.molecular_species('R{3}',ic=REP_con)

for n in range(len(IN_temp1)):
    
    model1.molecular_species('I{7}',DNA_con=IN_temp1[n])
    model1.molecular_species('I{6}',DNA_con=IN_temp2[n])
    model1.molecular_species('I{4}',DNA_con=IN_temp3[n])
    
    # simulate the model
    model1.simulate(t_sim,smethod='BDF') #BDF methos is used because of varying time scales
    
    
    # pull out the species from the model solution to plot
    S1 = model1.output_concentration('S{1}')
    S2 = model1.output_concentration('S{2}')
    S3 = model1.output_concentration('S{3}')
    
    plt.subplot(2,5,1+n*2)
    plt.plot(model1.t/60,(S1/REP_con)*100,color='red',linewidth=2,linestyle='--')
    plt.plot(model1.t/60,(S2/REP_con)*100,color='blue',linewidth=2,linestyle='--')
    plt.plot(model1.t/60,(S3/REP_con)*100,color='orange',linewidth=2,linestyle='--')
    
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
        plt.title('I{7} > I{6},I{4}')
    elif n ==1:
        plt.title('I{6} > I{7},I{4}')
    else:
        plt.title('I{4} > I{6},I{7}')
    plt.legend(['S{1}','S{2}','S{3}'],frameon=False,fontsize=10)
        
    

plt.suptitle('Three CG Simulation')