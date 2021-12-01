from time import strftime
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from student import Student
from train import Train
#from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #first image
        img=Image.open("E:/python/Face_Recognition_Attendace_System/images/pic2.png")
        #img=Image.open("D:/face_recon/images/pic2.png")
        img=img.resize((550,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0, width=550, height=130)

        #second image

        img1=Image.open(r"E:/python/Face_Recognition_Attendace_System/images/pic1.gif")
        #img1=Image.open("D:/face_recon/images/pic1.gif")
        img1=img1.resize((550,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500,y=0, width=550, height=130)

        #thired image

        img2=Image.open(r"E:/python/Face_Recognition_Attendace_System/images/pic3.jpg")
        #img2=Image.open("D:/face_recon/images/pic3.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000,y=0, width=550, height=130)

        #bg image

        img3=Image.open(r"E:/python/Face_Recognition_Attendace_System/images/bgpic1.jpg")
        #img3=Image.open("D:/face_recon/images/bgpic1.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDACE SYSTEM", font=("time new roman", 35, "bold"), bg="red" , fg="white",bd=4, relief=RIDGE)
        title_lbl.place(x=0, y=0, width=1530, height=45)

        def time():
            str1 = strftime("%I:%M:%S %p")
            lbl.config(text=str1)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl, font=("Times 16 bold"), bg = "red")
        lbl.place(x=5, y=2, width=120,  height=30)
        time()

        #student button
        img4=Image.open("E:/python/Face_Recognition_Attendace_System/images/student.jpg")
        #img4=Image.open("D:/face_recon/images/student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2", command=self.student_details)
        b1.place(x=350,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2", command=self.student_details, font=("time new roman", 15, "bold"), bg="blue" , fg="white")
        b1_1.place(x=350,y=300,width=220,height=40)

        #train face button
        img8=Image.open("E:/python/Face_Recognition_Attendace_System/images/traindata.jpg")
        #img8=Image.open("D:/face_recon/images/traindata.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=650,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman", 15, "bold"), bg="blue" , fg="white")
        b1_1.place(x=650,y=300,width=220,height=40)

        #Attendance face button
        img6=Image.open("E:/python/Face_Recognition_Attendace_System/images/att.png")
        #img6=Image.open("D:/face_recon/images/att.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.att_data)
        b1.place(x=950,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.att_data, font=("time new roman", 15, "bold"), bg="blue" , fg="white")
        b1_1.place(x=950,y=300,width=220,height=40)

        #photos button
        img9=Image.open("E:/python/Face_Recognition_Attendace_System/images/photos.jpg")
        #img9=Image.open("D:/face_recon/images/photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2", command=self.open_img)
        b1.place(x=350,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img, font=("time new roman", 15, "bold"), bg="blue" , fg="white")
        b1_1.place(x=350,y=580,width=220,height=40)

        #Developer button
        img10=Image.open("E:/python/Face_Recognition_Attendace_System/images/deve.jpg")
        #img10=Image.open("D:/face_recon/images/deve.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.dev)
        b1.place(x=650,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.dev ,font=("time new roman", 15, "bold"), bg="blue" , fg="white")
        b1_1.place(x=650,y=580,width=220,height=40)

        #exit button
        img11=Image.open("E:/python/Face_Recognition_Attendace_System/images/exit.jpg")
        #img11=Image.open("D:/face_recon/images/exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2", command=self.exit)
        b1.place(x=950,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",  font=("time new roman", 15, "bold"), bg="blue" , fg="white", command=self.exit)
        b1_1.place(x=950,y=580,width=220,height=40)


    def open_img(self):
        #os.startfile("D:/FINAL YEAR PROJECT/FACE DATA")
        os.startfile("E:\python\Face_Recognition_Attendace_System\data")


    def exit(self):
        self.exit = msg.askyesno("Face Recognition", "Are you want to Exit.", parent = self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def att_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def dev(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()