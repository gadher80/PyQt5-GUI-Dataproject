# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\UI Project\UIProject\ProbUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 258)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(130, 50, 269, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(20)
        self.MainLabel.setFont(font)
        self.MainLabel.setMouseTracking(False)
        self.MainLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MainLabel.setObjectName("MainLabel")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(20, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Light")
        font.setPointSize(15)
        self.browseButton.setFont(font)
        self.browseButton.setToolTip("")
        self.browseButton.setObjectName("browseButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 120, 411, 31))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 18))
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
        self.MainLabel.setText(_translate("MainWindow", "Renewable Energy Sources"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
