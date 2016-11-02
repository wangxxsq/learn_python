# -*- coding: utf-8 -*-
# Python操作excel表格（写）
# 创建名为'hello.xlsx'文件，并在第一行，第一列写入数据'Hello， world'.
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet('test')
worksheet.write('A1', 'Hello, world')
workbook.close()
