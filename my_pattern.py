# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:11:44 2020

@author: USER
"""

# pgm to remove
import re

kwd='\s'
rule='r'+kwd
freq='{1,10}'
argm=rule+freq
print(argm)

st1='this is  a   test       !'
pattern=re.compile(argm)
st1=re.sub(pattern, ' ',st1)