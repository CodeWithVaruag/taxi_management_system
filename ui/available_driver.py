import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from CRUD.driver import available_driver
from libs import Global




class Available_driver():

    def __init__(self,root):
        self.root=root
        self.root.title("driver dashboard")
        self.root.geometry("340x227+720+500")
        self.root.config(bg="white")

        requested_table = ttk.Treeview(root)
        requested_table['columns'] = ('did', 'driver_name')
        requested_table.column('#0', width=0, stretch=NO)
        requested_table.column('did', width=170, anchor=CENTER)
        requested_table.column('driver_name', width=170, anchor=CENTER)


        requested_table.heading('#0', text='', anchor=CENTER)
        requested_table.heading('did', text='driver id', anchor=CENTER)
        requested_table.heading('driver_name', text='driver name', anchor=CENTER)


        requested_table.place(x=0, y=0)

        def cusdas():
            cuspending = available_driver()
            for row in cuspending:
                requested_table.insert(parent='', index='end',
                                       values=(row[0], row[1]))

        cusdas()

        close_btn=Button(root,text="close",font="normal",bg='black',fg='white',command=root.destroy)
        close_btn.place(x=150,y=180)


if __name__=='__main__':
    root=Tk()
    Available_driver(root)
    root.mainloop()
