# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : http_request.py

import requests


class HttpRequest():
    """
    Request接口请求封装
    """

    def http_request(self,url,data,method,type,**parms):
        """
        接口请求方法
        :param url: 请求地址
        :param data: 请求参数
        :param method: 请求方法
        :param type: 请求参数(方法)类型
        :param parms: 其他参数
        :return:
        """

        try:
            if method.lower() == "get":
                res=requests.get(url,data,**parms)
            elif method.lower() == "post":
                if type == 'params':
                    res = requests.post(url,params=data,**parms)
                elif type == 'json':
                    res=requests.post(url,json=data,**parms)
                else:
                    res=requests.post(url,data=data,**parms)
            elif method.lower() == "put":
                if type == 'params':
                    res = requests.put(url, params=data, **parms)
                elif type == 'json':
                    res = requests.put(url, json=data, **parms)
                else:
                    res = requests.put(url, data=data, **parms)
            elif method.lower() == "delete":
                if type == 'params':
                    res = requests.delete(url, params=data, **parms)
                elif type == 'json':
                    res = requests.delete(url, json=data, **parms)
                else:
                    res = requests.delete(url, data=data, **parms)
            else:
                print("输入的请求方法不对")
        except Exception as e:
            print("请求报错了:{0}".format(e))
            raise e
        return res

if __name__ == '__main__':
    pass