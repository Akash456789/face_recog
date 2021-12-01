from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import mysql.connector

class Foget_passwrod():
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x500+350+100")
        self.root.title("Foget Password")
        self.root.resizable(0,0)
        self.root.option_add("*TCombobox*Listbox*font","Times 15 bold")

        self.f_name = StringVar()
        self.email = StringVar()
        self.question = StringVar()
        self.answer = StringVar()
        self.pswrd = StringVar()
        self.confirm_pswrd = StringVar()
        
        frame = Frame(self.root, bg = "skyblue4")
        frame.place(x =  0, y = 0, width = 700, height = 510)

        Label(frame, text="FORGET PASSWORD", font=("Times 32 bold underline"), bg = "skyblue4").place(x = 150, y = 0)

        Label(frame, text="First Name", font=("Times 20 bold"), bg = "skyblue4").place(x = 30, y = 90)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.f_name).place(x = 30, y = 140)

        Label(frame, text="Email", font=("Times 20 bold"), bg = "skyblue4").place(x = 370, y = 90)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.email).place(x = 370, y = 140)

        Label(frame, text="Select Security Question", font=("Times 20 bold"), bg = "skyblue4").place(x = 30, y = 200)
        ques = ttk.Combobox(frame, font=("Times 18 bold"), width=22, textvariable=self.question, state="readonly")
        ques["values"] = ("what is your favorite color?", "what is your pet name?", "what is your father name?")
        ques.place(x = 30, y = 250)

        Label(frame, text="Security Answer", font=("Times 20 bold"), bg = "skyblue4").place(x = 370, y = 200)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.answer).place(x = 370, y = 250)

        Label(frame, text="New Password", font=("Times 20 bold"), bg = "skyblue4").place(x = 30, y = 310)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.pswrd, show="*").place(x = 30, y = 360)

        Label(frame, text="Confirm New Password", font=("Times 20 bold"), bg = "skyblue4").place(x = 370, y = 310)
        Entry(frame, font=("Times 18 bold"), width=23, textvariable=self.confirm_pswrd, show="*").place(x = 370, y = 360)

        Button(frame, font=("Times 25 bold"), bg = "orange", activebackground="orange", relief=RAISED, bd =4, text="Change Password", command=self.save_pswrd).place(x=200, y=415)
    
    def save_pswrd(self):
        if self.f_name.get()=="" or self.email.get()=="" or self.question.get()=="" or self.answer.get()=="" or self.pswrd.get()=="":
            msg.showerror("Error", "All Fields are mandatory to fill.", parent = self.root)

        elif self.pswrd.get() != self.confirm_pswrd.get():
            msg.showerror("Error", "Confirm Password Not Matched to Your Password.", parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host = "localhost", username = "root", password = "7669454417", database = "register")
                cur=conn.cursor()
                db = "update registration set Password = %s where First_Name = %s and Email = %s and Security_Ques = %s and Answer = %s"

                cur.execute("select * from registration where First_Name = %s and Email = %s and Security_Ques = %s and Answer = %s",
                (self.f_name.get(), self.email.get(), self.question.get(), self.answer.get()))
                data = cur.fetchone()
                
                if data == None:
                    msg.showerror("Error", "Your Data is Not Matched with Our Database.", parent=self.root)

                else:
                    val = [(self.pswrd.get(), self.f_name.get(), self.email.get(), self.question.get(), self.answer.get())]
                    cur.executemany(db, val)
                    msg.showinfo("Success", "Your Password Update Successfully.", parent = self.root)
        
                conn.commit()
                conn.close()
                    
            except Exception as es:
                msg.showerror("Error", f"Due to:{str(es)}", parent=self.root)

if __name__=="__main__":
    root = Tk()    
    obj = Foget_passwrod(root)
    root.mainloop()