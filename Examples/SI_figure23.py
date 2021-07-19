import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
sys.path.insert(1,'C:\\Users\\sws5\\OneDrive - National Institute of Standards and Technology (NIST)\\Research\\Code\\General RSD simulator')
import RSD_simulator as RSDs
    
'''
##############################################################################
Simulations
##############################################################################
'''

'''
1_2r gate
'''

csl =[[0,0,0.5],[0.5,0,0]]

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
    
    plt.subplot(3,5,1)
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl[n],linewidth=1,linestyle='--')

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
model.DNA_species('input','I13',temp_con=25)
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
    
    plt.subplot(3,5,3)
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl[n],linewidth=1,linestyle='--')

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
