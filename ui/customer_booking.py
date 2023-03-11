from time import strftime
from tkinter import *
from tkinter import ttk, messagebox

from tkcalendar import *
from tktimepicker import AnalogPicker, AnalogThemes
from libs import Global
from CRUD.booking import insertBooking, custtable, deleteBooking, updateBooking
from libs.bookinglibs import Booking
from ui import login
from ui.login import Login
from PIL import Image,ImageTk


class Customerbooking():
    def __init__(self,root):
        self.root=root
        self.root.title("booking")
        self.root.geometry("1850x900")
        self.root.state("zoomed")
        self.root.config(bg="burlywood1")

        frame = Frame(root, height=500, width=705, bg="white", highlightbackground="black", highlightthickness=2)
        frame.place(x=10, y=270)

        def my_time():
            time_string = strftime('%x, %r')
            current_datetime.config(text=time_string)
            current_datetime.after(1000, my_time)

        current_datetime = Label(frame, font="normal",bg="burlywood1",fg="black",padx=246,pady=10)
        current_datetime.place(x=0,y=10)
        my_time()




        initialaddresslbl = Label(frame, text="Initial address", font="normal",bg="white").place(x=120, y=150)
        finaladdresslbl = Label(frame, text="Final address", font="normal",bg="white").place(x=120, y=200)
        pickupdatelbl = Label(frame, text="Pickup date", font="normal",bg="white").place(x=120, y=250)
        pickuptimelbl = Label(frame, text="Pickup Time", font="normal",bg="white").place(x=120, y=300)
        # pricelbl = Label(frame, text="Price", font="normal", fg="white", bg="black").place(x=50, y=250)

        initialaddress_txt = ttk.Combobox(frame, width=20, font="normal",values=['kathmandu','pokhara','biratnagar','butwal','chitwan'])
        initialaddress_txt.place(x=270, y=150)
        finaladdress_txt = ttk.Combobox(frame, width=20, font="normal",values=['kathmandu','pokhara','biratnagar','butwal','chitwan'])
        finaladdress_txt.place(x=270, y=200)

        cid_txt = Entry(frame, width=30, font="normal")

        cid_txt.insert(0, Global.currentuser[0])
        cid_txt.place()

        bid_txt = Entry(frame,width=30, font="normal")
        # bid_txt.place(x=270,y=350)


        # profileLbl=Label(root,text="  welcome {}".format(Global.currentuser[1]),font="normal",bg="black",fg="white",padx=300,pady=10)
        # profileLbl.place(x=0,y=10)

        # image12 = Image.open("C:\\Users\\ACER\\Pictures\\python project\\profi.jpg")
        # profile = ImageTk.PhotoImage(image12)
        # profile_btn = Button(root, image=profile)
        # profile_btn.image = image12
        # profile_btn.place(x=200, y=60)








        # a=initialaddress_txt.get()
        # b= finaladdress_txt.get()
        # price_txt= Entry(frame, width=20, font="normal")
        # price_txt.place(x=170, y=250)
        # if a=='kathmandu' and b=='pokhara':
        #     price_txt.insert(0,'1200')
        #
        # if a=='pokhara' and b=='kathmandu':
        #     price_txt.insert(0,'1200')



        pickupdate_txt = DateEntry(frame, selectmode='day', font="normal", padx=250)
        pickupdate_txt.place(x=270, y=250)
        pickuptime_txt=Entry(frame, width=20, font="normal")
        pickuptime_txt.place(x=270, y=300)



        def books():
            initialaddress = initialaddress_txt.get()
            finaladdress = finaladdress_txt.get()
            pickupdate = pickupdate_txt.get()
            pickuptime = pickuptime_txt.get()
            cid = cid_txt.get()




            book=Booking(bid='',initial_address=initialaddress,final_address=finaladdress,pickup_date=pickupdate,pickup_time=pickuptime,
                         bookings_status='pending',cid=cid)
            result1 = insertBooking(book)


            if result1==True:
                msg= messagebox.showinfo("Taxi Booking","Booked successful")
                requested_table.delete(*requested_table.get_children())
                table()
            else:
                msg = messagebox.showerror("Taxi Booking","Booked unsuccessful")

        booknowbtn = Button(frame, text="Book", bg="burlywood1", fg="black", height=1, width=7, font="normal", command=books).place(x=100, y=400)
        closebtn = Button(frame, text="Close", bg="burlywood1", fg="black", height=1, width=7, font="normal",
                            command=root.destroy).place(x=200, y=400)














        #
        # update_btn = Button(frame, text="update", fg="black", bg="white", height=1, width=5, font="normal",
        #                     command=blog).place(x=150, y=460)
        style = ttk.Style()
        style.theme_use("default")


        style.configure("Treeview.Heading",
                        background="black",
                        foreground="white",
                        relief="flat"
        )

        requested_table = ttk.Treeview(root)
        requested_table['columns'] = ('bid','p_address', 'd_address', 'p_date', 'p_time','b_status')
        requested_table.column('#0', width=0, stretch=NO)
        requested_table.column('bid', width=135, anchor=CENTER)
        requested_table.column('p_address', width=135, anchor=CENTER)
        requested_table.column('d_address', width=135, anchor=CENTER)
        requested_table.column('p_date', width=135, anchor=CENTER)
        requested_table.column('p_time', width=135, anchor=CENTER)
        requested_table.column('b_status', width=135, anchor=CENTER)

        requested_table.heading('#0', text='', anchor=CENTER)
        requested_table.heading('bid', text='bid', anchor=CENTER)
        requested_table.heading('p_address', text='initial Address', anchor=CENTER)
        requested_table.heading('d_address', text='final Address', anchor=CENTER)
        requested_table.heading('p_date', text='Pickup Date', anchor=CENTER)
        requested_table.heading('p_time', text='Pickup Time', anchor=CENTER)
        requested_table.heading('b_status', text='Booking status', anchor=CENTER)
        requested_table.pack(side=RIGHT,fill=BOTH)

        def table():

            pending = custtable(cid_txt.get())
            for row in pending:
                requested_table.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5]))

        table()

        def selectrequested_table(a):
            initialaddress_txt.delete(0, END)
            finaladdress_txt.delete(0, END)
            pickuptime_txt.delete(0, END)
            pickupdate_txt.delete(0, END)
            bid_txt.delete(0,END)

            selectitem = requested_table.selection()[0]
            initialaddress_txt.insert(0, requested_table.item(selectitem)['values'][1])
            finaladdress_txt.insert(0, requested_table.item(selectitem)['values'][2])
            pickuptime_txt.insert(0, requested_table.item(selectitem)['values'][4])
            pickupdate_txt.insert(0, requested_table.item(selectitem)['values'][3])
            bid_txt.insert(0, requested_table.item(selectitem)['values'][0])

        requested_table.bind('<<TreeviewSelect>>',selectrequested_table)


        initialaddress1 = initialaddress_txt.get()
        finaladdress1 = finaladdress_txt.get()
        pickupdate1 = pickupdate_txt.get()
        pickuptime1 = pickuptime_txt.get()
        bid1 = bid_txt.get()

        def cancel():

            result1=deleteBooking(bid_txt.get())
            print(result1)
            messagebox.showinfo("TBS","booking canceled succesfully")
            requested_table.delete(*requested_table.get_children())

            table()



        def update():

            z=Booking(bid=bid_txt.get(),initial_address=initialaddress_txt.get(),final_address=finaladdress_txt.get(),pickup_date=pickupdate_txt.get(),pickup_time=pickuptime_txt.get())
            updateBooking(z)
            messagebox.showinfo("TBS","update succesfully")
            requested_table.delete(*requested_table.get_children())
            table()

        def blog():
            self.root.destroy()
            root = Tk()
            login.Login(root)
            root.mainloop()

        cancel_btn = Button(frame, text="cancel", bg="burlywood1", fg="black", height=1, width=7, font="normal",
                            command=cancel)
        cancel_btn.place(x=300, y=400)

        update_btn = Button(frame, text="update", bg="burlywood1", fg="black", height=1, width=7, font="normal",
                            command=update)
        update_btn.place(x=400, y=400)

        backtolog = Button(frame, text="log out", bg="burlywood1", fg="black", height=1, width=7, font="normal",
                           command=blog)
        backtolog.place(x=500, y=400)







if __name__=='__main__':
    root=Tk()
    Customerbooking(root)
    root.mainloop()
