# -*- coding: utf-8 -*-
# Python操作excel表格（读）
import xlrd
# 打开文件
workbook = xlrd.open_workbook('F:/拆单/百兑通.xlsx')

# 获取工作表三种方法
table = workbook.sheets()[0]
table = workbook.sheet_by_index(0)
table = workbook.sheet_by_name('')

# 获取整行的值
print(table.row_values(1))
# 获取整列的值
print(table.col_values(2))

# 获取行数、列数
print(table.nrows)
print(table.ncols)

# 遍历行列表数据
for i in range(table.nrows):
    print(table.row_values(i))

# 单元格
cell_A1 = table.cell(0, 0).value
cell_B3 = table.cell(2, 1).value
print(cell_A1)
print(cell_B3)

# 使用行索引
cell_A1 = table.row(0)[0].value
cell_B3 = table.row(2)[1].value
print(cell_A1)
print(cell_B3)






