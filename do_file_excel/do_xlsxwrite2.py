# -*- coding: utf-8 -*-
# 新建一个表格‘test’， 新建sheet表‘test1’， 插入数据，中国移动流量包价格大小统计表。
import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet('test1')

data = (                 # 数据格式
    ['value', 'MB'],
    ['3', '10'],
    ['5', '30'],
    ['10', '70'],
    ['20', '150'],
    ['30', '500'],
    ['50', '1024'],
    ['70', '2048'],
    ['100', '3072'],
    ['130', '4096'],
    ['180', '6144'],
    ['280', '11264'],
)

row = 0
col = 0

for facevalue, size in (data):              # 插入数据
    worksheet.write(row, col,   facevalue)
    worksheet.write(row, col + 1, size)
    row += 1

workbook.close()






