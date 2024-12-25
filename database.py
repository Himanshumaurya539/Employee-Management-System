#Connecting python code with Mysql database we need external module from terminal 
#i.e pip install pymysql

import pymysql
from tkinter import messagebox

#defining a  function to connect database with python GUI
def connect_database():
    global mycursor , conn #making variable global to use in another function
    try:
        conn=pymysql.connect(host='localhost',user='root',password='root')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error','Something went wrong,Please open mysql before running')
        return
    
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(20),Name VARCHAR(50),Phone VARCHAR(15),Role VARCHAR(20),Gender VARCHAR(20),Salary DECIMAL(10,2))')




def insert (id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    # %s means place holder
    #to insert data we need to commit changes we will be using conn variable
    conn.commit() 
    

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result = mycursor.fetchone()
    print(result)
    #This output of this will 
    return result[0]> 0  #returnig 0 index value 



def fetch_employees():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result

connect_database()

