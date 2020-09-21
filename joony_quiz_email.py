# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 07:24:46 2020

@author: USER
"""
from datetime import datetime
from my_email import send_mail

today=datetime.now()
todate=today.strftime("%b_%d_%Y")
fname='joony_quiz_' + today.strftime("%b_%d_%Y") +'.txt'
fpath='D://Coding//'
attachment = fpath + fname

contents= todate +'의 퀴즈 - 10까지 덧셈'



send_mail('Taejun', 'jlee4@naver.com', contents)#, attachment)

