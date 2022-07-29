# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:31:11 2022

@author: tnm12
"""

import re
import numpy as np
import xlrd
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True


def ctRSD_seq_compile(name,Rz='Ro',L='L',term='T7t',hp5='5hp',eI='',eO='',s='',invert=0):

    

    input_file_loc = 'C:\\Users\\tnm12\\SURF\\SeqCompiler\\ctRSD_domains_list.xlsx'
    
    th_d = xlsheet_to_dict(input_file_loc, 'th', 1)  # toehold sequences
    # input branch migration seqeuences
    I_BM_d = xlsheet_to_dict(input_file_loc, 'I BM', 1)
    # output branch migration seqeuences
    O_BM_d = xlsheet_to_dict(input_file_loc, 'O BM', 1)
    r_d = xlsheet_to_dict(input_file_loc, 'r', 1)  # reversible domain on reporters
    L_d = xlsheet_to_dict(input_file_loc, 'L', 1)  # Linker for ribozyme
    # extended branch migration domain
    e_d = xlsheet_to_dict(input_file_loc, 'e', 1)
    Rz_d = xlsheet_to_dict(input_file_loc, 'Rz', 1)  # ribozymes
    term_d = xlsheet_to_dict(input_file_loc, 'term', 1)  # terminators
    hp5_d = xlsheet_to_dict(input_file_loc, '5hp', 1)  # 5' hairpin sequences
    # sequences upstream of promoter
    us_d = xlsheet_to_dict(input_file_loc, 'US', 1)
    # sequences downstream of terminator
    ds_d = xlsheet_to_dict(input_file_loc, 'DS', 1)







    #r_k only after output
    
    #error if eI, or eO not specfied in function declaration
    
    #e only after input and output
    
    #Input and fuel 1 output domain
    
    #threshold 1 input domain
    
    #all can have dashes
    
    #input, fuel, and threshold have eI
    
    #AG and T can have r_k, AG only in outout 
    
    #I,F,AG,CG,T
    
    i_th = ''
    o_th = ''
    i_bm = ''
    o_bm = ''
    
    gate = re.compile("(g|gate)\{\w\d+(\-\d+)*e*\,\w\d+(\-\d+)*(r*|e*)\}")
    gates = gate.fullmatch(name.lower())
    
    AG = re.compile("(ag|g|gate)\{\w\d+(\-\d+)*(\.|\&)\w\d+(\-\d+)*\,\w\d+(\-\d+)*r*\}")
    AGs = AG.fullmatch(name.lower())
    
    inp = re.compile("(i|in|inp|input)\{\w\d+(\-\d+)*e*\}")
    inps = inp.fullmatch(name.lower())
    
    thresh = re.compile("(tg|t|th)\{\w\d+(\-\d+)*(r*|e*)\}")
    threshs = thresh.fullmatch(name.lower())
    
    fuel = re.compile("f\{\w\d+(\-\d+)*e*\}")
    fuels = fuel.fullmatch(name.lower())
    
    CG = re.compile("cg\{\w\d+(\-\d+)*\,\w\d+(\-\d+)*\}")
    CGs = CG.fullmatch(name.lower())
    
    
    EcheckInp = re.compile("e\,")
    EcheckInps = EcheckInp.search(name.lower())
    
    EcheckOut = re.compile("e\}")
    EcheckOuts = EcheckOut.search(name.lower())
    
    if (eI == 0 and EcheckInps) or (eO == 0 and EcheckOuts):
        print('e included in species name, but no domain number was provided in function declaration.')
        exit()
    
    if gates:
    
        dashcheckInp = re.compile("\-\d+e*\,")
        dashcheckInps = dashcheckInp.search(name.lower())
        
        dashcheckOut = re.compile("\-\d+(r*|e*)\}")
        dashcheckOuts = dashcheckOut.search(name.lower())
        
        EcheckInp = re.compile("e\,")
        EcheckInps = EcheckInp.search(name.lower())
        
        EcheckOut = re.compile("e\}")
        EcheckOuts = EcheckOut.search(name.lower())
        
        Indf = re.findall("[a-z]\d+",name.lower())
        dashIndf = re.findall("\-\d+",name.lower())
        
        RcheckOut = re.compile("r\}")
        RcheckOuts = RcheckOut.search(name.lower())
        
        
        if dashcheckInps and dashcheckOuts:
            i_th = Indf[0]
            o_th = Indf[1]
            i_bm = 'I'+dashIndf[0][1:]
            o_bm = 'O'+dashIndf[1][1:]
            
            if RcheckOuts:
                r_k = 'r'+dashIndf[1][1:]
            
            
        elif dashcheckInps:
            i_th = Indf[0]
            o_th = Indf[1][0]
            i_bm = 'I'+dashIndf[0][1:]
            o_bm = 'O'+Indf[1][1:]
            
            if RcheckOuts:
                r_k = 'r'+Indf[1][1:]
            
        elif dashcheckOuts:
            i_th = Indf[0][0]
            o_th = Indf[1]
            i_bm = 'I'+Indf[0][1:]
            o_bm = 'O'+dashIndf[0][1:]
            
            if RcheckOuts:
                r_k = 'r'+dashIndf[0][1:]
                
            
        else:
            i_th = Indf[0][0]
            o_th = Indf[1][0]
            i_bm = 'I'+Indf[0][1:]
            o_bm = 'O'+Indf[1][1:]
            
            if RcheckOuts:
                r_k = 'r'+Indf[1][1:]
                
                
        if EcheckInps and EcheckOuts:
            eI = 'e'+eI
            eO = 'e'+eO
            
        
        elif EcheckInps:
            eI = 'e'+eI
            
        
        elif EcheckOuts:
            eO = 'e'+eO
            
            
        
        if RcheckOuts:
            r_S = r_d[r_k][0]
        else:
            r_S = ''
        o_bm_S = O_BM_d[o_bm][0]
        o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
        i_bm_S = I_BM_d[i_bm][0]
        i_th_S = th_d[i_th][0]
        i_bm_Sp = rc_seq(O_BM_d[o_bm][0])[1:-1]
        o_th_S = th_d[o_th][0]
        
            
    
        
    elif AGs:
        
        dashcheckInp1 = re.compile("\-\d+(\.|\&)")
        dashcheckInps1 = dashcheckInp1.search(name.lower())
        dashcheckInp2 = re.compile("\-\d+\,")
        dashcheckInps2 = dashcheckInp2.search(name.lower())
        
        dashcheckOut = re.compile("\-\d+r*\}")
        dashcheckOuts = dashcheckOut.search(name.lower())
        
        RcheckOut = re.compile("r\}")
        RcheckOuts = RcheckOut.search(name.lower())
        
        Indf = re.findall("[a-z]\d+",name.lower())
        dashIndf = re.findall("\-\d+",name.lower())
    
        
        
        if dashcheckInps1 and dashcheckInps2 and dashcheckOuts:
            i_th1 = Indf[0]
            i_th2 = Indf[1]
            o_th = Indf[2]
            i_bm1 = 'I'+dashIndf[0][1:]
            i_bm2 = 'I'+dashIndf[1][1:]
            o_bm = 'O'+dashIndf[2][1:]
            
            if RcheckOuts:
                r_k = 'r'+dashIndf[2][1:]
            
            
        elif dashcheckInps1 and dashcheckInps2:
            i_th1 = Indf[0]
            i_th2 = Indf[1]
            o_th = Indf[2][0]
            i_bm1 = 'I'+dashIndf[0][1:]
            i_bm2 = 'I'+dashIndf[1][1:]
            o_bm = 'O'+Indf[2][1:]
            
            if RcheckOuts:
                r_k = 'r'+Indf[2][1:]
            
        elif dashcheckInps1 and dashcheckOuts:
            i_th1 = Indf[0]
            i_th2 = Indf[1][0]
            o_th = Indf[2]
            i_bm1 = 'I'+dashIndf[0][1:]
            i_bm2 = 'I'+Indf[1][1:]
            o_bm = 'O'+dashIndf[1][1:]
            
            if RcheckOuts:
                r_k = 'r'+dashIndf[1][1:]
                
        elif dashcheckInps2 and dashcheckOuts:
            i_th1 = Indf[0][0]
            i_th2 = Indf[1]
            o_th = Indf[2]
            i_bm1 = 'I'+Indf[0][1:]
            i_bm2 = 'I'+dashIndf[0][1:]
            o_bm = 'O'+dashIndf[1][1:]
            
            if RcheckOuts:
                r_k = 'r'+dashIndf[1][1:]
        
        elif dashcheckInps1:
            i_th1 = Indf[0]
            i_th2 = Indf[1][0]
            o_th = Indf[2][0]
            i_bm1 = 'I'+dashIndf[0][1:]
            i_bm2 = 'I'+Indf[1][1:]
            o_bm = 'O'+Indf[2][1:]
            
            if RcheckOuts:
                r_k = 'r'+Indf[2][1:]
            
        elif dashcheckInps2:
            i_th1 = Indf[0][0]
            i_th2 = Indf[1]
            o_th = Indf[2][0]
            i_bm1 = 'I'+Indf[0][1:]
            i_bm2 = 'I'+dashIndf[0][1:]
            o_bm = 'O'+Indf[2][1:]
            
            if RcheckOuts:
                r_k = 'r'+Indf[2][1:]
        
        elif dashcheckOuts:
            i_th1 = Indf[0][0]
            i_th2 = Indf[1][0]
            o_th = Indf[2]
            i_bm1 = 'I'+Indf[0][1:]
            i_bm2 = 'I'+Indf[1][1:]
            o_bm = 'O'+dashIndf[0][1:]
            
            if RcheckOuts:
                r_k = 'r'+dashIndf[0][1:]
                       
        else:
            i_th1 = Indf[0][0]
            i_th2 = Indf[1][0]
            o_th = Indf[2][0]
            i_bm1 = 'I'+Indf[0][1:]
            i_bm2 = 'I'+Indf[1][1:]
            o_bm = 'O'+Indf[2][1:]
            
            if RcheckOuts:
                r_k = 'r'+Indf[2][1:]
                
    
        if RcheckOuts:
            r_S = r_d[r_k][0]
        else:
            r_S = ''
        o_bm_S = O_BM_d[o_bm][0]
        o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
        i_bm_S1 = I_BM_d[i_bm1][0]
        i_bm_S2 = I_BM_d[i_bm2][0]
        i_th_S1 = th_d[i_th1][0]
        i_th_S2 = th_d[i_th2][0]
        i_bm_Sp1 = rc_seq(O_BM_d[o_bm][0])[1:-1]
        i_bm_Sp2 = rc_seq(O_BM_d[o_bm][0])[1:-1]
        o_th_S = th_d[o_th][0]
        
                
                
    
    elif inps:
        
        dashcheckOut = re.compile("\-\d+e*\}")
        dashcheckOuts = dashcheckOut.search(name.lower())
        
        EcheckInp = re.compile("e\}")
        EcheckInps = EcheckInp.search(name.lower())
        
        Indf = re.findall("[a-z]\d+",name.lower())
        dashIndf = re.findall("\-\d+",name.lower())
        
        
            
        if dashcheckOuts:
            o_th = Indf[0]
            o_bm = 'O'+dashIndf[0][1:]
                
            
        else:
            o_th = Indf[0][0]
            o_bm = 'O'+Indf[0][1:]
                
                
        if EcheckInps:
            eI = 'e'+eI
            
            
        
        o_bm_S = O_BM_d[o_bm][0]
        o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
        o_th_S = th_d[o_th][0]
        i_bm_Sp = rc_seq(O_BM_d[o_bm][0])[1:-1]
        r_S = ''       
        i_bm_S = ''
        i_th_S = ''
        i_bm_Sp = ''
    
        
    
    elif threshs:
        
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
            i_bm = 'I'+dashIndf[0][1:]
            
            if RcheckOuts:
                r_k = 'r'+dashIndf[0][1:]
                
            
        else:
            i_th = Indf[0][0]
            i_bm = 'I'+Indf[0][1:]
            
            if RcheckOuts:
                r_k = 'r'+Indf[0][1:]
                
                  
        if EcheckInps:
            eI = 'e'+eI
            
            
            
        if RcheckOuts:
            r_S = r_d[r_k][0]
        else:
            r_S = ''
        i_bm_S = I_BM_d[i_bm][0]
        i_th_S = th_d[i_th][0]
        i_bm_Sp = ''
        o_bm_S = ''
        o_th_Sp = ''
        o_th_S = ''
            
        
        
            
    elif fuels:
        
        dashcheckOut = re.compile("\-\d+e*\}")
        dashcheckOuts = dashcheckOut.search(name.lower())
        
        EcheckInp = re.compile("e\}")
        EcheckInps = EcheckInp.search(name.lower())
        
        Indf = re.findall("[a-z]\d+",name.lower())
        dashIndf = re.findall("\-\d+",name.lower())
        
        
            
        if dashcheckOuts:
            o_th = Indf[0]
            o_bm = 'O'+dashIndf[0][1:]
                
            
        else:
            o_th = Indf[0][0]
            o_bm = 'O'+Indf[0][1:]
                
                
        if EcheckInps:
            eI = 'e'+eI
            
    
        o_bm_S = O_BM_d[o_bm][0]
        o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
        o_th_S = th_d[o_th][0]
        i_bm_Sp = rc_seq(O_BM_d[o_bm][0])[1:-1]
        r_S = ''
        i_bm_S = ''
        i_th_S = ''
        
        
        
            
    elif CGs:
        dashcheckInp = re.compile("\-\d+\,")
        dashcheckInps = dashcheckInp.search(name.lower())
        
        dashcheckOut = re.compile("\-\d+\}")
        dashcheckOuts = dashcheckOut.search(name.lower())
        
        Indf = re.findall("[a-z]\d+",name.lower())
        dashIndf = re.findall("\-\d+",name.lower())
        
        
        
        if dashcheckInps and dashcheckOuts:
            i_th = Indf[0]
            o_th = Indf[1]
            i_bm = 'I'+dashIndf[0][1:]
            o_bm = 'O'+dashIndf[1][1:]
        
            
            
        elif dashcheckInps:
            i_th = Indf[0]
            o_th = Indf[1][0]
            i_bm = 'I'+dashIndf[0][1:]
            o_bm = 'O'+Indf[1][1:]
            
    
            
        elif dashcheckOuts:
            i_th = Indf[0][0]
            o_th = Indf[1]
            i_bm = 'I'+Indf[0][1:]
            o_bm = 'O'+dashIndf[0][1:]
        
                
            
        else:
            i_th = Indf[0][0]
            o_th = Indf[1][0]
            i_bm = 'I'+Indf[0][1:]
            o_bm = 'O'+Indf[1][1:]
            
            
        
        
        o_bm_S = O_BM_d[o_bm][0]
        o_th_Sp = rc_seq(th_d[o_th][0])[1:-1]
        i_bm_S = I_BM_d[i_bm][0]
        i_th_S = th_d[i_th][0]
        i_bm_Sp = rc_seq(O_BM_d[o_bm][0])[1:-1]
        o_th_S = th_d[o_th][0]
        r_S = ''
        
            
    
       
    else:
        print('Incorrect Nomenclature')
        
    
    
    
    #Extracted sequences
    hp5_S = hp5_d[hp5][0]
    l_S = L_d[L][0]
    rz_S = Rz_d[Rz][0]
    term_S = term_d[term][0]
    ei_S = ''
    ei_Sp = ''
    eo_S = ''
    s_S = ''
    
     
    
    G_u1_w2r = hp5_S +\
        eo_S + r_S + o_bm_S + o_th_Sp + ei_S + i_bm_S +\
        l_S + rz_S +\
        s_S + i_th_S + i_bm_Sp + ei_Sp + o_th_S +\
        term_S
    
    G_temp = 'TTCTAATACGACTCACTATA' + rc_seq(G_u1_w2r, spec_out='s')[1:-1]
    
    '''
    
    Gi_u1_w2r = hp5_S +\
        s_S + i_th_S + i_bm_Sp + ei_Sp + o_th_S +\
        l_S + rz_S +\
        eo_S + r_S + o_bm_S + o_th_Sp + ei_S + i_bm_S +\
        term_S
    
    Gi_temp = 'TTCTAATACGACTCACTATA' + rc_seq(Gi_u1_w2r, spec_out='s')[1:-1]
    
    '''
    
    return(G_temp) 
    

def rc_seq(seq, spec_out='rc', rna=0):

    new_seq = '3'+seq+'5'
    new_seq = list(new_seq)
    seq = list(seq)
    ds = ''

    for i in range(len(seq)):
        if seq[i].lower() == 'u' and rna == 0:
            seq[i] = 'T'
        elif seq[i].lower() == 't' and rna == 1:
            seq[i] = 'u'
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


def xlsheet_to_dict(input_file_loc, sheet_name, ncol):

    seq_workbook = xlrd.open_workbook(input_file_loc)
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


def main():
    
    name = 'G{v4,u1}'

    seq = ctRSD_seq_compile(name)
    
    print(seq)
    
if __name__ == "__main__":
    main()