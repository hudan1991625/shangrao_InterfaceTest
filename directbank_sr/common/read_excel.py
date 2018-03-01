# coding:utf-8
import xlrd
# class ExcelUtil():
#     def __init__(self, filepath, sheetName):
#         self.data = xlrd.open_workbook(filepath)
#         self.table = self.data.sheet_by_name(sheetName)
#         # 获取第一行作为key值
#         self.keys = self.table.row_values(0)
#         # 获取总行数
#         self.rowNum = self.table.nrows
#         # 获取总列数
#         self.colNum = self.table.ncols
#
#     def dict_data(self):
#         if self.rowNum <= 1:
#             print("总行数小于1")
#         else:
#             infolist = [] #定义个空列表
#             j = 1
#             #控制行,i在(0,行数-1)
#             for i in range(self.rowNum - 1):
#                 s = [] #定义个空字典
#                 # 从第二行取对应values值
#                 values = self.table.row_values(j)
#                 #控制列
#                 for x in range(self.colNum):
#                     s[self.keys[x]] = values[x]
#                 infolist.append(s)
#                 j += 1
#             return infolist
#
# if __name__ == "__main__":
#     # datainfo=ExcelUtil.dict_data(r'E:\python\directbank_sr\excel\parameter.xlsx')
#     filepath = r'E:\python\directbank_sr\excel\parameter.xlsx'
#     sheetName = 'parameter'
#     data = ExcelUtil(filepath, sheetName)
#     print data.dict_data()


class XLDatainfo(object):
    def __init__(self,path=''):
        self.xl=xlrd.open_workbook(path)
    def get_sheetinfo_by_name(self,name):
        self.sheet=self.xl.sheet_by_name(name)

    def get_sheet_info(self):
        infolist=[]
        for row in range(0,self.sheet.nrows):
            info=self.sheet.row_values(row)
            infolist.append(info)
        return infolist

if __name__=='__main__':
    data=XLDatainfo(r'E:\python\directbank_sr\excel\parameter.xlsx')
    print data
    info=data.get_sheetinfo_by_name('parameter')
    print info

