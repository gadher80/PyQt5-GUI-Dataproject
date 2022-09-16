from email import message
from tkinter import messagebox
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox,QHBoxLayout, QWidget, QFrame
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
import random
import string
import uuid 
#add libraries

DataSets = {}
urlData = {}
addedDatabases = []
addedRows ={}

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
# print(addedRows.values())



class UI(QtWidgets.QDialog):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("DataMiner.ui", self)
        #add background image to the window
        #add background to the window


        self.DataTableWidget = self.findChild(QtWidgets.QTableWidget, "DataTableWidget")
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM addedData")
        records = cursor.fetchall()
        for row_number, row_data in enumerate(records):
            self.DataTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.DataTableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.DataTableWidget.resizeColumnsToContents()
        self.frame = self.findChild(QtWidgets.QFrame, "frame")
        #self.setStyleSheet("background-color: #000000;")

        self.datasetTextEdit = self.findChild(QtWidgets.QTextEdit,"datasetTextEdit")
        self.colNameslist = self.findChild(QtWidgets.QListWidget,"colNameslist")               
        self.commentLabel = self.findChild(QtWidgets.QLabel,"commentLabel")
        self.locationLabel = self.findChild(QtWidgets.QLabel,"locationLabel")
        self.urlTextEdit = self.findChild(QtWidgets.QTextEdit,"urlTextEdit")
        self.datasetLabel = self.findChild(QtWidgets.QLabel,"datasetLabel")
        
        self.EnergyComboList = self.findChild(QtWidgets.QComboBox, "EnergyComboList")
        self.colTextEdit = self.findChild(QtWidgets.QTextEdit, "colTextEdit")
        self.EnergycomboBox = self.findChild(QtWidgets.QComboBox, "EnergycomboBox")
        self.DataTableWidget = self.findChild(QtWidgets.QTableWidget, "DataTableWidget")
        self.updateButton = self.findChild(QtWidgets.QPushButton, "updateButton")
        self.commentTextEdit = self.findChild(QtWidgets.QTextEdit, "commentTextEdit")
        self.closeButton = self.findChild(QtWidgets.QPushButton, "closeButton")
        self.databaseButton = self.findChild(QtWidgets.QPushButton, "databaseButton")
        self.databaseComboBox = self.findChild(QtWidgets.QComboBox, "databaseComboBox")
        self.saveButton = self.findChild(QtWidgets.QPushButton, "saveButton")
        self.commentTextEdit.setPlaceholderText("Enter your Comments")
        self.urlTextEdit.setPlaceholderText("Enter URL")   
        self.insertButton = self.findChild(QtWidgets.QPushButton, "insertButton")
        self.deleteButton = self.findChild(QtWidgets.QPushButton, "deleteButton")
        self.EditButton = self.findChild(QtWidgets.QPushButton, "EditButton")
        self.openFileButton = self.findChild(QtWidgets.QPushButton, "openFileButton")
        self.ResetButton = self.findChild(QtWidgets.QPushButton, "ResetButton")
        self.mdiArea = self.findChild(QtWidgets.QMdiArea, "mdiArea")
   
        self.insertButton.clicked.connect(self.insertFile)
        self.updateButton.clicked.connect(self.updateDataView)
        self.EditButton.clicked.connect(self.editData)
<<<<<<< Updated upstream
        # self.EditButton.setIcon(QtGui.QIcon('383148_edit_icon(1).png'))
        # self.EditButton.setIconSize(QtCore.QSize(20,20 ))

=======
        self.EditButton.setIcon(QtGui.QIcon('383148_edit_icon(1).png'))
        self.EditButton.setIconSize(QtCore.QSize(20,20 ))
>>>>>>> Stashed changes
        self.deleteButton.clicked.connect(self.deleteRecord)
        # self.deleteButton.setIcon(QtGui.QIcon('3669361_delete_ic_icon.png'))
        # self.deleteButton.setIconSize(QtCore.QSize(20,20 ))

        self.openFileButton.clicked.connect(self.openFile)
        #self.openFileButton.setIcon(QtGui.QIcon('5925643_file_folder_open_icon.png'))
        # self.openFileButton.setIconSize(QtCore.QSize(20,20 ))
        self.ResetButton.clicked.connect(self.reset)
        self.databaseButton.clicked.connect(self.insertDatabase)
<<<<<<< Updated upstream
        self.closeButton.clicked.connect(self.closeGUI)
        # self.closeButton.setIcon(QtGui.QIcon('4781839_cancel_circle_close_delete_discard_icon.png'))
        # self.closeButton.setIconSize(QtCore.QSize(20,20 ))
        self.saveButton.clicked.connect(self.saveToDatabase)
  
        #set icon color
        # self.closeButton.setStyleSheet("background-color:#f0f0f0;"  "color: Black;")
        # self.updateButton.setStyleSheet("background-color:#f0f0f0;" )
        # self.databaseButton.setStyleSheet("background-color:#f0f0f0;" )
        # self.openFileButton.setStyleSheet("background-color:#f0f0f0;" )
        # self.ResetButton.setStyleSheet("background-color:#f0f0f0;" )
        # self.deleteButton.setStyleSheet("background-color:#f0f0f0;" )
        # self.insertButton.setStyleSheet("background-color:#f0f0f0;" )
        # self.EditButton.setStyleSheet("background-color:#f0f0f0;"   )

        self.datasetTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.colTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.commentTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.urlTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.EnergyComboList.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.EnergycomboBox.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.databaseComboBox.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.locationLabel.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.colNameslist.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )

        self.EnergycomboBox.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
=======
        self.closeButton.clicked.connect(self.closeEvent)
        self.closeButton.setIcon(QtGui.QIcon('4781839_cancel_circle_close_delete_discard_icon.png'))
        self.closeButton.setIconSize(QtCore.QSize(20,20 ))
        self.databasecheckBox.stateChanged.connect(self.saveToDatabase)

        self.closeButton.setStyleSheet("background-color:#9BB1BF;" "border-radius: 7px;" "color: Black;")
        self.submitButton.setStyleSheet("background-color:#9BB1BF;" "border-radius: 7px;")
        self.databaseButton.setStyleSheet("background-color:#9BB1BF;" "border-radius: 7px;")
        self.openFileButton.setStyleSheet("background-color:#9BB1BF;" "border-radius: 7px;")
        self.ResetButton.setStyleSheet("background-color:#9BB1BF;" "border-radius: 7px;")
        self.deleteButton.setStyleSheet("background-color:#9BB1BF;" "border-radius: 7px;")
        self.insertButton.setStyleSheet("background-color:#9BB1BF;" "border-radius: 7px;")
        self.EditButton.setStyleSheet("background-color:#9BB1BF;"   "border-radius: 7px;")

        self.datasetTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
        self.colTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
        self.commentTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
        self.urlTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
        self.EnergyComboList.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
        self.EnergycomboBox.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
        self.databaseComboBox.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
        self.locationLabel.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
        self.colNameslist.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
        self.EnergycomboBox.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" "border-radius: 7px;")
>>>>>>> Stashed changes
        self.datasetTextEdit.setPlaceholderText("Enter your Dataset Name")
        self.show()

    def buttonStatusChanged(self):
        if self.DataTableWidget.rowCount() > 0:
            self.deleteButton.setDisabled(False)
            self.openFileButton.setDisabled(False)
            self.EditButton.setDisabled(False)
            self.saveButton.setDisabled(False)
        else:
            self.deleteButton.setDisabled(True)
            self.openFileButton.setDisabled(True)
            self.EditButton.setDisabled(True)
            self.saveButton.setDisabled(True)
            

         
        self.show()
    
    def saveToDatabase(self):
<<<<<<< Updated upstream
        users = pd.read_csv(fname[0], encoding= 'unicode_escape')
        users.to_sql(self.datasetTextEdit.toPlainText(), connection, if_exists='replace', index = False)
        

    def closeGUI(self):
=======
        if self.databasecheckBox.isChecked():
            self.databaseComboBox.setDisabled(False)
            self.databaseButton.setDisabled(False)
        else:
            self.databaseComboBox.setDisabled(False)
            self.databaseButton.setDisabled(False)
        
>>>>>>> Stashed changes

        #addedDataframe = pd.DataFrame(list(addedRows.values()), columns = ['Name of Dataset', 'Energy Type', 'File Type', 'Comments', 'Created Date'])   
        #addedDataframe.to_sql('addedData', connection, if_exists='replace', index = False)
        #message box to close the window and save
        if self.DataTableWidget.rowCount() > 0:
            reply = QtWidgets.QMessageBox.question(self, 'Message', "Do you want to save the data?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)
            if reply == QtWidgets.QMessageBox.Yes:
                self.saveToDatabase()
                self.close()
                
            elif reply == QtWidgets.QMessageBox.No:
                self.close()
                
        else:
                self.close()


    def openFile(self):
        openRow = self.DataTableWidget.currentRow()
        selectedPath = fname[0]
        pyquark.filestart(selectedPath)
        self.buttonStatusChanged()

        # print(selectedPath)
        # os.startfile(selectedPath)

    def deleteRecord(self):
            message = QtWidgets.QMessageBox()
            message.setWindowTitle("Delete")
            message = QtWidgets.QMessageBox.question(self, "Delete", "Are you sure you want to delete?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if message == QtWidgets.QMessageBox.Yes:
                # connection = sqlite3.connect(DataSets[self.DataTableWidget.currentRow()][3])
                # cursor = connection.cursor()
                # tobeDeleted = str(self.DataTableWidget.item(self.DataTableWidget.currentRow(), 0).text())
                # print(tobeDeleted)
                # cursor.execute("DROP TABLE IF EXISTS" + ' '+ tobeDeleted)
                # connection.commit()
                self.DataTableWidget.removeRow(self.DataTableWidget.currentRow())
            self.buttonStatusChanged()

    def insertFile(self):
        self.updateButton.setDisabled(False)
        global fname
        fname = QFileDialog.getOpenFileName(self, "Choose CSV", "","All files(*);;(*.csv);;(*.json);;(*.xlsm);;(*.xlsx)")

        if fname: 
            
            self.locationLabel.setText(fname[0])
            self.datasetTextEdit.setPlainText(Path(fname[0]).stem)
            self.datasetTextEdit.setReadOnly(False)
            self.colTextEdit.setReadOnly(False)
            fileExtension = os.path.splitext(fname[0])[1].replace(".","").upper()
            self.EnergyComboList.setCurrentText(fileExtension) 
            global df
            df = pd.read_csv(fname[0], encoding= 'unicode_escape')
            

            for item in df.columns.values.tolist():
                 self.colNameslist.addItem(item)
            self.colTextEdit.setPlainText(str(self.colNameslist.count()))
            self.buttonStatusChanged()

    def insertDatabase(self):
        dataBasename = QFileDialog.getOpenFileName(self, "Choose Database File", "","(*.db)")
        if os.path.basename(dataBasename[0]) not in addedDatabases:
            addedDatabases.append(os.path.basename(dataBasename[0]))
            self.databaseComboBox.addItem(os.path.basename(dataBasename[0]))
        self.databaseComboBox.setCurrentText(os.path.basename(dataBasename[0]))
        self.buttonStatusChanged()
        
        
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
        self.buttonStatusChanged()
    
        
        
    def updateDataView(self):

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
<<<<<<< Updated upstream
            
                              
=======
            users = pd.read_csv(fname[0], encoding= 'unicode_escape')
            
            if self.databasecheckBox.isChecked():
                users.to_sql(self.datasetTextEdit.toPlainText(), connection, if_exists='replace', index = False)
>>>>>>> Stashed changes
            self.loaddata()
            self.locationLabel.clear()
            self.datasetTextEdit.clear()
            self.urlTextEdit.clear()
            self.commentTextEdit.clear()
            self.colNameslist.clear()
            self.colTextEdit.clear()
        self.buttonStatusChanged()
        
    def editData(self):
        self.datasetTextEdit.setText(self.DataTableWidget.item(self.DataTableWidget.currentRow(), 0).text())
        self.urlTextEdit.setText(DataSets[self.DataTableWidget.currentRow()][1])
        self.locationLabel.setText(DataSets[self.DataTableWidget.currentRow()][0])
        self.commentTextEdit.setText(self.DataTableWidget.item(self.DataTableWidget.currentRow(), 3).text())
        self.colNameslist.insertItems(0, DataSets[self.DataTableWidget.currentRow()][2])
        # connection = sqlite3.connect(DataSets[self.DataTableWidget.currentRow()][3])
        # cursor = connection.cursor()
        # tobeDeleted = str(self.DataTableWidget.item(self.DataTableWidget.currentRow(), 0).text())
        # print(tobeDeleted)
        # cursor.execute("DROP TABLE IF EXISTS" + ' '+ tobeDeleted)
        # connection.commit()
        # self.colTextEdit.setPlainText(str(len(DataSets[self.DataTableWidget.currentRow()][2])))
        self.colTextEdit.setPlainText(addedRows[self.DataTableWidget.currentRow()][8])
        
        self.EnergycomboBox.setCurrentText(DataSets[self.DataTableWidget.currentRow()][4])
        self.EnergyComboList.setCurrentText(DataSets[self.DataTableWidget.currentRow()][5])
        self.databaseComboBox.setCurrentText(DataSets[self.DataTableWidget.currentRow()][3])
        self.DataTableWidget.removeRow(self.DataTableWidget.currentRow())
        self.buttonStatusChanged()


    def loaddata(self):
        
        Data = [{"Name of Dataset": self.datasetTextEdit.toPlainText(),
                "Energy Type": self.EnergycomboBox.currentText(),
                    "File Type": self.EnergyComboList.currentText(), 
                    "Comments": self.commentTextEdit.toPlainText(),
                    "Location": self.locationLabel.text(),
                    "URL": self.urlTextEdit.toPlainText(),
                    "Created Date": now.strftime("%Y-%m-%d %H:%M:%S"),
                    "Database": self.databaseComboBox.currentText(),
                    "NoColumns": self.colTextEdit.toPlainText(),
                    "ColumnNames": df.columns.values.tolist()
                    
                    }]
        
        row = self.DataTableWidget.rowCount()       
        self.DataTableWidget.setRowCount(row + 1 ) 
        
        for data in Data:
            self.DataTableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data["Name of Dataset"]))
            self.DataTableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data["Energy Type"]))
            self.DataTableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data["File Type"]))
            self.DataTableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data["Comments"]))
            self.DataTableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data["Created Date"]))
            #addedRows[row] =[data["Name of Dataset"],data["Energy Type"],data["File Type"],data["Comments"],data["Created Date"]]
            #generate a random ID for each row


            #generate a random ID for each row
            randomID = random.randint(1000000000, 9999999999)

            rowID = str(randomID)+ ''.join(random.choices(data["Name of Dataset"] + data["Energy Type"] + data["File Type"], k=5)))
            addedRows[row] = [
                        data["Name of Dataset"],data["Energy Type"],data["File Type"],
                        data["Comments"],data["Created Date"],data["Location"],
                        data["URL"],data["Database"],data["NoColumns"],data["ColumnNames"]
                        ]

            DataSets[row] = [data["Location"], data["URL"], data["ColumnNames"], data['Database'], data["Energy Type"], data["File Type"]]
            Data.clear()
        self.buttonStatusChanged()

app = QtWidgets.QApplication(sys.argv)
UIWindow = UI()
app.exec_()
