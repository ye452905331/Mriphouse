# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audio_car.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_car = QtWidgets.QLabel(self.centralwidget)
        self.label_car.setGeometry(QtCore.QRect(160, 80, 491, 341))
        self.label_car.setStyleSheet("image: url(/home/pi/mywork/test7/car/UIimage/v_pearlwhite_0008.png);")
        #image: url(/home/pi/Downloads/car/v_pearlwhite_0008.png)
        self.label_car.setText("")
        self.label_car.setObjectName("label_car")
        self.label_frdoor = QtWidgets.QLabel(self.centralwidget)
        self.label_frdoor.setGeometry(QtCore.QRect(150, 100, 521, 301))
        self.label_frdoor.setStyleSheet("image: url(/home/pi/mywork/test7/car/UIimage/v_pearlwhite_frontright_open.png);")
        self.label_frdoor.setText("")
        self.label_frdoor.setObjectName("label_frdoor")
        self.label_trunk = QtWidgets.QLabel(self.centralwidget)
        self.label_trunk.setGeometry(QtCore.QRect(130, 100, 521, 311))
        self.label_trunk.setStyleSheet("image: url(/home/pi/mywork/test7/car/UIimage/v_pearlwhite_trunk_open.png);")
        self.label_trunk.setText("")
        self.label_trunk.setObjectName("label_trunk")
        self.label_bdoor = QtWidgets.QLabel(self.centralwidget)
        self.label_bdoor.setGeometry(QtCore.QRect(130, 90, 521, 321))
        self.label_bdoor.setStyleSheet("\n"
"image: url(/home/pi/mywork/test7/car/UIimage/v_pearlwhite_backleft_open.png);")
        self.label_bdoor.setText("")
        self.label_bdoor.setObjectName("label_bdoor")
        self.label_fldoor = QtWidgets.QLabel(self.centralwidget)
        self.label_fldoor.setGeometry(QtCore.QRect(140, 100, 521, 301))
        self.label_fldoor.setStyleSheet("image: url(/home/pi/mywork/test7/car/UIimage/v_pearlwhite_frontleft_open.png);")
        self.label_fldoor.setText("")
        self.label_fldoor.setObjectName("label_fldoor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def fldoorFuction(self,isopen):
        if isopen:
            self.label_fldoor.setVisible(True)
        else:
            self.label_fldoor.setVisible(False)
    
    def frdoorFuction(self,isopen):
        if isopen:
            self.label_frdoor.setVisible(True)
        else:
            self.label_frdoor.setVisible(False)

    def bdoorFuction(self,isopen):
        if isopen:
            self.label_bdoor.setVisible(True)
        else:
            self.label_bdoor.setVisible(False)

    def trunkFuction(self,isopen):
        if isopen:
            self.label_trunk.setVisible(True)
        else:
            self.label_trunk.setVisible(False)



        

