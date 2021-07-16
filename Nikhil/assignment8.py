from tkinter import *
from tkinter import filedialog
import pandas as pd
import pyodbc
import os

studio = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-9T4GEVI;''Database=patil;''Trusted_Connection=yes;')


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV","*.csv*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    processtable(filename)
      

def processtable(filename):          
    data = pd.read_csv(filename)
    cursor = studio.cursor()
    for row in data.itertuples():
        var = str(row.ID)
        if var[0] == '4':
            amount = int(row.TotalAmount) - (int(row.TotalAmount) * 2 / 100)
            cursor.execute('INSERT INTO Table_01(NAME, ID, TotalAmount, discount)VALUES (?,?,?,?)',row.NAME, row.ID, amount, int(row.TotalAmount) * 2 / 100)

        elif var[0] == '5':
            amount = int(row.TotalAmount) - (int(row.TotalAmount) * 3 / 100)      
            cursor.execute('INSERT INTO Table_02(NAME, ID, TotalAmount, discount)VALUES (?,?,?,?)',row.NAME, row.ID, amount , int(row.TotalAmount) * 3 / 100)

        elif var[0] == '6':
            amount = int(row.TotalAmount) - (int(row.TotalAmount) * 4 / 100)
            cursor.execute('INSERT INTO Table_03(NAME, ID, TotalAmount, discount)VALUES (?,?,?,?)',row.NAME, row.ID, amount, int(row.TotalAmount) * 4 / 100)
        else:
            print("pass")
        cursor.commit()
    cursor.close()
    createcsv('Table_01')
    createcsv('Table_02')
    createcsv('Table_03')

def createcsv(table):
    cwd = os.getcwd()
    data = pd.read_sql("SELECT * FROM "+table, studio)
    data.to_csv(cwd+ "\\" + table + ".csv" , index = False, header=True)

                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,text = "Information",width = 100, height = 4)
  
      
button_explore = Button(window,text = "Browse CSV and Process",command = browseFiles)
  
button_exit = Button(window, text = "#Exit",command = exit)

label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 4)

# Let the window wait for any events
window.mainloop()