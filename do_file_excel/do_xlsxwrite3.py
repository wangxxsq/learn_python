# -*- coding: utf-8 -*-
# 添加一些格式
import xlsxwriter
workbook = xlsxwriter.Workbook('test2.xlsx')
worksheet = workbook.add_worksheet('test2')

bold = workbook.add_format({'bold': True})  # 设置粗体，默认False
money = workbook.add_format({'num_format': '$#,##0'})   # 定义数字格式

worksheet.write('A1', 'Item', bold)     # 设置自定义表头加粗
worksheet.write('B1', 'Cost', bold)

expenses = (
     ['Rent', 1000],
     ['Gas',   100],
     ['Food',  300],
     ['Gym',    50],
 )

row = 1
col = 0

for item, cost in (expenses):
    worksheet.write(row, col, item)    # 默认格式写入
    worksheet.write(row, col + 1, cost, money)   # 设置带money格式写入
    row += 1

worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)

workbook.close()
