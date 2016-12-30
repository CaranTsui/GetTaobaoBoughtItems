# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:25:42 2016

@author: Caran
"""

import io
import re

pattern_orderinfo = re.compile(ur'orderInfo')
pattern_id = re.compile(ur'\bcreateDay.*?\bid":"(\d*)')
pattern_detail = re.compile(ur'\bitemInfo.+?skuText.+?\[(.*?)\].*?title":"(.*?)",".*?\bpriceInfo.*?\brealTotal":"(\d*.\d{2}).*?quantity":"(\d*)\b')

#==============================================================================
## 获取订单明细
#==============================================================================


a = io.open('taobaoorderdetail.csv', 'w', encoding = 'utf-8')
b = io.open('taobaoordersdetail_error.txt', 'a', encoding = 'utf-8')

a.write(unicode("id,orderid,product,detail,fee,quantity\n", 'utf-8'))
for page_source in page_source_array:
    orders = re.split(pattern_orderinfo,page_source)    
    for o in orders:
        id_info = re.findall(pattern_id, o)
        detail_info = re.findall(pattern_detail, o)
        
        if len(id_info) != 1:
            b.write(unicode(o, 'utf-8'))
            b.write(unicode("==========", 'utf-8'))
            b.flush()
            continue
        
        if len(detail_info) <= 0:
            b.write(unicode(o, 'utf-8'))
            b.write(unicode("==========", 'utf-8'))
            b.flush()
            continue
        
        id_str = id_info[0]
        for d in detail_info:
            detailStr = ",{0},{1},{2},{3},{4}\n".format(id_str,d[1],d[0],d[2],d[3])
            a.write(unicode(detailStr, 'utf-8'))
            a.flush()
        

a.flush()
b.flush()        
a.close()
b.close()   

#==============================================================================
## 获取有退款的订单号（可能存在非整单退款的情况，需手工分辨） 
#==============================================================================


pattern_refund = re.compile(ur'\bcreateDay.*?\bid":"(\d*).*?\u67e5\u770b\u9000\u6b3e')

c = io.open('taobaorefund.txt', 'w', encoding = 'utf-8')

for page_source in page_source_array:
    orders = re.split(pattern_orderinfo,page_source)    
    for o in orders:
        if o.find('查看退款') != -1:
            refundID = re.findall(pattern_id, o)
        else:
            continue
        
        if len(refundID) != 1:
            continue
        
        c.write(refundID[0] + unicode("\n", 'utf-8'))
        c.flush()

c.flush()
c.close()        
        
        
