# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonPercentage = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.press_it("%"))
        self.pushButtonPercentage.setGeometry(QtCore.QRect(30, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPercentage.setFont(font)
        self.pushButtonPercentage.setObjectName("pushButtonPercentage")
        self.pushButtonC = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.press_it("C"))
        self.pushButtonC.setGeometry(QtCore.QRect(110, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonC.setFont(font)
        self.pushButtonC.setObjectName("pushButtonC")
        self.pushButtonErase = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("<<"))
        self.pushButtonErase.setGeometry(QtCore.QRect(190, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonErase.setFont(font)
        self.pushButtonErase.setObjectName("pushButtonErase")
        self.pushButtonDiv = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("/"))
        self.pushButtonDiv.setGeometry(QtCore.QRect(270, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDiv.setFont(font)
        self.pushButtonDiv.setObjectName("pushButtonDiv")
        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.pushButton7.setGeometry(QtCore.QRect(30, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton7.setFont(font)
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
        self.pushButton8.setGeometry(QtCore.QRect(110, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton8.setFont(font)
        self.pushButton8.setObjectName("pushButton8")
        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.pushButton9.setGeometry(QtCore.QRect(190, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton9.setFont(font)
        self.pushButton9.setObjectName("pushButton9")
        self.pushButtonX = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
        self.pushButtonX.setGeometry(QtCore.QRect(270, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonX.setFont(font)
        self.pushButtonX.setObjectName("pushButtonX")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.pushButton4.setGeometry(QtCore.QRect(30, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.pushButton5.setGeometry(QtCore.QRect(110, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.pushButton6.setGeometry(QtCore.QRect(190, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName("pushButton6")
        self.pushButtonMinus = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.pushButtonMinus.setGeometry(QtCore.QRect(270, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonMinus.setFont(font)
        self.pushButtonMinus.setObjectName("pushButtonMinus")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.pushButton1.setGeometry(QtCore.QRect(30, 350, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.pushButton2.setGeometry(QtCore.QRect(110, 350, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.pushButton3.setGeometry(QtCore.QRect(190, 350, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        self.pushButtonPlus = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.pushButtonPlus.setGeometry(QtCore.QRect(270, 350, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPlus.setFont(font)
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.pushButtonPlusMinus = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+/-"))
        self.pushButtonPlusMinus.setGeometry(QtCore.QRect(30, 430, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPlusMinus.setFont(font)
        self.pushButtonPlusMinus.setObjectName("pushButtonPlusMinus")
        self.pushButton0 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.pushButton0.setGeometry(QtCore.QRect(110, 430, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton0.setFont(font)
        self.pushButton0.setObjectName("pushButton0")
        self.pushButtonDot = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dot_it())
        self.pushButtonDot.setGeometry(QtCore.QRect(190, 430, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDot.setFont(font)
        self.pushButtonDot.setObjectName("pushButtonDot")
        self.pushButtonEqual = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("="))
        self.pushButtonEqual.setGeometry(QtCore.QRect(270, 430, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEqual.setFont(font)
        self.pushButtonEqual.setObjectName("pushButtonEqual")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def dot_it(self):
        screen = self.label.text()
        if "." in screen:
            pass
        else:
            self.label.setText(f"{screen}.")


    def press_it(self, pressed):

        if pressed == "C":
            self.label.setText("0")
        else:
            if self.label.text() == "0":
                self.label.setText("")
            self.label.setText(f"{self.label.text()}{pressed}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonPercentage.setText(_translate("MainWindow", "%"))
        self.pushButtonC.setText(_translate("MainWindow", "C"))
        self.pushButtonErase.setText(_translate("MainWindow", "<<"))
        self.pushButtonDiv.setText(_translate("MainWindow", "/"))
        self.pushButton7.setText(_translate("MainWindow", "7"))
        self.pushButton8.setText(_translate("MainWindow", "8"))
        self.pushButton9.setText(_translate("MainWindow", "9"))
        self.pushButtonX.setText(_translate("MainWindow", "X"))
        self.pushButton4.setText(_translate("MainWindow", "4"))
        self.pushButton5.setText(_translate("MainWindow", "5"))
        self.pushButton6.setText(_translate("MainWindow", "6"))
        self.pushButtonMinus.setText(_translate("MainWindow", "-"))
        self.pushButton1.setText(_translate("MainWindow", "1"))
        self.pushButton2.setText(_translate("MainWindow", "2"))
        self.pushButton3.setText(_translate("MainWindow", "3"))
        self.pushButtonPlus.setText(_translate("MainWindow", "+"))
        self.pushButtonPlusMinus.setText(_translate("MainWindow", "+/-"))
        self.pushButton0.setText(_translate("MainWindow", "0"))
        self.pushButtonDot.setText(_translate("MainWindow", "."))
        self.pushButtonEqual.setText(_translate("MainWindow", "="))
        self.label.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
