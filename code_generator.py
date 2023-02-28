import mysql.connector
import tkinter

from tkinter import ttk
from tkinter import *

con=mysql.connector.connect(user='root',host='localhost',password='piyush123',database='dict')
cur=con.cursor(buffered=True)
try:
    cur.execute("describe persons")
except:
    cur.execute("create table persons( id int primary key auto_increment, name varchar(255), ans varchar(220))")


win=tkinter.Tk()
win.geometry('700x500')
win.title('Dictionary')
l1=tkinter.Label(win,text="word")
l1.grid(row=1,column=1)
l2=tkinter.Label(win,text="meaning")
l2.grid(row=2,column=1)
l3=tkinter.Label(win,text="Search Area",font="bold")
l3.grid(row=4,column=3)
l4=tkinter.Label(win,text="WORD")
l4.grid(row=5,column=1)
l5=tkinter.Label(win,text="MEANING")
l5.grid(row=7,column=1)
e1=tkinter.Entry(win)
e1.grid(row=1,column=2)
e2=tkinter.Entry(win)
e2.grid(row=2,column=2)
e3=tkinter.Entry(win)
e3.grid(row=5,column=2)
e4=tkinter.Entry(win)
e4.grid(row=7,column=2)
def registration():
    
    keys=e1.get()
    valuess=e2.get()
    cur.execute("insert into persons(name,ans) values('"+keys+"','"+valuess+"')")
    print("Record inserted")
    con.commit()
def done():
    global myresult
    word=e3.get()
    meaning=e4.get()
    con=mysql.connector.connect(user='root',host='localhost',password='piyush123',database='dict')
    cur=con.cursor(buffered=True)

    try:
        cur.execute("select * from persons where name='"+word+"'")
        myresult=cur.fetchall()
        for x in myresult:
            print(x)
        e4.delete(0, END)
        e4.insert(END ,x[2])

    except Exception as e:
        print(e)
        con.rollback()
        con.close()

b=tkinter.Button(win,text="Submit", command=registration)
b.grid(row=3,column=1)
b1=tkinter.Button(win,text="Search", command =done)
b1.grid(row=6,column=1)


win.mainloop()
