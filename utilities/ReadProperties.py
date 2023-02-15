import configparser
from configparser import ConfigParser
config=configparser.RawConfigParser()
import os
file_name= ".//configuration//config.ini"
config.read((os.path.relpath(file_name)))

class configRead:

    @staticmethod
    def ReadUrl():
        url=config.get('common Info', 'base_url')
        print(url)
        return url

    @staticmethod
    def ReadUsername():
        username=config.get('common Info', 'username')
        return username

    @staticmethod
    def Readpassword():
        password=config.get('common Info', 'password')
        return password

    @staticmethod
    def ReadWaitTime():
        waitTime = config.get('common Info', 'wait')
        print(waitTime)
        return waitTime

    @staticmethod
    def ReadApiUrl():
        url = config.get('api Info', 'base_url_api')
        print(url)
        return url

    @staticmethod
    def ReadGetUrl():
        url = config.get('api Info', 'get_url')
        print(url)
        return url

    @staticmethod
    def ReadPostUrl():
        url = config.get('api Info', 'post_url')
        print(url)
        return url

    @staticmethod
    def ReadPutUrl():
        url = config.get('api Info', 'put_url')
        print(url)
        return url

    @staticmethod
    def ReadDeleteUrl():
        url = config.get('api Info', 'delete_url')
        print(url)
        return url

    @staticmethod
    def Read_DB_Config(filename=file_name, section='mysql'):
        """ Read database configuration file and return a dictionary object
                 :param filename: name of the configuration file
                 :param section: section of database configuration
                 :return: a dictionary of database parameters
                 """
        db = {}
        if config.has_section(section):
            items = config.items(section)
            for item in items:
                db[item[0]] = item[1]
        else:
            raise Exception('{0} not found in the {1} file'.format(section, filename))
        print("Printing from ReadProperties file--->", db)
        return db


'''when you run read properties you will not get returned value but you will get error
but when you import this read properties and run from test method you will
get returned value and can check by printing value there in test method.
this is because we have use relative path in line6'''
