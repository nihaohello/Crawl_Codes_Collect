#!/usr/bin/env python
# coding=utf-8
# https://www.cnblogs.com/wzjbg/p/6507497.html
# https://www.cnblogs.com/0x03/p/7329039.html
# https://blog.csdn.net/loner_fang/article/details/80940600
import requests
import json
import codecs
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    "Host": "music.163.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
    # "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection": "keep-alive",
    "Cookie": "usertrack=ezq0pFtlxVq4szHJYeuTAg==; _ntes_nnid=f99b273c8a19af47c3672c01c547a4fb,1533396315891; _ntes_nuid=f99b273c8a19af47c3672c01c547a4fb; _ga=GA1.2.1928701583.1533396320; vjuids=-11ec78d03e.16573afe130.0.2f9b23bd1d4888; vjlast=1535244231.1536662062.11; UM_distinctid=16594cd55fba-057f7d37c28bbf-4c312b7b-13c680-16594cd55fc3c5; vinfo_n_f_l_n3=334b77b93d1e9712.1.0.1535799811609.0.1535799894376; __f_=1537078049493; JSESSIONID-WYYY=VKQZYGUK9r4n469hGlukf8JvGPNmGAay%2Bn3WkSIY5wJkcrqPPxIoFfKIlzQJpwOJhaRVrHaKd3FAUt%5CIhVqZRNIA6l5nR9SjOxF1zExgodn%2F2zusQlhpYz%2BMZ11OGYFtgMxsP63cPdyDlz1WvcdJijpj76Jq58yW%2B5HaCvvWgJbmN5Jx%3A1540014522386; _iuqxldmzr_=32; __utma=94650624.1928701583.1533396320.1540003964.1540008259.8; __utmz=94650624.1540000175.6.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=QPL1l9POIsJnIUcJG3RbdTucAhwqe27g5aDofnTyrwhVOgUFoAZk5nvThJhsQUL9ZYBB4AInrd3SJDHun2m%2Fe%2B8uYrh4OrFvlzcuFhpzn48nfLrrnxS3VSGxontNKqZeNlo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea5ae7b9294feaddc52b1b48aa6d84a939a8b85bc419b89e58cc53cf4ace58cf32af0fea7c3b92a939084d2ef3394918794c9668b8badabc63992beacb5f86983b8b992e83af5b9fb82c765a6b29c9af17dac8a8188d84ead9f968cb866b68ca8abeb79938b84dad953829efca2cc66b2bcfdb4c9508caba2d3f025a7f5f896dc7aacec8193c57eb0a6ad96c564b4a6a2d5bb66a694be93ed7491ed9ab4c674adb2bcafca7b9abb828dee37e2a3; WM_TID=U7h%2Fe%2BztB6z0t%2BVYYsxC8b6yfZ6GZqvd; __utmc=94650624; playerid=57933716",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "http://music.163.com/"

}
'''
url="http://music.163.com/api/v1/resource/comments/R_SO_4_395729?limit=100&offset=1"
r=requests.get(url,headers=headers)
s=r.content
with open("123.json","w+") as f:
	f.write(s.encode("utf-8"))
f=json.loads(s)
f1=f['comments']
print type(f1) 
print len(f1)
print f1[0]
print f1[0]['content']
print f1[0]['user']['nickname']
'''
list_ = range(20000)
for i in range(90):
    time.sleep(rand(1, 2))
    print i
    url = "http://music.163.com/api/v1/resource/comments/R_SO_4_395729?limit=100&offset=" + str(i)
    response = requests.get(url=url, headers=headers)
    res = json.loads(response.content)
    print type(response.content)
    res = res['comments']
    for j in range(100):
        # print j
        m = i * 100 + j
        n = m + 1
        list_[n] = res[j]["content"]
        list_[m] = res[j]['user']["nickname"]

with codecs.open("pinglun.txt", "w+", "utf-8") as f:
    for i in range(0, 9000, 2):
        f.write(list_[i])
        f.write(list_[i + 1])
        f.write("\n")
f.close()