from common.HttpService import HttpService
from read_excel import ExcelUtil
def get_url(EndPoint):
    host=Config.url()
    endpoint=EndPoint
    url=''.join(host,endpoint)
    return url

def get_response(url,Method,**DataALL):
    if Method=='get':
        resp=HttpService.MyHTTP().get(url,**DataALL)
    elif Method=='post':
        resp=HttpService.MyHTTP().post(url,**DataALL)
    return resp

def get_data(testfile,sheetname):
    datainfo=ExcelUtil.dict_data(r'E:\python\directbank_sr\excel\%s'%testfile)
    Data=datainfo.get_sheet_by_name(sheetname)
    # data = ExcelUtil(filepath, sheetName)
    return  Data

