import pandas as pd
import pyodbc
import os

def process_table(dataset):
    conn = pyodbc.connect('Driver={SQL Server};''Server=localhost;''Database=agsdb;''UID = SA;''PWD = Bose2515;''Trusted_Connection=yes;')+';UID='+username+';PWD='+ password) 
    data1 = pd.read_csv(dataset,delimiter='|')
    cursor = conn.cursor()
    for row in data1.itertuples():
        cursor.execute("INSERT into tabledata values(?,?,?,?)",row.NAME,row.ID,row.Total_Amount)
        cursor.commit()
    cursor.close()
    conn.close()

def display_table(table):
    conn = pyodbc.connect('Driver={SQL Server};''Server=localhost;''Database=agsdb;''UID = SA;''PWD = Bose2515;''Trusted_Connection=yes;')+';UID='+username+';PWD='+ password) 
    cursor1 = conn.cursor()
    cursor1.execute("select * from "+table)
    cursor1.close()
    conn.close()
    return cursor1