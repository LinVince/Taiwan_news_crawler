#add requests
import requests
import re
from bs4 import BeautifulSoup



def news(n):
    response = requests.get("https://www.taiwannews.com.tw/en/news/" + str(n))
    soup = BeautifulSoup(response.text, "html.parser")
    example_sentence = ''
    t_list = soup.find_all('title')
    title = t_list[0].getText()
    p_list = soup.find_all('div', itemprop="articleBody")
    parse = p_list[0].getText()
    body = parse.split('\n')
    text = ''
    count = 0
    for i in body:
      i = i.lstrip()
      count += 1
      if i.endswith('... '):
        continue
      if i.find('AP Photo') != -1:
        continue
      if i.find('{') != -1: 
        continue
      if len(i) < 2:
        continue
      if i.find('use strict') != -1:
        continue
      if i.find('id: u') != -1:
        continue
      if i.find('return;') != -1:
        continue
      if i.find('{') != -1:
        continue
      if i.find('}') != -1:
        continue
      if i.find('photo)') != -1:
        continue
      if i.find('Photo') != -1:
        continue
      if i.find('AP)') != -1:
        continue
      
      
      #if i.startswith('"'):
      text += i + '\n'
    
    print (n)
    print (title)
    print (text)
    

def news_collect(x,y):
  for i in range(x,y):
    try:
      news(i)
    except:
      continue
    

