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
"Host":"college.gaokao.com",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
#"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Connection":"keep-alive",
"Cookie":"UM_distinctid=16695fc2f18a-0837bc20071e68-4c312878-100200-16695fc2f196b; CNZZDATA1997329=cnzz_eid%3D1868723432-1540109282-null%26ntime%3D1540114682; __utma=243165661.1788037469.1540114624.1540114624.1540114624.1; __utmc=243165661; __utmz=243165661.1540114624.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_aa27487f630124a75eaf9c8ac900811c=1540114625; Hm_lpvt_aa27487f630124a75eaf9c8ac900811c=1540116820",
"Upgrade-Insecure-Requests":"1",
"Referer":"http://college.gaokao.com/schlist/a30/"

}
url="http://college.gaokao.com/schlist/"

'''
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,"lxml")
#print soup
res=soup.select("#wrapper > div.cont_l.in > div.scores_List > dl:nth-of-type(3) > dd > ul > li:nth-of-type(6) ")
m=res[0].string
m=str(m)
n=m.split(".")
print n[-3]+'.'+n[-2]+'.'+n[-1]
'''
num=107*50
list_=range(107)
for i in range(107):
	#print i
	sum_num1=0
	sum_num=i+1
	url="http://college.gaokao.com/schlist/"
	response=requests.get(url=url,headers=headers)
	url=url+"p"+str(i+2)
	for j in range(3,53):
		soup=BeautifulSoup(response.content,'lxml')
		res=soup.select("#wrapper > div.cont_l.in > div.scores_List > dl:nth-of-type("+str(j)+") > dd > ul > li:nth-of-type(6)")
		try:
			m=res[0].string
			m=str(m)
			n=m.split(".")
			#print n
			try:
				mn=n[-3]+'.'+n[-2]+'.'+n[-1]
				if mn.endswith("/"):
					mn= mn[:-1]
				print mn
				#print sum_num*j
				list_[sum_num1]=mn
				sum_num1=sum_num1+1
			except:
				continue
		except:
			continue
with codecs.open("aq_url.txt","w+") as f:
	for i in range(0,num):
		#print i
		#print list_[3]
		try:
			f.write(list_[i])
			f.write("\n")
		except:
			continue
f.close()
