import os
import sys

path_public=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+r'\public'
sys.path.append(path_public)

from browser_actions import Commonweb


common=Commonweb()

url={'uat':'http://zscw.yilvbao.cn/system/#/login','sit':'http://www.baidu.com'}

class logintest():

    def __init__(self):
        common.open_browser()

    def logincase(self,type):
        try:
            if type=='uat':
                common.open_web(url['uat'])
                common.web_click('css,ddddd')
            else:
                common.open_web(url['sit'])
        except Exception as msg:
            common.get_screenpict('test')

lgo=logintest()
lgo.logincase('uat')