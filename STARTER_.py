# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'starter.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Starter(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon.fromTheme("Basic")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 471, 351))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setStyleSheet("image:url(:/Pics/Official Logo [Azeem Ent.].jpg);")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 430, 171, 16))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 460, 111, 31))
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(34, 107, 74);\n"
"border-radius:100px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(110, 480, 71, 71))
        self.exit_btn.setStyleSheet("background-image:url(:/Pics/exit.png);")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.Reg_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Reg_Btn.setGeometry(QtCore.QRect(320, 380, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Reg_Btn.setFont(font)
        self.Reg_Btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Reg_Btn.setStyleSheet("QPushButton{\n"
"background-color:red;\n"
"border-radius:20;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:green;\n"
"}\n"
"")
        self.Reg_Btn.setObjectName("Reg_Btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Azeem Enterprises"))
        self.label_2.setText(_translate("MainWindow", "Already a member?"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.Reg_Btn.setText(_translate("MainWindow", "Register"))

