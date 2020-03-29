from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
from urllib.request import urlretrieve

html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

data1 = soup.find('div', {'class':'list_area daily_all'})
#data2 = soup.find('div', {'class':'col col_selected'})
#data3 = data2.findAll('a', {'class':'title'})

#for i in data3:
#    print (i.text)

data2 = data1.findAll('div', {'class':'col_inner'})
for i in data2:
    data3 = i.findAll('a', {'class':'title'})
    for j in data3:
        print(j.text)
