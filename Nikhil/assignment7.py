from tkinter import *
from tkinter import filedialog
import pandas as pd
import pyodbc  


data = pd.read_csv (r'C:\Users\Nikhil\Desktop\ags_intern\dataset.csv')
studio = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-9T4GEVI;''Database=patil;''Trusted_Connection=yes;')

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV","*.csv*"), ("all files",    "*.*")))
   
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
            cursor.execute('INSERT INTO Table_01(ID,Name, TotalAmount, discount)VALUES (?,?,?,?)', row.ID,row.Name, row.TotalAmount, int(row.TotalAmount) * 2 / 100)

        elif var[0] == '5':
            amount = int(row.TotalAmount) - (int(row.TotalAmount) * 3 / 100)      
            cursor.execute('INSERT INTO Table_02(ID,Name, TotalAmount, discount)VALUES (?,?,?,?)', row.ID,row.Name, row.TotalAmount , int(row.TotalAmount) * 3 / 100)

        elif var[0] == '6':
            amount = int(row.TotalAmount) - (int(row.TotalAmount) * 4 / 100)
            cursor.execute('INSERT INTO Table_03(ID,Name, TotalAmount, discount)VALUES (?,?,?,?)', row.ID,row.Name ,row.TotalAmount, int(row.TotalAmount) * 4 / 100)
        else:
            print("pass")
        cursor.commit()
    cursor.close()

def displaytable(table):
    pass
    
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('Data INFO')
  
# Set window size
window.geometry("500x500")
  

# Create a File Explorer label
label_file_explorer = Label(window,text = "Information",width = 100, height = 4)
  
      
button_explore = Button(window,text = "Browse CSV and Process",command = browseFiles)
  
button_exit = Button(window, text = "Exit",command = exit)

button_Table_01 = Button(window, text = " Table_01",command = displaytable('Table_01'))
button_Table_02 = Button(window, text = " Table_02",command = displaytable('Table_02'))
button_Table_03 = Button(window, text = " Table_03",command = displaytable('Table_03'))

label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 4)
button_Table_01.grid(column = 0, row = 3)
button_Table_02.grid(column = 1, row = 3)
button_Table_03.grid(column = 2, row = 3)
  
# Let the window wait for any events
window.mainloop()