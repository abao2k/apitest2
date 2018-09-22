__author__ = 'abao2k'
import unittest
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath
import xlrd


Testdata = xlrd.open_workbook(GetTestDataPath()) # 选择excle表中的sheet
class TestInterface(unittest.TestCase):

    def setUp(self):
        #print ('begin')
        self.url = 'http://127.0.0.1:8000'

    def test_get_question(self):#问题列表
        try:
            table = Testdata.sheets()[1] # 选择excle表中的sheet
            for i in range(13,14):
                restatus  = table.cell(i, 0).value
                remsg = table.cell(i,1).value
                hdata = {}
                htestcassid = '001'
                htestcassname = 'week5' + htestcassid
                htesthope = str(int(restatus))
                fanhuitesthope = str(remsg)
                headers = {'content-type': "application/x-www-form-urlencoded"}
                r = TestGetRequest(self.url + '/polls/', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope,'status')
        except Exception as e:
            print(e)

    def test_get_detail(self):#问题详情
        try:
            table = Testdata.sheets()[1] # 选择excle表中的sheet
            for i in range(21,22):
                hdata = {}
                restatus  = table.cell(i, 0).value
                remsg = table.cell(i,1).value

                htestcassid = '002'
                htestcassname = 'week5' + htestcassid
                htesthope = str(int(restatus))
                fanhuitesthope =  str(remsg)
                headers = {'content-type': "application/json;charset=UTF-8"}
                r = TestGetRequest(self.url + '/polls/1', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope,'status')
        except Exception as e:
            print(e)

    def test_do_vote(self):#投票
        try:
            table = Testdata.sheets()[1] # 选择excle表中的sheet
            for i in range(3,5):
                choice_id  = table.cell(i, 0).value
                restatus  = table.cell(i, 1).value
                remsg = table.cell(i,2).value
                hdata = {'choice':str(int(choice_id))}
                htestcassid = '003'
                htestcassname = 'week5' + htestcassid
                htesthope = str(int(restatus))
                fanhuitesthope = str(remsg)
                headers = {'content-type': "application/x-www-form-urlencoded"}
                r = TestPostRequest(self.url + '/polls/vote/1', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope)
        except Exception as e:
            print(e)

    def tearDown(self):
        pass
        #print ('end')

if __name__ == '__main__':
    unittest.main()





