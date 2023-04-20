# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 16:48:16 2023

@author: aa255165
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.airbnb.com/s/United-Kingdom/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=4&date_picker_type=calendar&source=structured_search_input_header&search_type=category_change&place_id=ChIJqZHHQhE7WgIReiWIMkOg-MQ&checkin=2023-03-06&checkout=2023-03-10&adults=2&children=1&pets=1&query=United%20Kingdom&search_mode=flex_destinations_search&location_search=MIN_MAP_BOUNDS&category_tag=Tag%3A7769'

page=requests.get(url)

soup=BeautifulSoup(page.text,'lxml')

df=pd.DataFrame({'name':[''],
                 'description':[''],
                 'price':[''],
                 'reviews':[''],
                 'link':['']})
x=0
while x<10:    
    
    posts=soup.find_all('div',class_='c4mnd7m dir dir-ltr')
    
    for post in posts:
        try:
            link=post.find('a',class_='l1j9v1wn bn2bl2p dir dir-ltr').get('href')
            post_link='https://www.airbnb.com'+link
            
            title=post.find('div',class_='t1jojoys dir dir-ltr').text
            description=post.find('div',class_='nquyp1l s1cjsi4j dir dir-ltr').text
            price=post.find('div',class_='_1jo4hgw').text.strip()
            reviews=post.find('span','r1dxllyb dir dir-ltr').text
            
            df=df.append({'name':title,
                             'description':description,
                             'price':price,
                             'reviews':reviews,
                             'link':post_link},ignore_index=True)
        except:
            pass
        
        
    next_page=soup.find('a',{'aria-label':'Next'}).get('href')
    print(next_page)
    basic="https://www.airbnb.com"
    link=basic+next_page
    url=requests.get(link)
    soup=BeautifulSoup(url.text,'lxml')
    x+=1
    
    
        
df.to_csv('C:/Users/aa255165/OneDrive - Teradata/Desktop/Python WS/AirBNB_Posts.csv')


