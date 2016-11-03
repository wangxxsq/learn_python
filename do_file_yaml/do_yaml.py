# -*- coding: utf-8 -*-
import yaml   # 导入模块
import os

config_path = 'E:/xinxin/learn_python'

# 读
config = yaml.load(open(os.path.join(config_path, 'config.yaml'), encoding='utf8'))  # 加载文件
print(config)   # 读取文件所有内容
print(config['cache'])  # 获取cache
print(config['database'])  # 获取database
print(config['database']['url'])  # 获取databese的url

# 写
f = open(os.path.join(config_path, 'config.yaml'), 'w', encoding='utf8')
print(f)
data = {'safety': {'white_list': ['127.0.0.1', '::1', '192.168.1.101', '192.168.1.102', '192.168.1.103'], 'secret': 'asingo5l86jigncu'}}
yaml.dump(data, f)
f.close()












