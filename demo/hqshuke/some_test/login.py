import os
import sys

path_public=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+r'\public'
sys.path.append(path_public)
sys.path.append(os.path.join(path_public,'config'))


from browser_actions import Commonweb
from read_dataconfig import ReadConfig
from handlelog import MyLog
from handlepath import BASEDIR


common=Commonweb()
read=ReadConfig()
log=MyLog()
print(BASEDIR)

# class logintest():

#     # def test(self):
#     #     print(555)
#     #     log.my_logger.info('执行test444')
#     def __init__(self):
#         common.open_browser()

#     def logincase(self,type):
#         try:
#             if type=='jc':
#                 common.open_web(read.get_value('url', 'jc'))
#                 common.web_click('css,ddddd')
#             else:
#                 common.open_web(read.get_value('url', 'zsc'))
#         except Exception as msg:
#             common.get_screenpict('test')
#         finally:
#             log.my_logger().info('执行登陆')

# if __name__ == '__main__':
#     lgo=logintest()
#     lgo.logincase('jc')
