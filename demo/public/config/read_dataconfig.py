import configparser
import os

data_config_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data_config.ini')

config=configparser.ConfigParser()

config.read(data_config_path,encoding='utf-8')#读取配置文件

config.sections() #获取sections节点

config.options('mysql') #获取指定sections的options,即该节点的所有的键：['name', 'host', 'proxy', 'password', 'pool']

config.get('mysql', 'name')  #获取mysql这个section节点下指定option的值：admin

config.getint('mysql', 'proxy') #将获取到的值转换成int型:603


