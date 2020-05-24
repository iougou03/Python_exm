#!/usr/bin/python

import requests, elasticsearch, re
from bs4 import BeautifulSoup
import json
from collections import OrderedDict #값을 넣은 순서대로 dict이 출력됨( 기존의 dict은 무작위로 출력했음 )
from elasticsearch import Elasticsearch

URL = "https://cassandra.apache.org/"
req = requests.get(URL)
html = req.text
soup=BeautifulSoup(html,"html.parser")

sentence_list_01=soup.select(
    "body > div.topnav > nav > div > div.jumbotron > h1"
)
sentence_list_02=soup.select(
    'p'
)
sentence_list_03=soup.select(
   'h4'
)
sentence_list=[h.get_text() for h in sentence_list_01] + [b.get_text() for b in sentence_list_02] + [ bt.get_text() for bt in sentence_list_03]

word_fre_num=OrderedDict()
words_frequecy=OrderedDict()
for s in sentence_list:
    word_list=re.findall("[A-Za-z']+",s.strip()) #영어 단어만 추출, quotation mark포함
    for w in word_list:
        if (w in word_fre_num) == True:
            word_fre_num[w]+=1  #+= 연산이기 때문에 조건문을 써줘야함
        else:
            word_fre_num[w]=1

    # print(word_list)

#sorted(word_fre_num.items(),key=lambda k:k[1],reverse=True)  #buitin함수 sorted는 list를 반환
word_fre_num={k: v for k, v in sorted(word_fre_num.items(), key=lambda item: item[1],reverse=True)} #{}, dict 반환
words_frequecy["URL"]=URL
words_frequecy["words"]=list(word_fre_num.keys())  #From Python : "keys() will return dictionary view object"
words_frequecy["frequencies"] = list(word_fre_num.values())
with open("words_freq.json",'w',encoding="utf-8") as mkf:
    json.dump(words_frequecy,mkf, ensure_ascii=False,indent="\t")

es_host="127.0.0.1"
es_port="9200"

if __name__ == '__main__':
    with open('words_freq.json','r') as w:
        jf=json.load(w)
    es=Elasticsearch([{'host':es_host,'port':es_port}],timeout=10)
    res=es.index(index='web',doc_type='word',id=1,body=jf)