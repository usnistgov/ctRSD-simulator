# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 12:08:25 2022

@author: tnm12
"""
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

import sys
import Simulatorv2021 as RSDs #import version 2.0.2.1 of simulator


'''
WILL USE SIMULATION DATA AS TEST DATA TO SHOW FUNCTIONALITY OF TRANSCRIPTION_CALIBRATION
'''

fs = 12 #fontsize

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = .0045 #transcription rate for simulatio data

REP_con = 500 #reporter concentration

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involved in the reaction
model.molecular_species('O{1,2}',DNA_con=25) 
model.molecular_species('REP{2}',DNA_con=REP_con)
 

model.global_rate_constants(ktxn=k_txn) #globally changes transcription rates

# run simulaton (input is simulaton time)
model.simulate(t_sim,smethod='LSODA')

# pull out the species from the model solution to plot
S2 = model.output_concentration('S{2}') #data to be inputted into calibration function


'''
TESTING FIRST SET OF TRANSCRIPTION RATES
'''
k_txn1 = [0.015,0.009,0.006,0.0045,.02,.0065] #transcription rates
t_sim = np.linspace(0,6,1001)*3600 # seconds

model = RSDs.RSD_sim() # define the model instance 

model.transcription_calibration(simTime=t_sim,data=S2,ktxn=k_txn1) #calling function with corresponding index in k_txn as a specific rate
         


