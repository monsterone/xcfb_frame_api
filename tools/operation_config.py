
# @Author : Monster

from tools.project_path import file_path
import configparser
class OperaConfig():
    """
    操作配置文件
    """

    @staticmethod
    def read_config(file_path,section,option):
        """
        读取配置文件config
        :param file_path:配置文件路径
        :param section:
        :param option:
        :return:
        """
        cf=configparser.ConfigParser()
        cf.read(file_path)
        # return cf.get(section,option)
        return cf[section][option]

    @staticmethod
    def write_config(file_path, section, option,value):
        """
        写入配置文件config
        :param file_path: 配置文件路径
        :param section: 
        :param option: 
        :param value: 写入值
        :return: 
        """""
        cf = configparser.ConfigParser()
        cf.add_section(section)
        cf.set(section, option, str(value))
        with open(file_path, "a+") as f:
            cf.write(f)

    @staticmethod
    def remove_config(file_path,section):
        """
        删除配置文件config
        :param file_path: 配置文件路径
        :param section: 
        :param option: 
        :param value: 写入值
        :return: 
        """""
        cf = configparser.ConfigParser()
        cf.read(file_path)
        # cf.remove_option(section,option)
        cf.remove_section(section)
        with open(file_path, "w") as f:
            cf.write(f)

    @staticmethod
    def clear_config(file_path):
        """
        清空配置文件config
        :param file_path: 配置文件路径
        :param section: 
        :param option: 
        :param value: 写入值
        :return: 
        """""
        cf = configparser.ConfigParser()
        cf.read(file_path)
        cf.clear()
        with open(file_path, "w") as f:
            cf.write(f)

    @staticmethod
    def more_write_config(file_path,value):
        """
        多条写入配置文件config
        :param file_path: 配置文件路径
        :param section: 
        :param option: 
        :param value: 写入值
        :return: 
        """""
        cf = configparser.ConfigParser()
        try:
            for section in value:
                cf.add_section(section)
                for option in value[section]:
                    cf.set(section,option,str(value[section][option]))
            with open(file_path, "a+") as f:
                cf.write(f)
        except Exception as e:
            print("多配置写入出错！！！")
            raise e
