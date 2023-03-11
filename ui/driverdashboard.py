import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from libs import Global

from CRUD.driver import driver_table, changedriverstatus, changedriverstatus1
from libs.bookinglibs import Booking
from libs.driverlibs import Diver
from ui import login


class Driver_Dashboard():

    def __init__(self,root):
        self.root=root
        self.root.title("driver dashboard")
        self.root.geometry("1500x450")
        self.root.resizable(False,False)
        self.root.config(bg="burlywood1")

        did_txt=Entry(root)
        did_txt.insert(0,Global.currentdriver[0])
        did1=did_txt.get()

        bid_txt = Entry(root)
        bid_txt.place()


        requested_table = ttk.Treeview(root)
        requested_table['columns'] = ('bid','cid','customer_name','initial_address','final_address','date','time','booking_status')
        requested_table.column('#0', width=0, stretch=NO)
        requested_table.column('bid', width=170, anchor=CENTER)
        requested_table.column('cid', width=170, anchor=CENTER)
        requested_table.column('customer_name', width=170, anchor=CENTER)
        requested_table.column('initial_address', width=170, anchor=CENTER)
        requested_table.column('final_address', width=170, anchor=CENTER)
        requested_table.column('date', width=170, anchor=CENTER)
        requested_table.column('time', width=170, anchor=CENTER)
        requested_table.column('booking_status', width=170, anchor=CENTER)




        requested_table.heading('#0', text='', anchor=CENTER)
        requested_table.heading('bid', text='bid', anchor=CENTER)
        requested_table.heading('cid', text='cid', anchor=CENTER)
        requested_table.heading('customer_name', text='customer_name', anchor=CENTER)
        requested_table.heading('initial_address', text='initial_address', anchor=CENTER)
        requested_table.heading('final_address', text='final_address', anchor=CENTER)
        requested_table.heading('date', text='date', anchor=CENTER)
        requested_table.heading('time', text='time', anchor=CENTER)
        requested_table.heading('booking_status', text='booking_status', anchor=CENTER)

        requested_table.place(x=50, y=100)

        def cusdas():
            cuspending1 = driver_table(did1)
            for row in cuspending1:
                requested_table.insert(parent='', index='end',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

        cusdas()

        # profileLbl = Label(root, text="  welcome {}".format(Global.currentdriver[1]), font="normal", bg="black",
        #                    fg="white", padx=300, pady=10)
        # profileLbl.place(x=0, y=400)

        def selectrequested_table(a):
            bid_txt.delete(0, END)


            selectitem = requested_table.selection()[0]
            bid_txt.insert(0, requested_table.item(selectitem)['values'][0])


        requested_table.bind('<<TreeviewSelect>>', selectrequested_table)



        def accept_trip():
            bid1=bid_txt.get()
            print(bid1)

            changedriverstatus(bid1)
            changedriverstatus1(did1)
            requested_table.delete(*requested_table.get_children())
            cusdas()
            messagebox.showinfo("TBS","trip accepted")

        accept_btn = Button(root, text="accept", font="normal", bg='black', fg='white', command=accept_trip)
        accept_btn.place(x=700, y=400)

        def logout():
            self.root.destroy()
            root = Tk()
            login.Login(root)
            root.mainloop()
            pass

        logout = Button(root, text="log out", font="normal", bg='white', fg='black', command=logout)
        logout.place(x=800, y=400)







if __name__=='__main__':
    root=Tk()
    Driver_Dashboard(root)
    root.mainloop()