import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

def RSD_eqs(t,x,RSD_temp,IN_temp,F_temp):
    
    # designed rates
    k_txn = 0.013 # per second
    ksd = 1*10**3/10**9 # 1/nM-s
    kfsd = 1*10**3/10**9 # 1/nM-s
    krev = 10**3/10**9 # 1/nM-s
    kf_rep = 10**4/10**9 # 1/nM-s
    kRz = 0.25/60 # 1/s
    
    uRSDg = x[0] # uncleaved folded gate
    RSDg = x[1] # cleaved gate 
    IN = x[2] # I1
    OUT = x[3] # O2
    DRL = x[4] # DNA reporter
    ROL = x[5] # Reacted reporter
    I_RSDg = x[6] # gate:I1 complex
    F = x[7] # fuel strand
    F_RSDg = x[8] # fuel:gate complex
    
    duRSDg = k_txn*RSD_temp- kRz*uRSDg
    
    dRSDg = kRz*uRSDg - ksd*RSDg*IN + krev*I_RSDg*OUT
    
    dIN = k_txn*IN_temp - ksd*RSDg*IN + krev*I_RSDg*OUT + kfsd*I_RSDg*F
    
    dOUT = ksd*RSDg*IN - kf_rep*OUT*DRL - krev*I_RSDg*OUT
    
    dDRL = - kf_rep*OUT*DRL
    
    dROL = kf_rep*OUT*DRL
    
    dI_RSDg = ksd*RSDg*IN - krev*I_RSDg*OUT - kfsd*I_RSDg*F
    
    dF = k_txn*F_temp - kfsd*I_RSDg*F + ksd*F_RSDg*IN
    
    dF_RSDg = kfsd*I_RSDg*F - ksd*F_RSDg*IN
    
    
    return [duRSDg,dRSDg,dIN,dOUT,dDRL,dROL,dI_RSDg,dF,dF_RSDg]

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

t_sim = np.linspace(0,6,1001)*3600 # seconds

int_con = [0,0,0,0,500,0,0,0,0]
RSD_temp = 25
IN_temp = [50,25,12.5,6.25,2.5,0]
# esp = np.linspace(0,1,len(IN_temp)+1)
# csl = [cm.winter(x) for x in esp]

fs = 12 

plt.subplot(3,5,1)

for n in range(len(IN_temp)):
    F_temp = 0
    
    sol = spi.solve_ivp(lambda t, x: RSD_eqs(t,x,RSD_temp,IN_temp[n],F_temp),[t_sim[0],t_sim[-1]],int_con,t_eval=t_sim)
    
    RSDg = sol.y[1]
    IN = sol.y[2]
    OUT = sol.y[3]
    DRL = sol.y[4]
    ROL = sol.y[5]
    I_RSDg = sol.y[6]
    F = sol.y[7]
    F_RSDg = sol.y[8]
    
    
    plt.plot(sol.t/60,ROL/int_con[4]*100,color=csl[n],linewidth=1,linestyle='--')

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