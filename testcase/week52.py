__author__ = 'abao2k'
import unittest
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath
import xlrd
from TestRequest import TestDeleteRequest


Testdata = xlrd.open_workbook(GetTestDataPath()) # 选择excle表中的sheet

class TestInterface(unittest.TestCase):

    def setUp(self):
        #print ('begin')
        self.url = 'https://www.apiopen.top'

    def test_login(self):#登陆接口
        try:
            table = Testdata.sheets()[2] # 选择excle表中的sheet
            for i in range(3,4):
                key	 = table.cell(i, 0).value
                phone = table.cell(i, 1).value
                passwd = table.cell(i, 2).value
                restatus  = table.cell(i, 3).value
                remsg = table.cell(i,4).value
                hdata = {
                    'key' : key,
                    'phone' : str(int(phone)),
                    'passwd' : str(int(passwd)),
                }
                htestcassid = '101'
                htestcassname = 'week5' + htestcassid
                htesthope = str(int(restatus))
                fanhuitesthope = str(remsg)
                headers = {'content-type': "application/json;charset=utf-8"}
                r = TestGetRequest(self.url + '/login', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope,'code')

        except Exception as e:
            print(e)

    def test_api1(self):#天气获取接口
        try:
            table = Testdata.sheets()[2] # 选择excle表中的sheet
            for i in range(13,15):
                city	 = table.cell(i, 0).value
                restatus  = table.cell(i, 1).value
                remsg = table.cell(i,2).value
                hdata = {
                    'city' : city,
                }
                htestcassid = '102'
                htestcassname = 'week5' + htestcassid
                htesthope = str(int(restatus))
                fanhuitesthope = str(remsg)
                headers = {'content-type': "application/json;charset=utf-8"}
                r = TestGetRequest(self.url + '/weatherApi', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope,'code')

        except Exception as e:
            print(e)

    def test_api2(self):#个性网名获取接口
        try:
            table = Testdata.sheets()[2] # 选择excle表中的sheet
            for i in range(21,22):
                page	 = table.cell(i, 0).value
                restatus  = table.cell(i, 1).value
                remsg = table.cell(i,2).value
                hdata = {
                    'page' : page,
                }
                htestcassid = '103'
                htestcassname = 'week5' + htestcassid
                htesthope = str(int(restatus))
                fanhuitesthope = str(remsg)
                headers = {'content-type': "application/json;charset=utf-8"}
                r = TestGetRequest(self.url + '/femaleNameApi', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope,'code')

        except Exception as e:
            print(e)

    def test_api3(self):#小说搜索接口
        try:
            table = Testdata.sheets()[2] # 选择excle表中的sheet
            for i in range(31,33):
                name	 = table.cell(i, 0).value
                restatus  = table.cell(i, 1).value
                remsg = table.cell(i,2).value
                hdata = {
                    'name' : name,
                }
                htestcassid = '104'
                htestcassname = 'week5' + htestcassid
                htesthope = str(int(restatus))
                fanhuitesthope = str(remsg)
                headers = {'content-type': "application/json;charset=utf-8"}
                r = TestGetRequest(self.url + '/novelSearchApi', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope,'code')

        except Exception as e:
            print(e)


    def tearDown(self):
        pass
        #print ('end')

if __name__ == '__main__':
    unittest.main()





