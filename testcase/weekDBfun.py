__author__ = 'abao2k'
import unittest
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath
import xlrd
import sys
import sqlite3 as db
from ReadFromDB import db_get_cursor
from TestRequest import TestDeleteRequest
import threading


def caserun(funname):
    #根据方法名称取用例，可能含有多个用例
    sql = 'SELECT id, funname, caseid, casename  from polls_case where funname=\''+funname+'\'  order by caseid'
    cursor = db_get_cursor(sql)
    rows = cursor.fetchall()

    for row in rows:

        caseid = row[2]
        print ("caseid=="+str(caseid))
        casename = row[3]
        hdata = {}
        headers = {}
        remsg =''
        recode = ''
        restatus = ''
        unionurl =''
        method = ''
        #使用用例id获取该用例下的参数信息，含case=0的通用参数
        sqlparam = 'SELECT paramtype, paramname, paramvalue from polls_caseparam where caseid in (\''+str(caseid)+'\',\'0\')'

        cursor = db_get_cursor(sqlparam)
        rowparams = cursor.fetchall()
        for rowparam in rowparams:
            paramtype = rowparam[0]
            paramname = rowparam[1]
            paramvalue = rowparam[2]
            if paramtype == 'common':#common存放公共headers与主url信息
                if paramname =='content-type':
                    headers[paramname] = paramvalue
                if paramname == 'url':
                    unionurl = paramvalue
            if paramtype == 'url':#url存放主url后面需拼接的url信息
                unionurl = unionurl+paramname
            if paramtype == 'content-type':#如果特殊用例不是使用共用headers的情况，可以单独定义
                headers[paramname] = paramvalue
            if paramtype == 'in':#存放入参，即data的内容
                hdata[paramname] = paramvalue
            if paramtype == 'out':#存放出参，其中recode为不同平台成功状态的编码，可能不同 例如：code、state等
                if paramname =='msg':
                    recode = 'msg'
                    remsg = paramvalue
                else:
                    recode = paramname
                    restatus = paramvalue
            if paramtype == 'method':#存放调用方法如 get post delete
                method = paramname
        htestcassid = caseid#用例id
        htestcassname = casename#用例名称
        htesthope = str(int(restatus))#期望返回的成功状态
        fanhuitesthope = str(remsg)#期望返回的结果信息
        if method=='get':
            r = TestGetRequest(unionurl, hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope,recode)
        elif method=='post':
            r = TestPostRequest(unionurl, hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope)
        elif method=='delete':
            r = TestDeleteRequest(unionurl, hdata,headers,htestcassid,htestcassname,htesthope, fanhuitesthope)




def test_login():#登陆接口
    try:
        funname = sys._getframe().f_code.co_name
        caserun(funname)
    except Exception as e:
        print(e)

def test_api1():#天气获取接口
    try:
        funname = sys._getframe().f_code.co_name
        caserun(funname)
    except Exception as e:
        print(e)

def test_api2():#个性网名获取接口
    try:
        funname = sys._getframe().f_code.co_name
        caserun(funname)
    except Exception as e:
        print(e)

def test_api3():#小说搜索接口
    try:
        funname = sys._getframe().f_code.co_name
        caserun(funname)
    except Exception as e:
        print(e)


