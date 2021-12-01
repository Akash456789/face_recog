from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from forget_password import Foget_passwrod
from main import Face_Recognition_System
import mysql.connector

class Login_window():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Admin Login Page")

        #img = Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\login_bg.png")
        img=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\login_bg.png")
        img = img.resize((1530, 800))
        self.bg = ImageTk.PhotoImage(img)
        lbl_bg = Label(self.root, image = self.bg, borderwidth=0)
        lbl_bg.place(x = 0, y = 0)
        
        # frame for login details
        frame = Frame(self.root, bg = "gray8" )
        frame.place(x = 500, y = 120, width = 380, height = 510)
        
        img1=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\stud_icon.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.stud_img = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(frame, image=self.stud_img, bg = "gray8", bd = 2, borderwidth=0)
        lbl_img1.place(x = 150, y = 10, width=100, height=100) 

        Label(frame, text="Admin Login Page", font=("Times 25 bold"), bg = "gray8", fg = "cadetblue2").place(x = 65, y = 110)

        #img2 = Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\user.png")
        img2=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\user.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.user_icon = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(frame, image=self.user_icon, bg = "gray8", bd = 2, borderwidth=0)
        lbl_img2.place(x = 20, y = 182, width=25, height=25) 
        
        Label(frame, text="Username:", font=("Times 18 bold"), bg = "gray8", fg = "yellow").place(x = 50, y = 180)
        self.user = ttk.Entry(frame, font=("Times 19 bold"))
        self.user.place(x = 15, y = 220, width=350)

        #img3 = Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\pass.png")
        img3=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\pass.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.pswrd_icon = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(frame, image=self.pswrd_icon, bg = "gray8", bd = 2, borderwidth=0)
        lbl_img3.place(x = 20, y = 275, width=25, height=25) 

        Label(frame, text="Password:", font=("Times 18 bold"), bg = "gray8", fg = "yellow").place(x = 50, y = 270)
        self.pswrd = ttk.Entry(frame, font=("Times 19 bold"), show="*")
        self.pswrd.place(x = 15, y = 310, width=350)


        #btn_img = Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\login.png")
        btn_img=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\login.png")
        btn_img = btn_img.resize((150, 60), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(btn_img)

        Button(frame, image=self.img, command=self.login, border=0).place(x = 120, y = 370)

        new_register = Button(frame, text="New User Register!!", font=("Times 13 bold"), bg = "gray8", 
                                            activebackground="gray8", fg="white", border=0, command=self.registeration)
        new_register.place(x = 20, y = 445)

        forget_pass = Button(frame, text="Forget Password?", font=("Times 13 bold"), bg = "gray8",
                                            activebackground="gray8", fg="white", border=0, command=self.forget_pass)
        forget_pass.place(x = 20, y = 470)


    def login(self):
        if self.user.get()=="" or self.pswrd.get()=="":
            msg.showerror("Error", "All fields are required.")
        
        else:
            try:
                conn=mysql.connector.connect(host = "localhost", username = "root", password = "root5", database = "face_recognizer")
                cur=conn.cursor()
                cur.execute("select Email, Password from registration where Email = %s and Password = %s",(self.user.get(), self.pswrd.get()))
                data = cur.fetchone()
                
                if data == None:
                    msg.showerror("Invalid", "Invalid Username and Password.", parent = self.root)
                else:
                    msg.showinfo("Success", "You Logged In Successfully.", parent = self.root)
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                    
                conn.commit()
                conn.close()
            
            except Exception as es:
                msg.showerror("Error", f"Due to:{str(es)}", parent=self.root)
            
    
    def registeration(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
    
    def forget_pass(self):
        self.new_window = Toplevel(self.root)
        self.app = Foget_passwrod(self.new_window)

class Register():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Admin Registeration Page")
        self.root.option_add("*TCombobox*Listbox*font","Times 15 bold")

        #----------------Variable----------------------
        self.f_name = StringVar()
        self.l_name = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.question = StringVar()
        self.answer = StringVar()
        self.pswrd = StringVar()
        self.confirm_pswrd = StringVar()
        self.check = IntVar()

        #img=Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\reg_bg.png")
        img=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\tem1.jpg")
        img=img.resize((1530,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        lbl=Label(self.root, image=self.photoimg, borderwidth=0)
        lbl.place(x=0,y=0)

        frame = Frame(self.root, bg = "khaki", width=1220, height=600)
        frame.place(x = 150, y = 100)

        #img1=Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\reg_bg.png")
        img1=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\reg_bg.png")
        img1=img1.resize((500,600),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbl=Label(frame, image=self.photoimg1, borderwidth=0)
        lbl.place(x=0,y=0)

        Label(frame, text="REGISTER HERE", font=("Times 45 bold underline"), bg = "khaki", fg="orangered").place(x = 650, y = 0)

        Label(frame, text="First Name", font=("Times 20 bold"), bg = "khaki").place(x = 580, y = 90)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.f_name).place(x = 580, y = 130)

        Label(frame, text="Last Name", font=("Times 20 bold"), bg = "khaki").place(x = 920, y = 90)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.l_name).place(x = 920, y = 130)

        Label(frame, text="Contact No.", font=("Times 20 bold"), bg = "khaki").place(x = 580, y = 175)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.phone).place(x = 580, y = 215)

        Label(frame, text="Email", font=("Times 20 bold"), bg = "khaki").place(x = 920, y = 175)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.email).place(x = 920, y = 215)

        Label(frame, text="Select Security Question", font=("Times 20 bold"), bg = "khaki").place(x = 575, y = 260)
        ques = ttk.Combobox(frame, font=("Times 18 bold"), width=22, textvariable=self.question, state="readonly")
        ques["values"] = ("what is your favorite color?", "what is your pet name?", "what is your father name?")
        ques.place(x = 580, y = 300)

        Label(frame, text="Security Answer", font=("Times 20 bold"), bg = "khaki").place(x = 920, y = 260)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.answer).place(x = 920, y = 300)

        Label(frame, text="Password", font=("Times 20 bold"), bg = "khaki").place(x = 580, y = 345)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.pswrd, show="*").place(x = 580, y = 385)

        Label(frame, text="Confirm Password", font=("Times 20 bold"), bg = "khaki").place(x = 920, y = 345)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.confirm_pswrd, show="*").place(x = 920, y = 385)

        chk_btn = Checkbutton(frame, text="I Agree the Terms & Conditions.", variable=self.check, font=("Times 15 bold"), bg = "khaki", activebackground="khaki")
        chk_btn.place(x = 580, y = 430)

        #btn_img = Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\reg.png")
        btn_img=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\save.png")
        btn_img = btn_img.resize((355, 80), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(btn_img)

        Button(frame, image=self.img, relief=RIDGE, width=320, height=65, command=self.registeration_form, border=0).place(x=730, y=475)
        
        Button(frame, text="Already Registered. Log In",font=("Times 15 bold"),bg="khaki",fg="blue",activebackground="khaki",border=0,command=self.login).place(x=570, y=555)
        
    def registeration_form(self):
        if self.f_name.get()=="" or self.l_name.get()=="" or self.phone.get()=="" or self.email.get()=="" or self.pswrd.get()=="" or self.check.get()==0:
            msg.showerror("Error", "All Fields are mandatory to fill.", parent = self.root)
        
        elif self.pswrd.get() != self.confirm_pswrd.get():
            msg.showerror("Error", "Confirm Password Not Matched to Your Password.", parent = self.root)
        
        else:
            try:
                conn=mysql.connector.connect(host = "localhost", username = "root", password = "root5", database = "face_recognizer")
                cur=conn.cursor()
                cur.execute("create table IF NOT EXISTS registration(First_Name varchar(100), Last_Name varchar(100), Contact int(200), Email varchar(200), Security_Ques varchar(400), Answer varchar(100), Password varchar(150))")
                conn.commit()
                inset_data=("insert into registration(First_Name,Last_Name,Contact,Email,Security_Ques,Answer,Password) Values(%s,%s,%s,%s,%s,%s,%s)")
                val = [(self.f_name.get(),self.l_name.get(),self.phone.get(),self.email.get(),str(self.question.get()),self.answer.get(),self.pswrd.get())]
                cur.executemany(inset_data, val)
                conn.commit()
                conn.close()
                msg.showinfo("Success", "You Registered Successfully.", parent = self.root)
                self.clear()
            except Exception as es:
                msg.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def clear(self):
        self.f_name.set("")
        self.l_name.set("")
        self.phone.set("")
        self.email.set("")
        self.question.set("")
        self.answer.set("")
        self.pswrd.set("")
        self.confirm_pswrd.set("")
        self.check.set("")

    def login(self):
        self.new_window = Toplevel(self.root)
        self.app = Login_window(self.new_window)


if __name__=="__main__":
    root = Tk()    
    obj = Login_window(root)
    obj1 = Register(root)
    root.mainloop()