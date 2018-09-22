__author__ = 'abao2k'

import os
import time
import xlrd

def GetTestDataPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "testdata", "TestData.xls")


#得到测试报告路径
def GetTestReport():
    now = time.strftime("%Y-%m-%d-%H-%M-%S-", time.localtime(time.time()))
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "testreport", now +"TestReport.xls")



def GetTestLogPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "logs", "log.txt")


def GetConfig(configname):
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", configname)





#print (GetTestDataPath())
#print (GetTestReport())
'''
# 读取测试数据
Testdata = xlrd.open_workbook(GetTestDataPath()) # 选择excle表中的sheet
table = Testdata.sheets()[0]
# 从测试数据中读取url
hurl = table.cell(7, 1).value
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
sku_id = table.cell(11, 1).value
'''


