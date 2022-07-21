# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:20:49 2022

@author: tnm12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
import Simulator1 as RSDs #import first version of simulator
    
'''
##############################################################################
Simulations
##############################################################################
'''

'''
1_2r gate
'''

csl =[[0,0,0.5],[0.5,0,0]]

color1 = ['aqua','blue']

t_sim = np.linspace(0,8,1001)*3600 # seconds

k_txn = 0.01

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25) # thresholding gate

model.DNA_species('reporter','REP2',temp_con=500)

IN1 = [10,10]

ksd1 = [1e3/1e9,2e1/1e9] # 1/nM-s
ksd = 1e3/1e9 # 1/nM-s
kfsd = 1e3/1e9 # 1/nM-s
krev = 270/1e9 # 1/nM-s
kf_rep = 1e4/1e9 # 1/nM-s
kr_rep = 0*1e2/1e9 # 1/nM-s
kf_wta = 1e6/1e9 # 1/nM-s
kr_wta = 0.4 # 1/s
kRz = 0.25/60 # 1/s
kth = 1e5/1e9 # 1/nM-s
kd = 0

i = 0

for n in range(len(ksd1)):
    
    model.DNA_species('input','I1',temp_con=IN1[n])
    
    rte=[[k_txn],[ksd1[n],ksd,ksd,ksd,ksd],[kfsd],[krev,5/1e9,krev,krev,krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]
    
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    #model.simulate(t_sim,1,k_txn)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.subplot(2,4,1)
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=color1[n],linewidth=2,linestyle='-')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,400)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)

'''
AND gate
'''

t_sim = np.linspace(0,8,1001)*3600 # seconds

k_txn = 0.01

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','3&1_2',temp_con=25) # thresholding gate
model.DNA_species('input','I3',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)

IN1 = [10,10]

ksd1 = [1e3/1e9,0.5e1/1e9] # 1/nM-s
ksd = 1e3/1e9 # 1/nM-s
kfsd = 1e3/1e9 # 1/nM-s
krev = 270/1e9 # 1/nM-s
kf_rep = 1e4/1e9 # 1/nM-s
kr_rep = 0*1e2/1e9 # 1/nM-s
kf_wta = 1e6/1e9 # 1/nM-s
kr_wta = 0.4 # 1/s
kRz = 0.25/60 # 1/s
kth = 1e5/1e9 # 1/nM-s
kd = 0

i = 0

for n in range(len(ksd1)):
    
    model.DNA_species('input','I1',temp_con=IN1[n])
    
    rte=[[k_txn],[ksd1[n],ksd,ksd,ksd,ksd],[kfsd],[krev,5/1e9,krev,krev,krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]
    
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    #model.simulate(t_sim,1,k_txn)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.subplot(2,4,3)
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=color1[n],linewidth=2,linestyle='-')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,400)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)




import Simulatorv2021 as RSDs #import first version of simulator
    
'''
##############################################################################
Simulations
##############################################################################
'''

'''
1_2r gate
'''

csl =[[0,0,0.5],[0.5,0,0]]

color1 = ['red','orange']

t_sim = np.linspace(0,8,1001)*3600 # seconds

k_txn = 0.01

IN1 = 10
REP_con = 500

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# Initialize species involved in the reaction
model.molecular_species('gate{1,2}',DNA_con=25,krev=5/1e9) #updtes corresponding reverse rate
model.molecular_species('REP{2}',DNA_con=REP_con)
model.molecular_species('I{1}',DNA_con=IN1)


ksd1 = [1e3/1e9,2e1/1e9] # 1/nM-s

i = 0

for n in range(len(ksd1)):
    
    
    model.global_rate_constants(ktxn=k_txn,krsd=ksd1[n]) #globally change needed rates
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim) 
    
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.subplot(2,4,1)
    plt.plot(model.t/60,(S2 / REP_con)*100,color=color1[n],linewidth=2,linestyle='--')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,400)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.legend(['V1 Fast','V1 Slow','V2 Fast','V2 Slow'],frameon=False)
plt.title('Gate{1,2}')

'''
AND gate
'''

IN1 = 10

t_sim = np.linspace(0,8,1001)*3600 # seconds

k_txn = 0.01

model = RSDs.RSD_sim(5) # define the model instance and # of domains

# initialize species involved in the reaction
model.molecular_species('I{1}',DNA_con=IN1)
model.molecular_species('I{3}',DNA_con=25)
model.molecular_species('REP{2}',DNA_con=REP_con)

ksd1 = [1e3/1e9,0.5e1/1e9] # 1/nM-s



i = 0

for n in range(len(ksd1)):
      
    model.global_rate_constants(ktxn=k_txn) #globally changes needed rates
    model.molecular_species('I{1}',DNA_con=IN1)
    model.molecular_species('ag{3.1,2}',DNA_con=25,krevA=5/1e9) #changes reverse rate for reaction
    model.molecular_species('g{1,2}',krsdA=ksd1[n]) #changes rate for second gate in reaction
    
    
    # simulate the model (input is simulation time)
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.subplot(2,4,3)
    plt.plot(model.t/60,(S2 / REP_con)*100,color=color1[n],linewidth=2,linestyle='--')


plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,400)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)
plt.legend(['V1 Fast','V1 Slow','V2 Fast','V2 Slow'],frameon=False)
plt.title('Gate{3,2} AND Gate{1,2}')

plt.suptitle('SA22_SIfigure26 Comparison')