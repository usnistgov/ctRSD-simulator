import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import sys
sys.path.insert(1,'C:\\Users\\sws5\\OneDrive - National Institute of Standards and Technology (NIST)\\Research\\Code\\General RSD simulator')
import RSD_simulator as RSDs

fs = 12

csl = [[255/255,170/255,170/255],  # Io
       [1,0,0],      # I3
       [170/255,238/255,255/255],  
       [0/255,170/255,212/255],       
       [204/255,170/255,255/255],
       [147/255,42/255,255/255], 
       [255/255,204/255,170/255],      
       [1,0.5,0]]      


csl2 = [[255/255,170/255,170/255],
       [0.5,0,0],      
       [170/255,238/255,255/255],  
       [0/255,125/255,150/255],       
       [204/255,170/255,255/255],
       [100/255,42/255,150/255], 
       [255/255,204/255,170/255],      
       [1,0.25,0]]      


'''
##############################################################################
Simulations
##############################################################################
'''

t_sim = np.linspace(0,6,1001)*3600 # seconds

k_txn = 0.0075

model = RSDs.RSD_sim() # define the model instance

# specify DNA txn templates and reporters and concentrations
model.DNA_species('gate','1_2',temp_con=25) # thresholding gate

model.DNA_species('reporter','REP2',temp_con=500)

IN1 = [0,50,0,0,0,0,0,0]
IN4 = [0,0,0,0,0,50,0,0]
IN5 = [0,0,0,50,0,0,0,0]
IN3 = [0,0,0,0,0,0,0,50]

i = 0

plt.subplot(3,5,1)
for n in range(len(IN1)):
    
    model.DNA_species('input','I1',temp_con=IN1[n])
    model.DNA_species('input','I4',temp_con=IN4[n])
    model.DNA_species('input','I5',temp_con=IN5[n])
    model.DNA_species('input','I3',temp_con=IN3[n])
    if n > 1:
        model.DNA_species('gate','5_1',temp_con=25) # output gate
    if n > 3:
        model.DNA_species('gate','4_5',temp_con=25) # output gate
    if n > 5: 
        model.DNA_species('gate','3_4',temp_con=25) # output gate
    
    
    # simulate the model
    model.simulate(t_sim,1,k_txn)
    #model.simulate(t_sim,1,k_txn)
    
    # pull out the species from the model solution to plot
    REP = model.output_concentration['REP2']
    
    fs = 12
    
    plt.plot(model.sol.t/60,100*(1-REP/model.REP_con[1]),color=csl2[n],linewidth=1,linestyle='--')

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