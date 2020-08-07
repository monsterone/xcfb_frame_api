# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : run.py


import unittest
from test_result.TestRunner.HTMLTestRunnerCN import HTMLTestReportCN
from tools.project_path import *
from test_suite.test_case import TestHttpRequest

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))


with open(test_report_path,'wb') as file:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=file,
                                             verbosity=2,
                                             title="测试用例",
                                             description="cs",
                                             tester="monster")
    runner.run(suite)

