# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:20:54 2022

@author: tnm12
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import Simulator1 as RSDs #import first version of simulator
    
'''
##############################################################################
Simulations
##############################################################################
'''

cslr = [[0.1,0,0],
       [0.4,0,0],
       [0.6,0,0],
       [1,0,0],
       [1,0.3,0],
       [1,0.5,0],
       [1,0.75,0]]

cslrb = [[1,0.75,0],[1,0.5,0],[1,0.3,0],[1,0,0], [0.6,0,0],[0.4,0,0],[0.1,0,0]]

cslb = [[0,0,0.1],
       [0,0,0.4],
       [0,0,0.6],
       [0,0,1],
       [0,0.3,1],
       [0,0.5,1],
       [0,0.75,1]]


IN_temp = 50

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.01

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

X = [0,1,5,10,25,50,100] # fold increase of reverse reaction rate

'''
Panel A
'''

# model with inputs
model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)
model.DNA_species('input','I1',temp_con=IN_temp)

plt.subplot(3,5,2)
for n in range(len(X)):
    rte=[[k_txn],[ksd],[kfsd],[X[n]*krev,X[n]*5/1e9,X[n]*krev,X[n]*krev,X[n]*krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]
        
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=cslb[n],linewidth=1,linestyle='-')

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

'''
Panel B
'''

# model with inputs
model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','3_1',temp_con=25)
model.DNA_species('reporter','REP1',temp_con=500)
model.DNA_species('input','I3',temp_con=IN_temp)

plt.subplot(3,5,4)
for n in range(len(X)):
    rte=[[k_txn],[ksd],[kfsd],[X[n]*krev,X[n]*5/1e9,X[n]*krev,X[n]*krev,X[n]*krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]
        
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP1']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[0])*100,color=cslr[n],linewidth=1,linestyle='-')

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

'''
Panel C, left
'''

# model with inputs
model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','3_1',temp_con=25)
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)
model.DNA_species('input','I3',temp_con=IN_temp)

plt.subplot(3,5,11)
for n in range(len(X)):
    rte=[[k_txn],[ksd],[kfsd],[X[n]*krev,X[n]*5/1e9,X[n]*krev,X[n]*krev,X[n]*krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]
        
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=cslb[n],linewidth=1,linestyle='-')

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

'''
Panel C, middle
'''

# model with inputs
model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','4_3',temp_con=25)
model.DNA_species('gate','3_1',temp_con=25)
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)
model.DNA_species('input','I4',temp_con=IN_temp)

plt.subplot(3,5,13)
for n in range(len(X)):
    rte=[[k_txn],[ksd],[kfsd],[X[n]*krev,X[n]*5/1e9,X[n]*krev,X[n]*krev,X[n]*krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]
        
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=cslb[n],linewidth=1,linestyle='-')

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

'''
Panel C, right
'''

# model with inputs
model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','5_4',temp_con=25)
model.DNA_species('gate','4_3',temp_con=25)
model.DNA_species('gate','3_1',temp_con=25)
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)
model.DNA_species('input','I5',temp_con=IN_temp)

plt.subplot(3,5,15)
for n in range(len(X)):
    rte=[[k_txn],[ksd],[kfsd],[X[n]*krev,X[n]*5/1e9,X[n]*krev,X[n]*krev,X[n]*krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]
        
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=cslb[n],linewidth=1,linestyle='-')

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

'''
Panel A
'''

# model with inputs
model = RSDs.RSD_sim(5) # define the model instance

# initialize species involvded in the reaction
model.molecular_species('REP{2}',DNA_con=REP_con)
model.molecular_species('I{1}',DNA_con=IN_temp)

plt.subplot(3,5,2)
for n in range(len(X)):
    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n])
    model.molecular_species('g{1,2}',DNA_con=25,krev=(5/1e9)*X[n]) #looping through fold increase of reverse rate
    
    
    # simulate the model
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=cslr[n],linewidth=1,linestyle='--')

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
model = RSDs.RSD_sim(5) # define the model instance

# specify DNA txn templates and reporters and concentrations
model.molecular_species('REP{1}',DNA_con=REP_con)
model.molecular_species('I{3}',DNA_con=IN_temp)
model.molecular_species('gate{3,1}',DNA_con=25)

plt.subplot(3,5,4)
for n in range(len(X)):
    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n]) 

    
    # simulate the model
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S1 = model.output_concentration('S{1}')
    
    fs = 12
    
    plt.plot(model.t/60,(S1/REP_con)*100,color=cslb[n],linewidth=1,linestyle='--')

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
model = RSDs.RSD_sim(5) # define the model instance

# specify DNA txn templates and reporters and concentrations
model.molecular_species('gate{3,1}',DNA_con=25)
model.molecular_species('REP{2}',DNA_con=REP_con)
model.molecular_species('I{3}',DNA_con=IN_temp)

plt.subplot(3,5,11)
for n in range(len(X)):
   
    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n])
    model.molecular_species('gate{1,2}',DNA_con=25,krev=(5/1e9)*X[n])
    
    # simulate the model
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=cslrb[n],linewidth=1,linestyle='--')

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
model = RSDs.RSD_sim(5) # define the model instance

# specify DNA txn templates and reporters and concentrations
model.molecular_species('gate{4,3}',DNA_con=25)
model.molecular_species('gate{3,1}',DNA_con=25)
model.molecular_species('REP{2}',DNA_con=500)
model.molecular_species('I{4}',DNA_con=IN_temp)

plt.subplot(3,5,13)
for n in range(len(X)):
    
    
    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n])
    model.molecular_species('gate{1,2}',DNA_con=25,krev=(5/1e9)*X[n])
    
    # simulate the model
    model.simulate(t_sim)
    
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=cslrb[n],linewidth=1,linestyle='--')

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
model = RSDs.RSD_sim(5) # define the model instance

# specify DNA txn templates and reporters and concentrations
model.molecular_species('gate{5,4}',DNA_con=25)
model.molecular_species('gate{4,3}',DNA_con=25)
model.molecular_species('gate{3,1}',DNA_con=25)
model.molecular_species('REP{2}',DNA_con=REP_con)
model.molecular_species('I{5}',DNA_con=IN_temp)

plt.subplot(3,5,15)
for n in range(len(X)):

    model.global_rate_constants(ktxn=k_txn,krev=(270/1e9)*X[n])
    model.molecular_species('gate{1,2}',DNA_con=25,krev=(5/1e9)*X[n])    
    
    # simulate the model
    model.simulate(t_sim)
    
    # pull out the species from the model solution to plot
    S2 = model.output_concentration('S{2}')
    
    fs = 12
    
    plt.plot(model.t/60,(S2/REP_con)*100,color=cslrb[n],linewidth=1,linestyle='--')

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


plt.suptitle('SA22_SI_figure19 Comparison')