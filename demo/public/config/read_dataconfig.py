import configparser
import os

data_config_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data_config.ini')

config=configparser.ConfigParser()

config.read(data_config_path,encoding='utf-8')#读取配置文件

config.sections() #获取sections节点

config.options('mysql') #获取指定sections的options,即该节点的所有的键：['name', 'host', 'proxy', 'password', 'pool']

config.get('mysql', 'name')  #获取mysql这个section节点下指定option的值,返回为string：admin

config.getint('mysql', 'proxy') #将获取到的值转返回为int型的值:630 type:int

config.getboolean('mysql', 'pool') #将获取到的值返回为布尔值的值：true type:bool

config.getfloat('mysql', 'time') #将获取的值转换为浮点型，返回为float型的值：3.0 type:float

print(config.items('mysql')) #获取指定section下的所有配置信息 [('name', 'admin'), ('host', '255.255.255.0'), ('proxy', '603'), ('password', '123456'), ('pool', 'true'), ('time', '3')]

