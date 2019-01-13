#!/usr/bin/env python
# coding=utf-8
import requests
import json
import codecs
import time
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
"Host":"www.52bug.cn",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
#"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Connection":"keep-alive",
"Cookie":"UM_distinctid=16524774ae1a7-0739fe89d538a6-4c312b7b-100200-16524774ae4eb; CNZZDATA1254095424=1662809224-1533912328-%7C1540032513",
"Content-Type": "application/x-www-form-urlencoded",
"Referer":"http://www.52bug.cn/"
}

'''
data={'startnum':'32'}
url="http://www.52bug.cn/getlist.php"
response=requests.post(url=url,headers=headers,data=data)
print type(response)
soup=BeautifulSoup(response.content,"lxml")
#print soup
list_=soup.select('li.todaynum_31 > a').get("href")
print list_


#print r
#print r.content

'''
def get_url(num):
	m=(num+1)*32
	list_=range(m)
	for i in range(num):
		url="http://www.52bug.cn/getlist.php"
		params={"startnum":i*32}
		r=requests.post(url=url,headers=headers,params=params)
		soup=BeautifulSoup(r.content,'lxml')
		for j in range(32):
			li='li.todaynum_'+str(j)+'>a'
			list_[m]=soup.select(li).get('href')
	return list_
def get_details(url):
	response=requests.get(url=url,headers=headers)
	soup=BeautifulSoup(response.content,'lxml')
	res=soup.select('.post-content')
	return res
def main():
	num=?
	sum_num=(num+1)*32
	list_=range(sum_num)
	list_=get_url(num)
	with codecs.open("details.txt","w+") as f:
		for i in range(sum_num):
			content=get_details()
			f.write(content)
			f.write('\n')
	f.close()
if __name__ == '__main__':
	main()