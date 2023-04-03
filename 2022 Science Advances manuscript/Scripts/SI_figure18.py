import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
sys.path.insert(1,'C:\\Users\\sws5\\OneDrive - National Institute of Standards and Technology (NIST)\\Research\\Code\\General RSD simulator')
import RSD_simulator as RSDs

'''
##############################################################################
Simulations (xRz reactions)
##############################################################################
'''

'''
Fast reverse reaction with xRz  gate
'''

ksd = 1e3/1e9 # 1/nM-s
kfsd = 1e3/1e9 # 1/nM-s
krev = 270/1e9 # 1/nM-s
kf_rep = 1e4/1e9 # 1/nM-s
kr_rep = 0*1e2/1e9 # 1/nM-s
kf_wta = 1e5/1e9 # 1/nM-s
kr_wta = 0.4 # 1/s
kRz = 0.25/60 # 1/s
kth = 1e5/1e9 # 1/nM-s
kd = 0

k_txn = 0.015

rte=[[k_txn],[ksd,ksd,ksd,ksd,ksd],[kfsd],[krev,5/1e9*2e5,krev,krev,krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]

t_sim = np.linspace(0,6,1001)*3600 # seconds

IN = [0,25]

csl1 = [[0.2,0.2,0.2],
       [0,0,0.5]]

csl2 = [[0.2,0.2,0.2],
       [0.5,0,0]]

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)

plt.subplot(3,5,1)
for n in range(len(IN)):
    model.DNA_species('input','I1',temp_con=IN[n])
    
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl2[n],linewidth=1,linestyle='--')

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
    
'''
Slow forward reaction with xRz gate
'''
    
ksd = 1e1/1e9 # 1/nM-s
kfsd = 1e3/1e9 # 1/nM-s
krev = 270/1e9 # 1/nM-s
kf_rep = 1e4/1e9 # 1/nM-s
kr_rep = 0*1e2/1e9 # 1/nM-s
kf_wta = 1e5/1e9 # 1/nM-s
kr_wta = 0.4 # 1/s
kRz = 0.25/60 # 1/s
kth = 1e5/1e9 # 1/nM-s
kd = 0

k_txn = 0.015

rte=[[k_txn],[ksd,ksd,ksd,ksd,ksd],[kfsd],[krev,5/1e9,krev,krev,krev],[kf_rep],[kr_rep],[kf_wta],[kr_wta],[kRz],[kth],[kd]]

t_sim = np.linspace(0,6,1001)*3600 # seconds

IN = [0,25]

csl1 = [[0.2,0.2,0.2],
       [0,0,0.5]]

csl2 = [[0.2,0.2,0.2],
       [0.5,0,0]]

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)

plt.subplot(3,5,1)
for n in range(len(IN)):
    model.DNA_species('input','I1',temp_con=IN[n])
    
    # simulate the model
    model.simulate(t_sim,1,k_txn,rate_constants=rte)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl2[n],linewidth=1,linestyle=':')
    
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