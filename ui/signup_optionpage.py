from PIL import ImageTk,Image
from tkinter import *

from ui.customer_booking import Customer_booking
from ui.customer_registration import Customer_registration


class Signup_optionpage():

    def __init__(self,root):
        self.root=root
        self.root.title(" sign up ")
        self.root.geometry("595x500")
        self.root.resizable(False,False)
        # background = ImageTk.PhotoImage(Image.open("signup_img.jpg"))
        # imglbl = Label(root, image=background).pack()
        self.root.config(bg="burlywood1")
        lbl = Label(root, text=" SIGN UP ", bg="black", fg="white", font="normal", padx=260, pady=10)
        lbl.place(x=0, y=50)

        def custo():
            self.root.destroy()
            root = Tk()
            Customer_registration(root)
            root.mainloop()

        customer_btn = Button(root, text="Customer", font="normal", width=8, height=2, fg="black", bg="white",command=custo)
        customer_btn.place(x=150,y=200)

        driver_btn = Button(root, text="Driver", font="normal", width=8, height=2, fg="black", bg="white")
        driver_btn.place(x=350,y=200)




if __name__=='__main__':
    root=Tk()
    Signup_optionpage(root)
    root.mainloop()
