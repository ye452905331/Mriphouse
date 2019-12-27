import sys
import time
from PyQt5.QtWidgets import QApplication , QMainWindow
sys.path.append('/home/pi/mywork/test7/car/Source')
from Ui_handle import Ui_MainWindow
from xfyun_audiorec import xfyu_audiohadle
from carlib import car_ctlMatch


ui = Ui_MainWindow()

def ctlAll(isopen):
    ui.fldoorFuction(isopen)
    ui.frdoorFuction(isopen)
    ui.bdoorFuction(isopen)
    ui.trunkFuction(isopen)

def audioCommand(au_thing,isopen):
    if au_thing == '左前门'or au_thing == '左门':
        ui.fldoorFuction(isopen)
    elif au_thing == '右前门':
        ui.frdoorFuction(isopen)
    elif au_thing == '左后门'or au_thing == '后门':
        ui.bdoorFuction(isopen)
    elif au_thing == '尾箱'or au_thing == '后尾箱':
        ui.trunkFuction(isopen) 
    elif au_thing == '全':
        ctlAll(isopen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui.setupUi(mainWindow) 
    mainWindow.show()
    ctlAll(0)
    print('Welcome to EISA Please Press following choice:')
    print('  A:Start to contral the car')
    print('  B:Exit')
    ch = input("Press :")
    if ch =='A':
        print('getting start...')
    else :
        sys.exit()
    while True:
        result = xfyu_audiohadle()
        print('result:',result)
        word = result
        #ccmd = input("input you cmd :")
        cthing,ccmd = car_ctlMatch(word)
        if ccmd == '开':
            audioCommand(cthing,1)
        elif ccmd == '关':
            audioCommand(cthing,0)

   
