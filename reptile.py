import time

import pymongo
import requests
from bs4 import BeautifulSoup
import os
from entity import Cat

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
db = mongo_client.tiny

cat_url = 'http://thecatapi.com/api/images/get'
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/59.0.3071.104Safari/537.36'}


# 爬取数据
def reptile():
    res = requests.get(cat_url + '?format=xml&results_per_page=1000', header)
    print(str(res.text))
    # 解析网页
    soup = BeautifulSoup(res.text, 'xml')
    for c in soup.find_all('image'):
        cat = Cat(c.find('id').text, c.find('url').text)
        print(cat.__dict__)
        db.tiny.save(cat.__dict__)
