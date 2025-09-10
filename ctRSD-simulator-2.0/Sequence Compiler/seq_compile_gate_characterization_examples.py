
import sys
sys.path.insert(1,'file path to location of simulator on local computer')
import ctRSD_simulator_200 as RSDs #import simulator


model = RSDs.RSD_sim() # define the model instance

# file path for ctRSD Domains List
filepath = '\\file path\\ctRSD_domains_list_200.xls'


'''
###############################################################################
# Figure 2A
###############################################################################
'''

G_temp_MT2A = model.ctRSD_seq_compile('G{u3,w2r}',filepath,\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
G_temp_MT2C = model.ctRSD_seq_compile('G{u3,w1r}',filepath,\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
G_temp_MT2Dl = model.ctRSD_seq_compile('G{u3,u2r}',filepath,\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
G_temp_MT2Dr = model.ctRSD_seq_compile('G{u3,u1r}',filepath,\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
I_temp_MT2 = model.ctRSD_seq_compile('I{u3}',filepath,\
                                            us=['ga4'],\
                                            ds=['duet','pet','exc'],\
                                            temp_len=300)
    

'''
###############################################################################
# Figure 3B,C toehold variants
###############################################################################
'''

# Gate: input toehold variant
G_temp_MT3B = model.ctRSD_seq_compile('G{t1-1,u2r}',filepath,\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
# Gate: output toehold variant
G_temp_MT3C = model.ctRSD_seq_compile('G{u1,t1-2r}',filepath,\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)

# input with a toehold variant sequence
I_temp_MT3B = model.ctRSD_seq_compile('I{t1-1}',filepath,\
                                            #hp5='5hpT',\
                                            us=['ga4'],\
                                            ds=['duet','pet','exc'],\
                                            temp_len=300) 
    
#######################
# v toeholds

G_temp_MT3D = model.ctRSD_seq_compile('G{v5,u2r}',filepath,\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
    
I_temp_MT3D = model.ctRSD_seq_compile('I{v5}',filepath,\
                                            #hp5='5hpT',\
                                            us=['ga4'],\
                                            ds=['duet','pet','exc'],\
                                            temp_len=300) 
    
'''
###############################################################################
# Figure 4 and SI Figure 12, ribozyme variants
###############################################################################
'''   

G_temp_MT4B = model.ctRSD_seq_compile('G{u1,w2r}',filepath,\
                                                Rz='R3',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)

G_temp_SI12 = model.ctRSD_seq_compile('G{u1,w2r}',filepath,\
                                                prom='T7p1',\
                                                L='L2',\
                                                Rz='Rg',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
'''
###############################################################################
# Figure 5D
###############################################################################
'''   
    
G_temp_MT5D = model.ctRSD_seq_compile('G{u3e,v6}',filepath,\
                                                prom='T7p',\
                                                eI='02',\
                                                Rz='R3',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
I_temp_MT5D = model.ctRSD_seq_compile('I{u3e}',filepath,\
                                            eO='02',\
                                            term='T7tA',\
                                            us=['ga4'],\
                                            ds=['duet','pet','exc'],\
                                            temp_len=300)
    
'''
###############################################################################
# Figure 6, inverted transcription order
###############################################################################
'''   

G_temp_6C_1 = model.ctRSD_seq_compile('G{u1,w2r}',filepath,\
                                                prom='T7p1',\
                                                L='L4',\
                                                invert=1,\
                                                term='T7tI',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
G_temp_6C_3 = model.ctRSD_seq_compile('G{u3,w2r}',filepath,\
                                                prom='T7p1',\
                                                invert=1,\
                                                term='T7tI',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
 
'''
###############################################################################
# SI Figure 4 extended input branch migration domains
###############################################################################
'''

G_temp_SI4B = model.ctRSD_seq_compile('G{u1e,w2r}',filepath,\
                                                prom='T7p1',\
                                                eI='2',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)


I_temp_SI4B = model.ctRSD_seq_compile('I{u1e}',filepath,\
                                            prom='T7p1',\
                                            eO='2',\
                                            us=['ga4'],\
                                            ds=['duet','pet','exc'],\
                                            temp_len=300)

G_temp_SI4C = model.ctRSD_seq_compile('G{u5e,u1e}',filepath,\
                                                prom='T7p1',\
                                                eI='2',\
                                                eO='2',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)


'''
###############################################################################
# SI Figure 15,16 gates with spacers
###############################################################################
'''

G_temp_SI15 = model.ctRSD_seq_compile('G{v1,u2r}',filepath,\
                                                Rz='R3',\
                                                s='s4',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
    
G_temp_SI16 = model.ctRSD_seq_compile('G{u3e,v6}',filepath,\
                                                Rz='R3',\
                                                eI='02',\
                                                s='s4',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
    
'''
###############################################################################
# SI Figure 19 3' hairpin linker
###############################################################################
'''
 
G_temp_SI19 = model.ctRSD_seq_compile('G{u1,w2r}',filepath,\
                                                #prom='T7p1',\
                                                L='3hp',\
                                                #Rz='Rg',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)
        
'''
###############################################################################
# SI Figure 20 alternative 5' hairpins
###############################################################################
'''

G_temp_SI20 = model.ctRSD_seq_compile('G{v1,u2r}',filepath,\
                                                hp5='pHPR1',\
                                                us=['ga4'],\
                                                ds=['pet','duet','exc'],\
                                                temp_len=300)

I_temp_SI20 = model.ctRSD_seq_compile('I{v1}',filepath,\
                                            hp5='pHPR1',\
                                            us=['ga4'],\
                                            ds=['duet','pet','exc'],\
                                            temp_len=300)
    
    
'''
###############################################################################
# SI Figure 21 terminator variants
###############################################################################
'''

G_temp_SI21_wt = model.ctRSD_seq_compile('G{u1,w2r}',filepath,\
                                                term='T7t',\
                                                us=['ga4'],\
                                                ds=['pet','pet_seq','glhp','exc'],\
                                                temp_len=300)

G_temp_SI21_0 = model.ctRSD_seq_compile('G{u1,w2r}',filepath,\
                                                term='T0t',\
                                                us=['ga4'],\
                                                ds=['pet','pet_seq','glhp','exc'],\
                                                temp_len=300)