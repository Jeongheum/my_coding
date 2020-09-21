# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:08:39 2020

@author: USER
"""

f_name='band_fr1_str.txt'

with open(f_name,'r') as f:
    band=f.readlines()
#band=band.replace('\n','')

# band_l=band.split(' ')

# bnum=band_l[0:14*6:6]
# bnum.append(band_l[14*6:14*6+5])

# band_d={}
# x=0
# #for x in range(0,len(band_l)-1,6):
# for x in range(0,12,6):
#     print(x, x+1, x+2, x+3, x+4, x+5)
#     band_d=dict(key=band_l[x], value={band_l[x+1], band_l[x+2], band_l[x+3], band_l[x+4], band_l[x+5]})