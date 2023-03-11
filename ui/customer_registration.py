from tkinter import *
from tkinter import messagebox, ttk

from CRUD.registration import insertCustomer
from libs.customerlibs import Customer
from ui import login


class Customer_registration():
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.state("zoomed")
        self.root.config(bg="burlywood1")

        frame = Frame(self.root, bg="white", height=650, width=700, highlightbackground="black", highlightthickness=2)
        frame.place(x=450, y=100)

        lbl = Label(frame, text=" Registration ", bg="white", fg="black", font="normal", padx=280, pady=10)
        lbl.place(x=0, y=0)

        name_lbl=Label(frame, font="normal", text="Name", bg="white", fg="black")
        name_lbl.place(x=130, y=100)

        email_lbl = Label(frame, font="normal", text="Email", bg="white", fg="black")
        email_lbl.place(x=130, y=170)

        contact_lbl = Label(frame, font="normal", text="Contact", bg="white", fg="black")
        contact_lbl.place(x=130, y=240)

        address_lbl = Label(frame, font="normal", text="Address", bg="white", fg="black")
        address_lbl.place(x=130, y=310)

        password_lbl = Label(frame, font="normal", text="Password", bg="white", fg="black")
        password_lbl.place(x=130, y=380)

        payment_lbl= Label(frame, font="normal", text="credit no", bg="white", fg="black")
        payment_lbl.place(x=130, y=450)

        name_txt = Entry(frame, width=30, font="normal")
        name_txt.place(x=280, y=100)

        email_txt = Entry(frame, width=30, font="normal")
        email_txt.place(x=280, y=170)

        contact_txt = Entry(frame, width=30, font="normal")
        contact_txt.place(x=280, y=240)

        address_txt = Entry(frame, width=30, font="normal")
        address_txt.place(x=280, y=310)

        password_txt = Entry(frame, width=30, font="normal")
        password_txt.place(x=280, y=380)

        payment_txt = Entry(frame, width=30, font="normal")
        payment_txt.place(x=280, y=450)






        def registor1():
            name1= name_txt.get()
            email1=email_txt.get()
            contact1=contact_txt.get()
            address1=address_txt.get()
            password1=password_txt.get()
            payement1=payment_txt.get()


            reg=Customer(cid='',name=name1,email=email1,contact=contact1,address=address1,password=password1,payment=payement1)
            result1=insertCustomer(reg)
            print(result1)

            if name1=='' or email1=='' or contact1=='' or address1=='' or password1=='' and payement1=='':
                messagebox.showerror("taxi booking","fill details properly")

            if result1==True:
                msg= messagebox.showinfo("Taxi Booking","Registered successful")






        registor_btn = Button(frame, text="Registration", bg="white", height=1, font="normal", command=registor1)
        registor_btn.place(x=300, y=555)

        def blog():
            self.root.destroy()
            root = Tk()
            login.Login(root)
            root.mainloop()

        logbtn = Button(frame, text="login page", bg="white", height=1, font="normal", command=blog)
        logbtn.place(x=450, y=555)






if __name__=='__main__':
    root=Tk()
    Customer_registration(root)
    root.mainloop()