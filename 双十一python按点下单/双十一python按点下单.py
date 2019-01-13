# _*_ coding:utf-8_*_

from selenium import webdriver
import datetime
import time

print("ready to loading...")
# driver=webdriver.Chrome('D:\geckodriver\chromedriver.exe')
#driver=webdriver.Firefox(executable_path = 'D:\geckodriver\geckodriver.exe')
driver=webdriver.Chrome('/chromedriver.exe')
print("start webdriver")
def login(uname, passwd):
	#driver = webdriver.
	print("start process")
	driver.get("http://www.jd.com")
	print("get web in")
	time.sleep(3)
	driver.find_element_by_link_text("你好，请登录").click()
	time.sleep(3)
	driver.find_element_by_link_text("账户登录").click()
	time.sleep(3)
	print("已登陆")
	driver.find_element_by_name("loginname").send_keys(uname)
	driver.find_element_by_name("nloginpwd").send_keys(passwd)
	driver.find_element_by_id("loginsubmit").click()
	time.sleep(5)
	driver.find_element_by_link_text("我的购物车").click()
	driver.find_element_by_link_text("去结算").click()
	time.sleep(20)
	#driver.get("https://item.m.jd.com/product/31862750655.html?resourceType=jdapp_share&resourceValue=QQfriends&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=QQfriends")
	time.sleep(1000)
'''
	buy_time = '2018-11-11 14:00:00'
	print("buy_time :" + buy_time + "等待时间到达")
	while True:
		now = datetime.datetime.now()
		if now.strftime('%Y-%m-%d %H:%M:%S') == buy_time:
			driver.find_element_by_id("choose-btn-ko").click()
			time.sleep(3)
			driver.find_element_by_link_text("保存收货人信息").click()
			time.sleep(3)
			driver.find_element_by_id("order-submit").click()
			print("已提交订单")
		time.sleep(0.5)
'''
# entrance
login('','')   # your username and password