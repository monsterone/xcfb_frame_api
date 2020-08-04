# -*- coding: utf-8 -*-
# @Author   : Monster
# @File     : read_config.py

import configparser

class ReadConfig():

    @staticmethod
    def get_config(file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')
        return cf[section][option]

