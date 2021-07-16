from tkinter import *
import tkinter as tk

import pandas as pd
import pyodbc  
from tkinter import filedialog

studio = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-9T4GEVI;''Database=patil;''Trusted_Connection=yes;')
filename = ""
def csv_file():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("CSV","*.csv*"),
                                                       ("all files",
                                                        "*.*")))
r = tk.Tk()

r.title('Counting Seconds')
button = tk.Button(r, text='select csv file', width=25, command=csv_file)
button.pack()                                         

def process_data():
    cursor = studio.cursor()
    data = pd.read_csv (filename)
    for row in data.itertuples():
        var = str(row.ID)
        if var[0] == '4':
            discount = int(row.TotalAmount) - (int(row.TotalAmount) * 2 / 100)
            cursor.execute('INSERT INTO Table_01(ID, Name, TotalAmount, discount)VALUES (?,?,?,?)',row.ID, row.Name, row.TotalAmount, int(row.TotalAmount) * 2 / 100)
            print(discount)
        elif var[0] == '5':
            TotalAmount = int(row.TotalAmount) - (int(row.TotalAmount) * 3 / 100)
            cursor.execute('INSERT INTO Table_02(ID, Name, TotalAmount, discount)VALUES (?,?,?,?)',row.ID, row.Name, row.TotalAmount, int(row.TotalAmount) * 3 / 100)
        
        elif var[0] == '6': 
            TotalAmount = int(row.TotalAmount) - (int(row.TotalAmount) * 4 / 100)  
            cursor.execute('INSERT INTO Table_03(ID, Name, TotalAmount, discount)VALUES (?,?,?,?)',row.ID, row.Name, row.TotalAmount, int(row.TotalAmount) * 4 / 100)

        else:
            print("pass")
    cursor.close()
button = tk.Button(r, text='process data', width=25, command=process_data)
button.pack()     

button = tk.Button(r, text='exit', width=25, command=r.destroy)
button.pack()

r.mainloop()