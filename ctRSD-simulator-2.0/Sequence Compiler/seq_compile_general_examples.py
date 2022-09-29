# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:58:13 2022

@author: tnm12
"""

import sys
sys.path.insert(1,'file path to location of simulator on local computer')
import ctRSD_simulator_200 as RSDs #import simulator


model = RSDs.RSD_sim() # define the model instance

# file path for ctRSD Domains List
filepath = 'file path to location of ctRSD_domains_list.xls on local computer'

'''
###############################################################################
# Specifying eBlock temps to order (need to be 300 bases long)
'''

G_temp_eB = model.ctRSD_seq_compile('G{u1,w2r}',filepath,us=['ga4'],ds=['pet','duet','exc'],temp_len=300)

I_temp_eB = model.ctRSD_seq_compile('I{u1}',filepath,us=['ga4'],ds=['duet','pet','exc'],temp_len=300)

'''
##############################################################################
# Some custom gate and input examples
'''

# A gate with an alternative ribozyme sequence
G_temp1 = model.ctRSD_seq_compile('G{u1,w2r}',filepath,Rz='R3')

# A gate with a 4 base spacer between the ribozyme and the input toehold
G_temp2 = model.ctRSD_seq_compile('G{u5,v1}',filepath,s='s4')

# A gate with a 4 base spacer between the ribozyme and the input toehold and and alternative ribozyme sequence
G_temp3 = model.ctRSD_seq_compile('G{v3,u2r}',filepath,s='s4',Rz='R3')

# A gate with an alternative terminator and 5' hairpin sequence
G_temp4 = model.ctRSD_seq_compile('G{u6,w1r}',filepath,term='T7tA',hp5='5hpT')

# A gate with an ribozyme and ribozyme linker sequence
G_temp5 = model.ctRSD_seq_compile('G{u11,w2r}',filepath,L='L2',Rz='Rg')

# Gate with inverted transcription order
G_temp6 = model.ctRSD_seq_compile('G{v1,u2r}',filepath,invert=1)

# Gate under control of the T3 promoter
G_temp7 = model.ctRSD_seq_compile('G{v1,u2r}',filepath,prom='T3')

# produce just the RNA sequence of this input
I_rna = model.ctRSD_seq_compile('I{v5}',filepath,rna=1)

'''
###############################################################################
# Specifying eBlock temps to order for outputs (need to be 300 bases long)
'''

# with Rz domain - ends with 3' L seqeuence after cleavage
O_temp_eB_w1 = model.ctRSD_seq_compile('O{1,w1r}',filepath,us=['ga4'],ds=['pet','duet','exc'],temp_len=300)

O_temp_eB_u1 = model.ctRSD_seq_compile('O{1,u1r}',filepath,us=['ga4'],ds=['pet','duet','exc'],temp_len=300)

O_temp_eB_inv = model.ctRSD_seq_compile('O{1,w2r}',filepath,invert=1,term='T7tI',us=['ga4'],ds=['pet','duet','exc'],temp_len=300)

O_temp_eB_3hp = model.ctRSD_seq_compile('O{1,w2r}',filepath,L='3hp',us=['ga4'],ds=['pet','duet','exc'],temp_len=300)


# without Rz domain - ends with terminator
O_temp_term_eB_w1 = model.ctRSD_seq_compile('O{1,w1r}',filepath,otype=0,us=['ga4'],ds=['pet','duet','exc'],temp_len=300)

O_temp_term_eB_u1 = model.ctRSD_seq_compile('O{1,u1r}',filepath,otype=0,us=['ga4'],ds=['pet','duet','exc'],temp_len=300)


'''
###############################################################################
# AND gates
'''

AG_temp1 = model.ctRSD_seq_compile('AG{u5.u4,w2r}',filepath)

# example with alternative linker between input domains (input for agL is the sequence you want used)
AG_temp2 = model.ctRSD_seq_compile('AG{u5.u4,w2r}',filepath,agL='CT')

# example with 6 base toehold loop and different linker between inputs
AG_temp3 = model.ctRSD_seq_compile('AG{u5.u4,w2r}',filepath,AGiloop=6,agL='T')

# Alternative nomenclature that also works
AG_temp4 = model.ctRSD_seq_compile('AG{u5&u4,w2r}',filepath)

# example with inverted transcription order and altenative terminator 
AG_temp5 = model.ctRSD_seq_compile('AG{u5.u4,w2r}',filepath,invert=1,term='T7t1')

'''
###############################################################################
# Fuel
'''

# fuel for a gate defined as G{u1,vX}
F_temp = model.ctRSD_seq_compile('F{v1}',filepath)

'''
###############################################################################
# Comparator gates
'''
# WARNING: The designs for these gates have not been experimentally validated

CG_temp = model.ctRSD_seq_compile('CG{v8,v9}',filepath,s='s4',L='L3')

'''
###############################################################################
# Threshold gates
'''
# WARNING: The designs for these gates have not been experimentally validated

# the 'r' domain needs to be specified for the threshold gate to be 16 bases long
TG_temp = model.ctRSD_seq_compile('TG{u1r}',filepath)



