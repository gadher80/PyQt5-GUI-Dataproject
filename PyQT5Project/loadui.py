from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox,QHBoxLayout, QWidget
import sys
import pandas as pd
import os,sys, subprocess
from pathlib import Path
import validators
from validators import ValidationFailure
import requests
import csv, sqlite3
import pyquark
from datetime import datetime
#add libraries

DataSets = {}
urlData = {}
addedDatabases = []


class UI(QtWidgets.QDialog):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("DataMiner.ui", self)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.datasetTextEdit = self.findChild(QtWidgets.QTextEdit,"datasetTextEdit")
        self.colNameslist = self.findChild(QtWidgets.QListWidget,"colNameslist")               
        self.commentLabel = self.findChild(QtWidgets.QLabel,"commentLabel")
        self.locationLabel = self.findChild(QtWidgets.QLabel,"locationLabel")
        self.urlTextEdit = self.findChild(QtWidgets.QTextEdit,"urlTextEdit")
        self.datasetLabel = self.findChild(QtWidgets.QLabel,"datasetLabel")
        self.DataTableWidget = self.findChild(QtWidgets.QTableWidget, "DataTableWidget")
        self.EnergyComboList = self.findChild(QtWidgets.QComboBox, "EnergyComboList")
        self.colTextEdit = self.findChild(QtWidgets.QTextEdit, "colTextEdit")
        self.EnergycomboBox = self.findChild(QtWidgets.QComboBox, "EnergycomboBox")
        self.DataTableWidget = self.findChild(QtWidgets.QTableWidget, "DataTableWidget")
        self.submitButton = self.findChild(QtWidgets.QPushButton, "submitButton")
        self.commentTextEdit = self.findChild(QtWidgets.QTextEdit, "commentTextEdit")
        self.closeButton = self.findChild(QtWidgets.QPushButton, "closeButton")
        self.databaseButton = self.findChild(QtWidgets.QPushButton, "databaseButton")
        self.databaseComboBox = self.findChild(QtWidgets.QComboBox, "databaseComboBox")
        self.commentTextEdit.setPlaceholderText("Enter your Comments")
        
        


        self.insertButton = self.findChild(QtWidgets.QPushButton, "insertButton")
        self.deleteButton = self.findChild(QtWidgets.QPushButton, "deleteButton")
        self.EditButton = self.findChild(QtWidgets.QPushButton, "EditButton")
        self.openFileButton = self.findChild(QtWidgets.QPushButton, "openFileButton")
        self.ResetButton = self.findChild(QtWidgets.QPushButton, "ResetButton")

        
        self.insertButton.clicked.connect(self.insertFile)
        self.submitButton.clicked.connect(self.sumbit)
        self.EditButton.clicked.connect(self.editData)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.openFileButton.clicked.connect(self.openFile)
        self.ResetButton.clicked.connect(self.reset)
        self.databaseButton.clicked.connect(self.insertDatabase)
        self.closeButton.clicked.connect(self.close)
        

        

        self.insertButton.setStyleSheet("background-color: #009DE1;" "color: white;" 
                                        "font-size: 10px;" "font-weight: bold;" 
                                        "border-radius: 4px;" "border: 1px solid #009DE1;" 
                                        "opacity: 0.8;")

        self.ResetButton.setStyleSheet("background-color: #009DE1;" "color: white;" 
                                        "font-size: 10px;" "font-weight: bold;" 
                                        "border-radius: 4px;" "border: 1px solid #009DE1;" 
                                        "opacity: 0.8;")
        self.EditButton.setStyleSheet("background-color: #009DE1;" "color: white;" 
                                        "font-size: 10px;" "font-weight: bold;" 
                                        "border-radius: 4px;" "border: 1px solid #009DE1;" 
                                        "opacity: 0.8;")
        self.submitButton.setStyleSheet("background-color: #009DE1;" "color: white;" 
                                        "font-size: 10px;" "font-weight: bold;" 
                                        "border-radius: 4px;" "border: 1px solid #009DE1;" 
                                        "opacity: 0.8;")
        self.deleteButton.setStyleSheet("background-color: #009DE1;" "color: white;" 
                                        "font-size: 10px;" "font-weight: bold;" 
                                        "border-radius: 4px;" "border: 1px solid #009DE1;" 
                                        "opacity: 0.8;")
        self.openFileButton.setStyleSheet("background-color: #009DE1;" "color: white;" 
                                        "font-size: 10px;" "font-weight: bold;" 
                                        "border-radius: 4px;" "border: 1px solid #009DE1;" 
                                        "opacity: 0.8;")

        self.databaseButton.setStyleSheet("background-color: #009DE1;" "color: white;" 
                                        "font-size: 10px;" "font-weight: bold;" 
                                        "border-radius: 4px;" "border: 1px solid #009DE1;" 
                                        "opacity: 0.8;")

        self.closeButton.setStyleSheet("background-color: #009DE1;" "color: white;" 
                                        "font-size: 10px;" "font-weight: bold;" 
                                        "border-radius: 4px;" "border: 1px solid #009DE1;" 
                                        "opacity: 0.8;")                                


        self.deleteButton.setDisabled(True)
        self.openFileButton.setDisabled(True)
        self.EditButton.setDisabled(True)
        self.submitButton.setDisabled(True)

       
        self.show()




    def openFile(self):
        openRow = self.DataTableWidget.currentRow()
        selectedPath = fname[0]
        pyquark.filestart(selectedPath)

        #print(selectedPath)
        #os.startfile(selectedPath)

    def deleteRecord(self):
            message = QtWidgets.QMessageBox()
            message.setWindowTitle("Delete")
            message = QtWidgets.QMessageBox.question(self, "Delete", "Are you sure you want to delete?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if message == QtWidgets.QMessageBox.Yes:
                connection = sqlite3.connect(DataSets[self.DataTableWidget.currentRow()][3])
                cursor = connection.cursor()
                tobeDeleted = str(self.DataTableWidget.item(self.DataTableWidget.currentRow(), 0).text())
                print(tobeDeleted)
                cursor.execute("DROP TABLE IF EXISTS" + ' '+ tobeDeleted)
                connection.commit()
                self.DataTableWidget.removeRow(self.DataTableWidget.currentRow())

    def insertFile(self):
        self.submitButton.setDisabled(False)
        global fname
        fname = QFileDialog.getOpenFileName(self, "Choose CSV", "","All files(*);;(*.csv);;(*.json);;(*.xlsm);;(*.xlsx)")

        if fname: 
            print(fname[0])
            self.locationLabel.setText(fname[0])
            self.datasetTextEdit.setPlainText(Path(fname[0]).stem)
            fileExtension = os.path.splitext(fname[0])[1].replace(".","").upper()
            self.EnergyComboList.setCurrentText(fileExtension) 
            global df
            df = pd.read_csv(fname[0], encoding= 'unicode_escape')
            self.colTextEdit.setPlainText(str(len(df.columns)))
            

            for item in df.columns.values.tolist():
                 self.colNameslist.addItem(item)

    def insertDatabase(self):
        dataBasename = QFileDialog.getOpenFileName(self, "Choose Database File", "","(*.db)")
        if os.path.basename(dataBasename[0]) not in addedDatabases:
            addedDatabases.append(os.path.basename(dataBasename[0]))
            self.databaseComboBox.addItem(os.path.basename(dataBasename[0]))
        self.databaseComboBox.setCurrentText(os.path.basename(dataBasename[0]))
        
        

        
    def reset(self):
        message = QtWidgets.QMessageBox()
        message.setWindowTitle("Reset")
        message = QtWidgets.QMessageBox.question(self, "Reset", "Are you sure you want to reset?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if message == QtWidgets.QMessageBox.Yes:
            self.locationLabel.clear()
            self.datasetTextEdit.clear()
            self.urlTextEdit.clear()
            self.commentTextEdit.clear()
            self.colNameslist.clear()
            self.colTextEdit.clear()
        

    def sumbit(self):

        #check if given URL is existing
        #url validation
        global now
        now = datetime.now()
        validationValue =validators.url(self.urlTextEdit.toPlainText())

        
        if self.datasetTextEdit.toPlainText() == "": 
            
            message = QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a dataset name")
            
        elif validationValue != True:
            message = QtWidgets.QMessageBox.warning(self, "Warning", "Invalid URL") 
            

        elif self.commentTextEdit.toPlainText() == "":
            message = QtWidgets.QMessageBox.warning(self, "Warning", "Please write a comment")
         

        else:         
            global targetedDatabase
            targetedDatabase = self.databaseComboBox.currentText()
            connection = sqlite3.connect(targetedDatabase)
            cursor = connection.cursor()

            users = pd.read_csv(fname[0], encoding= 'unicode_escape')

            # messege box for : do you want to save it to Databse or not?
            message = QtWidgets.QMessageBox.question(self, "Save", "Do you want to save it to Database?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if message == QtWidgets.QMessageBox.Yes:
                users.to_sql(f'{self.datasetTextEdit.toPlainText()}', connection, if_exists='append', index = False)
            self.loaddata()
            self.locationLabel.clear()
            self.datasetTextEdit.clear()
            self.urlTextEdit.clear()
            self.commentTextEdit.clear()
            self.colNameslist.clear()
            self.colTextEdit.clear()
            if self.DataTableWidget.rowCount() > 0:
                self.deleteButton.setDisabled(False)
                self.openFileButton.setDisabled(False)
                self.EditButton.setDisabled(False)
        
    def editData(self):
        self.datasetTextEdit.setText(self.DataTableWidget.item(self.DataTableWidget.currentRow(), 0).text())
        self.urlTextEdit.setText(DataSets[self.DataTableWidget.currentRow()][1])
        self.locationLabel.setText(DataSets[self.DataTableWidget.currentRow()][0])
        self.commentTextEdit.setText(self.DataTableWidget.item(self.DataTableWidget.currentRow(), 3).text())
        self.colNameslist.insertItems(0, DataSets[self.DataTableWidget.currentRow()][2])
        connection = sqlite3.connect(DataSets[self.DataTableWidget.currentRow()][3])
        cursor = connection.cursor()
        tobeDeleted = str(self.DataTableWidget.item(self.DataTableWidget.currentRow(), 0).text())
        print(tobeDeleted)
        cursor.execute("DROP TABLE IF EXISTS" + ' '+ tobeDeleted)
        connection.commit()
        self.colTextEdit.setPlainText(str(len(DataSets[self.DataTableWidget.currentRow()][2])))
        self.EnergycomboBox.setCurrentText(DataSets[self.DataTableWidget.currentRow()][4])
        self.EnergyComboList.setCurrentText(DataSets[self.DataTableWidget.currentRow()][5])
        self.databaseComboBox.setCurrentText(DataSets[self.DataTableWidget.currentRow()][3])
        self.DataTableWidget.removeRow(self.DataTableWidget.currentRow())
        
        if self.DataTableWidget.rowCount() == 0:
            self.deleteButton.setDisabled(True)
            self.openFileButton.setDisabled(True)
            self.EditButton.setDisabled(True)


    def loaddata(self):
        
        Data = [{"Name of Dataset": self.datasetTextEdit.toPlainText(),
                "Energy Type": self.EnergycomboBox.currentText(),
                    "File Type": self.EnergyComboList.currentText(), 
                    "Comments": self.commentTextEdit.toPlainText(),
                    "Location": self.locationLabel.text(),
                    "URL": self.urlTextEdit.toPlainText(),
                    "Created Date": now.strftime("%Y-%m-%d %H:%M:%S"),
                    }]

        row = self.DataTableWidget.rowCount()
        self.DataTableWidget.setRowCount(row + 1 ) 
        
        for data in Data:
            self.DataTableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data["Name of Dataset"]))
            self.DataTableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data["Energy Type"]))
            self.DataTableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data["File Type"]))
            self.DataTableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data["Comments"]))
            self.DataTableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data["Created Date"]))
            DataSets[row] = [data["Location"], data["URL"], df.columns.values.tolist(), self.databaseComboBox.currentText(), data["Energy Type"], data["File Type"]]
            Data.clear()
        
        
    

app = QtWidgets.QApplication(sys.argv)
UIWindow = UI()
app.exec_()