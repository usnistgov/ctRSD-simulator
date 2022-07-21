# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 12:49:02 2022

@author: tnm12
"""
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

import sys
import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator

fs = 12 #fontsize


'''
Creating simulation data to act as data for function input
'''

k_txn = .01

t_sim = np.linspace(0,6,1001)*3600 # seconds

REP_con = 500 #reporter concentration

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involved in the reaction
model.molecular_species('O{1,2}',DNA_con=25) 
model.molecular_species('REP{2}',DNA_con=REP_con)
 
plt.subplot(2,4,1)

model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates

# run simulaton (input is simulaton time)
model.simulate(t_sim,smethod='LSODA')

# pull out the species from the model solution to plot
S2 = model.output_concentration('S{2}') #data for function input




model = RSDs.RSD_sim() #define model instance

model.transcription_calibration(simTime=t_sim,data=S2) #function call without ktxn specified will run against assortment of usual suspects for rates

model.transcription_calibration(simTime=t_sim,data=S2,ktxn=[0.005,0.0075,0.01,0.0125,.015,.02,.02125,.025,.0275]) #function call with ktxn specified runs data against specified transcription rates (also works with single value)


