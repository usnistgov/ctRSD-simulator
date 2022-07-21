# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:26:36 2022

@author: tnm12
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator
    

'''
##############################################################################
Simulations
##############################################################################
'''

color = ['yellow','pink','aqua','red','green','purple']

IN_temp = [50,25,12.5,6.25,2.5,0] #input template

REP_con = 500 #reporter concentration

t_sim = np.linspace(0,6,1001)*3600 # seconds


# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

# specify species involved in the reactio 
model.molecular_species('gate{1,2}',DNA_con=25)
model.molecular_species('reporter{2}',DNA_con=REP_con)



fs = 12

plt.subplot(2,4,1)
for n in range(len(IN_temp)):
    
    model.molecular_species('input{1}',DNA_con=IN_temp[n])
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    plt.rcParams.update({'font.sans-serif':'Verdana'})
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=color[n],linewidth=2,linestyle='--')

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

plt.title('Figure 2D')

