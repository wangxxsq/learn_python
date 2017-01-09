# -*- coding: utf-8 -*-
# Pytohn解析带命名空间的XML报文
import xml.etree.ElementTree as ET


s = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.test.org/2017/01/soap-envelope" xmlns:xsi="http://www.test.org/2017/XMLSchema-instance" xmlns:xsd="http://www.test.org/2017/XMLSchema">
<soap:Body>
<getOrderResponse xmlns="http://testService.org/">
<getOrderStatus>&lt;result&gt;&lt;status&gt;00&lt;/status&gt;&lt;msg&gt;操作成功&lt;/msg&gt;&lt;data&gt;&lt;datalist&gt;&lt;charged&gt;&lt;orderid&gt;Q2017010317251410068716&lt;/orderid&gt;&lt;state&gt;7777&lt;/state&gt;&lt;/charged&gt;&lt;/datalist&gt;&lt;/data&gt;&lt;/result&gt;</getOrderStatus>
</getOrderResponse>
</soap:Body>
</soap:Envelope>
'''


root = ET.fromstring(s)
code = root.find('.//{http://testService.org/}getOrderStatus')
print(code)
print(code.text)

root2 = ET.fromstring(code.text)
status = root2.find('status').text
print('STATUS: ', status)
charged = root2.find('.//data/datalist/charged')
state = charged.find('state').text
print('STATE: ', state)

