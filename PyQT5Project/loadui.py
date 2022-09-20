from argparse import FileType
from calendar import EPOCH
from email import message
from multiprocessing import connection
from smtplib import quotedata
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox,QHBoxLayout, QWidget, QFrame
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



class UI(QtWidgets.QDialog):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("DataMiner.ui", self)

        #get data from sqlite3
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM data")    
        rows = cursor.fetchall()
        connection.close()
        #add data to table
        for row in rows:
            self.DataTableWidget.insertRow(self.DataTableWidget.rowCount())
            self.DataTableWidget.setItem(self.DataTableWidget.rowCount()-1, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.DataTableWidget.setItem(self.DataTableWidget.rowCount()-1, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.DataTableWidget.setItem(self.DataTableWidget.rowCount()-1, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.DataTableWidget.setItem(self.DataTableWidget.rowCount()-1, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.DataTableWidget.setItem(self.DataTableWidget.rowCount()-1, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.DataTableWidget.setItem(self.DataTableWidget.rowCount()-1, 5, QtWidgets.QTableWidgetItem(row[5]))
        self.DataTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)    
        # cursor.execute("SELECT  FROM sqlite_master WHERE type='table';")

        # # if os.path.exists('DataSets.xlsx'):
        # #     df2 = pd.read_excel('DataSets.xlsx')
        # #     #df with condition
        # #     cond = (df2['saved'] ==  True)
        # #     savedDf = df2.loc[cond]

        # #     for index in savedDf.index:
        # #         self.DataTableWidget.insertRow(index)
        # #         self.DataTableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(df2['Name of Dataset'][index])))
        # #         self.DataTableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(str(df2['Energy Type'][index])))
        # #         self.DataTableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(str(df2['File Type'][index])))
        # #         self.DataTableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(str(df2['Comments'][index])))
        # #         self.DataTableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(str(df2['Created Date'][index])))


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
        self.searchFileButton = self.findChild(QtWidgets.QPushButton, "searchFileButton")
        self.searchbar = self.findChild(QtWidgets.QLineEdit, "searchbar")
        self.searchbar.setPlaceholderText("Search using Dataset Name")

        
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
        self.saveButton.clicked.connect(self.saveToDatabase)
        #self.searchFileButton.clicked.connect(self.findName)
  
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
        self.show()

        global clickedInsertButton 
        global clickedSaveButton
        
        clickedSaveButton = False
        clickedInsertButton = False
        
        #set model to QtableWidget
  




        self.searchbar.textChanged.connect(self.findName)
        self.searchbar.setPlaceholderText("Search using Dataset Name")
        self.searchbar.setStyleSheet("border: 1px solid ;" "background-color: #FFFFFF;" )



    def findName(self, text):


        self.table.setCurrentItem(None)

        if not text:
            # Empty string, don't search.
            return

        if matching_items := self.DataTableWidget.findItems(s, Qt.MatchContains):
            # We have found something.
            item = matching_items[0]  # Take the first.
            self.table.setCurrentItem(item)
            text = self.searchbar.text()
            

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
    
    def saveToDatabase(self):
        self.updateDataView()

        for saveRow in range(self.DataTableWidget.rowCount()):

            
            nameOfDatabase = self.DataTableWidget.item(saveRow,0 ).text()
            Energy = self.DataTableWidget.item(saveRow,1 ).text()
            FileType = self.DataTableWidget.item(saveRow,2 ).text()
            comments = self.DataTableWidget.item(saveRow,3 ).text()
            Time = self.DataTableWidget.item(saveRow, 4).text()
            path = self.DataTableWidget.item(saveRow, 5).text()
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            #create table
            cursor.execute("CREATE TABLE IF NOT EXISTS data (nameOfDatabase TEXT, Energy TEXT, FileType TEXT, comments TEXT, Time TEXT, path TEXT)")

            #compare time if exist
            if cursor.execute("SELECT Time FROM data WHERE Time = ?", (Time,)).fetchone() is None:
                cursor.execute("INSERT INTO data VALUES(?,?,?,?,?,?)", (nameOfDatabase, Energy, FileType, comments, Time, path))
                connection.commit()
                connection.close()
            else:
                print("Time already exists")
                connection.close()
                continue

            # cursor.execute("SELECT Time FROM data WHERE Time = ?", (Time,))
            
            # cursor.execute("INSERT INTO data VALUES (?,?,?,?,?,?)", (nameOfDatabase, Energy, FileType, comments, Time, path))
            # connection.commit()
            # connection.close()

            #df2 = pd.read_excel('DataSets.xlsx')
            # condForDb = (df2['Created Date'] == Time)
            # databasedf = df2.loc[condForDb]
            # path = databasedf.iloc[saveRow]['Location']
   
            # df2.at[saveRow, 'saved'] = True
            # df2.to_excel('DataSets.xlsx')
            
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            users = pd.read_csv(path, encoding= 'unicode_escape')
            users.to_sql(nameOfDatabase, connection, if_exists='replace', index=False)


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
                    # connection = sqlite3.connect(DataSets[self.DataTableWidget.currentRow()][3])
                    # cursor = connection.cursor()
                    # tobeDeleted = str(self.DataTableWidget.item(self.DataTableWidget.currentRow(), 0).text())
                    # print(tobeDeleted)
                    # cursor.execute("DROP TABLE IF EXISTS" + ' '+ tobeDeleted)
                    # connection.commit()
                    nameOfDatabase = self.DataTableWidget.item(
                        selectedRow, 0).text()
                    connection = sqlite3.connect('data.db')
                    cursor = connection.cursor()
                    cursor.execute("DROP TABLE IF EXISTS" +
                                   ' ' + nameOfDatabase)
                    #delete row from database
                    cursor.execute(
                        "DELETE FROM data WHERE nameOfDatabase = ?", (nameOfDatabase,))
                    connection.commit()
                    connection.close()

                    self.DataTableWidget.removeRow(selectedRow)

            self.buttonStatusChanged()

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
        #write if one of both buttons are clicked


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

        #check if given URL is existing
        #url validation
        global now
        now = time.time()

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
        
    def editData(self):

        selectedRow = self.DataTableWidget.currentRow()
            
        message = QtWidgets.QMessageBox()
        message.setWindowTitle("Warnig")
        message = QtWidgets.QMessageBox.question(
                self, "Edit", "Are you sure you want to edit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if message == QtWidgets.QMessageBox.Yes:
            self.locationLabel.setText(self.DataTableWidget.item(selectedRow, 1).text())
            self.datasetTextEdit.setPlainText(self.DataTableWidget.item(selectedRow, 0).text())
            self.urlTextEdit.setPlainText(self.DataTableWidget.item(selectedRow, 2).text())
            self.commentTextEdit.setPlainText(self.DataTableWidget.item(selectedRow, 3).text())
            self.colNameslist.clear()
            self.colTextEdit.clear()
            self.colNameslist.addItems(self.DataTableWidget.item(selectedRow, 4).text().split(","))
            self.colTextEdit.setPlainText(str(self.colNameslist.count()))
            self.EnergyComboList.setCurrentText(self.DataTableWidget.item(selectedRow, 5).text())
            self.DataTableWidget.removeRow(selectedRow)
            self.buttonStatusChanged()
        
            nameOfDatabase = self.DataTableWidget.item(selectedRow, 0).text()
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS" +' ' + nameOfDatabase)
                    #delete row from database
            cursor.execute("DELETE FROM data WHERE nameOfDatabase = ?", (nameOfDatabase,))
            connection.commit()
            connection.close()

            self.DataTableWidget.removeRow(selectedRow)

        self.buttonStatusChanged()
            
        
        # selectedRow = self.DataTableWidget.currentRow()

        # Time = self.DataTableWidget.item(selectedRow, 4).text()
        # df2 = pd.read_excel('DataSets.xlsx')
        # condForDb = (df2['Created Date'] == Time)
        # databasedf = df2.loc[condForDb]
        # #saveTothisDatabase = databasedf.iloc[selectedRow]['Database']
        # path = databasedf.iloc[selectedRow]['Location']
        # datasettext = databasedf.iloc[selectedRow]['Name of Dataset']
        # urltext = databasedf.iloc[selectedRow]['URL']
        # commenttext = databasedf.iloc[selectedRow]['Comments']
        # coltext = databasedf.iloc[selectedRow]['NoColumns']
        # energytext = databasedf.iloc[selectedRow]['Energy Type']
        # fileType = databasedf.iloc[selectedRow]['File Type']

        # # self.databaseComboBox.addItem(saveTothisDatabase)
        # # self.databaseComboBox.setCurrentText(saveTothisDatabase)
        # self.datasetTextEdit.setText(datasettext)
        # self.urlTextEdit.setText(urltext)
        # self.locationLabel.setText(path)
        # self.commentTextEdit.setText(commenttext)   
        # self.colTextEdit.setPlainText(str(coltext.item()))
        # self.EnergycomboBox.setCurrentText(energytext)
        # self.EnergyComboList.setCurrentText(fileType)
        # #self.databaseComboBox.setCurrentText(saveTothisDatabase)
        # editedDf = pd.read_csv(path, encoding= 'unicode_escape')
        # self.colNameslist.insertItems(0,editedDf.columns.values.tolist())
        # self.DataTableWidget.removeRow(self.DataTableWidget.currentRow())
        # self.buttonStatusChanged()


    def loaddata(self):
        epochTimes[now] = datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
        global Data
        Data = [{"Name of Dataset": self.datasetTextEdit.toPlainText(),
                "Energy Type": self.EnergycomboBox.currentText(),
                    "File Type": self.EnergyComboList.currentText(), 
                    "Comments": self.commentTextEdit.toPlainText(),
                    "Path": self.locationLabel.text(),
                    "URL": self.urlTextEdit.toPlainText(),
                    "Time": datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S'),
                    "Database": 'data.db',
                    "NoColumns": self.colTextEdit.toPlainText(),
                    "saved": False,
                    }]

        # rowTobeAdded = [list(Data[0].values())]

        # if os.path.exists('DataSets.xlsx'):
        #     df2 = pd.read_excel('DataSets.xlsx')
        #     df2 = df2.append(pd.DataFrame(rowTobeAdded, columns=list(Data[0].keys())), ignore_index=True)
        # else:
        #     df2 = pd.DataFrame(rowTobeAdded, columns=list(Data[0].keys()))
        # df2.to_excel('DataSets.xlsx', index=False)


        row = self.DataTableWidget.rowCount()
        self.DataTableWidget.setRowCount(row + 1 )      

        for data in Data:

            self.DataTableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data["Name of Dataset"]))
            self.DataTableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data["Energy Type"]))
            self.DataTableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data["File Type"]))
            self.DataTableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data["Comments"]))
            self.DataTableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data["Time"]))
            self.DataTableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(data["Path"]))  
 
            Data.clear()
        self.buttonStatusChanged()

app = QtWidgets.QApplication(sys.argv)
UIWindow = UI()
app.exec_()
