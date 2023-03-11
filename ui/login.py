from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ui
from PIL import ImageTk,Image
from CRUD.admin import Check_admin
from CRUD.registration import Check_cus
from libs import Global
from libs.adminlibs import Admin
from libs.customerlibs import Customer
from libs.driverlibs import Diver
from ui import customer_booking
from ui.admin_dashboard import Admindashboard
from ui.customer_registration import Customer_registration
from CRUD.driver import Check_driver
from ui.driverdashboard import Driver_Dashboard


class Login():
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.state("zoomed")
        self.root.config(bg="burlywood1")




        image12=Image.open("C:\\Users\\ACER\\Pictures\\python project\\img1.jpg")
        background = ImageTk.PhotoImage(image12)
        imglbl = Label(self.root, image=background)
        imglbl.image=background
        imglbl.place(x=500,y=0)




        frame=Frame(self.root,bg="white",height=300,width=400,highlightbackground="black", highlightthickness=2)
        frame.place(x=50, y=200)



        lbl = Label(root, text=" LOGIN ", bg="white", fg="black", font="normal", padx=212, pady=10)
        lbl.place(x=0, y=0)

        email_lbl=Label(frame,font="normal",text="Email",bg="white",fg="black")
        email_lbl.place(x=50,y=100)

        password_lbl = Label(frame, font="normal", text="Password", bg="white",fg="black")
        password_lbl.place(x=50, y=150)

        email_txt=Entry(frame,width=20,font="normal")
        email_txt.place(x=150,y=100)

        password_txt=Entry(frame,width=20,font="normal",show="•")
        password_txt.place(x=150,y=150)

        def log():
            email1=email_txt.get()
            password1=password_txt.get()


            if email1=='' and password1=='':
                messagebox.showerror("taxi booking","fill the info")



            log1 = Customer(email=email1, password=password1)
            record1 = Check_cus(log1)
            print(record1)

            log2 = Admin(email=email1, password=password1)
            record2 = Check_admin(log2)
            print(record2)

            log3 = Diver(email=email1, password=password1)
            record3 = Check_driver(log3)
            print(record3)




            if record1 != None:
                Global.currentuser = record1
                mes = messagebox.showinfo("taxi Management", "Welcome " + record1[1])
                self.root.destroy()
                root = Tk()
                customer_booking.Customerbooking(root)
                root.mainloop()






            if record2 != None:
                Global.currentadmin = record2
                mes = messagebox.showinfo("taxi Management", "Welcome " + record2[1])
                self.root.destroy()
                root = Tk()
                Admindashboard(root)
                root.mainloop()


            if record3 != None:
                Global.currentdriver = record3
                mes = messagebox.showinfo("taxi Management", "Welcome " + record3[1])
                self.root.destroy()
                root = Tk()
                Driver_Dashboard(root)
                root.mainloop()

            if (record1 == None) and (record2 == None) and (record3 == None):
                mes=messagebox.showerror("taxi Management","no records founds")




        def sign():
            self.root.destroy()
            root = Tk()
            Customer_registration(root)
            root.mainloop()

        login_btn = Button(frame, text="Login", bg="burlywood1", height=1, width=8, font="normal", command=log)
        login_btn.place(x=180, y=230)

        signup_btn = Button(root, text="---Click here to Sign up----", bg="white", fg="black",font="normal", command=sign,padx=130, pady=8)
        signup_btn.place(x=0,y=750)




if __name__=='__main__':
    root=Tk()
    Login(root)
    root.mainloop()




