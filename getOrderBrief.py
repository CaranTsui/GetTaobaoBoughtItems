# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:38:32 2016

@author: Administrator
"""

import io
import re

pattern_orderinfo = re.compile(ur'orderInfo')
pattern_date_fee = re.compile(ur'\bcreateDay.*(\d{4}-\d*-\d*)\b.*?\bid":"(\d*).*?\bactual\w*":"(\d*\.\d*)","')
pattern_shop = re.compile(ur'\bseller.*nick":"(.*?)","|\bshopName":"(.*?)","\b')
a = io.open('taobaoorders.csv', 'w', encoding = 'utf-8')
b = io.open('taobaoorders_error.txt', 'a', encoding = 'utf-8')

#if first use
a.write(unicode("id,orderid,date,fee,shop\n", 'utf-8'))
for page_source in page_source_array:
    orders = re.split(pattern_orderinfo,page_source)    
    for o in orders:
        date_info = re.findall(pattern_date_fee, o)
        shop_info = re.findall(pattern_shop, o)
        
        if len(date_info) != 1:
            b.write(unicode(o, 'utf-8'))
            b.write(unicode("==========", 'utf-8'))
            b.flush()
            continue
        
        if len(shop_info) <= 0 or len(shop_info) > 2:
            b.write(unicode(o, 'utf-8'))
            b.write(unicode("==========", 'utf-8'))
            b.flush()
            continue
        
        if len(shop_info) == 1:
            shop_str = shop_info[0][0]
        else:
            shop_str = shop_info[1][1]
            
        orderStr = ",{0},{1},{2},{3}\n".format(date_info[0][1],date_info[0][0],date_info[0][2],shop_str)
        a.write(unicode(orderStr, 'utf-8'))
        a.flush()
        
        
a.flush()
b.flush()        
a.close()
b.close()        