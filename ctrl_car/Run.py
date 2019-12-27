#/Code/python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/28 16:58 
# @Author : ye
# @Site :  
# @File : 
# @Software: VS

import sys
import time
from PyQt5.QtWidgets import QApplication , QMainWindow
sys.path.append('/home/pi/mywork/test7/car/Source')
from Ui_handle import Ui_MainWindow
from xfyun_audiorec import xfyu_audiohadle
from carlib import car_ctlMatch


ui = Ui_MainWindow()

#全部控制函数
def ctlAll(isopen):
    ui.fldoorFuction(isopen)
    ui.frdoorFuction(isopen)
    ui.bdoorFuction(isopen)
    ui.trunkFuction(isopen)
    
#单步控制函数
def audioCommand(au_thing,isopen):
    if au_thing == '左前门'or au_thing == '左门' or au_thing == '前门':
        ui.fldoorFuction(isopen)
    if au_thing == '右前门' or au_thing == '前门':
        ui.frdoorFuction(isopen)
    if au_thing == '左后门'or au_thing == '后门':
        ui.bdoorFuction(isopen)
    if au_thing == '箱'or au_thing == '后尾箱':
        ui.trunkFuction(isopen) 
    if au_thing == '全' or au_thing == '所有':
        ctlAll(isopen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow() #建立QT窗体
    ui.setupUi(mainWindow)     #搭建汽车模型
    mainWindow.show()
    ctlAll(0)                  #初始化汽车全部设备关闭
    print('Welcome to EISA Please Press following choice:')
    print('  A:Start to contral the car')
    print('  B:Exit')
    ch = input("Press :")
    if ch =='A':
        print('getting start...')
    else :
        sys.exit()
    while True:
        result = xfyu_audiohadle()#启动录音，发送给讯飞web接口，获取文本result
        print('result:',result)

        #根据车语义库，分析result的动作，控制设备
        #ccmd返回 动作
        #cthing返回 控制设备
        cthing,ccmd = car_ctlMatch(result) 
        if ccmd == '开':
            audioCommand(cthing,1)
        elif ccmd == '关':
            audioCommand(cthing,0)

   
