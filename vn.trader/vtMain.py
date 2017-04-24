# encoding: UTF-8

'''
History
<id>            <author>        <description>
2017042400      hetajen         根据bat脚本参数自动选择交易账户

'''

import sys
import os
import ctypes
import platform

import vtPath
from vtEngine import MainEngine
from uiMainWindow import *

# 文件路径名
path = os.path.abspath(os.path.dirname(__file__))
ICON_FILENAME = 'vnpy.ico'
ICON_FILENAME = os.path.join(path, ICON_FILENAME)

SETTING_FILENAME = 'VT_setting.json'
SETTING_FILENAME = os.path.join(path, SETTING_FILENAME)

#----------------------------------------------------------------------
def main():
    """主程序入口"""
    # 重载sys模块，设置默认字符串编码方式为utf8
    reload(sys)
    sys.setdefaultencoding('utf8')

    # 设置Windows底部任务栏图标
    if 'Windows' in platform.uname() :
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('vn.trader')

    # 初始化Qt应用对象
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(ICON_FILENAME))
    app.setFont(BASIC_FONT)

    # 设置Qt的皮肤
    try:
        f = file(SETTING_FILENAME)
        setting = json.load(f)
        if setting['darkStyle']:
            import qdarkstyle
            app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    except:
        pass

    # 初始化主引擎和主窗口对象
    mainEngine = MainEngine()
    mainWindow = MainWindow(mainEngine, mainEngine.eventEngine)
    mainWindow.showMaximized()

    # 在主线程中启动Qt事件循环
    sys.exit(app.exec_())

'''2017042400 Add by hetajen begin'''
def choose_user(argv):
    if len(argv) > 1:
        path_src = os.path.join(os.path.abspath('.'), u'ctpGateway\\CTP_connect' + unicode(argv[1]))
    else:
        path_src = os.path.join(os.path.abspath('.'), u'ctpGateway\\CTP_connect_simnow.json')

    path_dst = os.path.join(os.path.abspath('.'), u'ctpGateway\\CTP_connect.json')
    try:
        with open(unicode(path_src), 'r') as src:
            with open(unicode(path_dst), "w") as dst:
                dst.write(src.read())
    except IOError:
        print "func(%s)'s Error: %s" % (sys._getframe().f_code.co_name, IOError)
'''2017042400 Add by hetajen end'''

if __name__ == '__main__':
    '''2017042400 Add by hetajen begin'''
    choose_user(sys.argv)
    '''2017042400 Add by hetajen end'''
    main()