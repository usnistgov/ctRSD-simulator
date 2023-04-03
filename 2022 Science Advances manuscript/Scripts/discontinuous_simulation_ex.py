import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
sys.path.insert(1,'C:\\Users\\sws5\\OneDrive - National Institute of Standards and Technology (NIST)\\Research\\Code\\General RSD simulator')
#import RSD_simulator_mb_corr as RSDs
import RSD_simulator as RSDs
    
'''
##############################################################################
Simulations
In this example, the 1_2 gate is initially transcribed for an hour in the
absence of the I1 template. After the first hour, the I1 template is added and
the reaction is resumed for another 3 hours
##############################################################################
'''

csl = [[0.25,0,0.25],
       [0.5,0,0.5],
       [0.8,0,0.8],
       [0,0,1],
       [1,0.5,0],
       [1,0,0],
       [0.5,0,0]]

REP_con = 500

k_txn = 0.01

    
t_sim = np.linspace(0,1,1001)*3600 # seconds

# model with inputs
model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations

model.DNA_species('gate','1_2',temp_con=25)
model.DNA_species('reporter','REP2',temp_con=REP_con)

# simulate the model (before addition of the input template)
model.simulate(t_sim,1,k_txn)

# updating the simulation time for the second phase of the simulation
t_sim2 = np.linspace(t_sim[-1]/3600,4,1001)*3600 # seconds

# adding the I1 template to the model
model.DNA_species('input','I1',temp_con=25)

# simulate the model (after addition of the input template)
model.simulate(t_sim2,2,k_txn)

# pulling out the reporter concentration for plotting
REP = model.output_concentration['REP2']

fs = 12
plt.subplot(3,5,1)
plt.plot(model.sol.t/60,(1-REP/REP_con)*100,color=[0,0,1],linewidth=1,linestyle='--')
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,240)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
#ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('Reacted reporter (%)',fontsize=fs)