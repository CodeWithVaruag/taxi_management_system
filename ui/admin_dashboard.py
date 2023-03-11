import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from libs import Global

from CRUD.admin import manage_customer_table, assign_booking
from libs.bookinglibs import Booking
from ui import login
from ui.available_driver import Available_driver
from ui.driver_registration import Driver_registration


class Admindashboard():

    def __init__(self,root):
        self.root=root
        self.root.title("driver dashboard")
        self.root.state("zoomed")
        self.root.config(bg="white")



        frame1=Frame(root,bg="burlywood1",height=750,width=250)
        frame1.place(x=10,y=20)

        # profileLbl = Label(frame1, text="  welcome {}".format(Global.currentadmin[1]), font="normal", bg="black",
        #                    fg="white",padx=42,pady=10)
        # profileLbl.place(x=0, y=30)

        def regdriver():
            root = Tk()
            Driver_registration(root)
            root.mainloop()




        btn_reg_driver = Button(root, text="register driver", height=1, width=16, font="normal",bg='white',command=regdriver)
        btn_reg_driver.place(x=30,y=200)

        def logout():
            self.root.destroy()
            root = Tk()
            login.Login(root)
            root.mainloop()

        logout_btn = Button(root, text="Log Out", height=1, width=16, font="normal",bg='white',command=logout)
        logout_btn.place(x=30,y=300)



        frame2 = Frame(root, height=750, width=1200,bg="white" )
        frame2.place(x=300, y=20)

        style = ttk.Style()
        style.theme_use("default")


        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=('Times New Roman', 14))


        requested_table = ttk.Treeview(frame2)
        requested_table['columns'] = ('bid','p_customer_name', 'p_address', 'd_address', 'p_date', 'p_time','p_bookingstatus')
        requested_table.column('#0', width=0, stretch=NO)
        requested_table.column('bid', width=170, anchor=CENTER)
        requested_table.column('p_customer_name', width=170, anchor=CENTER)
        requested_table.column('p_address', width=170, anchor=CENTER)
        requested_table.column('d_address', width=170, anchor=CENTER)
        requested_table.column('p_date', width=170, anchor=CENTER)
        requested_table.column('p_time', width=175, anchor=CENTER)
        requested_table.column('p_bookingstatus', width=175, anchor=CENTER)

        requested_table.heading('#0', text='', anchor=CENTER)
        requested_table.heading('bid', text='bid', anchor=CENTER)
        requested_table.heading('p_customer_name', text='customer name', anchor=CENTER)
        requested_table.heading('p_address', text='initial Address', anchor=CENTER)
        requested_table.heading('d_address', text='final Address', anchor=CENTER)
        requested_table.heading('p_date', text='Pickup Date', anchor=CENTER)
        requested_table.heading('p_time', text='Pickup Time', anchor=CENTER)
        requested_table.heading('p_bookingstatus', text='booking status', anchor=CENTER)
        requested_table.place(x=0,y=0)

        def cusdas():
            cuspending = manage_customer_table()
            for row in cuspending:
                requested_table.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6]))

        cusdas()

        # aid_txt = Entry(frame2, width=18, font="normal")
        # aid_txt.insert(0, Global.currentadmin[0])
        # aid_txt.place()

        customer_name_label=Label(frame2,text="Name",font="normal",bg='white')
        customer_name_label.place(x=450,y=300)

        customer_name_txt=Entry(frame2,width=18,font="normal")
        customer_name_txt.place(x=560,y=300)

        Driver_id_label= Label(frame2, text="Driver id", font="normal", bg='white')
        Driver_id_label.place(x=450, y=350)

        Driver_id_txt = Entry(frame2, width=18, font="normal")
        Driver_id_txt.place(x=560, y=350)

        bid_txt= Entry(frame2, width=18, font="normal")
        bid_txt.place()


        def search():
            root = Tk()
            Available_driver(root)
            root.mainloop()





        search_btn = Button(frame2, text="search", font="normal",bg="black",fg="white",command=search)
        search_btn.place(x=520,y=420)

        def selectrequested_table(a):
            customer_name_txt.delete(0, END)
            bid_txt.delete(0, END)

            selectitem = requested_table.selection()[0]
            customer_name_txt.insert(0, requested_table.item(selectitem)['values'][1])
            bid_txt.insert(0, requested_table.item(selectitem)['values'][0])


        requested_table.bind('<<TreeviewSelect>>', selectrequested_table)


        def assign():

            Driver_id1=Driver_id_txt.get()
            Bid1=bid_txt.get()

            bk=Booking(bid=Bid1,did=Driver_id1)
            assign_booking(bk)
            requested_table.delete(*requested_table.get_children())
            cusdas()
            messagebox.showinfo("Taxi booking system","succesfully driver assigned")


        assign_btn=Button(frame2,text="assign",font="normal",command=assign,bg="black",fg="white")
        assign_btn.place(x=600,y=420)


# registration of driver












if __name__=='__main__':
    root=Tk()
    Admindashboard(root)
    root.mainloop()
