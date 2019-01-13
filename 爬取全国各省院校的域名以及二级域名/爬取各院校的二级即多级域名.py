#!/usr/bin/env python
# coding=utf-8
import requests
import json
import codecs
import time
import sys
from bs4 import BeautifulSoup
from lxml import html
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
"Host":"webscan.360.cn",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
#"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Connection":"keep-alive",
"Cookie":"__huid=11FzZkAXsn+4D+jXy29T9hoh5mYaFeFizxTcyxwg6ugnc=; __guid=132730903.3669407648386075000.1533346706178.1292; __gid=3537848.747332566.1533468508829.1534383127048.16; NTKF_T2D_CLIENTID=guest7527ACC1-5533-3E11-8881-09D882EE03C0; __DC_gid=3537848.747332566.1533468508829.1537754853262.84; Q=u%3D360H725528230%26n%3D%26le%3D%26m%3DZGHmWGWOWGWOWGWOWGWOWGWOZmVk%26qid%3D725528230%26im%3D1_t01923d359dad425928%26src%3Dpcw_webscan%26t%3D1; T=s%3Db88ad106c2ec6191a3f1e5deccecf66e%26t%3D1537071007%26lm%3D%26lf%3D2%26sk%3De86433ab7f115768b16625085fbae0ac%26mt%3D1537071007%26rc%3D%26v%3D2.0%26a%3D1; UM_distinctid=1669a0dbaa7408-00e84dc19b2e4f-4c312878-100200-1669a0dbaa9377; CNZZDATA1254937590=2028766517-1540181945-%7C1540289981; 360webscan_tongji_cookie=%7B%22nofen%22%3A%5B%22zxzfxy.ynnu.edu.cn%22%2C%22jyxxw.ynnu.edu.cn%22%2C%22vtc.sicnu.edu.cn%22%5D%7D; __utma=184508192.1203706003.1540182937.1540211853.1540211853.3; __utmz=184508192.1540182937.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=311ac35b86d48c207757b547da5f34a0",
"Content-Type": "application/x-www-form-urlencoded",
"Referer":"http://webscan.360.cn/index/checkwebsite/"
}
'''
##sub_conlist > dl:nth-of-type(1) > dd:nth-of-type(2) > strong:nth-of-type(1)
url="http://webscan.360.cn/sub/index/?url=sicnu.edu.cn"
try:
	s=requests.get(url)
	soup=BeautifulSoup(s.content,"lxml")
	s=soup.select("#sub_conlist > dl:nth-of-type(1) > dd:nth-of-type(2) > strong:nth-of-type(1)")
	print type(s)
	si=s[0].string
	print si
	sj=si.split(".")
	print sj[0]
	if len(s)==0:
		print "yes"
except:
	print "no"

'''
url="http://webscan.360.cn/sub/index/?url="
proxies={
	"http":"",
	"https":"",
}
urls=range(3)
m=0
f=open("domain_urls.txt")
for i in f.readlines():
	urls[m]=i.strip('\n')
	#print urls[m]
	m=m+1
#print urls
f.close()
for j in range(3):
	try:
		u_url=url+urls[j]
		response=requests.get(url=u_url,headers=headers)
		soup=BeautifulSoup(response.content,"lxml")
		name=urls[j].split(".")
		name=name[0]
		sum_num=range(1000)
		n=1
		#print name
		#print j
		#print u_url
		while True:
			res=soup.select("#sub_conlist > dl:nth-of-type(1) > dd:nth-of-type("+str(n)+") > strong:nth-of-type(1)")
			#print n
			if len(res)==0:
				break
			#print res[0].string
			sum_num[n]=res[0].string
			#print sum_num[n]
			#print n
			n=n+1
		#print n
		#print sum_num
		with codecs.open(name+".txt","w+") as f1:
			print sum_num[100]
			print n
			for num in range(n):
				print sum_num[num]
				f1.write(sum_num[num])
				f1.write("\n")
		f1.close()
		time.sleep(rand(5,7))
	except:
		continue