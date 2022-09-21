from argparse import FileType
from calendar import EPOCH
from email import message
from multiprocessing import connection
from smtplib import quotedata
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import pandas as pd
import os,sys, subprocess
from pathlib import Path
from os.path import exists
import validators
from validators import ValidationFailure
import requests
import csv, sqlite3
import pyquark
from datetime import datetime
import random
import string
import uuid 
import time
from openpyxl import Workbook, load_workbook
from xlsxwriter import Workbook
#add libraries

urlData = {}
addedDatabases = []
addedRows ={}
epochTimes = {}

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


class UI(QtWidgets.QDialog):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("DataMiner.ui", self)

        self.displayData()

        self.DataTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)    

        self.datasetTextEdit = self.findChild(QtWidgets.QTextEdit,"datasetTextEdit")
        self.colNameslist = self.findChild(QtWidgets.QListWidget,"colNameslist")
        self.commentLabel = self.findChild(QtWidgets.QLabel,"commentLabel")
        self.locationLabel = self.findChild(QtWidgets.QLabel,"locationLabel")
        self.urlTextEdit = self.findChild(QtWidgets.QTextEdit,"urlTextEdit")
        self.searchbar = self.findChild(QtWidgets.QLineEdit,"searchbar")
        #self.datasetLabel = self.findChild(QtWidgets.QLabel,"datasetLabel")

        self.EnergyComboList = self.findChild(QtWidgets.QComboBox, "EnergyComboList")
        self.colTextEdit = self.findChild(QtWidgets.QTextEdit, "colTextEdit")
        self.EnergycomboBox = self.findChild(QtWidgets.QComboBox, "EnergycomboBox")
        self.DataTableWidget = self.findChild(QtWidgets.QTableWidget, "DataTableWidget")
        #self.updateButton = self.findChild(QtWidgets.QPushButton, "updateButton")
        self.commentTextEdit = self.findChild(QtWidgets.QTextEdit, "commentTextEdit")
        self.closeButton = self.findChild(QtWidgets.QPushButton, "closeButton")
        #self.databaseButton = self.findChild(QtWidgets.QPushButton, "databaseButton")
        #self.databaseComboBox = self.findChild(QtWidgets.QComboBox, "databaseComboBox")
        self.saveButton = self.findChild(QtWidgets.QPushButton, "saveButton")
        self.commentTextEdit.setPlaceholderText("Enter your Comments")
        self.urlTextEdit.setPlaceholderText("Enter URL")
        self.insertButton = self.findChild(QtWidgets.QPushButton, "insertButton")
        self.deleteButton = self.findChild(QtWidgets.QPushButton, "deleteButton")
        self.EditButton = self.findChild(QtWidgets.QPushButton, "EditButton")
        self.openFileButton = self.findChild(QtWidgets.QPushButton, "openFileButton")
        self.ResetButton = self.findChild(QtWidgets.QPushButton, "ResetButton")
        self.mdiArea = self.findChild(QtWidgets.QMdiArea, "mdiArea")
        #self.searchFileButton = self.findChild(QtWidgets.QPushButton, "searchFileButton")
        self.searchbar = self.findChild(QtWidgets.QLineEdit, "searchbar")
        self.searchbar.setPlaceholderText("   "+"Search using Dataset Name or Energy Type or File Type")
        #self.searchbar.textChanged.connect(self.autocompletion)







        self.SearchToolButton = self.findChild(QtWidgets.QToolButton, "SearchToolButton")
        self.BacktoolButton = self.findChild(QtWidgets.QToolButton, "BacktoolButton")
        


        self.insertButton.clicked.connect(self.insertFile)
        #self.updateButton.clicked.connect(self.updateDataView)
        self.EditButton.clicked.connect(self.editData)
        # self.EditButton.setIcon(QtGui.QIcon('383148_edit_icon(1).png'))
        # self.EditButton.setIconSize(QtCore.QSize(20,20 ))

        self.deleteButton.clicked.connect(self.deleteRecord)
        #shortcut for delete button
        self.deleteButton.setShortcut("Delete")

        # self.deleteButton.setIcon(QtGui.QIcon('3669361_delete_ic_icon.png'))
        # self.deleteButton.setIconSize(QtCore.QSize(20,20 ))

        self.openFileButton.clicked.connect(self.openFile)
        #self.openFileButton.setIcon(QtGui.QIcon('5925643_file_folder_open_icon.png'))
        # self.openFileButton.setIconSize(QtCore.QSize(20,20 ))
        self.ResetButton.clicked.connect(self.reset)
        #self.databaseButton.clicked.connect(self.insertDatabase)
        self.closeButton.clicked.connect(self.closeGUI)
        # self.closeButton.setIcon(QtGui.QIcon('4781839_cancel_circle_close_delete_discard_icon.png'))
        # self.closeButton.setIconSize(QtCore.QSize(20,20 ))
        self.saveButton.clicked.connect(self.updateDataView)
        #connect tool button to search function
        #set icon for search button
        self.SearchToolButton.setIcon(QtGui.QIcon('magnifying-glass.png'))
        self.SearchToolButton.setIconSize(QtCore.QSize(20,20 ))
        self.SearchToolButton.clicked.connect(self.findName)
        self.SearchToolButton.setShortcut("Enter")
        self.DataTableWidget.doubleClicked.connect(self.openFile)


        #set icon for back button
        # self.BacktoolButton.setIcon(QtGui.QIcon('left-arrow.png'))
        # self.BacktoolButton.setIconSize(QtCore.QSize(20,20 ))
        self.BacktoolButton.clicked.connect(self.back)

        self.datasetTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.colTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.commentTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.urlTextEdit.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.EnergyComboList.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.EnergycomboBox.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        #self.databaseComboBox.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.locationLabel.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.colNameslist.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )

        self.EnergycomboBox.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )
        self.datasetTextEdit.setPlaceholderText("Enter your Dataset Name")
        self.autocompletion()

        self.show()

        global clickedInsertButton
        global clickedSaveButton
        global clickedSearchToolButton
        global clickedBacktoolButton

        clickedInsertButton = False
        clickedSaveButton = False
        clickedSearchToolButton = False
        clickedBacktoolButton = False

        

    def back(self):

        #check if serachToolButton is clicked
        if clickedSearchToolButton == False:
            self.searchbar.setText("")
            for i in reversed(range(self.DataTableWidget.rowCount())):
                    self.DataTableWidget.removeRow(i)
            self.displayData()
        else:
            print('Wrong button')
        
    def findName(self):
        #search matching name in database


        searchName = self.searchbar.text()
        if searchName != "":
            #self.searchbar.setText("")
            query = ("Select *   from TempData where nameOfDatabase Like ? or energyType like ? or fileType like? ")
            results = cursor.execute(query,('%'+searchName+'%','%'+searchName+'%','%'+searchName+'%'))
            results = cursor.fetchall()

            if results == []:
                message = QtWidgets.QMessageBox.information(self, "Information", "No matching record found")
                #
            else:
                clickedSearchToolButton = True
                for i in reversed(range(self.DataTableWidget.rowCount())):
                    self.DataTableWidget.removeRow(i)

                for row_data in results:
                    row_number = self.DataTableWidget.rowCount()
                    self.DataTableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.DataTableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        
            
    def autocompletion(self):
        cursor.execute("SELECT nameOfDatabase, energyType, FileType FROM TempData")
        data = cursor.fetchall()
        completionList = []
        for rowdata in data:
            completionList.extend(iter(rowdata))
            #to remove duplicates
        #print(list(dict.fromkeys(completionList)))
        self.completer = QCompleter(list(dict.fromkeys(completionList)))
        #set completer for any character
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)

            

    def buttonStatusChanged(self):
        if self.DataTableWidget.rowCount() > 0:
            self.deleteButton.setDisabled(False)
            self.openFileButton.setDisabled(False)
            self.EditButton.setDisabled(False)
        else:
            self.deleteButton.setDisabled(True)
            self.openFileButton.setDisabled(True)
            self.EditButton.setDisabled(True)
        self.saveButton.setDisabled(False)
        self.show()

    def displayData(self):

        cursor.execute("SELECT nameOfDatabase, energyType, FileType, comments, CreatedDate, location FROM TempData")      
        data = cursor.fetchall()
        
        
        for row_number, row_data in enumerate(data):
            self.DataTableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.DataTableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    
    def closeGUI(self):


        if self.DataTableWidget.rowCount() > 0:
            if clickedSaveButton == True:
                reply = QtWidgets.QMessageBox.question(self, 'Message', "Do you want to save the data?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)
                if reply == QtWidgets.QMessageBox.Yes:
                    self.saveToDatabase()
                    self.close()                    
                elif reply == QtWidgets.QMessageBox.No:
                    self.close()                    
            else:
                    self.close()


    def openFile(self):
        selectedRow = self.DataTableWidget.currentRow()
        path = self.DataTableWidget.item(selectedRow, 5).text()
        pyquark.filestart(path)
        self.buttonStatusChanged()

        # print(selectedPath)
        # os.startfile(selectedPath)

    def deleteRecord(self):
            selectedRow = self.DataTableWidget.currentRow()
            
            message = QtWidgets.QMessageBox()
            message.setWindowTitle("Delete")
            message = QtWidgets.QMessageBox.question(
                   self, "Delete", "Are you sure you want to delete?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if message == QtWidgets.QMessageBox.Yes:
                    
                    nameOfDatabase = self.DataTableWidget.item(selectedRow, 0).text()
                   
                    cursor.execute("DROP TABLE IF EXISTS" +' ' + nameOfDatabase)
                    #delete row from database
                    cursor.execute("DELETE FROM TempData WHERE nameOfDatabase = ?", (nameOfDatabase,))
                    connection.commit()
                    self.DataTableWidget.removeRow(selectedRow)

            self.buttonStatusChanged()
            self.autocompletion()

    def insertFile(self):  # sourcery skip: use-named-expression
        clickedInsertButton = True
        #self.updateButton.setDisabled(False)
        global fname
        fname = QFileDialog.getOpenFileName(self, "Choose CSV", "","(*.csv);;(*.json);;(*.xlsm);;(*.xlsx)")
        if fname[0] != '':
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
 
            
        else:
            self.locationLabel.setText("No file selected")
            self.datasetTextEdit.setPlainText("")
            self.colTextEdit.setPlainText("")
            self.colNameslist.clear()
            self.buttonStatusChanged()

        self.show()
    
  
    # def insertDatabase(self):
    #     clickeddatabaseButton = True
    #     dataBasename = QFileDialog.getOpenFileName(self, "Choose Database File", "","(*.db)")
    #     if os.path.basename(dataBasename[0]) not in addedDatabases:
    #         addedDatabases.append(os.path.basename(dataBasename[0]))
    #         self.databaseComboBox.addItem(os.path.basename(dataBasename[0]))
    #     self.databaseComboBox.setCurrentText(os.path.basename(dataBasename[0]))
    #     self.buttonStatusChanged()
        
        
    def reset(self):
        
        
        if clickedInsertButton == True:
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
                #self.databaseComboBox.clear()
            self.buttonStatusChanged()
        else:
            message = QtWidgets.QMessageBox()
            message.setWindowTitle("Reset")
            message = QtWidgets.QMessageBox.information(self, "Reset", "No data inseted", QtWidgets.QMessageBox.Ok)
        
        
    def updateDataView(self):

        validationValue =validators.url(self.urlTextEdit.toPlainText())
        if self.datasetTextEdit.toPlainText() == "":             
            message = QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a dataset name")            
        elif validationValue != True:
            message = QtWidgets.QMessageBox.warning(self, "Warning", "Invalid URL") 
        elif self.commentTextEdit.toPlainText() == "":
            message = QtWidgets.QMessageBox.warning(self, "Warning", "Please write a comment")
         
        else:                                     
            self.loaddata()
            self.locationLabel.clear()
            self.datasetTextEdit.clear()
            self.urlTextEdit.clear()
            self.commentTextEdit.clear()
            self.colNameslist.clear()
            self.colTextEdit.clear()
        self.buttonStatusChanged()
        self.autocompletion()
        
    def editData(self):

        selectedRow = self.DataTableWidget.currentRow()            
        message = QtWidgets.QMessageBox()
        message.setWindowTitle("Warning")
        message = QtWidgets.QMessageBox.question(
                self, "Edit", "Are you sure you want to edit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if message == QtWidgets.QMessageBox.Yes:
            
            self.datasetTextEdit.setPlainText(self.DataTableWidget.item(selectedRow, 0).text())
            self.EnergycomboBox.setCurrentText(self.DataTableWidget.item(selectedRow, 1).text())
            self.EnergyComboList.setCurrentText(self.DataTableWidget.item(selectedRow, 2).text())
            self.commentTextEdit.setPlainText(self.DataTableWidget.item(selectedRow, 3).text())
            self.locationLabel.setText(self.DataTableWidget.item(selectedRow, 5).text())

            #grab a url from the database
            cursor.execute("SELECT url FROM TempData WHERE nameOfDatabase = ?", (self.DataTableWidget.item(selectedRow, 0).text(),))
            url = cursor.fetchone()
            self.urlTextEdit.setPlainText(url[0])

            #convert path to dataframe and display column names
            df = pd.read_csv(self.DataTableWidget.item(selectedRow, 5).text(), encoding= 'unicode_escape')
            for item in df.columns.values.tolist():
                self.colNameslist.addItem(item)
            self.colTextEdit.setPlainText(str(self.colNameslist.count()))
            cursor.execute("DROP TABLE IF EXISTS" +' ' + self.DataTableWidget.item(selectedRow, 0).text())
            cursor.execute("DELETE FROM TempData WHERE nameOfDatabase = ?", (self.DataTableWidget.item(selectedRow, 0).text(),))
            connection.commit()
            
            self.DataTableWidget.removeRow(selectedRow)

        self.buttonStatusChanged()
        self.autocompletion()


    def loaddata(self):
        now = time.time()
        Data = {"Name of Dataset": self.datasetTextEdit.toPlainText(),
                "Energy Type": self.EnergycomboBox.currentText(),
                    "File Type": self.EnergyComboList.currentText(), 
                    "Comments": self.commentTextEdit.toPlainText(),
                    "Time": datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S'),
                    "Path": self.locationLabel.text()
                    }
        self.DataTableWidget.insertRow(0)
        for column, value in enumerate(Data.values()):
            self.DataTableWidget.setItem(0, column, QtWidgets.QTableWidgetItem(str(value)))

 
        
        cursor.execute("CREATE TABLE IF NOT EXISTS TempData (nameOfDatabase TEXT, energyType TEXT, fileType TEXT, comments TEXT, location TEXT, url TEXT, createdDate TEXT, noColumns TEXT)")
        cursor.execute("INSERT INTO TempData VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (self.datasetTextEdit.toPlainText(), 
                                                                                self.EnergycomboBox.currentText(), 
                                                                                self.EnergyComboList.currentText(), 
                                                                                self.commentTextEdit.toPlainText(), 
                                                                                self.locationLabel.text(), 
                                                                                self.urlTextEdit.toPlainText(), 
                                                                                datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S'), 
                                                                                self.colTextEdit.toPlainText()))
        connection.commit()

        users = pd.read_csv(self.locationLabel.text(), encoding= 'unicode_escape')
        users.to_sql(self.datasetTextEdit.toPlainText(), connection, if_exists='replace', index=False)

        self.buttonStatusChanged()

app = QtWidgets.QApplication(sys.argv)
UIWindow = UI()
app.exec_()
