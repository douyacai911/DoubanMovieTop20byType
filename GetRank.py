import re
from urllib import request
from urllib.parse import quote
import string
import json
from bs4 import BeautifulSoup
'''
Created on 2017/12/27

@author: douyacai911
'''
response = request.urlopen("https://movie.douban.com/chart")
html = response.read().decode("utf-8")
soup = BeautifulSoup(html,"lxml")


print("OK")

for child in soup.body.find_all(href=re.compile("typerank\?type_name")):
    print(child.text)
    typeNo = re.findall(r"type=(.+?)&amp;",str(child))[0]
    response3 = request.urlopen('https://movie.douban.com/j/chart/top_list?type=' +typeNo+ '&interval_id=100%3A90&action=&start=0&limit=20')
    text = json.loads(response3.read().decode("utf-8"))
    print(text)
    print("Rank\tRating\tTitle\tUrl")
    for mo in text:
        print(str(mo.get('rank')) + "\t" + mo.get('rating')[0] + "\t" + mo.get('title') + "\t" + mo.get('url'))
#     s = quote('https://movie.douban.com'+ str(child.get('href')), safe=string.printable)
#     print(s)
#     response2 = request.urlopen(s)
#     html2 = response2.read().decode('utf-8')
#     soup2 = BeautifulSoup(html2,"lxml")
#     print(soup2)
#     for child2 in soup2.body.find_all(class_=re.compile("movie-list-item[\S\s]+watched")):
#         print("ok2")
#         print(child2)



# for span in soup.body.find(class_='types'):
#     for child in span.find_all(href=True):
#         print(child)

# for child in soup.head.stripped_strings:
#     print(repr(child))
#
# for child2 in soup.body.find(class_='types').children:
#     for child3 in child2:
#         print(repr(child3))
