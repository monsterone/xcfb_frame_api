# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : project_path.py

import os,sys

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
#配置文件

#测试用例路径
test_case_path = os.path.join(BASE_DIR,'test_data','xcfb_api8.xlsx')

#测试报告路径
test_report_path = os.path.join(BASE_DIR,'test_result','html_report','result.html')

#配置文件的路径
case_config_path = os.path.join(BASE_DIR,'conf','case.config')


#ini配置文件的路径
file_path = os.path.join(BASE_DIR,'conf','case.ini')