import tkinter as tk
from tkinter import *
from tkinter import END
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

my_win = tk.Tk()
my_win.title("My First GUI")
my_win.geometry("750x550")

font1= ('Times', 26, 'bold')
lbl = tk.Label(my_win, text="MySQL Connector", font=font1)
lbl.grid(row=0, column=1, columnspan=8)


#myfunc
def display_data():
        str1= "mysql+mysqlconnector://"+userid.get()+":"\
        +password.get()+"@"+Host.get()+"/"+Database.get()
        print("string is----->", str1)
        t1.delete("1.0", END)
        t1.update()
        my_output=''
        try:
                my_conn = create_engine(str1)
                # records = my_conn.execute("Show tables")
                with my_conn.connect() as conn:
                        records = conn.execute("Show tables")
                        for i in records:
                                my_output+str(i[0]) +"\n"
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                my_output=error
        t1.insert(tk.END, my_output)


        


#button1
pw= tk.StringVar()
b1 = tk.Button(my_win, text='connect', width=10, command=lambda :display_data())
b1.grid(row=1, column=9)
t1=tk.Text(my_win, height=26, width=75)
t1.grid(row=2, column=1, columnspan=8)

#label1
l1=tk.Label(my_win, text='Host')
l1.grid(row=1, column=1, padx=5)
Host = tk.StringVar()
Host.set('localhost')
e1= tk.Entry(my_win, textvariable=Host, width=10)
e1.grid(row=1, column=2)

#label2
l2=tk.Label(my_win, text='Database')
l2.grid(row=1, column=3, padx=5)
Database = tk.StringVar()
Database.set('')
e2= tk.Entry(my_win, textvariable=Database, width=10)
e2.grid(row=1, column=4)

#label3
l3=tk.Label(my_win, text='UserID')
l3.grid(row=1, column=5, padx=5)
userid = tk.StringVar()
userid.set('')
e3= tk.Entry(my_win, textvariable=userid, width=10)
e3.grid(row=1, column=6)

#label4
l4=tk.Label(my_win, text='Password')
l4.grid(row=1, column=7, padx=5)
password = tk.StringVar()
password.set('')
e4= tk.Entry(my_win, textvariable=password, width=10)
e4.grid(row=1, column=8)

#entrybox

t1= tk.Text(my_win, height=20, width=40)
t1.grid(row=2, column=1, columnspan=8)

my_win.mainloop()
