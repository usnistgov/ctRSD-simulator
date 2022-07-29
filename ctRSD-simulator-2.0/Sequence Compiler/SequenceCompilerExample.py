# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:58:13 2022

@author: tnm12
"""

import sys
sys.path.insert(1,'C:\\Users\\tnm12\\SURF')
import Simulatorv2021 as RSDs
import xlwt
from xlwt import Workbook



model = RSDs.RSD_sim() # define the model instance

# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sequences')

filepath = 'C:\\Users\\tnm12\\SURF\\SeqCompiler\\ctRSD_domains_list.xlsx'

names = ['G{v4,u1}','I{u1}','TG{v2}','F{v1}','CG{u2,v1}']

for i in range(len(names)):

    seq = model.ctRSD_seq_compile(names[i],filepath)
    
      
    sheet1.write(1+i, 0, names[i])
    sheet1.write(1+i,1,seq)
      
wb.save('Sequences.xls')