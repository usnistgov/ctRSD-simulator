# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:23:42 2022

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


IN_temp = 50 #input template
REP_con = 500 #reporter concentration

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.01 #transcription rate 


X = [0,1,5,10,25,50,100] # fold increase of reverse reaction rate

cslr = [[0.1,0,0],
       [0.4,0,0],
       [0.6,0,0],
       [1,0,0],
       [1,0.3,0],
       [1,0.5,0],
       [1,0.75,0]]
                    #colors for plotting
cslb = [[0,0,0.1],
       [0,0,0.4],
       [0,0,0.6],
       [0,0,1],
       [0,0.3,1],
       [0,0.5,1],
       [0,0.75,1]]



'''
Panel A
'''

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involvded in the reaction
model.molecular_species('REP{2}',DNA_con=REP_con)
model.molecular_species('I{1}',DNA_con=IN_temp)

plt.subplot(3,5,2)
for n in range(len(X)):
    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n]) #globally change transcription/reverse rates
    model.molecular_species('g{1,2}',DNA_con=25,krev=(5/1e9)*X[n]) #looping through fold increase of corresponding reverse rate
    
    
    # simulate the model (input is time of simulation)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=cslb[n],linewidth=1,linestyle='--')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,200)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('One Layer',fontsize=fs)

'''
Panel B
'''

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involved in reaction
model.molecular_species('REP{1}',DNA_con=REP_con)
model.molecular_species('I{3}',DNA_con=IN_temp)
model.molecular_species('gate{3,1}',DNA_con=25)

plt.subplot(3,5,4)
for n in range(len(X)):
    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n]) #globally change transcription / reverse rates

    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S1 = model.output_concentration('S{1}')
    
    fs = 12
    
    plt.plot(model.t/60,(S1/REP_con)*100,color=cslr[n],linewidth=1,linestyle='--')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,200)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('One Layer',fontsize=fs)

'''
Panel C, left
'''

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involved in the reaction
model.molecular_species('gate{3,1}',DNA_con=25)
model.molecular_species('REP{2}',DNA_con=REP_con)
model.molecular_species('I{3}',DNA_con=IN_temp)

plt.subplot(3,5,11)
for n in range(len(X)):
   
    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n]) #globally change transcription / reverse rates
    model.molecular_species('gate{1,2}',DNA_con=25,krev=(5/1e9)*X[n]) #update correspodning reverse rate
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=cslb[n],linewidth=1,linestyle='--')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,200)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('Two Layer',fontsize=fs)

'''
Panel C, middle
'''

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involved in the reaction
model.molecular_species('gate{4,3}',DNA_con=25)
model.molecular_species('gate{3,1}',DNA_con=25)
model.molecular_species('REP{2}',DNA_con=500)
model.molecular_species('I{4}',DNA_con=IN_temp)

plt.subplot(3,5,13)
for n in range(len(X)):
    
    
    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n]) #globally change transcription / reverse rates
    model.molecular_species('gate{1,2}',DNA_con=25,krev=(5/1e9)*X[n]) #update corresponding reverse rate
    
    # simulate the model (input is simulation time )
    model.simulate(t_sim)
    
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=cslb[n],linewidth=1,linestyle='--')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,200)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('Three Layer',fontsize=fs)

'''
Panel C, right
'''

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involved in the reaction
model.molecular_species('gate{5,4}',DNA_con=25)
model.molecular_species('gate{4,3}',DNA_con=25)
model.molecular_species('gate{3,1}',DNA_con=25)
model.molecular_species('REP{2}',DNA_con=REP_con)
model.molecular_species('I{5}',DNA_con=IN_temp)

plt.subplot(3,5,15)
for n in range(len(X)):

    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n]) #globally change transcription / reverse rates
    model.molecular_species('gate{1,2}',DNA_con=25,krev=(5/1e9)*X[n])    
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=cslb[n],linewidth=1,linestyle='--')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,200)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.title('Four Layer',fontsize=fs)



plt.suptitle('SA22_SI_figure19')