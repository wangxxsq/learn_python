# -*- coding: utf-8 -*-
# Pytohn解析XML报文
import xml.etree.ElementTree as ET

s = '''<?xml version="1.0" encoding="GB2312" ?>
<orderinfo>
    <err_msg></err_msg>
    <status>1</status>
        <orderid>Q1608192552735</orderid>
        <msg>提交成功</msg>
        <price>3</price>
        <sporder_id>1476589680</sporder_id>
</orderinfo>'''

root = ET.fromstring(s)
status = root.find('status').text
msg = root.find('msg').text
print('STATUS: ', status)
print('MSG: ', msg)












