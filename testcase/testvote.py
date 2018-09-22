__author__ = 'abao2k'
from TestRequest import  TestPostRequest
from TestRequest import  TestGetRequest
testurl = "http://127.0.0.1:8000"


def test_post_vote():
    try:
        hdata = {
        'choice':'1'
        }
        htestcassid = '1002'
        htestcassname = 'case' + htestcassid
        htesthope = '200'
        fanhuitesthope = 'success'
        headers = {
            'content-type': "application/x-www-form-urlencoded"
            }

        r = TestPostRequest(testurl + '/polls/vote/1', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope)

    except Exception as e:
        print(e)





def test_get_vote():
    try:
        hdata = {}
        htestcassid = '1001'
        htestcassname = 'case' + htestcassid
        htesthope = '200'
        fanhuitesthope = 'success'
        headers = {
            'content-type': "application/json;charset=UTF-8"
            }
        r = TestGetRequest(testurl + '/polls/1', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope,'status')

    except Exception as e:
        print(e)


def test_delete_question():
    try:
        hdata = {}
        htestcassid = '1003'
        htestcassname = 'case' + htestcassid
        htesthope = '200'
        fanhuitesthope = 'success'
        headers = {
            'content-type': "application/json;charset=UTF-8"
            }
        r = TestGetRequest(testurl + '/polls/delete/3', hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope,'status')

    except Exception as e:
        print(e)


#test_delete_question()
#test_post_vote()
#test_delete_question()