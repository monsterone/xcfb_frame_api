# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : test_case.py


import unittest
from ddt import ddt,data
from tools.http_request import HttpRequest
from tools.do_excel import DoExcel
from tools.get_token import GetToken
from tools.project_path import *
from tools.read_config import ReadConfig
from tools.operation_config import OperaConfig
test_data= DoExcel(test_case_path).get_data() #读取用例

@ddt
class TestHttpRequest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        登录获取(后台)token
        :return:
        """
        # 获取主机地址
        HOST = ReadConfig.get_config(case_config_path, 'ADDRESS', 'host')
        url = f'{HOST}/api/auth/oauth/user/token'
        param = {"username":"more","password":"666666"}
        header = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Basic QmFzZVBsYXRmb3JtOjEyMzQ1Ng=="}
        res = HttpRequest().http_request(url,param,'post','params',headers=header)
        setattr(GetToken,"Token",res.json()['value'])  # 反射设置token值
        get_header = {"Content-Type": "application/json;charset=UTF-8",
                  "Authorization": "Bearer " + getattr(GetToken, "Token")}
        setattr(GetToken, "header",get_header) # 反射设置header值

    @classmethod
    def tearDownClass(cls) -> None:
        """
        清除数据：case.ini
        :return:
        """
        OperaConfig.clear_config(file_path)


    @data(*test_data)
    def test_api(self,item):
        # 获取主机地址
        HOST = ReadConfig.get_config(case_config_path, 'ADDRESS', 'host')
        item['url'] = HOST + item['url']  # 获取url
        #提交data为空，关联值get_value不为空
        if  item['data'] == None and item['get_value'] != None:
           if type(eval(item['get_value'])) == dict :
                res = HttpRequest().http_request(item['url'],None,item['method'],item['type'],headers=getattr(GetToken,"header"))
                if res.json()['msg'] == 'OK':
                    get_data = eval(item['get_value'])
                    for keys in get_data.keys():
                        key = keys
                        value = get_data[key]
                    add = 'res.json()'+value
                    add = eval(add)
                    OperaConfig.write_config(file_path, key, key, add)
                try:
                    self.assertEqual(item['expected'],res.json()['msg'])
                    TestResult='PASS'
                except AssertionError as e:
                    TestResult = 'FAIL'
                    print("执行用例出错：{0}".format(e))
                    raise e
                finally:
                    #写回结果(str(res.json()),excel只能写字符串，数字，不能写字典
                    DoExcel(test_case_path,item['sheet_name']).write_back(item['case_id']+1,str(res.json()),TestResult)
                    print("获取到的结果是：{0}".format(res.json()))
        # 提交data不为空，关联值get_value不为空（字符串：使用值）
        elif item['data'] != None and item['get_value'] != None and type(item['get_value']) == str:
            data1 = OperaConfig.read_config(file_path, item['get_value'], item['get_value']) #获取配置文件值
            if item['url'].find(item['get_value']) != -1:
                url = item['url'].replace("{{"+item['get_value']+"}}",data1)
                res = HttpRequest().http_request(url, eval(item['data']), item['method'], item['type'],
                                             headers=getattr(GetToken, "header"))
            elif item['data'] != None and item['data'].find(item['get_value']) != -1:
                data = item['data'].replace("{{"+item['get_value']+"}}",data1)
                res = HttpRequest().http_request(item['url'], eval(data), item['method'], item['type'],
                                          headers=getattr(GetToken, "header"))
            try:
                self.assertEqual(item['expected'],res.json()['msg'])
                TestResult='PASS'
            except AssertionError as e:
                TestResult = 'FAIL'
                print("执行用例出错：{0}".format(e))
                raise e
            finally:
                #写回结果(str(res.json()),excel只能写字符串，数字，不能写字典
                DoExcel(test_case_path,item['sheet_name']).write_back(item['case_id']+1,str(res.json()),TestResult)
                print("获取到的结果是：{0}".format(res.json()))
        # 提交data为空，关联值get_value为空（普通get）
        elif item['data'] == None and item['get_value'] == None:
            res = HttpRequest().http_request(item['url'], None, item['method'], item['type'],
                                             headers=getattr(GetToken, "header"))
            try:
                self.assertEqual(item['expected'], res.json()['msg'])
                TestResult = 'PASS'
            except AssertionError as e:
                TestResult = 'FAIL'
                print("执行用例出错：{0}".format(e))
                raise e
            finally:
                # 写回结果(str(res.json()),excel只能写字符串，数字，不能写字典
                DoExcel(test_case_path, item['sheet_name']).write_back(item['case_id'] + 1, str(res.json()), TestResult)
                print("获取到的结果是：{0}".format(res.json()))
        # 其他
        else:
            res = HttpRequest().http_request(item['url'], eval(item['data']), item['method'], item['type'],
                                             headers=getattr(GetToken, "header"))
            try:
                self.assertEqual(item['expected'],res.json()['msg'])
                TestResult='PASS'
            except AssertionError as e:
                TestResult = 'FAIL'
                print("执行用例出错：{0}".format(e))
                raise e
            finally:
                #写回结果(str(res.json()),excel只能写字符串，数字，不能写字典
                DoExcel(test_case_path,item['sheet_name']).write_back(item['case_id']+1,str(res.json()),TestResult)
                print("获取到的结果是：{0}".format(res.json()))

if __name__ == '__main__':
    # pytest -s test_case.py --alluredir=../test_result/allure_reports --clean-alluredir
    unittest.main()