from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from login import Login_window
from tkinter import messagebox as msg
import mysql.connector

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
        
        Button(frame, text="Already Registered. Log In",font=("Times 15 bold"),bg="khaki",activebackground="khaki",border=0,command=self.login).place(x=570, y=555)
        
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
    obj = Register(root)
    root.mainloop()