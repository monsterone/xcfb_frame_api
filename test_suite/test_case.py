# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : test_case.py


import unittest
from ddt import ddt,data
from tools.http_request import HttpRequest
from tools.do_excel import DoExcel
from tools.project_path import *
test_data= DoExcel(test_case_path).get_data() #读取用例

@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self,item):
        res = HttpRequest().http_request(item['url'],eval(item['data']),item['method'])
        try:
            self.assertEqual(item['expected'],res.json()['code'])
            TestResult='PASS'
        except AssertionError as e:
            TestResult = 'FAIL'
            print("执行用例出错：{0}".format(e))
            raise e
        finally:#不管错对，一定执行
            #写回结果(str(res.json()),excel只能写字符串，数字，不能写字典
            DoExcel(test_case_path,item['sheet_name']).write_back(item['case_id']+1,str(res.json()),TestResult)
            print("获取到的结果是：{0}".format(res.json()))

