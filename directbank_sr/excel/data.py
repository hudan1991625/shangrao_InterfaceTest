# coding:utf-8
import xlrd
data = xlrd.open_workbook(r'E:\python\directbank_sr\excel\parameter.xlsx')
# table = data.sheets()[0]           #  通过索引顺序获取
# table = data.sheet_by_index(0)     #  通过索引顺序获取
table = data.sheet_by_name(u'parameter')
# 获取总行数
nrows = table.nrows
# 获取总列数
ncols = table.ncols
# 获取第一行值
print table.row_values(0)
# 获取第一列值
print table.col_values(0)

