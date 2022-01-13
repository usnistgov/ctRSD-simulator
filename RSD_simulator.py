# -*- coding: utf-8 -*-
"""
###############################################################################
Things that need added:
    - Fueling the output of an AND gate
    - Fan-out is not supported in current implementation 
    
###############################################################################
General notes on how this simulator works
- RSD gates are defined by their inputs
- Leak is modeled as straight transcription of output from each gate at a much slower rate than designed transcription
"""

import numpy as np
import scipy.integrate as spi
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import re

'''
###############################################################################
Helper functions
###############################################################################
'''

# function to assemble connectivity matrices
def con_vec2mat(con_vec,ortho_nodes,ind_nodes):
    '''
    This function converts connectivity vectors into connectivity matrices
    '''
    con_mat = np.zeros([ortho_nodes,ind_nodes], dtype = int)
    
    for n in range(len(con_vec)):
        if con_vec[n] != 0:
            con_mat[con_vec[n]-1,n] = 1
    
    return con_mat

# equations for RNA strand displacement cascades
def RSD_eqs(t,x,IN_con,RSD_con,RSD_conA,F_con,WTA_con,TH_con,OUT_con,rsd_mat,rsd_matA1,rsd_matA2,rsd_matAL,wta_mat,k_txn,ksd,kfsd,krev,kf_rep,kr_rep,kf_wta,kr_wta,kRz,kth,kd,REP_tot,leak,leakA):
    
    # # designed reaction parameters
    # ksd = 1*10**3/10**9 # 1/nM-s
    # kfsd = 1*10**3/10**9 # 1/nM-s
    # krev = 10**4/10**9 # 1/nM-s
    # kf_rep = 10**3/10**9 # 1/nM-s
    # kr_rep = 0*10**2/10**9 # 1/nM-s
    # kf_wta = 10**6/10**9 # 1/nM-s
    # kr_wta = 0.4 # 1/s
    # kRz = 0.25/60 # 1/s
                
    # leak reaction parameters
    k_txnL = leak*k_txn # per second (for single gates)
    k_txnLA = leakA*k_txn # per second (for AND gates)
    
    # converting lists to numpy arrays for linear algebra
    IN_con = np.array(IN_con)
    RSD_con = np.array(RSD_con)
    RSD_conA = np.array(RSD_conA)
    F_con = np.array(F_con)
    WTA_con = np.array(WTA_con)
    
    # Normalization factor for OR gates
    #tot = rsd_mat.T@(rsd_mat@(RSD_con*IN_con))
    normf = np.ones(len(RSD_con)) # a since remove normalization factor
    # for n in range(len(RSD_con)):
    #     if tot[n] != 0:
    #         normf[n] = (RSD_con[n]*IN_con[n])/tot[n]
     
    k = len(IN_con)
    
    # designed products
    IN = x[0:k] # inputs
    RSDg = x[k:2*k] # single RSD gates
    OUT = x[2*k:3*k] # outputs
    REP = x[3*k:4*k] # reporters
    RSDgA1 = x[4*k:5*k] # 1st AND gate input / output
    RSDgA2 = x[5*k:6*k] # 2nd AND gate input / output
    I_RSDg = x[6*k:7*k] # IN bound to RSD gate
    F = x[7*k:8*k] # fuel strands
    F_RSDg = x[8*k:9*k] # fuel bound to RSD gates
    uRSDg = x[9*k:10*k] # uncleaved RSD gates
    uRSDgA = x[10*k:11*k] # uncleaved AND RSD gates
    uWTA = x[11*k:12*k] # uncleaved WTA gates 
    WTA = x[12*k:13*k] # cleaved WTA gates 
    WTA1 = x[13*k:14*k] # WTA gate bound to one input
    WTA2 = x[14*k:15*k] # WTA gate bound to the other input
    uTH = x[15*k:16*k] # uncleaved threshold gates
    TH = x[16*k:17*k] # cleaved threshold gates
    O_RSDg = x[17*k:18*k] # output bound to gate
    I_RSDgA = x[18*k:19*k] # input bound to AND gate
    O_RSDgA = x[19*k:20*k] # output bound to AND gate
    
    # # Normalization factor for OR gates (ratio of OUT rates...)
    # tot = rsd_mat.T@(rsd_mat@(RSD_con*IN_con))
    # normf = np.ones(len(RSD_con))
    # ratef = np.zeros(len(RSD_con))
    # for n in range(len(RSD_con)):
    #     if tot[n] != 0:
    #         #normf[n] = (RSD_con[n]*IN_con[n])/tot[n]
    #         ratef[n]=ksd[n]*IN[n]*RSDg[n] # rate of output production
    # for n in range(len(RSD_con)):
    #     if tot[n] != 0:
    #         if sum(ratef) == 0:
    #               normf[n] = 1
    #         else:
    #             normf[n] = ratef[n]/sum(ratef)
    
    '''
    ###########################################################################
    # ODEs
    ###########################################################################
    '''
    dIN = k_txn*IN_con - ksd*RSDg*IN - ksd*RSDgA1*IN - ksd*RSDgA2*IN + kfsd*I_RSDg*F - ksd*F_RSDg*IN - kth*TH*IN + (rsd_mat.T@(krev*OUT))*I_RSDg*normf + (rsd_matA2.T@(krev*OUT))*I_RSDgA - kd*IN
    
    dRSDg = kRz*uRSDg - ksd*RSDg*IN - ksd*RSDg*OUT + (rsd_mat.T@(krev*OUT))*I_RSDg*normf + (rsd_mat.T@(krev*OUT))*O_RSDg*normf - kd*RSDg
    
    dOUT = k_txn*OUT_con + ksd*rsd_mat@(RSDg*IN) + ksd*rsd_mat@(RSDg*OUT) - ksd*RSDg*OUT + ksd*rsd_matA2@(RSDgA2*IN) + ksd*rsd_matA2@(RSDgA2*OUT) - ksd*RSDgA2*OUT - kf_rep*OUT*REP \
           + k_txnL*rsd_mat@RSD_con + k_txnLA*rsd_matAL@RSD_conA + kr_rep*(REP_tot-REP)*(REP_tot-REP) \
           - kf_wta*WTA*OUT - kf_wta*(wta_mat@WTA)*OUT - kf_wta*WTA1*OUT - kf_wta*WTA2*OUT + kr_wta*wta_mat.T@WTA1 + kr_wta*wta_mat@WTA2 \
           - kth*TH*OUT - krev*(rsd_mat@(I_RSDg*normf))*OUT - krev*(rsd_mat@(O_RSDg*normf))*OUT + (rsd_mat.T@(krev*OUT))*O_RSDg*normf - kd*OUT \
           - krev*(rsd_matA2@I_RSDgA)*OUT - krev*(rsd_matA2@O_RSDgA)*OUT + (rsd_matA2.T@(krev*OUT))*O_RSDgA + kfsd*O_RSDg*F - ksd*F_RSDg*OUT  
    
    dREP = - kf_rep*OUT*REP - kf_rep*IN*REP + kr_rep*(REP_tot-REP)*(REP_tot-REP) + kd*(REP_tot-REP)
    
    dRSDgA1 = kRz*uRSDgA - ksd*RSDgA1*IN - ksd*RSDgA1*OUT - kd*RSDgA1
    
    dRSDgA2 = ksd*rsd_matA1@(RSDgA1*IN) + ksd*rsd_matA1@(RSDgA1*OUT) - ksd*RSDgA2*IN - ksd*RSDgA2*OUT - kd*RSDgA2 \
              + (rsd_matA2.T@(krev*OUT))*I_RSDgA + (rsd_matA2.T@(krev*OUT))*O_RSDgA
    
    dI_RSDg = ksd*RSDg*IN - kfsd*I_RSDg*F + ksd*F_RSDg*IN - (rsd_mat.T@(krev*OUT))*I_RSDg*normf - kd*I_RSDg
    
    dF = k_txn*F_con - kfsd*I_RSDg*F + ksd*F_RSDg*IN - kfsd*O_RSDg*F + ksd*F_RSDg*OUT - kd*F
    
    dF_RSDg = kfsd*I_RSDg*F - ksd*F_RSDg*IN + kfsd*O_RSDg*F - ksd*F_RSDg*OUT - kd*F_RSDg
    
    duRSDg = k_txn*RSD_con - kRz*uRSDg - kd*uRSDg
    
    duRSDgA = k_txn*RSD_conA - kRz*uRSDgA - kd*uRSDgA
    
    duWTA = k_txn*WTA_con - kRz*uWTA - kd*uWTA
    
    dWTA = kRz*uWTA - kf_wta*WTA*OUT - wta_mat.T@(kf_wta*OUT)*WTA - wta_mat.T@(kf_wta*WTA1*OUT) - kf_wta*WTA2*OUT + kr_wta*wta_mat.T@WTA1 + kr_wta*WTA2 - kd*WTA
    
    dWTA1 = wta_mat@(kf_wta*WTA*OUT) - kf_wta*WTA1*OUT - kr_wta*WTA1 - kd*WTA1
    
    dWTA2 = wta_mat.T@(kf_wta*OUT)*WTA - kf_wta*WTA2*OUT - kr_wta*WTA2 - kd*WTA2
    
    duTH = k_txn*TH_con - kRz*uTH - kd*uTH
    
    dTH = kRz*uTH - kth*TH*IN - kth*TH*OUT - kd*TH
    
    dO_RSDg = ksd*RSDg*OUT - kfsd*O_RSDg*F + ksd*F_RSDg*OUT - (rsd_mat.T@(krev*OUT))*O_RSDg*normf - kd*O_RSDg
    
    dI_RSDgA = ksd*RSDgA2*IN - (rsd_matA2.T@(krev*OUT))*I_RSDgA - kd*I_RSDgA
    
    dO_RSDgA = ksd*RSDgA2*OUT - (rsd_matA2.T@(krev*OUT))*O_RSDgA - kd*O_RSDgA
    
    return np.concatenate([dIN,dRSDg,dOUT,dREP,dRSDgA1,dRSDgA2,dI_RSDg,dF,dF_RSDg,duRSDg,duRSDgA,duWTA,dWTA,dWTA1,dWTA2,duTH,dTH,dO_RSDg,dI_RSDgA,dO_RSDgA])

'''
###############################################################################
RSD_sim CLASS DEFINITION
###############################################################################
'''
class RSD_sim:
    def __init__(self,domains=5):
        
        self.k = domains
        # DNA template concentration vectors
        self.IN_con = domains*[0] # Inputs
        
        self.RSD_con = domains*[0] # single RNA gates
        self.RSD_conA = domains*[0] # AND gates
        self.F_con = domains*[0] # fuel strands
        self.WTA_con = domains*[0] # WTA gates
        self.TH_con = domains*[0] # threshold gates
        self.OUT_con = domains*[0] # Outputs
        
        # Initial species concentration vectors
        self.in_ic = domains*[0] # Inputs
        self.rsd_ic = domains*[0] # single RNA gates
        self.rsdA_ic = domains*[0] # AND gates
        self.REP_con = domains*[0] # reporters
        self.f_ic = domains*[0] # fuel strands
        self.wta_ic = domains*[0] # WTA strands
        self.th_ic = domains*[0] # threshold gates
        self.out_ic = domains*[0] # Outputs
        
        # Circuit connectivity vectors 
        self.rsd_vec = domains*[0] # single gates
        self.rsd_vecA1 = domains*[0] # AND gates first input
        self.rsd_vecA2 = domains*[0] # AND gates second inputs
        self.wta_vec = domains*[0] # WTA gates
        
        self.rsd_mat = np.zeros([domains,domains], dtype = int)
        self.rsd_matA1 = np.zeros([domains,domains], dtype = int)
        self.rsd_matA2 = np.zeros([domains,domains], dtype = int)
        self.rsd_matAL = np.zeros([domains,domains], dtype = int)
        self.wta_mat = np.zeros([domains,domains], dtype = int)
        
    # function for defining the DNA species in the model instance and the circuit connectivity
    def DNA_species(self,comp,name,temp_con=0,ic=0):
        
        if comp.lower() == 'input' or comp.lower() == 'inputs':
            if 'n' not in name.lower():
                iep = name.lower().rfind('i')
            else:
                iep = name.lower().rfind('n') # this is hard coded here... should make it more general for any letter (I1 vs IN1 for example)
                
            self.IN_con[int(name[iep+1:])-1]=temp_con
            self.in_ic[int(name[iep+1:])-1]=ic
            
        if comp.lower() == 'fuel' or comp.lower() == 'fuels':
            fep = name.lower().rfind('f')
            self.F_con[int(name[fep+1:])-1]=temp_con
            self.f_ic[int(name[fep+1:])-1]=ic
            # Error message
            if sum(self.rsd_matA2[:,int(name[fep+1:])-1]) != 0:
                # Fuel with the AND gate
                print('WARNING: Fuel reactions are not included for AND gates')
            
        if comp.lower() == 'reporter' or comp.lower() == 'reporters':
            rep = name.lower().rfind('p')
            self.REP_con[int(name[rep+1:])-1]=temp_con
            
        if comp.lower() == 'threshold' or comp.lower() == 'thresholds':
            tep = name.lower().rfind('h')
            self.TH_con[int(name[tep+1:])-1]=temp_con
            self.th_ic[int(name[tep+1:])-1]=ic
            
        if comp.lower() == 'output' or comp.lower() == 'outputs':
            oep = name.lower().rfind('t')
            self.OUT_con[int(name[oep+1:])-1]=temp_con
            self.out_ic[int(name[oep+1:])-1]=ic
        
        if comp.lower() == 'gate' or comp.lower() == 'gates':
            if '|' not in name and '&' not in name and 'wta' not in name.lower():
                # this is just a single RSD gate
                
                
                # Define the concentration of the gate (defined by the input domain)
                gep = name.rfind('_')
                self.RSD_con[int(name[0:gep])-1]=temp_con
                self.rsd_mat[int(name[gep+1:])-1,int(name[0:gep])-1] = 1
                
                self.rsd_ic[int(name[0:gep])-1]=ic
                
                # Error message
                if sum(self.rsd_mat[int(name[gep+1:])-1,:]) > 1:
                    # Fan-in (OR) gate
                    print('WARNING: Fan-in (OR) circuits overestimate reverse rates')
                    
                # Error message
                if sum(self.rsd_mat[:,int(name[0:gep])-1]) > 1:
                    # Attempted Fan-out circuit
                    print('WARNING: Fan-out circuits will use the concentration of the last gate defined')
                
                # # Define the connectivity vector and matrix
                # self.rsd_vec[int(name[0])-1] = int(name[-1])
                
                # self.wta_mat = con_vec2mat(self.wta_vec,self.k,self.k)
                # # filling in zero matrices for AND gates if not defined with other calls
                # self.rsd_matA1 = con_vec2mat(self.rsd_vecA1,self.k,self.k)
                # self.rsd_matA2 = con_vec2mat(self.rsd_vecA2,self.k,self.k)
                
                # Determining AND gate leak product from the A1 and A2 vectors
                self.rsd_vecAL = len(self.rsd_vecA1)*[0]
                for i in range(len(self.rsd_vecA1)):
                    if self.rsd_vecA1[i] != 0:
                        self.rsd_vecAL[i] = self.rsd_vecA2[self.rsd_vecA1[i]-1]
                
                self.rsd_matAL = con_vec2mat(self.rsd_vecAL,self.k,self.k)
                
            if '|' in name:
                # this is an OR gate (two RSD gates)   
                
                gep1 = name.rfind('|')
                gep2 = name.rfind('_')
            
                # Define the concentration of the gate (defined by the input domain)
                self.RSD_con[int(name[0:gep1])-1]=temp_con
                self.RSD_con[int(name[gep1+1:gep2])-1]=temp_con
                
                self.rsd_ic[int(name[0:gep1])-1]=ic
                self.rsd_ic[int(name[gep1+1:gep2])-1]=ic
                '''
                TO DO: add the ability to specify different OR gate concentrations
                '''
                self.rsd_mat[int(name[gep2+1:])-1,int(name[0:gep1])-1] = 1
                self.rsd_mat[int(name[gep2+1:])-1,int(name[gep1+1:gep2])-1] = 1
                # # Define the connectivity vectors and matrices
                # self.rsd_vec[int(name[0])-1] = int(name[-1])
                # self.rsd_vec[int(name[2])-1] = int(name[-1])
                # self.rsd_mat = con_vec2mat(self.rsd_vec,self.k,self.k)
                # self.wta_mat = con_vec2mat(self.wta_vec,self.k,self.k)
                # # filling in zero matrices for AND gates if not defined from other calls
                # self.rsd_matA1 = con_vec2mat(self.rsd_vecA1,self.k,self.k)
                # self.rsd_matA2 = con_vec2mat(self.rsd_vecA2,self.k,self.k)
                
                # Determining AND gate leak product from the A1 and A2 vectors
                self.rsd_vecAL = len(self.rsd_vecA1)*[0]
                for i in range(len(self.rsd_vecA1)):
                    if self.rsd_vecA1[i] != 0:
                        self.rsd_vecAL[i] = self.rsd_vecA2[self.rsd_vecA1[i]-1]
                
                self.rsd_matAL = con_vec2mat(self.rsd_vecAL,self.k,self.k)
                
            if '&' in name:
                # this is an AND gate (two RSD gates)   
                
                gep1 = name.rfind('&')
                gep2 = name.rfind('_')
            
                # Define the concentration of the gate (defined by the first input domain)
                self.RSD_conA[int(name[0:gep1])-1]=temp_con
                self.rsdA_ic[int(name[0:gep1])-1]=ic

                self.rsd_matA1[int(name[gep1+1:gep2])-1,int(name[0:gep1])-1] = 1
                self.rsd_matA2[int(name[gep2+1:])-1,int(name[gep1+1:gep2])-1] = 1
                
                # # Define the connectivity vectors and matrices
                self.rsd_vecA1[int(name[0:gep1])-1] = int(name[gep1+1:gep2])
                self.rsd_vecA2[int(name[gep1+1:gep2])-1] = int(name[gep2+1:])
                # self.rsd_matA1 = con_vec2mat(self.rsd_vecA1,self.k,self.k)
                # self.rsd_matA2 = con_vec2mat(self.rsd_vecA2,self.k,self.k)
                # filling in a zero matrices for single gates if not defined elsewhere
                # self.rsd_mat = con_vec2mat(self.rsd_vec,self.k,self.k)
                # self.wta_mat = con_vec2mat(self.wta_vec,self.k,self.k)
                
                # self.rsd_matAL[]
                
                # Error message
                if self.F_con[int(name[gep1+1:gep2])-1] != 0:
                    # Fuel with the AND gate
                    print('WARNING: Fuel reactions are not included for AND gates')
                
                # Determining AND gate leak product from the A1 and A2 vectors
                self.rsd_vecAL = len(self.rsd_vecA1)*[0]
                for i in range(len(self.rsd_vecA1)):
                    if self.rsd_vecA1[i] != 0:
                        self.rsd_vecAL[i] = self.rsd_vecA2[self.rsd_vecA1[i]-1]
                
                self.rsd_matAL = con_vec2mat(self.rsd_vecAL,self.k,self.k)
                
            if 'wta' in name.lower():
                # this is a winner-take-all (WTA) gate
                
                wep = name.rfind('_')
                wep2 = name.lower().rfind('w')
                # Define the concentration of the gate (defined by the first input domain)
                self.WTA_con[int(name[0:wep])-1]=temp_con
                self.wta_ic[int(name[0:wep])-1]=ic

                # # Define the connectivity vectors and matrices
                # self.wta_vec[int(name[0])-1] = int(name[2])
                self.wta_mat[int(name[wep+1:wep2-1])-1,int(name[0:wep])-1] = 1
                
                # Determining AND gate leak product from the A1 and A2 vectors
                self.rsd_vecAL = len(self.rsd_vecA1)*[0]
                for i in range(len(self.rsd_vecA1)):
                    if self.rsd_vecA1[i] != 0:
                        self.rsd_vecAL[i] = self.rsd_vecA2[self.rsd_vecA1[i]-1]
                
                self.rsd_matAL = con_vec2mat(self.rsd_vecAL,self.k,self.k)
                
    # function for simulating the model instance
    def simulate(self,t_vec,iteration,k_txn,rate_constants=[],leak=0.03,leakA=0.06):
        
        if len(rate_constants) == 0:
            # defining the rate constants (not sure the best place to put these?)
            self.k_txn = k_txn*np.ones(self.k) # txn rates
            self.ksd = 1e3*np.ones(self.k)/1e9 # forward RNA strand displacement rates
            self.kfsd = 1e3*np.ones(self.k)/1e9 # Fuel strand displacement rates
            self.krev = 270*np.ones(self.k)/1e9 # reverse RNA strand displacement rates
            self.krev[1] = 5/1e9 # reverse RNA strand displacement rates (for domain b the reverse reaction is negligible)
            self.kf_rep = 1e4*np.ones(self.k)/1e9 # forward DNA reporter rates
            self.kr_rep= 0e2*np.ones(self.k)/1e9 # reverse DNA reporter rates
            self.kf_wta = 1e6*np.ones(self.k)/1e9 # WTA forward rates
            self.kr_wta = 0.4*np.ones(self.k) # WTA reverse rates
            self.kRz = 0.25/60*np.ones(self.k) # ribozyme cleavage rates
            self.kth = 1e5*np.ones(self.k)/1e9 # forward thresholding reaction
            self.kd = 0/60*np.ones(self.k) # degradation rates
            
        elif len(rate_constants) != 0:
            
            # defining the rate constants
            if isinstance(rate_constants[0],list) and len(rate_constants[0])>1:
                self.k_txn = np.array(rate_constants[0])
            else:
                self.k_txn = rate_constants[0]*np.ones(self.k) 
            if isinstance(rate_constants[1],list) and len(rate_constants[1])>1:
                self.ksd = np.array(rate_constants[1])
            else:
                self.ksd = rate_constants[1]*np.ones(self.k) 
            if isinstance(rate_constants[2],list) and len(rate_constants[2])>1:
                self.kfsd = np.array(rate_constants[2])
            else:
                self.kfsd = rate_constants[2]*np.ones(self.k)
            if isinstance(rate_constants[3],list) and len(rate_constants[3])>1:
                self.krev = np.array(rate_constants[3])
            else:
                self.krev = rate_constants[3]*np.ones(self.k) 
            if isinstance(rate_constants[4],list) and len(rate_constants[4])>1:
                self.kf_rep= np.array(rate_constants[4])
            else:
                self.kf_rep = rate_constants[4]*np.ones(self.k) 
            if isinstance(rate_constants[5],list) and len(rate_constants[5])>1:
                self.kr_rep = np.array(rate_constants[5])
            else:
                self.kr_rep = rate_constants[5]*np.ones(self.k)
            if isinstance(rate_constants[6],list) and len(rate_constants[6])>1:
                self.kf_wta = np.array(rate_constants[6])
            else:
                self.kf_wta = rate_constants[6]*np.ones(self.k)
            if isinstance(rate_constants[7],list) and len(rate_constants[7])>1:
                self.kr_wta = np.array(rate_constants[7])
            else:
                self.kr_wta = rate_constants[7]*np.ones(self.k) 
            if isinstance(rate_constants[8],list) and len(rate_constants[8])>1:
                self.kRz = np.array(rate_constants[8])
            else:
                self.kRz = rate_constants[8]*np.ones(self.k) 
            if isinstance(rate_constants[9],list) and len(rate_constants[9])>1:
                self.kth = np.array(rate_constants[9])
            else:
                self.kth = rate_constants[9]*np.ones(self.k) 
            if isinstance(rate_constants[10],list) and len(rate_constants[10])>1:
                self.kd = np.array(rate_constants[10])
            else:
                self.kd = rate_constants[10]*np.ones(self.k) 
         
        if isinstance(leak,list):
           
            if len(leak)>1:
                self.leak = np.array(leak)
            else:
                self.leak = leak[0]*np.ones(self.k)
        else:
            self.leak = leak*np.ones(self.k) # txn rates
            
        if isinstance(leakA,list):
           
            if len(leakA)>1:
                self.leakA = np.array(leakA)
            else:
                self.leakA = leakA[0]*np.ones(self.k)
        else:
            self.leakA = leakA*np.ones(self.k) # txn rates
            
            
        if iteration == 1:

            # initial conditions
            int_con = self.in_ic+self.rsd_ic+self.k*[0]+self.REP_con+self.rsdA_ic+self.k*[0]+self.k*[0]+self.f_ic+self.k*[0]+self.k*[0]+self.k*[0]+self.k*[0]+self.wta_ic+self.k*[0]+self.k*[0]+self.k*[0]+self.th_ic+self.k*[0]+self.k*[0]+self.k*[0]
    
            # solver method
            meth = 'BDF'
            
            self.sol = spi.solve_ivp(lambda t, x: RSD_eqs(t,x,self.IN_con,self.RSD_con,self.RSD_conA,self.F_con,self.WTA_con,self.TH_con,self.OUT_con,self.rsd_mat,self.rsd_matA1,self.rsd_matA2,self.rsd_matAL,self.wta_mat,self.k_txn,self.ksd,self.kfsd,self.krev,self.kf_rep,self.kr_rep,self.kf_wta,self.kr_wta,self.kRz,self.kth,self.kd,self.REP_con,self.leak,self.leakA),[t_vec[0],t_vec[-1]],int_con,method=meth,t_eval=t_vec)
    
            out_cons = self.sol.y
        
            self.output_concentration = {}
        
            for i in range(self.k):
                # inputs
                self.output_concentration['IN'+str(i+1)] = out_cons[i]
                # cleaved RSD gates
                self.output_concentration['RSDg'+str(i+1)] = out_cons[self.k+i]
                # outputs
                self.output_concentration['OUT'+str(i+1)] = out_cons[2*self.k+i]
                # reporters
                self.output_concentration['REP'+str(i+1)] = out_cons[3*self.k+i]
                # first reacted AND gates
                self.output_concentration['RSDgA1'+str(i+1)] = out_cons[4*self.k+i]
                # second reacted AND gates
                self.output_concentration['RSDgA2'+str(i+1)] = out_cons[5*self.k+i]
                # input:RSDg complexes
                self.output_concentration['I_RSDg'+str(i+1)] = out_cons[6*self.k+i]
                # fuel strands
                self.output_concentration['F'+str(i+1)] = out_cons[7*self.k+i]
                # fuel:RSDg complexes
                self.output_concentration['F_RSDg'+str(i+1)] = out_cons[8*self.k+i]
                 # uncleaved RSD gates
                self.output_concentration['uRSDg'+str(i+1)] = out_cons[9*self.k+i]
                 # uncleaved AND gates
                self.output_concentration['uRSDgA'+str(i+1)] = out_cons[10*self.k+i]
                # uncleaved WTA gates
                self.output_concentration['uWTA'+str(i+1)] = out_cons[11*self.k+i]
                # cleaved WTA gates
                self.output_concentration['WTA'+str(i+1)] = out_cons[12*self.k+i]
                # WTA1 complexes
                self.output_concentration['WTA1 '+str(i+1)] = out_cons[13*self.k+i]
                # WTA2 complexes
                self.output_concentration['WTA2 '+str(i+1)] = out_cons[14*self.k+i]
                # uTH complexes
                self.output_concentration['uTH'+str(i+1)] = out_cons[15*self.k+i]
                # TH complexes
                self.output_concentration['TH'+str(i+1)] = out_cons[16*self.k+i]
                # O_RSDg complexes
                self.output_concentration['O_RSDg'+str(i+1)] = out_cons[17*self.k+i]
                # I_RSDgA complexes
                self.output_concentration['I_RSDgA'+str(i+1)] = out_cons[18*self.k+i]
                # O_RSDgA complexes
                self.output_concentration['O_RSDgA'+str(i+1)] = out_cons[19*self.k+i]

        elif iteration > 1:
                
            # time interval for simulation
            t_vec_n = t_vec # seconds
            
            # the initial conditions are now the last values of the previous
            int_con_n = self.sol.y[:,-1]
            
            # # defining individual species for convenience below
            # this block of code would be used if the code is extended to allow the user to input custom initial conditons for second iterations
            # I think they can already do this with the ic modifier of the DNA_species function
            # IN_n =  int_con_n[0:self.k] # inputs
            # RSDg_n = int_con_n[self.k:2*self.k] # single RSD gates
            # OUT_n = int_con_n[2*self.k:3*self.k] # outputs
            # REP_n = int_con_n[3*self.k:4*self.k] # reporters
            # RSDgA1_n = int_con_n[4*self.k:5*self.k] # 1st AND gate input / output
            # RSDgA2_n = int_con_n[5*self.k:6*self.k] # 2nd AND gate input / output
            # I_RSDg_n = int_con_n[6*self.k:7*self.k] # IN bound to RSD gate
            # F_n = int_con_n[7*self.k:8*self.k] # fuel strands
            # F_RSDg_n = int_con_n[8*self.k:9*self.k] # fuel bound to RSD gates
            # uRSDg_n = int_con_n[9*self.k:10*self.k] # uncleaved RSD gates
            # uRSDgA_n = int_con_n[10*self.k:11*self.k] # uncleaved AND RSD gates
            # uWTA_n = int_con_n[11*self.k:12*self.k] # uncleaved WTA gates 
            # WTA_n = int_con_n[12*self.k:13*self.k] # cleaved WTA gates 
            # WTA1_n = int_con_n[13*self.k:14*self.k] # WTA gate bound to one input
            # WTA2_n = int_con_n[14*self.k:15*self.k] # WTA gate bound to the other input
            # uTH_n = int_con_n[15*self.k:16*self.k] # uncleaved threshold gates
            # TH_n = int_con_n[16*self.k:17*self.k] # cleaved threshold gates
            # O_RSDg_n = int_con_n[17*self.k:18*self.k] # output bound to gate
            # I_RSDgA_n = int_con_n[18*self.k:19*self.k] # input bound to AND gate
            # O_RSDgA_n = int_con_n[19*self.k:20*self.k] # output bound to AND gate
            
            
            # initial conditions
            int_con = self.in_ic+self.rsd_ic+self.out_ic+self.REP_con+self.rsdA_ic+self.k*[0]+self.k*[0]+self.f_ic+self.k*[0]+self.k*[0]+self.k*[0]+self.k*[0]+self.wta_ic+self.k*[0]+self.k*[0]+self.k*[0]+self.th_ic+self.k*[0]+self.k*[0]+self.k*[0]
    
            # solver method
            meth = 'BDF'
            
            sol_n = spi.solve_ivp(lambda t, x: RSD_eqs(t,x,self.IN_con,self.RSD_con,self.RSD_conA,self.F_con,self.WTA_con,self.TH_con,self.OUT_con,self.rsd_mat,self.rsd_matA1,self.rsd_matA2,self.rsd_matAL,self.wta_mat,self.k_txn,self.ksd,self.kfsd,self.krev,self.kf_rep,self.kr_rep,self.kf_wta,self.kr_wta,self.kRz,self.kth,self.kd,self.REP_con,self.leak,self.leakA),[t_vec[0],t_vec[-1]],int_con_n,method=meth,t_eval=t_vec_n)
    
            # appending each nth iteration to the previous solutions
            self.sol.t = np.concatenate([self.sol.t,sol_n.t])
            self.sol.y = np.concatenate([self.sol.y,sol_n.y],axis=1)
        
            # Saving a dictionary of all solutions for easy parsing
            # saving all concentrations for convience in assembling dictionary
            out_cons = self.sol.y    
        
            self.output_concentration = {}
        
            for i in range(self.k):
                # inputs
                self.output_concentration['IN'+str(i+1)] = out_cons[i]
                # cleaved RSD gates
                self.output_concentration['RSDg'+str(i+1)] = out_cons[self.k+i]
                # outputs
                self.output_concentration['OUT'+str(i+1)] = out_cons[2*self.k+i]
                # reporters
                self.output_concentration['REP'+str(i+1)] = out_cons[3*self.k+i]
                # first reacted AND gates
                self.output_concentration['RSDgA1'+str(i+1)] = out_cons[4*self.k+i]
                # second reacted AND gates
                self.output_concentration['RSDgA2'+str(i+1)] = out_cons[5*self.k+i]
                # input:RSDg complexes
                self.output_concentration['I_RSDg'+str(i+1)] = out_cons[6*self.k+i]
                # fuel strands
                self.output_concentration['F'+str(i+1)] = out_cons[7*self.k+i]
                # fuel:RSDg complexes
                self.output_concentration['F_RSDg'+str(i+1)] = out_cons[8*self.k+i]
                 # uncleaved RSD gates
                self.output_concentration['uRSDg'+str(i+1)] = out_cons[9*self.k+i]
                 # uncleaved AND gates
                self.output_concentration['uRSDgA'+str(i+1)] = out_cons[10*self.k+i]
                # uncleaved WTA gates
                self.output_concentration['uWTA'+str(i+1)] = out_cons[11*self.k+i]
                # cleaved WTA gates
                self.output_concentration['WTA'+str(i+1)] = out_cons[12*self.k+i]
                # WTA1 complexes
                self.output_concentration['WTA1 '+str(i+1)] = out_cons[13*self.k+i]
                # WTA2 complexes
                self.output_concentration['WTA2 '+str(i+1)] = out_cons[14*self.k+i]
                # uTH complexes
                self.output_concentration['uTH'+str(i+1)] = out_cons[15*self.k+i]
                # TH complexes
                self.output_concentration['TH'+str(i+1)] = out_cons[16*self.k+i]
                # O_RSDg complexes
                self.output_concentration['O_RSDg'+str(i+1)] = out_cons[17*self.k+i]
                # I_RSDgA complexes
                self.output_concentration['I_RSDgA'+str(i+1)] = out_cons[18*self.k+i]
                # O_RSDgA complexes
                self.output_concentration['O_RSDgA'+str(i+1)] = out_cons[19*self.k+i]
                