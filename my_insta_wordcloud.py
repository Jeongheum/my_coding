# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:53:37 2020

@author: USER
"""
import requests 
from selenium import webdriver as wd 
import time 
import re 

keyword = "커피베이" 
url = "https://www.instagram.com/explore/tags/{}/".format(keyword) 

instagram_tags = [] 

driver = wd.Chrome("D:/Coding/chromedriver_win32/chromedriver") 
driver.get(url) 
time.sleep(3) 

# Enter ID, password

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click() 
for i in range(300): 
    time.sleep(1) 
    data = driver.find_element_by_css_selector('.C7I1f.X7jCj') # C7I1f X7jCj 
    tag_raw = data.text 
    tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw) 
    tag = ''.join(tags).replace("#"," ") 
    # "#" 제거 
    tag_data = tag.split() 
    for tag_one in tag_data: instagram_tags.append(tag_one) 
    print(instagram_tags) 
    driver.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click() 
    time.sleep(3) 
driver.close()

#출처:  [솜씨좋은장씨]
