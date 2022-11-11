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
filepath = '\\file path\\ctRSD_domains_list.xls'


import xlwt
from xlwt import Workbook #Python function for writing to excel files

model = RSDs.RSD_sim() # define the model instance

# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sequences')

# names of species sequences will be compiled for
names = ['G{v4,u1}','I{u1}','TG{v2}','F{v1}','CG{u2,v1}']

# loops through this list of names
for i in range(len(names)):
    
    #calls the sequence function (output is sequence for that name)
    seq = model.ctRSD_seq_compile(names[i],filepath)
    
    # writes to spreadsheet created above
    sheet1.write(1+i, 0, names[i])
    sheet1.write(1+i,1,seq)
  
#saves this spreadsheet into current folder    
wb.save('Sequences.xls')