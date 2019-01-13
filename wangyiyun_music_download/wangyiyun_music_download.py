#coding=utf-8
#https://blog.csdn.net/weixin_42337937/article/details/81838363
from copy import deepcopy
import json, base64
from binascii import hexlify
from Crypto.Cipher import AES
import os
import requests
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def create_secret_key(size):
	return hexlify(os.urandom(size))[:16].decode('utf-8')

def aes_encrypt(text, key):
	iv = '0102030405060708'
	pad = 16 - len(text) % 16
	text = text + pad * chr(pad)
	encryptor = AES.new(key, AES.MODE_CBC, iv)
	result = encryptor.encrypt(text)
	result_str = base64.b64encode(result).decode('utf-8')
	return result_str

def rsa_encrpt(text, pubKey, modulus):
	text = text[::-1]
	rs = pow(int(hexlify(text.encode('utf-8')), 16), int(pubKey, 16), int(modulus, 16))
	return format(rs, 'x').zfill(256)

def work(ids, br=128000):
	pub_key = '010001'
	modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
	nonce = '0CoJUm6Qyw8W8jud'
	text = {'ids': [ids], 'br': br, 'csrf_token': ''}
	text = json.dumps(text)
	i = create_secret_key(16)
	encText = aes_encrypt(text, nonce)
	encText = aes_encrypt(encText, i)
	encSecKey = rsa_encrpt(i, pub_key, modulus)
	data = {'params': encText, 'encSecKey': encSecKey}
	return data


#print len(sys.argv)
if len(sys.argv) != 3:
	print "python vip.py -d 280120"
	print "vip.exe -d 280120"
	print "其中第二个数字为收听歌曲的单个id，如 https://music.163.com/#/song?id=280120 ".decode('utf-8').encode('gb2312')
	print "作者的解密函数抄的 https://blog.csdn.net/weixin_42337937/article/details/81838363；需要批量下载看这个博客，此脚本不支持批量下载".decode('utf-8').encode('gb2312')
ids=sys.argv[2]
data=work(ids)
url="https://music.163.com/weapi/song/enhance/player/url?csrf_token="
headers={
	"Host": "music.163.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	"Accept-Encoding": "gzip, deflate",
	"Connection": "close",
	'Referer': 'http://music.163.com/search/'
}

response=requests.post(url=url,headers=headers,data=data)
req_url=json.loads(response.content)["data"][0]["url"]
response=requests.get(url=req_url,stream=True)
with codecs.open("123.mp3","wb") as f:
	f.write(response.content)
f.close()

print ("下载完成。").decode('utf-8').encode('gb2312')