import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Set the main window and title
        self.setWindowTitle("Hello World")

        # Set the layout    
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        myLabel = qtw.QLabel("Hello World, What is your name?")

        # Change the font size of the label
        myLabel.setFont(qtg.QFont("Helvetica", 18)) 

        # Add the label to the main window
        self.layout().addWidget(myLabel)

        myCombo = qtw.QComboBox(self, editable = True, insertPolicy = qtw.QComboBox.InsertAtTop)
        myCombo.addItems(["Solar", "Thermal", "Water", "Wind"])
        self.layout().addWidget(myCombo)
 
     

        # Create a button
        myButton = qtw.QPushButton("Click Me!", clicked = lambda: pressIt())
        self.layout().addWidget(myButton)

        # Show the app
        self.show() 

        def pressIt():
            myLabel.setText(f"Hi , it is {myCombo.currentText()}")
        
            print("You clicked the button")

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()