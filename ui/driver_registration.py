from tkinter import *
from tkinter import messagebox, ttk

from CRUD.driver import insertDriver
from libs.driverlibs import Diver


class Driver_registration():
    def __init__(self, root):
        self.root = root
        self.root.title(" System")
        self.root.geometry("720x670+500+100")
        self.root.config(bg="burlywood1")

        frame = Frame(self.root, bg="white", height=650, width=700,highlightbackground="black", highlightthickness=2)
        frame.place(x=10, y=10)

        lbl = Label(frame, text=" Driver Registration ", bg="burlywood1", fg="black", font="normal", padx=259, pady=10)
        lbl.place(x=0, y=0)

        name_lbl=Label(frame, font="normal", text="Name", bg="white")
        name_lbl.place(x=130, y=100)

        email_lbl = Label(frame, font="normal", text="Email", bg="white")
        email_lbl.place(x=130, y=170)

        contact_lbl = Label(frame, font="normal", text="Contact", bg="white",)
        contact_lbl.place(x=130, y=240)

        address_lbl = Label(frame, font="normal", text="Address", bg="white")
        address_lbl.place(x=130, y=310)

        lisence_no_lbl = Label(frame, font="normal", text="lisence no", bg="white")
        lisence_no_lbl.place(x=130, y=380)

        car_no_lbl = Label(frame, font="normal", text="Car no", bg="white")
        car_no_lbl.place(x=130, y=450)

        password_lbl = Label(frame, font="normal", text="Password", bg="white")
        password_lbl.place(x=130, y=520)



        name_txt = Entry(frame, width=30, font="normal")
        name_txt.place(x=280, y=100)

        email_txt = Entry(frame, width=30, font="normal")
        email_txt.place(x=280, y=170)

        contact_txt = Entry(frame, width=30, font="normal")
        contact_txt.place(x=280, y=240)

        address_txt = Entry(frame, width=30, font="normal")
        address_txt.place(x=280, y=310)

        lisence_no_txt = Entry(frame, width=30, font="normal")
        lisence_no_txt.place(x=280, y=380)

        car_no_txt = Entry(frame, width=30, font="normal")
        car_no_txt.place(x=280, y=450)

        password_txt = Entry(frame, width=30, font="normal")
        password_txt.place(x=280, y=520)




        def registor1():
            name1= name_txt.get()
            email1=email_txt.get()
            contact1=contact_txt.get()
            address1=address_txt.get()
            car_no1=car_no_txt.get()
            lisence_no1=lisence_no_txt.get()
            password1=password_txt.get()




            regdri=Diver(did='',name=name1,email=email1,contact=contact1,address=address1,lisence_no=lisence_no1,car_no=car_no1,password=password1,driver_status="active")
            result1=insertDriver(regdri)
            print(result1)

            if name1=='' or email1=='' or contact1=='' or address1=='' or car_no1=='' or lisence_no1=='' or password1=='' :
                messagebox.showerror("taxi booking","fill details properly")

            if result1==True:
                msg= messagebox.showinfo("Taxi Booking","Registered driver successful")
                # self.root.destroy()




        registor_btn = Button(frame, text="Registration", bg="white", height=1, font="normal", command=registor1)
        registor_btn.place(x=200, y=600)

        close_btn = Button(frame, text="close", bg="white", height=1, width=10 ,font="normal", command=root.quit)
        close_btn.place(x=380, y=600)






if __name__=='__main__':
    root=Tk()
    Driver_registration(root)
    root.mainloop()