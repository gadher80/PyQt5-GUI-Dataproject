# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataMiner.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1095, 453)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(510, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.EnergycomboBox = QtWidgets.QComboBox(Dialog)
        self.EnergycomboBox.setGeometry(QtCore.QRect(540, 120, 69, 21))
        self.EnergycomboBox.setObjectName("EnergycomboBox")
        self.EnergycomboBox.addItem("")
        self.EnergycomboBox.addItem("")
        self.EnergycomboBox.addItem("")
        self.EnergycomboBox.addItem("")
        self.EnergycomboBox.addItem("")
        self.EnergycomboBox.addItem("")
        self.DatasetLineEdit = QtWidgets.QLineEdit(Dialog)
        self.DatasetLineEdit.setGeometry(QtCore.QRect(140, 120, 381, 20))
        self.DatasetLineEdit.setObjectName("DatasetLineEdit")
        self.UrlLineEdit = QtWidgets.QLineEdit(Dialog)
        self.UrlLineEdit.setGeometry(QtCore.QRect(140, 150, 471, 20))
        self.UrlLineEdit.setObjectName("UrlLineEdit")
        self.locationLineEdit = QtWidgets.QLineEdit(Dialog)
        self.locationLineEdit.setGeometry(QtCore.QRect(140, 180, 471, 20))
        self.locationLineEdit.setObjectName("locationLineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 210, 69, 22))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.ColNamesLineEdit = QtWidgets.QLineEdit(Dialog)
        self.ColNamesLineEdit.setGeometry(QtCore.QRect(140, 240, 471, 20))
        self.ColNamesLineEdit.setObjectName("ColNamesLineEdit")
        self.ColLineEdit = QtWidgets.QLineEdit(Dialog)
        self.ColLineEdit.setGeometry(QtCore.QRect(340, 210, 41, 20))
        self.ColLineEdit.setObjectName("ColLineEdit")
        self.CommenttextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.CommenttextBrowser.setGeometry(QtCore.QRect(50, 290, 561, 121))
        self.CommenttextBrowser.setObjectName("CommenttextBrowser")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 240, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(240, 210, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 270, 101, 16))
        self.label_8.setObjectName("label_8")
        self.ResetButton = QtWidgets.QPushButton(Dialog)
        self.ResetButton.setGeometry(QtCore.QRect(460, 420, 75, 23))
        self.ResetButton.setObjectName("ResetButton")
        self.insertButton = QtWidgets.QPushButton(Dialog)
        self.insertButton.setGeometry(QtCore.QRect(50, 65, 86, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.insertButton.setFont(font)
        self.insertButton.setIconSize(QtCore.QSize(20, 20))
        self.insertButton.setCheckable(False)
        self.insertButton.setDefault(False)
        self.insertButton.setFlat(False)
        self.insertButton.setObjectName("insertButton")
        self.DataTableWidget = QtWidgets.QTableWidget(Dialog)
        self.DataTableWidget.setGeometry(QtCore.QRect(640, 60, 441, 381))
        self.DataTableWidget.setObjectName("DataTableWidget")
        self.DataTableWidget.setColumnCount(4)
        self.DataTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DataTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DataTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DataTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DataTableWidget.setHorizontalHeaderItem(3, item)
        self.submitButton = QtWidgets.QPushButton(Dialog)
        self.submitButton.setGeometry(QtCore.QRect(540, 420, 75, 23))
        self.submitButton.setObjectName("submitButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Data Miner App"))
        self.EnergycomboBox.setItemText(0, _translate("Dialog", "Solar"))
        self.EnergycomboBox.setItemText(1, _translate("Dialog", "Wind"))
        self.EnergycomboBox.setItemText(2, _translate("Dialog", "Biomass"))
        self.EnergycomboBox.setItemText(3, _translate("Dialog", "Geothermal"))
        self.EnergycomboBox.setItemText(4, _translate("Dialog", "Hydropower"))
        self.EnergycomboBox.setItemText(5, _translate("Dialog", "Other"))
        self.comboBox_2.setCurrentText(_translate("Dialog", "CSV"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "CSV"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Json"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "XLSM"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Excel"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Other"))
        self.label_2.setText(_translate("Dialog", "Name of Dataset"))
        self.label_3.setText(_translate("Dialog", "URL"))
        self.label_4.setText(_translate("Dialog", "File location"))
        self.label_5.setText(_translate("Dialog", "File type"))
        self.label_6.setText(_translate("Dialog", "Column names"))
        self.label_7.setText(_translate("Dialog", "Number of columns"))
        self.label_8.setText(_translate("Dialog", "Comments"))
        self.ResetButton.setText(_translate("Dialog", "Reset"))
        self.insertButton.setText(_translate("Dialog", "Insert Dataset"))
        item = self.DataTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "No."))
        item = self.DataTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name of Dataset"))
        item = self.DataTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "File Type"))
        item = self.DataTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Comments"))
        self.submitButton.setText(_translate("Dialog", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
