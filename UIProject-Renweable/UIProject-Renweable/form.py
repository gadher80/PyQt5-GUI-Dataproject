from cgitb import html
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Set the main window and title
        self.setWindowTitle("Hello World")

        # Set the layout 
        formLayout = qtw. QFormLayout()
        self.setLayout(formLayout)

        label01 = qtw.QLabel("Hello World, What is your name?")
        label01.setFont(qtg.QFont("Helvetica", 18))
        Email = qtw.QLineEdit(self)
        Name = qtw.QLineEdit(self)

        formLayout.addRow(label01)
        formLayout.addRow("Email", Email)
        formLayout.addRow("Name", Name)
        formLayout.addRow(qtw.QPushButton("Submit", clicked = lambda: pressIt()))

        # Show the app
        self.show() 

        def pressIt():
            label01.setText(f"Hi {Name.text()}")
            print("You clicked the button")

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()