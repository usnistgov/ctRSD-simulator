import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
sys.path.insert(1,'C:\\Users\\sws5\\OneDrive - National Institute of Standards and Technology (NIST)\\Research\\Code\\General RSD simulator')
import RSD_simulator as RSDs
    
fs = 12

csl = [[0.6,0.6,0.6],  # Io
       [1,0.5,0],      # I3
       [147/255,42/255,255/255],  # I4
       [0,0.75,0.9],  # I5
       [1,0.5,1],      # I3/I4
       [0,0.9,0.9],  # I3/I5
       [0,0,0.5],      # I4/I5
       [0,0,1]]        # I3/I4/I5

'''
##############################################################################
Simulations
##############################################################################
'''

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.01

IN3 = [0,25, 0, 0,25,25, 0,25]
IN4 = [0, 0,25, 0,25, 0,25,25]
IN5 = [0, 0, 0,25, 0,25,25,25]

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','4_1',temp_con=25)
model.DNA_species('gate','5_1',temp_con=25)
model.DNA_species('gate','3&1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)


for n in range(len(IN3)):
    model.DNA_species('input','I3',temp_con=IN3[n])
    model.DNA_species('input','I4',temp_con=IN4[n])
    model.DNA_species('input','I5',temp_con=IN5[n])
    
    # simulate the model
    model.simulate(t_sim,1,k_txn)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.subplot(3,5,1)
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl[n],linewidth=1,linestyle='--')

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