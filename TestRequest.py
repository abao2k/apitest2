# -*- coding:utf-8 -*-
import json
import requests
from log import logger

#http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
# 添加一个数组,用来装测试结果

#公共的头文件设置
header = {
'content-type': "application/json;charset=UTF-8"
}

hlist = []

def TestGetRequest(hurl, hdata, headers, htestcassid, htestcassname, htesthope, fanhuitesthope,hopetype):
    if hdata =="":
        hr = requests.get(hurl,  headers=header)
    else:
        hr = requests.get(hurl, params=hdata)
    hjson = json.loads(hr.text) # 获取并处理返回的json数据
    hstatus = str(hjson[hopetype])

    if str(hstatus) == str(htesthope) and fanhuitesthope in str(hjson):
        hhhdata = {"t_id": htestcassid,
                   "t_name": htestcassname,
                   "t_method": "GET",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope":  "期望值: status=" + str(htesthope) + ",msg包含:" + fanhuitesthope,
                    "t_actual":"实际值: status=" + hstatus + ",msg=" + str(hjson),
                    "t_result": "通过"}
        hlist.append(hhhdata) # 把测试结果添加到数组里面
        logger.info(htestcassname)
        logger.info("通过")
        logger.info("实际值"+str(hjson))
    else:
        hhhdata = {"t_id": htestcassid,
                   "t_name": htestcassname,
                    "t_method": "GET",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope": "期望值: status=" + str(htesthope) + ",msg包含:" + fanhuitesthope,
                    "t_actual":"实际值: status=" + hstatus + ",msg=" + str(hjson),
                    "t_result": "失败"}
        hlist.append(hhhdata)
        logger.error(htestcassname)
        logger.error("失败")
        logger.error("实际值"+str(hjson))
    #print (hlist)



def TestPostRequest(hurl, hdata, headers, htestcassid, htestcassname, htesthope, fanhuitesthope):

    #hr = requests.post(hurl, data=json.dumps(hdata), headers=headers)
    hr = requests.post(hurl, data=hdata, headers=headers)

    hjson = json.loads(hr.text) # 获取并处理返回的json数据
    hstatus = str(hjson["status"])

    #print (str(hstatus))
    #print (str(htesthope))
    if str(hstatus) == str(htesthope) and fanhuitesthope in str(hjson):
        hhhdata = {"t_id": htestcassid,
                   "t_name": htestcassname,
                   "t_method": "POST",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope": "期望值: status=" + str(htesthope) + ",msg包含:" + fanhuitesthope,
                    "t_actual":"实际值: status=" + hstatus + ",msg=" + str(hjson),
                    "t_result": "通过"}
        hlist.append(hhhdata) # 把测试结果添加到数组里面
        logger.info(htestcassname)
        logger.info("通过")
        logger.info("实际值"+str(hjson))

    else:
        hhhdata = {"t_id": htestcassid,
                   "t_name": htestcassname,
                    "t_method": "POST",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope": "期望值: status=" + str(htesthope) + ",msg包含:" + fanhuitesthope,
                    "t_actual":"实际值: status=" + hstatus + ",msg=" + str(hjson),
                    "t_result": "失败"}
        hlist.append(hhhdata)
        logger.error(htestcassname)
        logger.error("失败")
        logger.error("实际值"+str(hjson))
    #print (hlist)



def TestDeleteRequest(hurl, hdata, headers, htestcassid, htestcassname, htesthope, fanhuitesthope):

    if hdata =="":
        hr = requests.delete(hurl,  headers=header)
    else:
        hr = requests.delete(hurl, params=hdata, headers=header)

    hjson = json.loads(hr.text) # 获取并处理返回的json数据
    hstatus = str(hjson["status"])
    if str(hstatus) == str(htesthope) and fanhuitesthope in str(hjson):
        hhhdata = {"t_id": htestcassid,
                   "t_name": htestcassname,
                   "t_method": "DELETE",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope": "期望值: status=" + str(htesthope) + ",msg包含:" + fanhuitesthope,
                    "t_actual":"实际值: status=" + hstatus + ",msg=" + str(hjson),
                    "t_result": "通过"}
        hlist.append(hhhdata) # 把测试结果添加到数组里面
        logger.info(htestcassname)
        logger.info("通过")
        logger.info("实际值"+str(hjson))
    else:
        hhhdata = {"t_id": htestcassid,
                   "t_name": htestcassname,
                    "t_method": "DELETE",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope": "期望值: status=" + str(htesthope) + ",msg包含:" + fanhuitesthope,
                    "t_actual":"实际值: status=" + hstatus + ",msg=" + str(hjson),
                    "t_result": "失败"}
        hlist.append(hhhdata)
        logger.error(htestcassname)
        logger.error("失败")
        logger.error("实际值"+str(hjson))
    #print (hlist)

