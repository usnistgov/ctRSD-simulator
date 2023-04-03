# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 08:47:36 2020

@author: sws5
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt

def txn_cleave_eqs(t,x,temp_con,krz):
    
    k_txn = 0.025 # per second
    
    uRSDg = x[0]
    cRSDg = x[1]
    
    
    duRSDg = k_txn*temp_con - krz*uRSDg
    
    dcRSDg = krz*uRSDg
   
    
    return [duRSDg,dcRSDg]

csl =[[0,0,0.5],
      [0,0,1],
      [0,0.25,1],
      [0,0.5,1],
      [0,0.75,1]]

t_sim1 = np.linspace(0,15/60,1001)*3600 # seconds

#         
krz = [0.5/60,0.35/60,0.25/60,0.15/60,0.1/60] # per s


for n in range(len(krz)):
    
    int_con = [0,0]
    temp_con = 25
    sol1 = spi.solve_ivp(lambda t, x: txn_cleave_eqs(t,x,temp_con,krz[n]),[t_sim1[0],t_sim1[-1]],int_con,t_eval=t_sim1)
    
    t_sim = np.linspace(sol1.t[-1]/3600,1,1001)*3600 # seconds
    int_con = [sol1.y[0][-1],sol1.y[1][-1]]
    temp_con = 0
    
    sol2 = spi.solve_ivp(lambda t, x: txn_cleave_eqs(t,x,temp_con,krz[n]),[t_sim[0],t_sim[-1]],int_con,t_eval=t_sim)

    uRSDg = np.concatenate([sol1.y[0],sol2.y[0]])
    cRSDg = np.concatenate([sol1.y[1],sol2.y[1]])
    time = np.concatenate([sol1.t,sol2.t])
    
    plt.plot(time/60,cRSDg/(uRSDg+cRSDg),color=csl[n],linewidth=2)

plt.ylabel('Fraction cleaved',fontsize=15)
plt.xlabel('time (min)',fontsize=15)
plt.xlim(0,45)
plt.ylim(-0.1,1.1)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=5,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=5,width=1,direction='in',right='on')

