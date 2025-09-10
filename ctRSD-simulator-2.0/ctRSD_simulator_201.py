
# -*- coding: utf-8 -*-
"""

@author: tnm12

PATCH NOTES FROM VERSION 2.0.0

    
"""

import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
import re
import math
import xlrd
# xlrd.xlsx.ensure_elementtree_imported(False, None)
# xlrd.xlsx.Element_has_iter = True

'''
###############################################################################
Rate equations for ctRSD reactions
###############################################################################
'''

def rate_eqs(t,y,ktxnO,ktxnG,ktxnTG,ktxnF,ktxnAG,ktxnCG,krz,krsd,krev,krep,krepr,\
             kth,krzTG,krsdF,krevF,krsdA,krzA,krevCG,krsdCGa,krsdCGb,krzCG,leak,leakA,\
                 Otempm,Gtempm,Thtempv,Ftempv,AGtempm,AGmap,CGtempm,CGmap,kssdO,kssdF,\
                     kdsduG,kdsdG,kdsdGO,kdsduAG,kdsdAG,kdsduCG,kdsdCG,kdsduTG,kdsdTG,kdsdGF,\
                         kdsdAGOa,kdsdAGOb,kdsdAGFb,kdsdCGOa,kdsdCGOb,kdrd,khybO,khybR,N):

    
    uG = y[0:N**2]
    G = y[N**2:2*N**2]
    O = y[2*N**2:3*N**2]
    GO = y[3*N**2:4*N**2]
    Rv = y[4*N**2:N+4*N**2]
    Sv = y[N+4*N**2:2*N+4*N**2]
    RO = y[2*N+4*N**2:2*N+5*N**2]
    uThv = y[2*N+5*N**2:3*N+5*N**2]
    Thv = y[3*N+5*N**2:4*N+5*N**2]
    Fv = y[4*N+5*N**2:5*N+5*N**2]
    GFv = y[5*N+5*N**2:6*N+5*N**2]
    uAG = y[6*N+5*N**2:6*N+6*N**2]
    AG = y[6*N+6*N**2:6*N+7*N**2]
    AGOa = y[6*N+7*N**2:6*N+8*N**2]
    AGOb = y[6*N+8*N**2:6*N+9*N**2]
    uCG = y[6*N+9*N**2:6*N+10*N**2]
    CG = y[6*N+10*N**2:6*N+11*N**2]
    CGOa = y[6*N+11*N**2:6*N+12*N**2]
    CGOb = y[6*N+12*N**2:6*N+13*N**2]
    AGFbv = y[6*N+13*N**2:7*N+13*N**2]
    Qv = y[7*N+13*N**2:8*N+13*N**2]
    

    ##Reshaping
    
    uGm = np.array(uG).reshape(N,N)
    Gm = np.array(G).reshape(N,N)
    Om = np.array(O).reshape(N,N)
    
    
    GOm = np.array(GO).reshape(N,N)
    
    Rm = np.diag(Rv)
    
    Sm = np.diag(Sv)
    
    ROm = np.array(RO).reshape(N,N)
    
    Thm = np.diag(Thv)
    
    GFm = np.diag(GFv)
    
    uAGm = np.array(uAG).reshape(N,N)
    AGm = np.array(AG).reshape(N,N)
    AGOam = np.array(AGOa).reshape(N,N)
    AGObm = np.array(AGOb).reshape(N,N)
    
    AGFbm = np.diag(AGFbv)
    
    uCGm = np.array(uCG).reshape(N,N)
    CGm = np.array(CG).reshape(N,N)
    CGOam = np.array(CGOa).reshape(N,N)
    CGObm = np.array(CGOb).reshape(N,N)
    
    Qm = np.diag(Qv)
    
    
    
    ##Sum Vectors/Matrices
    
    krsd_Gmcsv = np.sum(krsd*Gm,axis=1)
    krsd_Gmcsd = np.diag(krsd_Gmcsv)
    
    krev_Omcsv = np.sum(krev*Om,axis=1)
    krev_Omcsd = np.diag(krev_Omcsv)
    
    krevF_Omrsv = np.sum(krevF*Om,axis=0)
    
    Omrsv = np.sum(Om,axis=0)
    Omrsd = np.diag(Omrsv)
    
    GOmrsv = np.sum(GOm,axis=0)
    GOmrsd = np.diag(GOmrsv)
    
    ROmrsv = np.sum(ROm,axis=0)
    
    krsdFm = np.diag(krsdF*Fv)
    
    krsdA_AGmcsv = np.sum(AGm*krsdA,axis=1)
    krsdA_AGmcsd = np.diag(krsdA_AGmcsv)
    
    krsdA_AGOamcsv = np.sum(AGOam*krsdA,axis=1)
    krsdA_AGOamcsd = np.diag(krsdA_AGOamcsv)
    
    AGObmrsv = np.sum(AGObm,axis=0)
    AGObmrsd = np.diag(AGObmrsv)
    
    krsdCGa_CGmrsv = np.sum(CGm*krsdCGa,axis=0)
    krsdCGa_CGmrsd = np.diag(krsdCGa_CGmrsv)
    # transposed rate constant matrix
    krsdCGb_CGmrsv = np.sum(CGm*krsdCGb,axis=0)
    krsdCGb_CGmrsd = np.diag(krsdCGb_CGmrsv)
    
    krsdCGa_CGmcsv = np.sum(CGm*krsdCGa,axis=1)
    krsdCGa_CGmcsd = np.diag(krsdCGa_CGmcsv)
    # transposed rate constant matrix
    krsdCGb_CGmcsv = np.sum(CGm*krsdCGb,axis=1)
    krsdCGb_CGmcsd = np.diag(krsdCGb_CGmcsv)
    
    krevCG_CGOamrsv = np.sum(CGOam*krevCG,axis=0)
    krevCG_CGOamrsd = np.diag(krevCG_CGOamrsv)
    
    krevCG_CGObmrsv = np.sum(CGObm*krevCG,axis=0)
    krevCG_CGObmrsd = np.diag(krevCG_CGObmrsv)

    krsdCG_CGannA = np.diag(np.sum((Om @ ((krsdCGb*CGmap).T)),axis=0))
    krsdCG_CGannB = np.diag(np.sum((Om @ (krsdCGa*CGmap)),axis=0))
    
    OMannA = Om @ np.diag(np.sum(CGOam @ (krsdCGb*CGmap),axis=0))
    OMannB = Om @ np.diag(np.sum(CGObm @ ((krsdCGa*CGmap).T),axis=0))
    # OMannA = Om @ np.diag(np.sum(krsdCG.T*CGOam @ CGmap,axis=0))
    # OMannB = Om @ np.diag(np.sum(krsdCG*CGObm @ CGmap.T,axis=0))
    
    khybO_Omrsv = np.sum(khybO*Om,axis=0)
    
    kdrd_ROmrsv = np.sum(ROm*kdrd,axis=0)
    
    ###########################################################################
    ##Rate Equations
    ###########################################################################
    duGm = (-krz*uGm + ktxnG*Gtempm - kdsduG*uGm).flatten()
    
    dGm = (krz*uGm - (Omrsd @ (krsd*Gm))  + GOmrsd @ (krev*Om) - kdsdG*Gm).flatten()
    
    dOm = (-kssdO*Om - (khybO*Om) @ Qm\
           -Om @ krsdCGb_CGmrsd + krevCG*CGObm - Om @ krsdCGa_CGmcsd + krevCG*CGOam - OMannB - OMannA \
           + Omrsd @ (krsdA*AGOam) -Om @ krsdA_AGmcsd - Om @ krsdA_AGOamcsd  + AGObmrsd @ (-krev*Om) + AGObm @ (krev_Omcsd) + AGmap @ (leakA*ktxnAG*AGtempm) \
           + GOm @ krsdFm - (krevF*Om) @ GFm + AGObm @ krsdFm - (krevF*Om) @ AGFbm\
           -kth*Om @ Thm \
           + ROm @ (krepr*Sm) + Omrsd @ (krsd*Gm) - Om @ krsd_Gmcsd - Om @ (krep*Rm) + GOmrsd @ (-krev*Om) + GOm @ krev_Omcsd  + leak*ktxnG*Gtempm + ktxnO*Otempm).flatten()
   
    dGOm = (-kdsdGO*GOm \
            -GOm @ krsdFm + (krevF*Om) @ GFm \
            + Om @ krsd_Gmcsd - (GOm) @ krev_Omcsd ).flatten()
    
    dRv = (-krep*Rv*Omrsv + krepr*Sv*ROmrsv + khybR*Sv*Qv)
    
    dSv = (krep*Rv*Omrsv - krepr*Sv*ROmrsv - khybR*Sv*Qv)
    
    dROm = (Om @ (krep*Rm) - ROm @ (krepr*Sm) - kdrd*ROm + (khybO*Om) @ Qm).flatten()
    
    duThv = (ktxnTG*Thtempv -krzTG*uThv -kdsduTG*uThv)
    
    dThv = (krzTG*uThv -kth*Thv*Omrsv -kdsdTG*Thv)
    
    dFv = (ktxnF*Ftempv - krsdF*Fv*GOmrsv + krevF_Omrsv*GFv - kssdF*Fv \
           -krsdF*Fv*AGObmrsv + krevF_Omrsv*AGFbv)
    
    dGFv = (krsdF*Fv*GOmrsv - krevF_Omrsv*GFv -kdsdGF*GFv)
    
    duAGm = (ktxnAG*AGtempm - krzA*uAGm - kdsduAG*uAGm).flatten()
    
    dAGm = (krzA*uAGm - Omrsd @ (krsdA*AGm) - kdsdAG*AGm).flatten()
    
    dAGOam = (AGmap @ (Omrsd @ (krsdA*AGm)) - Omrsd @ (krsdA*AGOam) + AGObmrsd @ (krev*Om) -kdsdAGOa*AGOam).flatten()
    #dAGOam = (AGmap @ (Om @ (krsdA*AGm)) - Omrsd @ (krsdA*AGOam) + AGObmrsd @ (krev*Om) -kdsdAGOa*AGOam).flatten()
    
    dAGObm = (Om @ krsdA_AGOamcsd -AGObm@krev_Omcsd \
              -AGObm @ krsdFm + (krevF*Om) @ AGFbm -kdsdAGOb*AGObm).flatten()
    
    dAGFbv = krsdF*Fv*AGObmrsv - krevF_Omrsv*AGFbv -kdsdAGFb*AGFbv
    
    duCGm = (ktxnCG*CGtempm - krzCG*uCGm - kdsduCG*uCGm).flatten()
    
    dCGm = (krzCG*uCGm  - (Omrsd @ (krsdCGb*CGm).T).T + CGmap @ krevCG_CGObmrsd - Omrsd@(krsdCGa*CGm) + krevCG_CGOamrsd @ CGmap - kdsdCG*CGm).flatten()
    
    dCGOam = (Om @ krsdCGa_CGmcsd - krevCG*CGOam - CGOam @ krsdCG_CGannA -kdsdCGOa*CGOam).flatten()
    
    dCGObm = (Om @ krsdCGb_CGmrsd - krevCG*CGObm - CGObm @ krsdCG_CGannB -kdsdCGOb*CGObm).flatten()
    
    dQv = (kdrd_ROmrsv - khybR*Sv*Qv - khybO_Omrsv*Qv)
    
    
    
    return(np.concatenate([duGm,dGm,dOm,dGOm,dRv,dSv,dROm,duThv,dThv,dFv,dGFv,duAGm,dAGm,dAGOam,dAGObm,duCGm,dCGm,dCGOam,dCGObm,dAGFbv,dQv]))

'''
###############################################################################
Helper functions for ctRSD_seq_compile()
###############################################################################
'''

def rc_seq(seq, spec_out='rc', rna=0):
    # Helper function for ctRSD_seq_compile()

    new_seq = '3'+seq+'5'
    new_seq = list(new_seq)
    seq = list(seq)
    ds = ''

    for i in range(len(seq)):
        if seq[i].lower() == 'u' and rna == 0:
            seq[i] = 'T'
        elif seq[i].lower() == 't' and rna == 1:
            seq[i] = 'U'
        if seq[i].lower() == 'g':
            new_seq[i+1] = 'C'
        elif seq[i].lower() == 'c':
            new_seq[i+1] = 'G'
        elif seq[i].lower() == 't':
            new_seq[i+1] = 'A'
        elif seq[i].lower() == 'u':
            new_seq[i+1] = 'A'
        elif seq[i].lower() == 'a' and rna == 0:
            new_seq[i+1] = 'T'
        elif seq[i].lower() == 'a' and rna == 1:
            new_seq[i+1] = 'U'

    if spec_out.lower() == 'rc':
        out_seq = ds.join(new_seq[::-1])
    elif spec_out.lower() == 'c':
        out_seq = ds.join(new_seq)
    elif spec_out.lower() == 'r':
        out_seq = '3'+ds.join(seq[::-1])+'5'
    elif spec_out.lower() == 's':
        out_seq = '5'+ds.join(seq[:])+'3'

    return out_seq


def xlsheet_to_dict(filepath, sheet_name, ncol):
    # Helper function for ctRSD_seq_compile()
    
    seq_workbook = xlrd.open_workbook(filepath)
    sheet = seq_workbook.sheet_by_name(sheet_name)
    sheet_dict = {}
    dv = [[0]*ncol for i in range(0, sheet.nrows)]
    for ri in range(1, sheet.nrows):
        dk = sheet.cell_value(ri, 0)
        a = 0
        for ci in range(0, ncol):
            dv[ri][a] = sheet.cell_value(ri, ci+1)
            a += 1

        sheet_dict.update({dk: dv[ri]})

    return sheet_dict

def create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len):
    # Helper function for ctRSD_seq_compile()
    
    if rna == 0:
        # full input sequence
        template = us_S + prom_S + rc_seq(ctRSD_part, spec_out='s')[1:-1] + ds_S
        # truncated sequence
        if temp_len != 0:
            # truncating template based on excess sequence downstream
            if len(template) >= temp_len and ds_S != '':
                template = template[0:temp_len]
            # truncating sequence based on excess sequence upstream
            elif len(template) >= temp_len and ds_S == '':
                strt = len(template) - temp_len
                template = template[strt:] 
            else:
                print('Issue processing template length request')
            
    elif rna == 1: 
        template = rc_seq(ctRSD_part, spec_out='s',rna=1)[1:-1]
        
    return template

'''
###############################################################################
Class definition
###############################################################################
'''

class RSD_sim:
    def __init__(self,domains=5):
        
        # Total input-output domains in the system
        self.N = domains
        
        # Initial template concentrations
        self.Gtemp_con = 0*np.ones((domains,domains))  # single RNA gates
        self.Otemp_con = 0*np.ones((domains,domains)) # Outputs
        self.TGtemp_con = 0*np.ones(domains) # threshold gates
        self.Ftemp_con = 0*np.ones(domains) # fuels
        self.AGtemp_con = 0*np.ones((domains,domains)) # and gates
        self.CGtemp_con = 0*np.ones((domains,domains)) # comparator gates
        
        # Initial species concentrations
        self.uG_ic = 0*np.ones((domains,domains)) # uncleaved gates
        self.GO_ic = 0*np.ones((domains,domains)) # gate:output complexes
        self.G_ic = 0*np.ones((domains,domains)) 
        self.R_ic = 0*np.ones(domains) # reporters
        self.RO_ic =  0*np.ones((domains,domains))
        self.S_ic = 0*np.ones(domains)
        self.O_ic = 0*np.ones((domains,domains)) # Outputs
        self.rep_ic_flag = np.array(domains*[0]) # saves if the reporter con was updated
        
        self.uTG_ic = 0*np.ones(domains)
        self.TG_ic = 0*np.ones(domains)
        
        self.F_ic = 0*np.ones(domains)
        self.GF_ic = 0*np.ones(domains)
        
        self.uAG_ic = 0*np.ones((domains,domains))
        self.AG_ic = 0*np.ones((domains,domains))
        self.AGOa_ic = 0*np.ones((domains,domains))
        self.AGOb_ic = 0*np.ones((domains,domains))
        self.AGmap = 0*np.ones((domains,domains))
        
        self.uCG_ic = 0*np.ones((domains,domains))
        self.CG_ic = 0*np.ones((domains,domains))
        self.CGOa_ic = 0*np.ones((domains,domains))
        self.CGOb_ic = 0*np.ones((domains,domains))
        self.CGmap = 0*np.ones((domains,domains))  
        
        self.AGFb_ic = 0*np.ones(domains)
        
        self.Q_ic = 0*np.ones(domains)
        
        # Rate constant definitions
        self.ktxnO = 0.013*np.ones((domains,domains))
        self.ktxnG = 0.013*np.ones((domains,domains))
        self.ktxnTG = np.array(domains*[0.013])
        self.ktxnF = np.array(domains*[0.013])
        self.ktxnAG = 0.013*np.ones((domains,domains))
        self.ktxnCG = 0.013*np.ones((domains,domains))
        self.krz = (.25/60)*np.ones((domains,domains))
        self.krsd = (1e3/1e9)*np.ones((domains,domains))
        
        self.krev = (270/1e9)*np.ones((domains,domains))
        # inputs are stored along the diagonal pf the ouptut matrix 
        # and should not have reverse rates
        for x in range(self.N):
            self.krev[x,x] = 0
            
        self.krep = np.array(domains*[1e4 / 1e9])
        self.krepr = 0*np.ones(domains)
        self.kth = np.array(domains*[1e5 / 1e9])
        self.krzTG = np.array(domains*[.00417])
        self.krsdF = np.array(domains*[1e3 / 1e9])
        # here inputs can have reverse rates to displace fuel strands so the diagonal is not zero as with krev
        self.krevF = (1e3/1e9)*np.ones((domains,domains))
        self.krzA = (.25/60)*np.ones((domains,domains))
        self.krsdA = (1e3/1e9)*np.ones((domains,domains))
            
        self.krzCG = .00417*np.ones((domains,domains))
        self.krsdCGa = (1e5/1e9)*np.ones((domains,domains))
        self.krsdCGb = (1e5/1e9)*np.ones((domains,domains))
        # here inputs can have reverse rates off of CG so the diagonal is not zero as with krev
        self.krevCG = (0.05)*np.ones((domains,domains))
        
        self.kssdO = 0*np.ones((domains,domains))
        self.kssdF = 0*np.ones(domains)
        self.kdsduG = 0*np.ones((domains,domains))
        self.kdsdG = 0*np.ones((domains,domains))
        self.kdsdGO = 0*np.ones((domains,domains))
        self.kdsdGF = 0*np.ones(domains)
        self.kdsduTG = 0*np.ones(domains)
        self.kdsdTG = 0*np.ones(domains)
        self.kdsduAG = 0*np.ones((domains,domains))
        self.kdsdAG = 0*np.ones((domains,domains))
        self.kdsdAGOa = 0*np.ones((domains,domains))
        self.kdsdAGOb = 0*np.ones((domains,domains))
        self.kdsdAGFb = 0*np.ones(domains)
        self.kdsduCG = 0*np.ones((domains,domains))
        self.kdsdCG = 0*np.ones((domains,domains))
        self.kdsdCGOa = 0*np.ones((domains,domains))
        self.kdsdCGOb = 0*np.ones((domains,domains))
        self.kdrd = 0*np.ones((domains,domains))
        self.khybO = 1e6/1e9*np.ones((domains,domains))
        self.khybR = np.array(domains*[1e6/1e9])
        
        self.leak = (0.03)*np.ones((domains,domains))
        self.leakA = (0.06)*np.ones((domains,domains))
        
        # checks for other functions
        self.AGcheck = False
        self.Fcheck = False    
        
        self.initialcheck = np.array((8*self.N+13*self.N**2)*[0])
        self.initialcheckIter = []
        
        self.plotCheck1 = False
        self.plotCheck2 = False
        
        
    # function for defining the DNA species in the model instance and the circuit connectivity
    def global_rate_constants(self,krz='False',krsd='False',krev='False',krep='False',krepr='False',\
                                   kth='False',krzTG='False',krsdF='False',krevF='False',\
                                   krsdA='False',krzA='False',krevCG='False',\
                                   krsdCGa='False',krsdCGb='False',krsdCG='False',krzCG='False',\
                                   ktxnO='False',ktxnG='False',ktxnTG='False',ktxnF='False',ktxnAG='False',\
                                   ktxnCG='False',ktxn='False',kssdO='False',kssdF='False',kdsduG='False',\
                                   kdsdG='False',kdsdGO='False',kdsduAG='False',kdsdAG='False',kdsduCG='False',\
                                   kdsdCG='False',kdsduTG='False',kdsdTG='False',kdsdGF='False',\
                                   kdsdAGOa='False',kdsdAGOb='False',kdsdAGFb='False',kdsdCGOa='False',kdsdCGOb='False',\
                                   kdrd='False',kdeg='False',kssd='False',kdsd='False',\
                                   khybO='False',khybR='False',khyb='False',leak='False',leakA='False'):
        
        if krz != 'False':
            self.krz = krz*np.ones((self.N,self.N))
        if krsd != 'False':
            self.krsd = krsd*np.ones((self.N,self.N))
        if krev != 'False':
            self.krev = krev*np.ones((self.N,self.N))
            for x in range(self.N):
                self.krev[x,x] = 0
        if krep != 'False':
            self.krep = np.array(self.N*[krep])
        if krepr != 'False':
            self.krepr = np.array(self.N*[krepr])
        if kth != 'False':
            self.kth = np.array(self.N*[kth])
        if krzTG != 'False':
            self.krzTG = np.array(self.N*[krzTG])
        if krsdF != 'False':
            self.krsdF = np.array(self.N*[krsdF])
        if krevF != 'False':
            self.krevF = krevF*np.ones((self.N,self.N))
        if krsdA != 'False':
            self.krsdA = krsdA*np.ones((self.N,self.N))
        if krzA != 'False':
            self.krzA = krzA*np.ones((self.N,self.N))
        if krsdCGa != 'False':
            self.krsdCGa = krsdCGa*np.ones((self.N,self.N))
        if krsdCGb != 'False':
            self.krsdCGb = krsdCGb*np.ones((self.N,self.N))
        if krsdCG != 'False':
            self.krsdCGa = krsdCG*np.ones((self.N,self.N))
            self.krsdCGb = krsdCG*np.ones((self.N,self.N))
        if krevCG != 'False':
            self.krevCG = krevCG*np.ones((self.N,self.N))
        if krzCG != 'False':
            self.krzCG = krzCG*np.ones((self.N,self.N))
        if ktxnO != 'False':
            self.ktxnO = ktxnO*np.ones((self.N,self.N))
        if ktxnG != 'False':
            self.ktxnG = ktxnG*np.ones((self.N,self.N))
        if ktxnTG != 'False':
            self.ktxnTG = np.array(self.N*[ktxnTG])
        if ktxnF != 'False':
            self.ktxnF = np.array(self.N*[ktxnF])
        if ktxnAG != 'False':
            self.ktxnAG = ktxnAG*np.ones((self.N,self.N))
        if ktxnCG != 'False':
            self.ktxnCG = ktxnCG*np.ones((self.N,self.N))
        if kdsdGF != 'False':
            self.kdsdGF = np.array(self.N*[kdsdGF])
        if kdsduTG != 'False':
            self.kdsduTG = np.array(self.N*[kdsduTG])
        if kdsdTG != 'False':
            self.kdsdTG = np.array(self.N*[kdsdTG])
        if kdsdAGOa != 'False':
            self.kdsdAGOa = kdsdAGOa*np.ones((self.N,self.N))
        if kdsdAGOb != 'False':
            self.kdsdAGOb = kdsdAGOb*np.ones((self.N,self.N))
        if kdsdAGFb != 'False':
            self.kdsdAGFb = np.array(self.N*[kdsdAGFb])
        if kdsdCGOa != 'False':
            self.kdsdCGOa = kdsdCGOa*np.ones((self.N,self.N))
        if kdsdCGOb != 'False':
            self.kdsdCGOb = kdsdCGOb*np.ones((self.N,self.N))
            
        if ktxn != 'False':
            self.ktxnO = ktxn*np.ones((self.N,self.N))
            self.ktxnG = ktxn*np.ones((self.N,self.N))
            self.ktxnTG = np.array(self.N*[ktxn])
            self.ktxnF = np.array(self.N*[ktxn])
            self.ktxnAG = ktxn*np.ones((self.N,self.N))
            self.ktxnCG = ktxn*np.ones((self.N,self.N))
        
        if kssdO != 'False':
            self.kssdO = kssdO*np.ones((self.N,self.N))
        if kssdF != 'False':
            self.kssdF = np.array(self.N*[kssdF])    
        if kdsduG != 'False':
            self.kdsduG = kdsduG*np.ones((self.N,self.N))
        if kdsdG != 'False':
            self.kdsdG = kdsdG*np.ones((self.N,self.N))
        if kdsdGO != 'False':
            self.kdsdGO = kdsdGO*np.ones((self.N,self.N))
        if kdsduAG != 'False':
            self.kdsduAG = kdsduAG*np.ones((self.N,self.N))
        if kdsdAG != 'False':
            self.kdsdAG = kdsdAG*np.ones((self.N,self.N))
        if kdsduCG != 'False':
            self.kdsduCG = kdsduCG*np.ones((self.N,self.N))
        if kdsdCG != 'False':
            self.kdsdCG = kdsdCG*np.ones((self.N,self.N))
        
        if kdrd != 'False':
            self.kdrd = kdrd*np.ones((self.N,self.N))
            
        if kdeg != 'False':
            self.kssdO = kdeg*np.ones((self.N,self.N))
            self.kssdF = kdeg*np.ones(self.N)
            self.kdsduG = kdeg*np.ones((self.N,self.N))
            self.kdsdG = kdeg*np.ones((self.N,self.N))
            self.kdsdGO = kdeg*np.ones((self.N,self.N))
            self.kdsduAG = kdeg*np.ones((self.N,self.N))
            self.kdsdAG = kdeg*np.ones((self.N,self.N))
            self.kdsduCG = kdeg*np.ones((self.N,self.N))
            self.kdsdCG = kdeg*np.ones((self.N,self.N))
            self.kdsdGF = kdeg*np.ones(self.N)
            self.kdsduTG = kdeg*np.ones(self.N)
            self.kdsdTG = kdeg*np.ones(self.N)
            self.kdsdAGOa = kdeg*np.ones((self.N,self.N))
            self.kdsdAGOb = kdeg*np.ones((self.N,self.N))
            self.kdsdAGFb = kdeg*np.ones(self.N)
            self.kdsdCGOa = kdeg*np.ones((self.N,self.N))
            self.kdsdCGOb = kdeg*np.ones((self.N,self.N))
            self.kdrd = kdeg*np.ones((self.N,self.N))
            
        if kssd != 'False':
            self.kssdO = kssd*np.ones((self.N,self.N))
            self.kssdF = kssd*np.ones(self.N)
        
        if kdsd != 'False':
            self.kdsduG = kdsd*np.ones((self.N,self.N))
            self.kdsdG = kdsd*np.ones((self.N,self.N))
            self.kdsdGO = kdsd*np.ones((self.N,self.N))
            self.kdsduAG = kdsd*np.ones((self.N,self.N))
            self.kdsdAG = kdsd*np.ones((self.N,self.N))
            self.kdsduCG = kdsd*np.ones((self.N,self.N))
            self.kdsdCG = kdsd*np.ones((self.N,self.N))
            self.kdsdGF = kdsd*np.ones(self.N)
            self.kdsduTG = kdsd*np.ones(self.N)
            self.kdsdTG = kdsd*np.ones(self.N)
            self.kdsdAGOa = kdsd*np.ones((self.N,self.N))
            self.kdsdAGOb = kdsd*np.ones((self.N,self.N))
            self.kdsdAGFb = kdsd*np.ones(self.N)
            self.kdsdCGOa = kdsd*np.ones((self.N,self.N))
            self.kdsdCGOb = kdsd*np.ones((self.N,self.N))
        
        if khybO != 'False':
            self.khybO = khybO*np.ones((self.N,self.N))
        if khybR != 'False':
            self.khybR = khybR*np.ones(self.N)
        if khyb != 'False':
            self.khybO = khyb*np.ones((self.N,self.N))
            self.khybR = khyb*np.ones(self.N)
            
        if leak != 'False':
            self.leak = leak*np.ones((self.N,self.N))
        if leakA != 'False':
            self.leakA = leakA*np.ones((self.N,self.N)) 
    
    
    def molecular_species(self,name,DNA_con=0,ic='False',krz='False',krsd='False',krev='False',\
                               krep='False',krepr='False',kth='False',krzTG='False',krsdF='False',\
                               krevF='False',krsdA='False',krzA='False',krevCG='False',krevCGa='False',krevCGb='False',\
                               krsdCG='False',krsdCGa='False',krsdCGb='False',krzCG='False',ktxnO='False',ktxnG='False',ktxnTG='False',\
                               ktxnF='False',ktxnAG='False',ktxnCG='False',kssdO='False',kssdF='False',\
                               kdsduG='False',kdsdG='False',kdsdGO='False',kdsduAG='False',kdsdAG='False',\
                               kdsduCG='False',kdsdCG='False',kdsduTG='False',kdsdTG='False',kdsdGF='False',\
                               kdsdAGOa='False',kdsdAGOb='False',kdsdAGFb='False',kdsdCGOa='False',kdsdCGOb='False',\
                               kdrd='False',khybO='False',khybR='False',leak='False',leakA='False'):
        
        inp = re.compile("(i|in|inp|input)\{\w*\d+\w*\}")
        inps = inp.fullmatch(name.lower())
        rep = re.compile("(r|rep|reporter)\{\w*\d+\w*\}")
        reps = rep.fullmatch(name.lower())
        out = re.compile("(o|out|output)\{\w*\d+\w*\,\w*\d+\w*\}")
        outs = out.fullmatch(name.lower())
        gate = re.compile("(g|gate)\{\w*\d+\w*\,\w*\d+\w*\}")
        gates = gate.fullmatch(name.lower())
        
        uG = re.compile("ug\{\w*\d+\w*\,\w*\d+\w*\}")
        uGs = uG.fullmatch(name.lower())
        GI = re.compile("gi\{\w*\d+\w*\}")
        GIs = GI.fullmatch(name.lower())
        GO = re.compile("go\{\w*\d+\w*\,\w*\d+\w*\}")
        GOs = GO.fullmatch(name.lower())
        RO = re.compile("ro\{\w*\d+\w*\,\w*\d+\w*\}")
        ROs = RO.fullmatch(name.lower())
        S =  re.compile("s\{\w*\d+\w*\}")
        Ss = S.fullmatch(name.lower())
        Q = re.compile("q\{\w*\d+\w*\}")
        Qs = Q.fullmatch(name.lower())
        
        uTh = re.compile("utg|ut|uth\{\w*\d+\w*\}")
        uThs = uTh.fullmatch(name.lower())
        thresh = re.compile("(tg|t|th)\{\w*\d+\w*\}")
        threshs = thresh.fullmatch(name.lower())
        
        fuel = re.compile("f\{\w*\d+\w*\}")
        fuels = fuel.fullmatch(name.lower())
        GF = re.compile("gf\{\w*\d+\w*\}")
        GFs = GF.fullmatch(name.lower())
        
        #AG = re.compile("ag\{\w*\d+(\.\d+)+\,\w*\d+\w*\}")
        uAG = re.compile("uag\{\w*\d+\w*(\.|\&)\w*\d+\w*\,\w*\d+\w*\}")
        uAGs = uAG.fullmatch(name.lower())
        AG = re.compile("(ag|g|gate)\{\w*\d+\w*(\.|\&)\w*\d+\w*\,\w*\d+\w*\}")
        AGs = AG.fullmatch(name.lower())
        AGOa = re.compile("agoa\{\w*\d+\w*\,\w*\d+\w*\}")
        AGOas = AGOa.fullmatch(name.lower())
        AGOb = re.compile("agob\{\w*\d+\w*\,\w*\d+\w*\}")
        AGObs = AGOb.fullmatch(name.lower())
        
        #AGFa  = re.compile("agfa\{\w*\d+\w*\,\w*\d+\w*\}")
        #AGFas = AGFa.fullmatch(name.lower())
        AGFb = re.compile("agfb\{\w*\d+\w*\}")
        AGFbs = AGFb.fullmatch(name.lower())
        
        uCG = re.compile("ucg\{\w*\d+\w*\,\w*\d+\w*\}")
        uCGs = uCG.fullmatch(name.lower())
        CG = re.compile("cg\{\w*\d+\w*\,\w*\d+\w*\}")
        CGs = CG.fullmatch(name.lower())
        CGOa = re.compile("cgoa\{\w*\d+\w*\,\w*\d+\w*\}")
        CGOas = CGOa.fullmatch(name.lower())
        CGOb = re.compile("cgob\{\w*\d+\w*\,\w*\d+\w*\}")
        CGObs = CGOb.fullmatch(name.lower())
        
        # Inputs
        if inps:
            inpInd1f = re.compile("\d+")
            inpInd1 = int(inpInd1f.search(name.lower()).group())-1
            
            self.Otemp_con[inpInd1,inpInd1]=DNA_con
            if ic != 'False':
                self.O_ic[inpInd1,inpInd1]=ic
                self.initialcheck[2*self.N**2+(self.N*inpInd1) + inpInd1] += 1
                
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to I')
            if ktxnO != 'False':
                self.ktxnO[inpInd1,inpInd1] = ktxnO
            if kssdO != 'False':
                self.kssdO[inpInd1,inpInd1] = kssdO
            if kdrd != 'False':
                self.kdrd[inpInd1,inpInd1] = kdrd
            if khybO != 'False':
                self.khybO[inpInd1,inpInd1] = khybO
            if krevCG != 'False':
                self.krevCG[inpInd1,inpInd1] = krevCG

                
        # Reporters   
        elif reps:
            repInd1f = re.compile('\d+')
            repInd1 = int(repInd1f.search(name.lower()).group())-1
            
            if ic == 'False':
                self.R_ic[repInd1]=DNA_con
            else:
                self.R_ic[repInd1] = ic
                self.initialcheck[4*self.N**2 + repInd1] += 1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to R')
            if krep != 'False':
                self.krep[repInd1] = krep
            if krepr != 'False':
                self.krepr[repInd1] = krepr
            if khybR != 'False':
                self.khybR[repInd1] = khybR
        
        # Outputs
        elif outs:
            outIndf = re.findall("\d+",name.lower())

            outInd1 = int(outIndf[0])-1
            outInd2 = int(outIndf[1])-1
            
            self.Otemp_con[outInd1,outInd2]=DNA_con
            if ic != 'False':
                self.O_ic[outInd1,outInd2]=ic
                self.initialcheck[2*self.N**2+(self.N*outInd1) + outInd2] += 1
            
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False'  or krzA != 'False' or krsdA != "False" or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to O')
            if ktxnO != 'False':
                self.ktxnO[outInd1,outInd2] = ktxnO
            if krev != 'False':
                self.krev[outInd1,outInd2] = krev
            if krevF != 'False':
                self.krevF[outInd1,outInd2] = krevF
            if krevCG != 'False':
                self.krevCG[outInd1,outInd2] = krevCG
            if kssdO != 'False':
                self.kssdO[outInd1,outInd2] = kssdO
            if khybO != 'False':
                self.khybO[outInd1,outInd2] = khybO
            if kdrd != 'False':
                self.kdrd[outInd1,outInd2] = kdrd
            
        # Gates
        elif gates:
            gateIndf = re.findall("\d+",name.lower())
            gateInd1 = int(gateIndf[0])-1
            gateInd2 = int(gateIndf[1])-1
            
            self.Gtemp_con[gateInd1,gateInd2]=DNA_con
            if ic != 'False':
                self.G_ic[gateInd1,gateInd2]=ic
                self.initialcheck[self.N**2+(self.N*gateInd1) + gateInd2] += 1
            
            if leakA != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to G')
            if krev != 'False':
                self.krev[gateInd1,gateInd2] = krev   
            if krsd != 'False':
                self.krsd[gateInd1,gateInd2] = krsd
            if krz != 'False':
                self.krz[gateInd1,gateInd2] = krz
            if ktxnG != 'False':
                self.ktxnG[gateInd1,gateInd2] = ktxnG
            if khybO != 'False':
                self.khybO[gateInd1,gateInd2] = khybO
            if kdsdG != 'False':
                self.kdsdG[gateInd1,gateInd2] = kdsdG
            if leak != 'False':
                self.leak[gateInd1,gateInd2] = leak
            
    
        # Uncleaved gates
        elif uGs:
            uGIndf = re.findall("\d+",name.lower())
            uGInd1 = int(uGIndf[0])-1
            uGInd2 = int(uGIndf[1])-1
            
            if ic != 'False':
                self.uG_ic[uGInd1,uGInd2]=ic
                self.initialcheck[0+(self.N*uGInd1) + uGInd2] += 1
            
            if leak != 'False' or leakA != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to uG')
            if krz != 'False':
                self.krz[uGInd1,uGInd2] = krz
            if ktxnG != 'False':
                self.ktxnG[uGInd1,uGInd2] = ktxnG
            if kdsduG != 'False':
                self.kdsduG[uGInd1,uGInd2] = kdsduG
            
        # Gate:Input complexes (Diagonal of GO)
        elif GIs:
            GIInd1f = re.compile("\d+")
            GIInd1 = int(GIInd1f.search(name.lower()).group())-1
            
            if ic != 'False':
                self.GO_ic[GIInd1,GIInd1]=ic
                self.initialcheck[3*self.N**2+(self.N*GIInd1) + GIInd1] += 1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to GI')
            if kdsdGO != 'False':
                self.kdsdGO[GIInd1,GIInd1] = kdsdGO
            
        # Gate:Output complexes
        elif GOs:
            GOIndf = re.findall("\d+",name.lower())
            GOInd1 = int(GOIndf[0])-1
            GOInd2 = int(GOIndf[1])-1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to GO')
            if kdsdGO != 'False':
                self.kdsdGO[GOInd1,GOInd2] = kdsdGO
            
            if ic != 'False':
                self.GO_ic[GOInd1,GOInd2]=ic
                self.initialcheck[3*self.N**2+(self.N*GOInd1) + GOInd2] += 1
        
        # Reporter:Output complexes
        elif ROs:
           ROIndf = re.findall("\d+",name.lower())
           ROInd1 = int(ROIndf[0])-1
           ROInd2 = int(ROIndf[1])-1
           
           if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
               print('This rate constant should not be changed with respect to RO')
           if kdrd != 'False':
               self.kdrd[ROInd1,ROInd2] = kdrd
          
           if ic != 'False':
               self.RO_ic[ROInd1,ROInd2]=ic
               self.initialcheck[2*self.N+4*self.N**2+(self.N*ROInd1) + ROInd2] += 1
         
        # Reporter Signal
        elif Ss:
            SInd1f = re.compile("\d+")
            SInd1 = int(SInd1f.search(name.lower()).group())-1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to S')
            
            if khybR != 'False':
                self.khybR[repInd1] = khybR
            
            if ic != 'False':
                self.S_ic[SInd1]=ic
                self.initialcheck[self.N+4*self.N**2 + SInd1] += 1
        
        # Uncleaved threshold gates
        elif uThs:
            uThInd1f = re.compile("\d+")
            uThInd1 = int(uThInd1f.search(name.lower()).group())-1
            
            if ic != 'False':
                self.uTG_ic[uThInd1] = ic
                self.initialcheck[2*self.N+5*self.N**2 + uThInd1] += 1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to uTG')
            if krzTG != 'False':
                self.krzTG[uThInd1] = krzTG
            if ktxnTG != 'False':
                self.ktxnTG[uThInd1] = ktxnTG
            if kdsduTG != 'False':
                self.kdsduTG[uThInd1] = kdsduTG
        
        # Threshold gates
        elif threshs:
            threshInd1f = re.compile("\d+")
            threshInd1 = int(threshInd1f.search(name.lower()).group())-1
            
            self.TGtemp_con[threshInd1] = DNA_con
            if ic != 'False':
                self.TG_ic[threshInd1] = ic
                self.initialcheck[3*self.N+5*self.N**2 + threshInd1] += 1
            
            if leak != 'False' or leakA != 'False' or krep != 'False' or krepr != 'False' or krev != 'False' or krsd != 'False' or krz != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to TG')
            if kth != 'False':
                self.kth[threshInd1] = kth
            if krzTG != 'False':
                self.krzTG[threshInd1] = krzTG
            if ktxnTG != 'False':
                self.ktxnTG[threshInd1] = ktxnTG
            if kdsdTG != 'False':
                self.kdsdTG[uThInd1] = kdsdTG
        
        # Fuel strands
        elif fuels:
            fuelInd1f = re.compile("\d+")
            self.fuelInd1 = int(fuelInd1f.search(name.lower()).group())-1
            
            self.Ftemp_con[self.fuelInd1] = DNA_con
            if ic != 'False':
                self.F_ic[self.fuelInd1] = ic
                self.initialcheck[4*self.N+5*self.N**2 + self.fuelInd1] += 1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to F')
            if krsdF != 'False':
                self.krsdF[self.fuelInd1] = krsdF
            if ktxnF != 'False':
                self.ktxnF[self.fuelInd1] = ktxnF
            if kssdF != 'False':
                self.kssdF[self.fuelInd1] = kssdF
            
            self.Fcheck = True
            
        # Gate:Fuel complexes   
        elif GFs:
            GFInd1f = re.compile("\d+")
            GFInd1 = int(GFInd1f.search(name.lower()).group())-1
            

            if ic != 'False':
                self.GF_ic[GFInd1] = ic
                self.initialcheck[5*self.N+5*self.N**2 + self.GFInd1] += 1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to GF')
            if ktxnF != 'False':
                self.ktxnF[GFInd1] = ktxnF
            if kdsdGF != 'False':
                self.kdsdGF[GFInd1] = kdsdGF
          
        # AND Gates
        elif AGs:
            AGIndf = re.findall("\d+",name.lower())
            self.AGInd1 = int(AGIndf[0])-1
            AGInd2 = int(AGIndf[-1])-1
            
            AGOInd1 = int(AGIndf[0])-1
            AGOInd2 = int(AGIndf[1])-1
            
            self.AGtemp_con[self.AGInd1,AGInd2] = DNA_con
            if ic != 'False':
                self.AG_ic[self.AGInd1,AGInd2] = ic
                self.initialcheck[6*self.N+6*self.N**2:+(self.N*self.AGInd1) + AGInd2] += 1
            
            self.AGmap[AGOInd1,AGOInd2] = 1
            
            if krz != 'False' or krsd != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to AG')
            if krsdA != 'False':
                self.krsdA[self.AGInd1,AGInd2] = krsdA
            if krzA != 'False':
                self.krzA[self.AGInd1,AGInd2] = krzA
            if ktxnAG != 'False':
                self.ktxnAG[self.AGInd1,AGInd2] = ktxnAG
            if kdsdAG != 'False':
                self.kdsdAG[self.AGInd1,AGInd2] = kdsdAG
            if krev != 'False':
                self.krev[AGOInd2,AGInd2] = krev
            if leakA != 'False':
                self.leakA[self.AGInd1,AGInd2] = leakA
            if leak != 'False':
                self.leakA[self.AGInd1,AGInd2] = leakA
                
            self.AGcheck = True
        
        # Uncleaved AND gates
        elif uAGs:
            uAGIndf = re.findall("\d+",name.lower())
            uAGInd1 = int(uAGIndf[0])-1
            uAGInd2 = int(uAGIndf[-1])-1
            
            if krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to uAG')
            if krzA != 'False':
                self.krzA[uAGInd1,uAGInd2] = krzA
            if ktxnAG != 'False':
                self.ktxnAG[uAGInd1,uAGInd2] = ktxnAG
            if kdsduAG != 'False':
                self.kdsduAG[uAGInd1,uAGInd2] = kdsduAG
            
            if ic != 'False':
                self.uAG_ic[uAGInd1,uAGInd2] = ic
                self.initialcheck[6*self.N+5*self.N**2:+(self.N*uAGInd1) + uAGInd2] += 1
        
        # AND gate:Output complex a
        elif AGOas:
            AGOaIndf = re.findall("\d+",name.lower())
            AGOaInd1 = int(AGOaIndf[0])-1
            AGOaInd2 = int(AGOaIndf[1])-1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to AGOa')
            if krsdA != 'False':
                self.krsdA[AGOaInd1,AGOaInd2] = krsdA
            if kdsdAGOa != 'False':
                self.kdsdAGOa[AGOaInd1,AGOaInd2] = kdsdAGOa
            
            if ic != 'False':
                self.AGOa_ic[AGOaInd1,AGOaInd2] = ic
                self.initialcheck[6*self.N+7*self.N**2:+(self.N*AGOaInd1) + AGOaInd2] += 1
        
        # AND gate:Output complex b
        elif AGObs:
            AGObIndf = re.findall("\d+",name.lower())
            AGObInd1 = int(AGObIndf[0])-1
            AGObInd2 = int(AGObIndf[1])-1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to AGOb')
            
            if kdsdAGOb != 'False':
                self.kdsdAGOb[AGObInd1,AGObInd2] = kdsdAGOb
            
            if ic != 'False':
                self.AGOb_ic[AGObInd1,AGObInd2] = ic
                self.initialcheck[6*self.N+8*self.N**2:+(self.N*AGObInd1) + AGObInd2] += 1
        
        # AND gate:Fuel complex b
        elif AGFbs:
            AGFbIndf = re.findall("\d+",name.lower())
            AGFbInd1 = int(AGFbIndf[0])-1
            
            if ic != 'False':
                self.AGFb_ic[AGFbInd1] = ic
                self.initialcheck[6*self.N+13*self.N**2 + self.AGFbInd1] += 1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to AGFb')
             
            if kdsdAGFb != 'False':
                self.kdsdAGFb[AGFbInd1] = kdsdAGFb
            
        
        # Comparator Gate
        elif CGs:
            CGIndf = re.findall("\d+",name.lower())
            
            CGInd1 = int(CGIndf[0])-1
            CGInd2 = int(CGIndf[1])-1
            
            
            self.CGtemp_con[CGInd1,CGInd2] = DNA_con
            if ic != 'False':
                self.CG_ic[CGInd1,CGInd2] = ic
                self.initialcheck[6*self.N+10*self.N**2:+(self.N*CGInd1) + CGInd2] += 1
            
            self.CGmap[CGInd1,CGInd2] = 1
            
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to CG')
            if krsdCG != 'False':
                self.krsdCGa[CGInd1,CGInd2] = krsdCG
                self.krsdCGb[CGInd1,CGInd2] = krsdCG
            if krsdCGa != 'False':
                self.krsdCGa[CGInd1,CGInd2] = krsdCGa
            if krsdCGb != 'False':
                self.krsdCGb[CGInd1,CGInd2] = krsdCGb
            if krevCG != 'False':
                self.krevCG[:,CGInd1] = krevCG
                self.krevCG[:,CGInd2] = krevCG
            if krevCGa != 'False':
                self.krevCG[:,CGInd1] = krevCGa
            if krevCGb != 'False':
                self.krevCG[:,CGInd2] = krevCGb
            if krzCG != 'False':
                self.krzCG[CGInd1,CGInd2] = krzCG
            if ktxnCG != 'False':
                self.ktxnCG[CGInd1,CGInd2] = ktxnCG
            if kdsdCG != 'False':
                self.kdsdCG[CGInd1,CGInd2] = kdsdCG
        
        # uncleaved Comparator Gate
        elif uCGs:
            uCGIndf = re.findall("\d+",name.lower())
            uCGInd1 = int(uCGIndf[0])-1
            uCGInd2 = int(uCGIndf[1])-1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to uCG')
            if krzCG != 'False':
                self.krzCG[uCGInd1,uCGInd2] = krzCG
            if ktxnCG != 'False':
                self.ktxnCG[uCGInd1,uCGInd2] = ktxnCG
            if kdsduCG != 'False':
                self.kdsduCG[uCGInd1,uCGInd2] = kdsduCG
            
            if ic != 'False':
                self.uCG_ic[uCGInd1,uCGInd2] = ic
                self.initialcheck[6*self.N+9*self.N**2:+(self.N*uCGInd1) + uCGInd2] += 1
        
        # Comparator Gate:Output complex a
        elif CGOas:
            CGOaIndf = re.findall("\d+",name.lower())
            CGOaInd1 = int(CGOaIndf[0])-1
            CGOaInd2 = int(CGOaIndf[1])-1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to CGOa')
            if krevCG != 'False':
                self.krevCG[CGOaInd1,CGOaInd2] = krevCG
            if kdsdCG != 'False':
                self.kdsdCG[CGOaInd1,CGOaInd2] = kdsdCG
            
            if ic != 'False':
                self.CGOa_ic[CGOaInd1,CGOaInd2] = ic
                self.initialcheck[6*self.N+11*self.N**2:+(self.N*CGOaInd1) + CGOaInd2] += 1
       
        # Comparator Gate:Output complex b    
        elif CGObs:
            CGObIndf = re.findall("\d+",name.lower())
            CGObInd1 = int(CGObIndf[0])-1
            CGObInd2 = int(CGObIndf[1])-1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False':
                print('This rate constant should not be changed with respect to CGOb')
            if krevCG != 'False':
                self.krevCG[CGObInd1,CGObInd2] = krevCG
            if kdsdCG != 'False':
                self.kdsdCG[CGObInd1,CGObInd2] = kdsdCG
            
            if ic != 'False':
                self.CGOb_ic[CGObInd1,CGObInd2] = ic
                self.initialcheck[6*self.N+12*self.N**2:+(self.N*CGObInd1) + CGObInd2] += 1
        
        # Reporter Signal Complement strand
        elif Qs:
            QInd1f = re.compile("\d+")
            QInd1 = int(QInd1f.search(name.lower()).group())-1
            
            if leak != 'False' or leakA != 'False' or krz != 'False' or krsd != 'False' or krev != 'False' or krep != 'False' or krepr != 'False' or kth != 'False' or krzTG != 'False' or krsdF != 'False' or krevF != 'False' or krsdA != 'False' or krzA != 'False' or krevCG != 'False' or krevCGa!= 'False' or krevCGb!= 'False' or krsdCG != 'False' or krsdCGa != 'False' or krsdCGb != 'False' or krzCG != 'False' or ktxnO != 'False' or ktxnG != 'False' or ktxnTG != 'False' or ktxnF != 'False' or ktxnAG != 'False' or ktxnCG != 'False' or kssdO != 'False' or kssdF != 'False' or kdsduG != "False" or kdsdG != 'False' or kdsdGO != 'False' or kdsduAG != 'False' or kdsdAG != 'False' or kdsduCG != 'False' or kdsdCG != 'False' or kdrd != 'False' or khybO != 'False' or khybR != 'False' or kdsduTG != 'False' or kdsdTG != 'False' or kdsdGF != 'False' or kdsdAGOa != 'False' or kdsdAGOb != 'False' or kdsdAGFb != 'False' or kdsdCGOa != 'False' or kdsdCGOb != 'False':
                print('This rate constant should not be changed with respect to Q')
            
            if ic != 'False':
                self.Q_ic[QInd1]=ic
                self.initialcheck[7*self.N+13*self.N**2 + QInd1] += 1 

            
        else:
            print("Please check documentation for correct nomenclature")
        
        if (self.AGcheck and self.Fcheck):
            if (self.fuelInd1 == self.AGInd1):
                print('Warning: Fuel reactions do not occur with first index of an AND Gate')
        
                
    # function for simulating the model instance
    def simulate(self,t_vec,smethod='False',iteration=1):
        
        #######################################################################
        # Warnings / Error Messages
        #######################################################################
        
        # Warnings for comparator gates that share the same index in either of their input domains
        if max(np.sum(self.CGmap,axis=0)) > 1:
            print('Warning: CGs share the same index for the second input domain. Simulation results are only accurate if these indices are unique across all CGs')
        
        if max(np.sum(self.CGmap,axis=1)) > 1:
            print('Warning: CGs share the same index for the first input domain. Simulation results are only accurate if these indices are unique across all CGs')
        
        
        if iteration == 1:
        
            self.initials = np.concatenate([self.uG_ic.flatten(),self.G_ic.flatten(),self.O_ic.flatten(),self.GO_ic.flatten(),self.R_ic.flatten(),self.S_ic.flatten(),self.RO_ic.flatten(),self.uTG_ic.flatten(),self.TG_ic.flatten(),self.F_ic.flatten(),self.GF_ic.flatten(),self.uAG_ic.flatten(),self.AG_ic.flatten(),self.AGOa_ic.flatten(),self.AGOb_ic.flatten(),self.uCG_ic.flatten(),self.CG_ic.flatten(),self.CGOa_ic.flatten(),self.CGOb_ic.flatten(),self.AGFb_ic.flatten(),self.Q_ic.flatten()])
            self.initialcheckIter.append(np.asarray(list(self.initialcheck)))
            
            if smethod != 'False':
                self.solve = spi.solve_ivp(lambda t,y: rate_eqs(t,y,self.ktxnO,self.ktxnG,self.ktxnTG,self.ktxnF,self.ktxnAG,self.ktxnCG,self.krz,self.krsd,self.krev,self.krep,self.krepr,self.kth,self.krzTG,self.krsdF,self.krevF,self.krsdA,self.krzA,self.krevCG,self.krsdCGa,self.krsdCGb,self.krzCG,self.leak,self.leakA,self.Otemp_con,self.Gtemp_con,self.TGtemp_con,self.Ftemp_con,self.AGtemp_con,self.AGmap.T,self.CGtemp_con,self.CGmap,self.kssdO,self.kssdF,self.kdsduG,self.kdsdG,self.kdsdGO,self.kdsduAG,self.kdsdAG,self.kdsduCG,self.kdsdCG,self.kdsduTG,self.kdsdTG,self.kdsdGF,self.kdsdAGOa,self.kdsdAGOb,self.kdsdAGFb,self.kdsdCGOa,self.kdsdCGOb,self.kdrd,self.khybO,self.khybR,self.N),\
                                           [t_vec[0],t_vec[-1]],self.initials,t_eval=t_vec,method=smethod)
            else:
                self.solve = spi.solve_ivp(lambda t,y: rate_eqs(t,y,self.ktxnO,self.ktxnG,self.ktxnTG,self.ktxnF,self.ktxnAG,self.ktxnCG,self.krz,self.krsd,self.krev,self.krep,self.krepr,self.kth,self.krzTG,self.krsdF,self.krevF,self.krsdA,self.krzA,self.krevCG,self.krsdCGa,self.krsdCGb,self.krzCG,self.leak,self.leakA,self.Otemp_con,self.Gtemp_con,self.TGtemp_con,self.Ftemp_con,self.AGtemp_con,self.AGmap.T,self.CGtemp_con,self.CGmap,self.kssdO,self.kssdF,self.kdsduG,self.kdsdG,self.kdsdGO,self.kdsduAG,self.kdsdAG,self.kdsduCG,self.kdsdCG,self.kdsduTG,self.kdsdTG,self.kdsdGF,self.kdsdAGOa,self.kdsdAGOb,self.kdsdAGFb,self.kdsdCGOa,self.kdsdCGOb,self.kdrd,self.khybO,self.khybR,self.N),\
                                           [t_vec[0],t_vec[-1]],self.initials,t_eval=t_vec,method='LSODA')
            
            
            self.t = self.solve.t
            self.uG_simcon = self.solve.y[0:self.N**2]
            self.G_simcon = self.solve.y[self.N**2:2*self.N**2]
            self.O_simcon = self.solve.y[2*self.N**2:3*self.N**2]
            self.GO_simcon = self.solve.y[3*self.N**2:4*self.N**2]
            self.R_simcon = self.solve.y[4*self.N**2:self.N+4*self.N**2]
            self.S_simcon = self.solve.y[self.N+4*self.N**2:2*self.N+4*self.N**2]
            self.RO_simcon = self.solve.y[2*self.N+4*self.N**2:2*self.N+5*self.N**2]
            self.uTh_simcon = self.solve.y[2*self.N+5*self.N**2:3*self.N+5*self.N**2]
            self.Th_simcon = self.solve.y[3*self.N+5*self.N**2:4*self.N+5*self.N**2]
            self.F_simcon = self.solve.y[4*self.N+5*self.N**2:5*self.N+5*self.N**2]
            self.GF_simcon = self.solve.y[5*self.N+5*self.N**2:6*self.N+5*self.N**2]
            self.uAG_simcon = self.solve.y[6*self.N+5*self.N**2:6*self.N+6*self.N**2]
            self.AG_simcon = self.solve.y[6*self.N+6*self.N**2:6*self.N+7*self.N**2]
            self.AGOa_simcon = self.solve.y[6*self.N+7*self.N**2:6*self.N+8*self.N**2]
            self.AGOb_simcon = self.solve.y[6*self.N+8*self.N**2:6*self.N+9*self.N**2]
            self.uCG_simcon = self.solve.y[6*self.N+9*self.N**2:6*self.N+10*self.N**2]
            self.CG_simcon = self.solve.y[6*self.N+10*self.N**2:6*self.N+11*self.N**2]
            self.CGOa_simcon = self.solve.y[6*self.N+11*self.N**2:6*self.N+12*self.N**2]
            self.CGOb_simcon = self.solve.y[6*self.N+12*self.N**2:6*self.N+13*self.N**2]
            self.AGFb_simcon = self.solve.y[6*self.N+13*self.N**2:7*self.N+13*self.N**2]
            self.Q_simcon = self.solve.y[7*self.N+13*self.N**2:8*self.N+13*self.N**2]
        
        if iteration > 1:
                     
            self.initialsNEW = np.array(self.solve.y[:,-1])
            self.initialsOLD = np.concatenate([self.uG_ic.flatten(),self.G_ic.flatten(),self.O_ic.flatten(),self.GO_ic.flatten(),self.R_ic.flatten(),self.S_ic.flatten(),self.RO_ic.flatten(),self.uTG_ic.flatten(),self.TG_ic.flatten(),self.F_ic.flatten(),self.GF_ic.flatten(),self.uAG_ic.flatten(),self.AG_ic.flatten(),self.AGOa_ic.flatten(),self.AGOb_ic.flatten(),self.uCG_ic.flatten(),self.CG_ic.flatten(),self.CGOa_ic.flatten(),self.CGOb_ic.flatten(),self.AGFb_ic.flatten(),self.Q_ic.flatten()])
            self.initialcheckIter.append(np.asarray(list(self.initialcheck)))
            
            
            
            for i in range(len(self.initialsOLD)):
                if self.initialcheckIter[iteration-1][i] != self.initialcheckIter[iteration-2][i]:
                    self.initialsNEW[i] = self.initialsOLD[i]
            
            
            
            if smethod != 'False':
                
                self.solveNEW = spi.solve_ivp(lambda t,y: rate_eqs(t,y,self.ktxnO,self.ktxnG,self.ktxnTG,self.ktxnF,self.ktxnAG,self.ktxnCG,self.krz,self.krsd,self.krev,self.krep,self.krepr,self.kth,self.krzTG,self.krsdF,self.krevF,self.krsdA,self.krzA,self.krevCG,self.krsdCGa,self.krsdCGb,self.krzCG,self.leak,self.leakA,self.Otemp_con,self.Gtemp_con,self.TGtemp_con,self.Ftemp_con,self.AGtemp_con,self.AGmap.T,self.CGtemp_con,self.CGmap,self.kssdO,self.kssdF,self.kdsduG,self.kdsdG,self.kdsdGO,self.kdsduAG,self.kdsdAG,self.kdsduCG,self.kdsdCG,self.kdsduTG,self.kdsdTG,self.kdsdGF,self.kdsdAGOa,self.kdsdAGOb,self.kdsdAGFb,self.kdsdCGOa,self.kdsdCGOb,self.kdrd,self.khybO,self.khybR,self.N),\
                                              [t_vec[0],t_vec[-1]],self.initialsNEW,t_eval=t_vec,method=smethod)
            else:
                self.solveNEW = spi.solve_ivp(lambda t,y: rate_eqs(t,y,self.ktxnO,self.ktxnG,self.ktxnTG,self.ktxnF,self.ktxnAG,self.ktxnCG,self.krz,self.krsd,self.krev,self.krep,self.krepr,self.kth,self.krzTG,self.krsdF,self.krevF,self.krsdA,self.krzA,self.krevCG,self.krsdCGa,self.krsdCGb,self.krzCG,self.leak,self.leakA,self.Otemp_con,self.Gtemp_con,self.TGtemp_con,self.Ftemp_con,self.AGtemp_con,self.AGmap.T,self.CGtemp_con,self.CGmap,self.kssdO,self.kssdF,self.kdsduG,self.kdsdG,self.kdsdGO,self.kdsduAG,self.kdsdAG,self.kdsduCG,self.kdsdCG,self.kdsduTG,self.kdsdTG,self.kdsdGF,self.kdsdAGOa,self.kdsdAGOb,self.kdsdAGFb,self.kdsdCGOa,self.kdsdCGOb,self.kdrd,self.khybO,self.khybR,self.N),\
                                              [t_vec[0],t_vec[-1]],self.initialsNEW,t_eval=t_vec,method='LSODA')
            
            self.solve.t = np.concatenate([self.solve.t,self.solveNEW.t])
            self.solve.y = np.concatenate([self.solve.y,self.solveNEW.y],axis=1)
            
            #self.solve.t = self.solveNEW.t
            #self.solve.y = self.solveNEW.y
            
            self.t = self.solve.t
            self.uG_simcon = self.solve.y[0:self.N**2]
            self.G_simcon = self.solve.y[self.N**2:2*self.N**2]
            self.O_simcon = self.solve.y[2*self.N**2:3*self.N**2]
            self.GO_simcon = self.solve.y[3*self.N**2:4*self.N**2]
            self.R_simcon = self.solve.y[4*self.N**2:self.N+4*self.N**2]
            self.S_simcon = self.solve.y[self.N+4*self.N**2:2*self.N+4*self.N**2]
            self.RO_simcon = self.solve.y[2*self.N+4*self.N**2:2*self.N+5*self.N**2]
            self.uTh_simcon = self.solve.y[2*self.N+5*self.N**2:3*self.N+5*self.N**2]
            self.Th_simcon = self.solve.y[3*self.N+5*self.N**2:4*self.N+5*self.N**2]
            self.F_simcon = self.solve.y[4*self.N+5*self.N**2:5*self.N+5*self.N**2]
            self.GF_simcon = self.solve.y[5*self.N+5*self.N**2:6*self.N+5*self.N**2]
            self.uAG_simcon = self.solve.y[6*self.N+5*self.N**2:6*self.N+6*self.N**2]
            self.AG_simcon = self.solve.y[6*self.N+6*self.N**2:6*self.N+7*self.N**2]
            self.AGOa_simcon = self.solve.y[6*self.N+7*self.N**2:6*self.N+8*self.N**2]
            self.AGOb_simcon = self.solve.y[6*self.N+8*self.N**2:6*self.N+9*self.N**2]
            self.uCG_simcon = self.solve.y[6*self.N+9*self.N**2:6*self.N+10*self.N**2]
            self.CG_simcon = self.solve.y[6*self.N+10*self.N**2:6*self.N+11*self.N**2]
            self.CGOa_simcon = self.solve.y[6*self.N+11*self.N**2:6*self.N+12*self.N**2]
            self.CGOb_simcon = self.solve.y[6*self.N+12*self.N**2:6*self.N+13*self.N**2]
            self.AGFb_simcon = self.solve.y[6*self.N+13*self.N**2:7*self.N+13*self.N**2]
            self.Q_simcon = self.solve.y[7*self.N+13*self.N**2:8*self.N+13*self.N**2]
        
    def output_concentration(self,name):
        inp = re.compile("(i|in|inp|input)\{\w*\d+\w*\}")
        inps = inp.fullmatch(name.lower())
        rep = re.compile("(r|rep|reporter)\{\w*\d+\w*\}")
        reps = rep.fullmatch(name.lower())
        out = re.compile("(o|out|output)\{\w*\d+\w*\,\w*\d+\w*\}")
        outs = out.fullmatch(name.lower())
        gate = re.compile("(g|gate)\{\w*\d+\w*\,\w*\d+\w*\}")
        gates = gate.fullmatch(name.lower())
        
        uG = re.compile("ug\{\w*\d+\w*\,\w*\d+\w*\}")
        uGs = uG.fullmatch(name.lower())
        GI = re.compile("gi\{\w*\d+\w*\}")
        GIs = GI.fullmatch(name.lower())
        GO = re.compile("go\{\w*\d+\w*\,\w*\d+\w*\}")
        GOs = GO.fullmatch(name.lower())
        RO = re.compile("ro\{\w*\d+\w*\,\w*\d+\w*\}")
        ROs = RO.fullmatch(name.lower())
        S =  re.compile("s\{\w*\d+\w*\}")
        Ss = S.fullmatch(name.lower())
        Q = re.compile("q\{\w*\d+\w*\}")
        Qs = Q.fullmatch(name.lower())
        
        
        uTh = re.compile("utg|ut|uth\{\w*\d+\w*\}")
        uThs = uTh.fullmatch(name.lower())
        thresh = re.compile("(tg|t|th)\{\w*\d+\w*\}")
        threshs = thresh.fullmatch(name.lower())
        
        fuel = re.compile("f\{\w*\d+\w*\}")
        fuels = fuel.fullmatch(name.lower())
        GF = re.compile("f\{\w*\d+\w*\}")
        GFs = GF.fullmatch(name.lower())
        
        #AG = re.compile("ag\{\w*\d+(\.\d+)+\,\w*\d+\w*\}")
        uAG = re.compile("uag\{\w*\d+\w*(\.|\&)\w*\d+\w*\,\w*\d+\w*\}")
        uAGs = uAG.fullmatch(name.lower())
        AG = re.compile("(ag|g|gate)\{\w*\d+\w*(\.|\&)\w*\d+\w*\,\w*\d+\w*\}")
        AGs = AG.fullmatch(name.lower())
        AGOa = re.compile("agoa\{\w*\d+\w*\,\w*\d+\w*\}")
        AGOas = AGOa.fullmatch(name.lower())
        AGOb = re.compile("agob\{\w*\d+\w*\,\w*\d+\w*\}")
        AGObs = AGOb.fullmatch(name.lower())
        
        #AGFa  = re.compile("agfa\{\w*\d+\w*\,\w*\d+\w*\}")
        #AGFas = AGFa.fullmatch(name.lower())
        AGFb = re.compile("agfb\{\w*\d+\w*\}")
        AGFbs = AGFb.fullmatch(name.lower())
        
        uCG = re.compile("ucg\{\w*\d+\w*\,\w*\d+\w*\}")
        uCGs = uCG.fullmatch(name.lower())
        CG = re.compile("cg\{\w*\d+\w*\,\w*\d+\w*\}")
        CGs = CG.fullmatch(name.lower())
        CGOa = re.compile("cgoa\{\w*\d+\w*\,\w*\d+\w*\}")
        CGOas = CGOa.fullmatch(name.lower())
        CGOb = re.compile("cgob\{\w*\d+\w*\,\w*\d+\w*\}")
        CGObs = CGOb.fullmatch(name.lower())
        
        
        if inps:
            inpInd1f = re.compile("\d+")
            inpInd1 = int(inpInd1f.search(name.lower()).group())-1
            
            return(self.O_simcon[self.N*inpInd1 + inpInd1])
                
            
        elif reps:
            repInd1f = re.compile('\d+')
            repInd1 = int(repInd1f.search(name.lower()).group())-1
            
            return(self.R_simcon[repInd1])
        elif outs:
            outIndf = re.findall("\d+",name.lower())

            outInd1 = int(outIndf[0])-1
            outInd2 = int(outIndf[1])-1
            
            return(self.O_simcon[self.N*outInd1 + outInd2])
        
            
        elif gates:
            gateIndf = re.findall("\d+",name.lower())

            gateInd1 = int(gateIndf[0])-1
            gateInd2 = int(gateIndf[1])-1
            
            return(self.G_simcon[self.N*gateInd1 + gateInd2])
    
        
        elif uGs:
            uGIndf = re.findall("\d+",name.lower())
            uGInd1 = int(uGIndf[0])-1
            uGInd2 = int(uGIndf[1])-1
            
            return(self.uG_simcon[self.N*uGInd1 + uGInd2])        
            
        elif GIs:
            GIInd1f = re.compile("\d+")
            GIInd1 = int(GIInd1f.search(name.lower()).group())-1
            
            return(self.GO_simcon[self.N*GIInd1 + GIInd1])
        elif GOs:
            GOIndf = re.findall("\d+",name.lower())
            GOInd1 = int(GOIndf[0])-1
            GOInd2 = int(GOIndf[1])-1
            
            return(self.GO_simcon[self.N*GOInd1 + GOInd2])
            
        elif ROs:
            ROIndf = re.findall("\d+",name.lower())
            ROInd1 = int(ROIndf[0])-1
            ROInd2 = int(ROIndf[1])-1
            
            
            return(self.RO_simcon[self.N*ROInd1 + ROInd2])
        elif Ss:
            SInd1f = re.compile("\d+")
            SInd1 = int(SInd1f.search(name.lower()).group())-1
                
            return(self.S_simcon[SInd1])
        
        elif Qs:
            QIndf = re.findall("\d+",name.lower())
            QInd1 = int(QIndf[0])-1
            
            
            return(self.Q_simcon[QInd1])
        
        elif uThs:
            uThInd1f = re.compile("\d+")
            uThInd1 = int(uThInd1f.search(name.lower()).group())-1
                     
            return(self.uTh_simcon[uThInd1])
        
        elif threshs:
            threshInd1f = re.compile("\d+")
            threshInd1 = int(threshInd1f.search(name.lower()).group())-1
               
            return(self.Th_simcon[threshInd1])
        
        elif fuels:
            fuelInd1f = re.compile("\d+")
            fuelInd1 = int(fuelInd1f.search(name.lower()).group())-1
            
            return(self.F_simcon[fuelInd1])
                
        elif GFs:
            GFInd1f = re.compile("\d+")
            GFInd1 = int(GFInd1f.search(name.lower()).group())-1
            
            return(self.GF_simcon[GFInd1]) 
        elif AGs:
            AGIndf = re.findall("\d+",name.lower())
            AGInd1 = int(AGIndf[0])-1
            AGInd2 = int(AGIndf[-1])-1
            
            
            return(self.AG_simcon[self.N*AGInd1 + AGInd2])
        
        elif uAGs:
            uAGIndf = re.findall("\d+",name.lower())
            uAGInd1 = int(uAGIndf[0])-1
            uAGInd2 = int(uAGIndf[-1])-1
            
            return(self.uAG_simcon[self.N*uAGInd1 + uAGInd2])
        
        elif AGOas:
            AGOaIndf = re.findall("\d+",name.lower())
            AGOaInd1 = int(AGOaIndf[0])-1
            AGOaInd2 = int(AGOaIndf[1])-1
            
            return(self.AGOa_simcon[self.N*AGOaInd1 + AGOaInd2])
        
        elif AGObs:
            AGObIndf = re.findall("\d+",name.lower())
            AGObInd1 = int(AGObIndf[0])-1
            AGObInd2 = int(AGObIndf[1])-1
            
            return(self.AGOb_simcon[self.N*AGObInd1 + AGObInd2])
        
        elif AGFbs:
            AGFbIndf = re.findall("\d+",name.lower())
            AGFbInd1 = int(AGFbIndf[0])-1
            
            
            return(self.AGFb_simcon[AGFbInd1])
        
        elif CGs:
            CGIndf = re.findall("\d+",name.lower())
            
            CGInd1 = int(CGIndf[0])-1
            CGInd2 = int(CGIndf[1])-1
           
            return(self.CG_simcon[self.N*CGInd1 + CGInd2])
            
            
                
        elif uCGs:
            uCGIndf = re.findall("\d+",name.lower())
            uCGInd1 = int(uCGIndf[0])-1
            uCGInd2 = int(uCGIndf[1])-1
            
            return(self.uCG_simcon[self.N*uCGInd1 + uCGInd2])
            
            
            
        elif CGOas:
            CGOaIndf = re.findall("\d+",name.lower())
            CGOaInd1 = int(CGOaIndf[0])-1
            CGOaInd2 = int(CGOaIndf[1])-1
            
            return(self.CGOa_simcon[self.N*CGOaInd1 + CGOaInd2])
            
        
        elif CGObs:
            CGObIndf = re.findall("\d+",name.lower())
            CGObInd1 = int(CGObIndf[0])-1
            CGObInd2 = int(CGObIndf[1])-1
            
            return(self.CGOb_simcon[self.N*CGObInd1 + CGObInd2])     
                        
        
        else:
            print("Please check documentation for correct nomenclature")
            
            
    def transcription_calibration(self,simTime,data,ktxn='False'):
        
        '''
        #######################################################################
        This function is very narrowly defined
        - it references the simulator name so if new verions are added the
          import statement below needs updated
        - This is also hardcoded for a 500 nM reporter and 25 nM output template
        #######################################################################
        '''
        
        
        if ktxn != 'False':
            
            self.plotCheck1 = True
            
            if self.plotCheck2 == True:
                plt.figure()
            else:
                plt.figure(1)
            
            
            
            import ctRSD_simulator_200 as RSDs #import simulator

            fs = 12 #fontsize

            # Modeling
            if type(ktxn) != list:
                k_txn = [ktxn] #transcription rates
            else:
                k_txn = ktxn

            REP_con = 500 #reporter concentration

            model = RSDs.RSD_sim(5) # define the model instance and # of domains

            # initialize species involved in the reaction
            model.molecular_species('O{1,2}',DNA_con=25) 
            model.molecular_species('REP{2}',DNA_con=REP_con)
            
            
            for n in range(len(k_txn)):           
            
                model.global_rate_constants(ktxn=k_txn[n]) #globally changes transcription rates
                
                # run simulaton (input is simulaton time)
                model.simulate(simTime,smethod='LSODA')
                
                # pull out the species from the model solution to plot
                S2 = model.output_concentration('S{2}')
                    
            
                if len(k_txn) <= 4:
                    plt.subplot(2,4,1+n)
                    if (1+n) == 1:
                        plt.ylabel('Reacted reporter (%)',fontsize=fs)
                    ax1 = plt.gca()
                    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
                    ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
                else:
                    if (1+n) <= (len(k_txn) / 2):
                        plt.subplot(3,int(math.ceil(len(k_txn)/2)),1+n)
                    else:
                        plt.subplot(3,int(math.ceil(len(k_txn)/2)),int(math.ceil((n+1)-len(k_txn)/2))+2*int(math.ceil(len(k_txn)/2)))   
                    ax1 = plt.gca()
                    ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
                    plt.tick_params(labelleft=False)
                    if (1+n) == 1 or (1+int(math.ceil((n+1)-len(k_txn)/2))+2*int(math.ceil(len(k_txn)/2))) % (int(math.ceil(len(k_txn)/2)) + 1) == 0:
                        plt.ylabel('Reacted reporter (%)',fontsize=fs)
                        plt.tick_params(labelleft=True, left=True)
                        ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
                    
   
                plt.plot(model.t/60,(data/REP_con)*100,color='aqua',linewidth=2,linestyle='-')
                plt.plot(model.t/60,(S2/REP_con)*100,color='orange',linewidth=2,linestyle='--')
                plt.xticks(fontsize=fs)
                plt.yticks(fontsize=fs)
                plt.ylim(-10,110)
                plt.xlim(0,120)
                ax1 = plt.gca()
                ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
                ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
                plt.xlabel('Time (min)',fontsize=fs)    
                plt.title('k='+str(k_txn[n]))
                plt.legend(['Raw Data','Calibrated'],frameon=False)
                
            
            
        
        else:
            
            self.plotCheck2 = True
            
            if self.plotCheck1 == True:
                plt.figure()
            else:
                plt.figure(1)
            
            
            
            import ctRSD_simulator_200 as RSDs #import simulator

            fs = 12 #fontsize

            # Modeling

            k_txn = [0.005,0.0075,0.01,0.0125,.015,.02] #transcription rates

            REP_con = 500 #reporter concentration

            model = RSDs.RSD_sim(5) # define the model instance and # of domains

            # initialize species involved in the reaction
            model.molecular_species('O{1,2}',DNA_con=25) 
            model.molecular_species('REP{2}',DNA_con=REP_con)
             
            
            for n in range(len(k_txn)):
                
                model.global_rate_constants(ktxn=k_txn[n]) #globally changes transcription rates
                
                # run simulaton (input is simulaton time)
                model.simulate(simTime,smethod='LSODA')
                
                # pull out the species from the model solution to plot
                S2 = model.output_concentration('S{2}')
                if (1+2*n > 5):
                    plt.subplot(3,5,1+2*n+4)
                    
                else:                   
                    plt.subplot(3,5,1+2*n)
                 
                plt.plot(model.t/60,(data/REP_con)*100,color='aqua',linewidth=2,linestyle='-')
                plt.plot(model.t/60,(S2/REP_con)*100,color='orange',linewidth=2,linestyle='--')
                plt.xticks(fontsize=fs)
                plt.yticks(fontsize=fs)
                plt.ylim(-10,110)
                plt.xlim(0,120)
                ax1 = plt.gca()
                ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
                #ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
                ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
                plt.xlabel('Time (min)',fontsize=fs)
                plt.ylabel('Reacted reporter (%)',fontsize=fs)
                plt.legend(['Raw Data','Calibrated'],frameon=False)
                plt.title('k='+str(k_txn[n]))
                
            
        

    def ctRSD_seq_compile(self,name,filepath,Rz='Ro',L='L',term='T7t',hp5='5hp',prom='T7p',\
                                             eI='',eO='',s='',invert=0,invL='A',agL='TA',AGiloop=5,otype=1,\
                                             rna=0,us=[],ds=[],temp_len=0):
        
        '''
        TO ADD:
            AND gate output generator? 
            Custom sequence input options for some of the optional variables
                If the key provided doesnt match then assume it is custom seq to insert
            
        '''
        
        th_d = xlsheet_to_dict(filepath, 'th', 1)  # toehold sequences
        I_BM_d = xlsheet_to_dict(filepath, 'I BM', 1) # input branch migration seqeuences
        O_BM_d = xlsheet_to_dict(filepath, 'O BM', 1) # output branch migration seqeuences
        r_d = xlsheet_to_dict(filepath, 'r', 1)  # reversible domain on reporters
        L_d = xlsheet_to_dict(filepath, 'L', 1)  # Linker for ribozyme
        e_d = xlsheet_to_dict(filepath, 'e', 1) # extended branch migration domain
        Rz_d = xlsheet_to_dict(filepath, 'Rz', 1)  # ribozymes
        term_d = xlsheet_to_dict(filepath, 'terminators', 1)  # terminators
        prom_d = xlsheet_to_dict(filepath, 'promoters', 1)  # promoters
        hp5_d = xlsheet_to_dict(filepath, '5hp', 1)  # 5' hairpin sequences
        s_d = xlsheet_to_dict(filepath, 's', 1)  # spacer sequences
        us_d = xlsheet_to_dict(filepath, 'US', 1) # sequences upstream of promoter
        ds_d = xlsheet_to_dict(filepath, 'DS', 1) # sequences downstream of terminator
        
        # converting into th' as code was originally written to handle that
        for n in th_d.keys():
            th_d[n] = [rc_seq(th_d[n][0])[1:-1]]

        i_th = ''
        o_th = ''
        i_bm = ''
        o_bm = ''
        
        #gate = re.compile("(g|gate)\{\w\d+(\-\d+)*e*\,\w\d+(\-\d+)*(r*|e*)\}")
        gate = re.compile("(g|gate)\{\w+\d+(\-\d+)*e*\,\w+\d+(\-\d+)*(r*|e*)\}")
        gates = gate.fullmatch(name.lower())
        
        AG = re.compile("(ag|g|gate)\{\w\d+(\-\d+)*(\.|\&)\w\d+(\-\d+)*e*\,\w\d+(\-\d+)*(r*|e*)\}")
        AGs = AG.fullmatch(name.lower())
        
        inp = re.compile("(i|in|inp|input)\{\w\d+(\-\d+)*(r*|e*)\}")
        inps = inp.fullmatch(name.lower())
        
        outp = re.compile("(o|out|output)\{\w*\d+(\-\d+)*e*\,\w\d+(\-\d+)*(r*|e*)\}")
        outps = outp.fullmatch(name.lower())
        
        thresh = re.compile("(tg|t|th)\{\w\d+(\-\d+)*(r*|e*)\}")
        threshs = thresh.fullmatch(name.lower())
        
        fuel = re.compile("f\{\w\d+(\-\d+)*e*\}")
        fuels = fuel.fullmatch(name.lower())
        
        CG = re.compile("cg\{\w\d+(\-\d+)*\,\w\d+(\-\d+)*\}")
        CGs = CG.fullmatch(name.lower())
        
        if threshs:
           EcheckInp = re.compile("e\}")
           EcheckInps = EcheckInp.search(name.lower())
           EcheckOuts = 0
        else:
            EcheckInp = re.compile("e\,")
            EcheckInps = EcheckInp.search(name.lower())
            
            EcheckOut = re.compile("e\}")
            EcheckOuts = EcheckOut.search(name.lower())
        
        if (eI == '' and EcheckInps) or (eO == '' and EcheckOuts):
            print('e included in species name, but no domain number was provided in function declaration.')
            return('Function terminated, see error.')
        
        
        if gates:
            '''
            ###################################################################
            GATES
            ###################################################################
            '''
            
            dashcheckInp = re.compile("\-\d+e*\,")
            dashcheckInps = dashcheckInp.search(name.lower())
            
            dashcheckOut = re.compile("\-\d+(r*|e*)\}")
            dashcheckOuts = dashcheckOut.search(name.lower())
            
            EcheckInp = re.compile("e\,")
            EcheckInps = EcheckInp.search(name.lower())
            
            EcheckOut = re.compile("e\}")
            EcheckOuts = EcheckOut.search(name.lower())
            
            Indf = re.findall("[a-z]+\d+",name.lower())
            dashIndf = re.findall("\-\d+",name.lower())
 
            RcheckOut = re.compile("r\}")
            RcheckOuts = RcheckOut.search(name.lower())
            
            if dashcheckInps and dashcheckOuts:
                i_th = Indf[0]
                o_th = Indf[1]
                i_bm = 'D'+dashIndf[0][1:]
                o_bm = 'D'+dashIndf[1][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[1][1:]
                
            elif dashcheckInps:
                i_th = Indf[0]
                o_th = Indf[1][0]
                i_bm = 'D'+dashIndf[0][1:]
                o_bm = 'D'+Indf[1][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[1][1:]
                
            elif dashcheckOuts:
                i_th = Indf[0][0]
                o_th = Indf[1]
                i_bm = 'D'+Indf[0][1:]
                o_bm = 'D'+dashIndf[0][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[0][1:]
                    
            else:
                i_th = Indf[0][0]
                o_th = Indf[1][0]
                i_bm = 'D'+Indf[0][1:]
                o_bm = 'D'+Indf[1][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[1][1:]
                    
            if EcheckInps and EcheckOuts:
                eI = 'e'+eI
                eO = 'e'+eO
                
                ei_S = e_d[eI][0]
                ei_Sp = rc_seq(e_d[eI][0])[1:-1]
                eo_S = e_d[eO][0] 
            
            elif EcheckInps:
                eI = 'e'+eI
                
                ei_S = e_d[eI][0]
                ei_Sp = rc_seq(e_d[eI][0])[1:-1]
                eo_S = '' 
            
            elif EcheckOuts:
                eO = 'e'+eO
                
                ei_S = ''
                ei_Sp = ''
                eo_S = e_d[eO][0]
                
            else:
                ei_S = ''
                ei_Sp = ''
                eo_S = ''    
            
            if RcheckOuts:
                r_S = r_d[r_k][0]
            else:
                r_S = ''
                
            if len(s) == 0:
                s_S = ''
            else:
                s_S = s_d[s][0]
                
            if len(us) == 0:
                us_S = ''
            else:
                us_S = ''
                for n in range(len(us)):
                    us_S = us_S + us_d[us[n]][0]
                    
            if len(ds) == 0:
                ds_S = ''
            else:
                ds_S = ''
                for n in range(len(ds)):
                    ds_S = ds_S + ds_d[ds[n]][0]
            
            #Extracted sequences    
            o_bm_S = O_BM_d[o_bm][0]
            o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
            i_bm_S = I_BM_d[i_bm][0]
            i_th_S = th_d[i_th][0]
            i_bm_Sp = rc_seq(O_BM_d[i_bm][0])[1:-1]
            o_th_S = th_d[o_th][0]
            # from optional inputs
            hp5_S = hp5_d[hp5][0]
            l_S = L_d[L][0]
            rz_S = Rz_d[Rz][0]
            term_S = term_d[term][0]
            prom_S = prom_d[prom][0]
            
            #Adding an indication of the Rz cleavage site for RNAs
            if rna == 1 and Rz[0].lower() != 'x':
                cl = '|'
            else:
                cl =''

            
            ###################################################################
            # Stitching gate sequences
            ###################################################################
            
            if invert == 0:
            
                ctRSD_part = hp5_S +\
                             r_S + eo_S + o_bm_S + o_th_Sp + ei_S + i_bm_S +\
                             l_S + cl + rz_S +\
                             s_S + i_th_S + i_bm_Sp + ei_Sp + o_th_S +\
                             term_S
                
                template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
                
            elif invert == 1:
                    
                ctRSD_part = hp5_S +\
                             s_S + i_th_S + i_bm_Sp + ei_Sp + o_th_S +\
                             l_S + cl + rz_S + invL +\
                             r_S + eo_S + o_bm_S + o_th_Sp + ei_S + i_bm_S +\
                             term_S
                
                template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
        
        elif outps:
            '''
            ###################################################################
            OUTPUTS
            ###################################################################
            '''
            
            dashcheckInp = re.compile("\-\d+e*\,")
            dashcheckInps = dashcheckInp.search(name.lower())
            
            dashcheckOut = re.compile("\-\d+(r*|e*)\}")
            dashcheckOuts = dashcheckOut.search(name.lower())
            
            EcheckInp = re.compile("e\,")
            EcheckInps = EcheckInp.search(name.lower())
            
            EcheckOut = re.compile("e\}")
            EcheckOuts = EcheckOut.search(name.lower())
            
            Indf = re.findall("[a-z]*\d+",name.lower())
            dashIndf = re.findall("\-\d+",name.lower())
            
            RcheckOut = re.compile("r\}")
            RcheckOuts = RcheckOut.search(name.lower())
            
            if dashcheckInps and dashcheckOuts:
                o_th = Indf[2]
                i_bm = 'D'+dashIndf[0][1:]
                o_bm = 'D'+dashIndf[1][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[-1][1:]
                
            elif dashcheckInps:
                o_th = Indf[-1][0]
                i_bm = 'D'+dashIndf[0][1:]
                o_bm = 'D'+Indf[-1][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[-1][1:]
                
            elif dashcheckOuts:
                o_th = Indf[1]
                if len(re.findall("[a-z]\d+",Indf[0].lower()))==0:
                    i_bm = 'D'+Indf[0][:]
                else:
                    i_bm = 'D'+Indf[0][1:]
                o_bm = 'D'+dashIndf[0][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[-1][1:]
                    
            else:
                o_th = Indf[1][0]
                if len(re.findall("[a-z]\d+",Indf[0].lower()))==0:
                    i_bm = 'D'+Indf[0][:]
                else:
                    i_bm = 'D'+Indf[0][1:]
                o_bm = 'D'+Indf[1][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[-1][1:]
                    
            if EcheckInps and EcheckOuts:
                eI = 'e'+eI
                eO = 'e'+eO
                
                ei_S = e_d[eI][0]
                ei_Sp = rc_seq(e_d[eI][0])[1:-1]
                eo_S = e_d[eO][0] 
            
            elif EcheckInps:
                eI = 'e'+eI
                
                ei_S = e_d[eI][0]
                ei_Sp = rc_seq(e_d[eI][0])[1:-1]
                eo_S = '' 
            
            elif EcheckOuts:
                eO = 'e'+eO
                
                ei_S = ''
                ei_Sp = ''
                eo_S = e_d[eO][0]
                
            else:
                ei_S = ''
                ei_Sp = ''
                eo_S = ''    
            
            if RcheckOuts:
                r_S = r_d[r_k][0]
            else:
                r_S = ''
                
            if len(s) == 0:
                s_S = ''
            else:
                s_S = s_d[s][0]
                
            if len(us) == 0:
                us_S = ''
            else:
                us_S = ''
                for n in range(len(us)):
                    us_S = us_S + us_d[us[n]][0]
                    
            if len(ds) == 0:
                ds_S = ''
            else:
                ds_S = ''
                for n in range(len(ds)):
                    ds_S = ds_S + ds_d[ds[n]][0]
                    
            if otype == 1:
                rz_S = Rz_d[Rz][0]
            else:
                rz_S = ''
            
            #Extracted sequences    
            o_bm_S = O_BM_d[o_bm][0]
            o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
            i_bm_S = I_BM_d[i_bm][0]
            #i_th_S = th_d[i_th][0]
            i_bm_Sp = rc_seq(O_BM_d[i_bm][0])[1:-1]
            o_th_S = th_d[o_th][0]
            # from optional inputs
            hp5_S = hp5_d[hp5][0]
            l_S = L_d[L][0]
            term_S = term_d[term][0]
            prom_S = prom_d[prom][0]
            
            #Adding an indication of the Rz cleavage site for RNAs
            if rna == 1  and otype == 1 and Rz[0].lower() != 'x':
                cl = '|'
            else:
                cl =''

            
            ###################################################################
            # Stitching output sequences
            ###################################################################
            
            if invert == 0:
            
                ctRSD_part = hp5_S +\
                             eo_S + r_S + o_bm_S + o_th_Sp + ei_S + i_bm_S +\
                             l_S + cl + rz_S +\
                             term_S
                
                template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
                
            elif invert == 1:
                    
                ctRSD_part = hp5_S +\
                             l_S + cl + rz_S + invL +\
                             eo_S + r_S + o_bm_S + o_th_Sp + ei_S + i_bm_S +\
                             term_S
                
                template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
            
        elif AGs:
            '''
            ###################################################################
            AND GATES
            ###################################################################
            '''
            
            dashcheckInp1 = re.compile("\-\d+(\.|\&)")
            dashcheckInps1 = dashcheckInp1.search(name.lower())
            dashcheckInp2 = re.compile("\-\d+\,")
            dashcheckInps2 = dashcheckInp2.search(name.lower())
            
            dashcheckOut = re.compile("\-\d+r*\}")
            dashcheckOuts = dashcheckOut.search(name.lower())
            
            EcheckInp = re.compile("e\,")
            EcheckInps = EcheckInp.search(name.lower())
            
            EcheckOut = re.compile("e\}")
            EcheckOuts = EcheckOut.search(name.lower())
            
            RcheckOut = re.compile("r\}")
            RcheckOuts = RcheckOut.search(name.lower())
            
            Indf = re.findall("[a-z]\d+",name.lower())
            dashIndf = re.findall("\-\d+",name.lower())
            
            
            if dashcheckInps1 and dashcheckInps2 and dashcheckOuts:
                i_th1 = Indf[0]
                i_th2 = Indf[1]
                o_th = Indf[2]
                i_bm1 = 'D'+dashIndf[0][1:]
                i_bm2 = 'D'+dashIndf[1][1:]
                o_bm = 'D'+dashIndf[2][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[2][1:]
                
            elif dashcheckInps1 and dashcheckInps2:
                i_th1 = Indf[0]
                i_th2 = Indf[1]
                o_th = Indf[2][0]
                i_bm1 = 'D'+dashIndf[0][1:]
                i_bm2 = 'D'+dashIndf[1][1:]
                o_bm = 'D'+Indf[2][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[2][1:]
                
            elif dashcheckInps1 and dashcheckOuts:
                i_th1 = Indf[0]
                i_th2 = Indf[1][0]
                o_th = Indf[2]
                i_bm1 = 'D'+dashIndf[0][1:]
                i_bm2 = 'D'+Indf[1][1:]
                o_bm = 'D'+dashIndf[1][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[1][1:]
                    
            elif dashcheckInps2 and dashcheckOuts:
                i_th1 = Indf[0][0]
                i_th2 = Indf[1]
                o_th = Indf[2]
                i_bm1 = 'D'+Indf[0][1:]
                i_bm2 = 'D'+dashIndf[0][1:]
                o_bm = 'D'+dashIndf[1][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[1][1:]
            
            elif dashcheckInps1:
                i_th1 = Indf[0]
                i_th2 = Indf[1][0]
                o_th = Indf[2][0]
                i_bm1 = 'D'+dashIndf[0][1:]
                i_bm2 = 'D'+Indf[1][1:]
                o_bm = 'D'+Indf[2][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[2][1:]
                
            elif dashcheckInps2:
                i_th1 = Indf[0][0]
                i_th2 = Indf[1]
                o_th = Indf[2][0]
                i_bm1 = 'D'+Indf[0][1:]
                i_bm2 = 'D'+dashIndf[0][1:]
                o_bm = 'D'+Indf[2][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[2][1:]
            
            elif dashcheckOuts:
                i_th1 = Indf[0][0]
                i_th2 = Indf[1][0]
                o_th = Indf[2]
                i_bm1 = 'D'+Indf[0][1:]
                i_bm2 = 'D'+Indf[1][1:]
                o_bm = 'D'+dashIndf[0][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[0][1:]
                           
            else:
                i_th1 = Indf[0][0]
                i_th2 = Indf[1][0]
                o_th = Indf[2][0]
                i_bm1 = 'D'+Indf[0][1:]
                i_bm2 = 'D'+Indf[1][1:]
                o_bm = 'D'+Indf[2][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[2][1:]
        
            if EcheckInps and EcheckOuts:
                eI = 'e'+eI
                eO = 'e'+eO
                
                ei_S = e_d[eI][0]
                ei_Sp = rc_seq(e_d[eI][0])[1:-1]
                eo_S = e_d[eO][0] 
            
            elif EcheckInps:
                eI = 'e'+eI
                
                ei_S = e_d[eI][0]
                ei_Sp = rc_seq(e_d[eI][0])[1:-1]
                eo_S = '' 
            
            elif EcheckOuts:
                eO = 'e'+eO
                
                ei_S = ''
                ei_Sp = ''
                eo_S = e_d[eO][0]
                
            else:
                ei_S = ''
                ei_Sp = ''
                eo_S = ''  
                
            if RcheckOuts:
                r_S = r_d[r_k][0]
            else:
                r_S = ''
                
            if len(s) == 0:
                s_S = ''
            else:
                s_S = s_d[s][0]
                
            if len(us) == 0:
                us_S = ''
            else:
                us_S = ''
                for n in range(len(us)):
                    us_S = us_S + us_d[us[n]][0]
                    
            if len(ds) == 0:
                ds_S = ''
            else:
                ds_S = ''
                for n in range(len(ds)):
                    ds_S = ds_S + ds_d[ds[n]][0]
                
            o_bm_S = O_BM_d[o_bm][0]
            o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
            i_bm_S1 = I_BM_d[i_bm1][0]
            i_bm_S2 = I_BM_d[i_bm2][0]
            i_th_S1 = th_d[i_th1][0]
            i_th_S2 = th_d[i_th2][0]
            i_th_Sp2 = rc_seq(th_d[i_th2][0])[1:-1]
            i_bm_Sp1 = rc_seq(O_BM_d[i_bm1][0])[1:-1]
            i_bm_Sp2 = rc_seq(O_BM_d[i_bm2][0])[1:-1]
            o_th_S = th_d[o_th][0]
             # from optional inputs
            hp5_S = hp5_d[hp5][0]
            l_S = L_d[L][0]
            rz_S = Rz_d[Rz][0]
            term_S = term_d[term][0]
            prom_S = prom_d[prom][0]
            agl_S = agL
            
            #Adding an indication of the Rz cleavage site for RNAs
            if rna == 1 and Rz[0].lower() != 'x':
                cl = '|'
            else:
                cl =''

            
            ###################################################################
            # Stitching and gate sequences
            ###################################################################
            
            if invert == 0:
            
                if AGiloop == 5: # internal loop size
                    
                    ctRSD_part = hp5_S +\
                                 eo_S + r_S + o_bm_S + o_th_Sp + ei_S + i_bm_S2 + agl_S + i_th_Sp2[-1] + ei_S + i_bm_S1 +\
                                 l_S + cl + rz_S +\
                                 s_S + i_th_S1 + i_bm_Sp1 + ei_Sp + i_th_S2 + i_bm_Sp2 + ei_Sp + o_th_S +\
                                 term_S
                    
                    template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
                    
                elif AGiloop == 6: # internal loop size
                    
                    ctRSD_part = hp5_S +\
                                 eo_S + r_S + o_bm_S + o_th_Sp + ei_S + i_bm_S2 + agl_S + ei_S + i_bm_S1 +\
                                 l_S + cl + rz_S +\
                                 s_S + i_th_S1 + i_bm_Sp1 + ei_Sp + i_th_S2 + i_bm_Sp2 + ei_Sp + o_th_S +\
                                 term_S
                    
                    template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
                        
            elif invert == 1:
                 
                if AGiloop == 5: # internal loop size
                    
                    ctRSD_part = hp5_S +\
                                 s_S + i_th_S1 + i_bm_Sp1 + ei_Sp + i_th_S2 + i_bm_Sp2 + ei_Sp + o_th_S +\
                                 l_S + cl + rz_S + invL +\
                                 eo_S + r_S + o_bm_S + o_th_Sp + ei_S + i_bm_S2 + agl_S + i_th_Sp2[-1] + ei_S + i_bm_S1 +\
                                 term_S
                    
                    template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
                        
                elif AGiloop == 6: # internal loop size
                    
                    ctRSD_part = hp5_S +\
                                 s_S + i_th_S1 + i_bm_Sp1 + ei_Sp + i_th_S2 + i_bm_Sp2 + ei_Sp + o_th_S +\
                                 l_S + cl + rz_S + invL +\
                                 eo_S + r_S + o_bm_S + o_th_Sp + ei_S + i_bm_S2 + agl_S + ei_S + i_bm_S1 +\
                                 term_S
                    
                    template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
               
                
        elif inps:
            '''
            ###################################################################
            INPUTS
            ###################################################################
            '''
            
            dashcheckOut = re.compile("\-\d+(r*|e*)\}")
            dashcheckOuts = dashcheckOut.search(name.lower())
            
            EcheckOut = re.compile("e\}")
            EcheckOuts = EcheckOut.search(name.lower())
            
            Indf = re.findall("[a-z]\d+",name.lower())
            dashIndf = re.findall("\-\d+",name.lower())
                        
            RcheckOut = re.compile("r\}")
            RcheckOuts = RcheckOut.search(name.lower())
                
            if dashcheckOuts:
                o_th = Indf[0]
                o_bm = 'D'+dashIndf[0][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[0][1:]
                    
            else:
                o_th = Indf[0][0]
                o_bm = 'D'+Indf[0][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[0][1:]
                    
            if EcheckOuts:
                eO = 'e'+eO
                eo_S = e_d[eO][0]
            else:
                eo_S = ''
                
            if len(us) == 0:
                us_S = ''
            else:
                us_S = ''
                for n in range(len(us)):
                    us_S = us_S + us_d[us[n]][0]
                    
            if len(ds) == 0:
                ds_S = ''
            else:
                ds_S = ''
                for n in range(len(ds)):
                    ds_S = ds_S + ds_d[ds[n]][0]
                    
            if RcheckOuts:
                r_S = r_d[r_k][0]
            else:
                r_S = ''
                    
            o_bm_S = O_BM_d[o_bm][0]
            o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
            
            hp5_S = hp5_d[hp5][0]
            term_S = term_d[term][0]
            prom_S = prom_d[prom][0]
            
            ###################################################################
            # Stitching input sequences
            ###################################################################
            
            ctRSD_part = hp5_S + r_S + eo_S + o_bm_S + o_th_Sp + term_S
            
            template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
        
        elif threshs:
            '''
            ###################################################################
            THRESHOLD GATES
            ###################################################################
            '''
            
            dashcheckInp = re.compile("\-\d+(r*|e*)\}")
            dashcheckInps = dashcheckInp.search(name.lower())
            
            EcheckInp = re.compile("e\}")
            EcheckInps = EcheckInp.search(name.lower())
            
            Indf = re.findall("[a-z]\d+",name.lower())
            dashIndf = re.findall("\-\d+",name.lower())
            
            RcheckOut = re.compile("r\}")
            RcheckOuts = RcheckOut.search(name.lower())
            
            
            if dashcheckInps:
                i_th = Indf[0]
                i_bm = 'D'+dashIndf[0][1:]
                
                if RcheckOuts:
                    r_k = 'r'+dashIndf[0][1:]      
                
            else:
                i_th = Indf[0][0]
                i_bm = 'D'+Indf[0][1:]
                
                if RcheckOuts:
                    r_k = 'r'+Indf[0][1:]
                           
            if EcheckInps:
                eI = 'e'+eI
                
                ei_S = e_d[eI][0]
                ei_Sp = rc_seq(e_d[eI][0])[1:-1]
                eo_S = '' 
            else:
                ei_S = ''
                ei_Sp = ''
                
            if RcheckOuts:
                r_S = r_d[r_k][0]
            else:
                r_S = ''
                
            if len(s) == 0:
                s = 's4'
                s_S = s_d[s][0]
            else:
                s_S = s_d[s][0]
            
            if len(us) == 0:
                us_S = ''
            else:
                us_S = ''
                for n in range(len(us)):
                    us_S = us_S + us_d[us[n]][0]
                    
            if len(ds) == 0:
                ds_S = ''
            else:
                ds_S = ''
                for n in range(len(ds)):
                    ds_S = ds_S + ds_d[ds[n]][0]
                    
            #Extracted sequences    
            i_bm_S = I_BM_d[i_bm][0]
            i_th_S = th_d[i_th][0]
            i_bm_Sp = rc_seq(O_BM_d[i_bm][0])[1:-1]
            # from optional inputs
            hp5_S = hp5_d[hp5][0]
            l_S = L_d[L][0]
            rz_S = Rz_d[Rz][0]
            term_S = term_d[term][0]
            prom_S = prom_d[prom][0]
            
            #Adding an indication of the Rz cleavage site for RNAs
            if rna == 1 and Rz[0].lower() != 'x':
                cl = '|'
            else:
                cl =''
            
            ###################################################################
            # Stitching thresholding gate sequences
            ###################################################################
            
            if invert == 0:
            
                ctRSD_part = hp5_S +\
                             r_S + ei_S + i_bm_S +\
                             l_S + cl + rz_S +\
                             s_S + i_th_S + i_bm_Sp + ei_Sp + rc_seq(r_S)[1:-1] +\
                             term_S
                
                template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
                
            elif invert == 1:
                    
                ctRSD_part = hp5_S +\
                             s_S + i_th_S + i_bm_Sp + rc_seq(r_S)[1:-1] +\
                             l_S + cl + rz_S + invL +\
                             r_S + i_bm_S +\
                             term_S
                
                template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
                
                
        elif fuels:
            '''
            ###################################################################
            FUELS
            ###################################################################
            '''
            
            dashcheckOut = re.compile("\-\d+e*\}")
            dashcheckOuts = dashcheckOut.search(name.lower())
            
            EcheckOut = re.compile("e\}")
            EcheckOuts = EcheckOut.search(name.lower())
            
            Indf = re.findall("[a-z]\d+",name.lower())
            dashIndf = re.findall("\-\d+",name.lower())
            
                
            if dashcheckOuts:
                o_th = Indf[0]
                o_bm = 'D'+dashIndf[0][1:]
                
            else:
                o_th = Indf[0][0]
                o_bm = 'D'+Indf[0][1:]
                    
            if EcheckOuts:
                eO = 'e'+eO
                eo_S = e_d[eO][0]
            else: 
                eo_S = ''
                
            if len(us) == 0:
                us_S = ''
            else:
                us_S = ''
                for n in range(len(us)):
                    us_S = us_S + us_d[us[n]][0]
                    
            if len(ds) == 0:
                ds_S = ''
            else:
                ds_S = ''
                for n in range(len(ds)):
                    ds_S = ds_S + ds_d[ds[n]][0]
                
            # Extracted sequence domains
            o_bm_S = O_BM_d[o_bm][0]
            o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
            # from optional inputs
            hp5_S = hp5_d[hp5][0]
            term_S = term_d[term][0]
            prom_S = prom_d[prom][0]
            
            ###################################################################
            # Stitching fuel sequences
            ###################################################################
            
            ctRSD_part = hp5_S + o_th_Sp + eo_S + o_bm_S + term_S
            
            template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
                
        elif CGs:
            '''
            ###################################################################
            COMPARATOR GATES
            ###################################################################
            '''
            
            dashcheckInp = re.compile("\-\d+\,")
            dashcheckInps = dashcheckInp.search(name.lower())
            
            dashcheckOut = re.compile("\-\d+\}")
            dashcheckOuts = dashcheckOut.search(name.lower())
            
            Indf = re.findall("[a-z]\d+",name.lower())
            dashIndf = re.findall("\-\d+",name.lower())
            
            if dashcheckInps and dashcheckOuts:
                i_th = Indf[0]
                o_th = Indf[1]
                i_bm = 'D'+dashIndf[0][1:]
                o_bm = 'D'+dashIndf[1][1:]
                
            elif dashcheckInps:
                i_th = Indf[0]
                o_th = Indf[1][0]
                i_bm = 'D'+dashIndf[0][1:]
                o_bm = 'D'+Indf[1][1:]
                
            elif dashcheckOuts:
                i_th = Indf[0][0]
                o_th = Indf[1]
                i_bm = 'D'+Indf[0][1:]
                o_bm = 'D'+dashIndf[0][1:]
            
            else:
                i_th = Indf[0][0]
                o_th = Indf[1][0]
                i_bm = 'D'+Indf[0][1:]
                o_bm = 'D'+Indf[1][1:]
                
            if len(s) == 0:
                s_S = ''
            else:
                s_S = s_d[s][0]
                
            if len(us) == 0:
                us_S = ''
            else:
                us_S = ''
                for n in range(len(us)):
                    us_S = us_S + us_d[us[n]][0]
                    
            if len(ds) == 0:
                ds_S = ''
            else:
                ds_S = ''
                for n in range(len(ds)):
                    ds_S = ds_S + ds_d[ds[n]][0]
                            
            # Extracted sequence domains
            I1_bm_S = O_BM_d[i_bm][0]
            I1_bm_Sp = rc_seq(O_BM_d[i_bm][0])[1:-1]
            I2_bm_S = O_BM_d[o_bm][0]
            I2_bm_Sp = rc_seq(O_BM_d[o_bm][0])[1:-1]
            i1_th_S = th_d[i_th][0]
            i2_th_S = th_d[o_th][0]
            c_S = 'CGC'
            c_Sp = 'GTG'
            # from optional inputs
            hp5_S = hp5_d[hp5][0]
            l_S = L_d[L][0]
            rz_S = Rz_d[Rz][0]
            term_S = term_d[term][0]
            prom_S = prom_d[prom][0]
            
            #Adding an indication of the Rz cleavage site for RNAs
            if rna == 1 and Rz[0].lower() != 'x':
                cl = '|'
            else:
                cl =''
                
            if invert == 1:
                print('To invert orientation, switch first and second input domains')
            
            ###################################################################
            # Stitching comparator gate sequences
            ###################################################################
            
            ctRSD_part = hp5_S + \
                         s_S + i1_th_S + I1_bm_Sp + c_S + I2_bm_S + \
                         l_S + cl + rz_S + \
                         s_S + i2_th_S + I2_bm_Sp + c_Sp + I1_bm_S + \
                         term_S
            
            template = create_template(ctRSD_part,prom_S,rna,us_S,ds_S,temp_len)
                           
        else:
            print('Incorrect Nomenclature')
            
        
        return(template) 






