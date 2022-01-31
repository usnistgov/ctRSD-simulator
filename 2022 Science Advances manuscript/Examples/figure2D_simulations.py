import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

import sys
sys.path.insert(1,'C:\\Users\\sws5\\OneDrive - National Institute of Standards and Technology (NIST)\\Research\\Code\\General RSD simulator')
import RSD_simulator as RSDs
    

'''
##############################################################################
Simulations
##############################################################################
'''

csl = [[0,0,0.1],
       [0,0,0.4],
       [0,0,0.6],
       [0,0,1],
       [0,0.3,1],
       [0.4,0.4,0.4]]

IN_temp = [50,25,12.5,6.25,2.5,0]

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.013

# model with inputs
model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=500)

fs = 12

plt.subplot(3,5,1)
for n in range(len(IN_temp)):
    
    model.DNA_species('input','I1',temp_con=IN_temp[n])
    
    # simulate the model
    model.simulate(t_sim,1,k_txn)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    plt.rcParams.update({'font.sans-serif':'Verdana'})
    
    plt.plot(model.sol.t/60,(1-REP/model.REP_con[1])*100,color=csl[n],linewidth=1,linestyle='--')

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