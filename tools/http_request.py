# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : http_request.py

import requests


class HttpRequest():

    def http_request(self,url,data,method,cookie=None):

        try:
            if method.lower() == "get":
                res=requests.get(url,data,cookies=cookie)
            elif method.lower() == "post":
                res=requests.post(url,data,cookies=cookie)
            else:
                print("输入的请求方法不对")
        except Exception as e:
            print("请求报错了:{0}".format(e))
            raise e
        return res

if __name__ == '__main__':
    pass