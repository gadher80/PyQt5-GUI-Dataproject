from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import pandas as pd


top = Tk()
top.geometry("900x900")

my_font1=('times', 12, 'bold')

l1 = Label(top,text='Read File & create DataFrame', width=30,font=my_font1).place(x= 10,y= 30)

DatasetName = Label(top,text= "Dataset Name").place(x= 40,y= 80)
fileType= Entry(top,width = 30).place(x = 150, y = 80)
										
t1=Text(top,width=40,height=5).place(x= 250,y= 360)

DatasetName = Label(top,text= "File").place(x= 40,y= 120)										
b1 = Button(top, text='Browse File', width=10,command = lambda:upload_file()).place(x = 370, y = 120)
fileType= Entry(top,width = 30).place(x = 150, y = 120)

def upload_file():

    f_types = [('CSV files',"*.csv"),('All',"*.*")]

    file = filedialog.askopenfilename(filetypes=f_types)

    l1.config(text=file)  
    df=pd.read_csv(file)
    str1="Rows:" + str(df.shape[0])+ "\nColumns:"+str(df.shape[1])

    #print(str1)
    t1.insert(Tk.END, str1)


def show(): 
    label.config( text = clicked.get()) 

options = [ 
    "Solar", 
    "Thermal", 
    "Hydro"
] 

clicked = StringVar() 
  
clicked.set( "Solar" ) 
  
drop = OptionMenu( top , clicked , *options ).place(x = 370, y = 75) 
  
button = Button( top , text = "Submit" , command = show ).place(x = 40, y = 190)
  
label = Label( top , text = " " ).place(x = 40, y = 210) 
 

top.mainloop()
