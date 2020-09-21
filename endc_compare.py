# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 07:47:36 2020

@author: USER
"""
import pandas as pd

# df=pd.read_excel('D://Coding//doit_pandas-master/data/endc1.xlsx', header=None)
# df2=pd.read_excel('D://Coding//doit_pandas-master/data/endc2.xlsx', header=None)

# # index1=range(6)
# # df=pd.DataFrame(df, columns=['combo'])
# # df2=pd.DataFrame(df2, columns=['combo'])
# df.head()
# df2.head()
# #df2.loc[4].drop()

# #df.compare(df2, keep_shape=True)


# 1 bands list
# 

import PyPDF2

pdfFileObj=open('D:/Coding/ts_13810101v160400p.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
pg=pdfReader.numPages
pageObj=pdfReader.getPage(24)
tt=pageObj.extractText()
tt=tt.strip().replace('Œ','')

t1=tt.replace('\n','').replace('MHz','')
t2=t1.replace(t1[0:263],'')
#.replace(tt[0:263],'').replace('MHz','')

t3=t2.split(' ')
# t4=[]
# k=0

while '' in t3:
    if not(t3[i]):
        t3.remove('')
    i=i+1


# with open('bands.txt','w') as f:
#      print(t2, file=f)

# df=pd.read_csv('D:/Coding/bands.txt',header=None)

    