#coding=utf-8

"""
Created on Mon Nov 14 ‏‎17:48:27 2016

@author: Caran
@brief:  python 爬虫获得所有淘宝购买记录
@detail:
1.  登录（难，暂时不处理）

2.  get购买记录页 https://buyertrade.taobao.com/trade/itemlist/list\_bought\_items.htm

    2.1 根据class获取当前页所有购买记录项
    2.2 分别获取记录项的表头和表数据
    2.3 从表头获取购买时间date，订单号ordernumber
    2.4 从表数据获取当前记录是否交易成功，是否退货，如果不成功或存在退货，不记录
        2.4.1 获得购买记录总价 totalcost
        2.4.2 统计表数据中共多少产品
        2.4.3 获取每一个产品的缩略图、名称、单价、数量，部分产品存在细节购买选项请注意获取
    2.5 记录2.4获得的数据     

用csv记录，方便后续入db
"""

from selenium import webdriver
import io
import re

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm')
#手工输入登录信息
driver.refresh()
try:
  page_source = driver.page_source
  pattern = re.compile(u'var data =.+?</script>', re.S)
  result = re.findall(pattern, page_source)
        
  orderpattern1 = re.compile('"orderInfo"+.+?"page"', re.S)
  order = re.findall(orderpattern1, result[0])
  orderpattern2 = re.compile('"orderInfo"', re.S)
  orders = re.split(orderpattern2, order[0])
        
  pattern_info = re.compile(ur'\bcreateDay.*(\d{4}-\d*-\d*)\b.*?\bid":"(\d*).*?\bactual\w*":"(\d*\.\d*)\b.*\bpostFees.*?\b.*\u542b\u8fd0\u8d39.+?\bvalue\w*":".(\d*.\d*)\b.*\bshopName":"(.*)","\bshopUrl\b')
  pattern_detail = re.compile(ur'\bitemInfo.+?skuText.+?name":"(.*?)","\bvalue":"(.*?)"}],"snapUrl\b.*?title":"(.*?)","xtCurrent\b.*?\bpriceInfo.*?\brealTotal":"(\d*.\d{2}).*?quantity":"(\d*)\b')

  orderInfo = []
  for o in orders:
    if o == '':
      continue
    good_info = re.findall(pattern_info, o)
    good_detail = re.findall(pattern_detail, o)
    orderdetail = []
    orderdetail.append(good_info[0])
    orderdetail.append(good_detail)
    orderInfo.append(orderdetail)
except:
  print 'some error occured.'
finally:
  driver.close()
  driver.quit()
