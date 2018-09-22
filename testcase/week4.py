__author__ = 'abao2k'
import unittest
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from TestRequest import TestDeleteRequest



class TestInterface(unittest.TestCase):

    def setUp(self):
        #print ('begin')
        self.url = 'http://127.0.0.1:8000'

    def test_get_question(self):#问题列表
        try:
            hdata = {}
            htestcassid = '001'
            htestcassname = 'week4' + htestcassid
            htesthope = '200'
            fanhuitesthope = 'success'
            headers = {'content-type': "application/x-www-form-urlencoded"}
            r = TestGetRequest(self.url + '/polls/', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope)
        except Exception as e:
            print(e)

    def test_get_detail(self):#问题详情
        try:
            hdata = {}
            htestcassid = '002'
            htestcassname = 'week4' + htestcassid
            htesthope = '200'
            fanhuitesthope = 'success'
            headers = {'content-type': "application/json;charset=UTF-8"}
            r = TestGetRequest(self.url + '/polls/1', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope)
        except Exception as e:
            print(e)

    def test_do_vote(self):#投票
        try:
            hdata = {'choice':'1'}
            htestcassid = '003'
            htestcassname = 'week4' + htestcassid
            htesthope = '200'
            fanhuitesthope = 'success'
            headers = {'content-type': "application/x-www-form-urlencoded"}
            r = TestPostRequest(self.url + '/polls/vote/1', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope)
        except Exception as e:
            print(e)

    def test_delete_question(self):#删除问题
        try:
            hdata = {}
            htestcassid = '004'
            htestcassname = 'week4' + htestcassid
            htesthope = '200'
            fanhuitesthope = 'success'
            headers = {'content-type': "application/x-www-form-urlencoded"}
            r = TestDeleteRequest(self.url + '/polls/delete/3', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope)
        except Exception as e:
            print(e)

    def tearDown(self):
        pass
        #print ('end')

if __name__ == '__main__':
    unittest.main()





