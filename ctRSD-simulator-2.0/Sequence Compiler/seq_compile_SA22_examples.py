
import sys
sys.path.insert(1,'file path to location of simulator on local computer')
import ctRSD_simulator_200 as RSDs #import simulator


model = RSDs.RSD_sim() # define the model instance

# file path for ctRSD Domains List
filepath = 'file path to location of ctRSD_domains_list.xls on local computer'


'''
###############################################################################
# Figure 2
###############################################################################
'''

gate_1_2 = model.ctRSD_seq_compile('G{u1,w2}',filepath)

gate_1_2r = model.ctRSD_seq_compile('G{u1,w2r}',filepath)
    
I1 = model.ctRSD_seq_compile('I{u1}',filepath,ds=['pet1'])
    

'''
###############################################################################
# Figure 3
###############################################################################
'''

gate_3_2 = model.ctRSD_seq_compile('G{u3,w2}',filepath)

gate_3_2r = model.ctRSD_seq_compile('G{u3,w2r}',filepath)
    
I3 = model.ctRSD_seq_compile('I{u3}',filepath,ds=['pet1'])


gate_4_2 = model.ctRSD_seq_compile('G{u4,w2}',filepath)

gate_4_2r = model.ctRSD_seq_compile('G{u4,w2r}',filepath)
    
I4 = model.ctRSD_seq_compile('I{u4}',filepath,ds=['pet1'])
    

gate_5_2 = model.ctRSD_seq_compile('G{u5,w2}',filepath)

gate_5_2r = model.ctRSD_seq_compile('G{u5,w2r}',filepath)
    
I5 = model.ctRSD_seq_compile('I{u5}',filepath,ds=['pet1'])

'''
###############################################################################
# Figure 4 and SI Figure 24 and SI Figure 25 
###############################################################################
'''   

# AND gates

G_3AND1_2r = model.ctRSD_seq_compile('AG{u3.u1,w2r}',filepath) 
# The above gate sequence is slightly different than in the manuscript.
# In the paper the GU wobble pair was moved in domain 3 to prevent 
#    secondary structure after I{u3} binding.

G_3AND1_2_6loop = model.ctRSD_seq_compile('AG{u3.u1,w2}',filepath,AGiloop=6,agL='C')
                                                
gate_5AND4_2r = model.ctRSD_seq_compile('AG{u5.u4,w2r}',filepath)

gate_5AND4_1 = model.ctRSD_seq_compile('AG{u5.u4,u1}',filepath)

# Fuel
F1 = model.ctRSD_seq_compile('F{w1}',filepathterm='T7t1',ds=['pet1'])
    
'''
###############################################################################
# Figure 5B
###############################################################################
'''   
    
gate_5_1 = model.ctRSD_seq_compile('G{u5,u1}',filepath)

gate_4_5 = model.ctRSD_seq_compile('G{u4,u5}',filepath,term='T7t2')

gate_3_4 = model.ctRSD_seq_compile('G{u3,u4}',filepath,term='T7t2')


'''
###############################################################################
# SI Figure 30, toehold and spacer variants
###############################################################################
'''   

gate_1_2r_8a = model.ctRSD_seq_compile('G{u08-1,w2r}',filepath)

gate_1_2r_10a = model.ctRSD_seq_compile('G{u010-1,w2r}',filepath)

gate_1_2r_12a = model.ctRSD_seq_compile('G{u012-1,w2r}',filepath)

I1_4a = model.ctRSD_seq_compile('I{u04-1}',filepath,term='T7tA',ds=['pet1'])

I1_8a = model.ctRSD_seq_compile('I{u08-1}',filepath,term='T7tA',ds=['pet1'])

I1_10a = model.ctRSD_seq_compile('I{u010-1}',filepath,term='T7tA',ds=['pet1'])

