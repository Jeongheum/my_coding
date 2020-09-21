# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 07:47:36 2020

@author: USER
"""
import PyPDF2, re

### Enter pdf file name to read
cdir='D:/Coding/'

fr=1  # 1 : FR1, 2: FR2, 3: LTE

if fr==1:
    fin_name='ts_13810101v160400p.pdf'
    
    fout_name1='band_fr1_str.txt'
    fout_name2='band_fr1_list.txt'
    num_page_to_read=24  # fr1
    kwd='n1'
    kwd3=0
elif fr==2:
    fin_name='ts_13810102v160400p.pdf'
    
    fout_name1='band_fr2_str.txt'
    fout_name2='band_fr2_list.txt'
    num_page_to_read=18  # fr2
    kwd='n257'
    kwd3='5.2A'
else:
    fin_name='ts_136101v160600p.pdf'
    
    fout_name1='band_lte_str.txt'
    fout_name2='band_lte_list.txt'
    num_page_to_read=45  # fr2
    kwd='FDL_high'
    kwd3='NOTE'

#num_page_to_read=input('Enter page number to read : ')

pdfFileObj = open(cdir+fin_name,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pg = pdfReader.numPages

pageObj = pdfReader.getPage(num_page_to_read)
itext= pageObj.extractText()

if kwd3:
    idx=itext.find(kwd3)
    itext=itext.replace(itext[idx:-1],'')
else:
    pass

### header remove
idx=itext.strip().find(kwd)+1

if fr ==3:
    idx=idx+9

### tidy
st1=itext.replace(itext[:idx],'')
st1=st1.replace('Œ','')
st1=st1.replace('\n','').replace('MHz','').replace('Mhz','')

# make string to regular single space
pattern=re.compile(r'\s{1,5}')
st1=re.sub(pattern, ' ',st1)
    
with open(fout_name1,'w', encoding='utf-8') as f1:
    print(st1, file=f1)
# ## string to list conversion
t3=st1.split(' ')
with open(fout_name2,'w', encoding='utf-8') as f2:
    print(t3, file=f2)
    
if fr ==3:
    kwd2='67'
    
    pageObj2 = pdfReader.getPage(num_page_to_read+1)
    itext2= pageObj2.extractText()
    idx2=itext2.strip().find(kwd2)
    idx3=itext2.find(kwd3)
    
    st2=itext2.replace(itext2[idx3:-1],'')
    st2=st2.replace(itext2[:idx2],'')
    st2=st2.replace('Œ','')
    st2=st2.replace('\n','').replace('MHz','')
    
    st2=re.sub(pattern, ' ',st2)
    with open(fout_name1,'a', encoding='utf-8') as f1:
        print(st2, file=f1)
    # ## string to list conversion
    st4=st2.split(' ')
    with open(fout_name2,'a', encoding='utf-8') as f2:
        print(st4, file=f2)