from tkinter import *
from PIL import Image, ImageTk
class Developer():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Developers Details")

        title_label= Label(self.root, text="DEVELOPERS  DETAILS", font=("Times 40 bold"), bg = "navyblue", fg = "white")
        title_label.place(x=0, y=0, width=1530, height=55)

        #img = Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\dev_bg.png")
        img=Image.open(r"E:/python/Face_Recognition_Attendace_System/images/dev_bg.png")
        img = img.resize((1530, 800), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=55, width=1530, height=750)

        # ======================================= Devloper-1 ==================================================
        frame1 = Frame(f_lbl, bd =2, bg = "cadetblue2")
        frame1.place(x=100, y=80, width=400, height=440)

        Label(frame1, text="Developer - 1", font=("Times 25 bold underline"), bg = "cadetblue2").place(x=100, y = 5)
        
        #dev_img_1 = Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\akash.png")
        dev_img_1 = Image.open(r"E:/python/Face_Recognition_Attendace_System/images/akash.png")
        dev_img_1 = dev_img_1.resize((150, 150), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(dev_img_1)
        dev_lbl_1 = Label(frame1, image=self.photoimg1)
        dev_lbl_1.place(x=120, y=65)
        
        dev_details_1 = Label(frame1, text="Name:\nCourse:\nBranch:\nSemester:\nContact:\n", bg = "cadetblue2",
                                    fg = "darkblue", font=("Times 20 bold"))
        dev_details_1.place(x = 50, y = 250)

        dev_data_1 = Label(frame1, text="Akash Dhiman\nB.Tech.\nIT\n7th\n+91 9758960541", bg = "cadetblue2",
                                    fg = "red", font=("Times 20 bold"))
        dev_data_1.place(x = 170, y = 250)

        # ======================================= Devloper-2 ==================================================
        frame2 = Frame(f_lbl, bd =2, bg = "springgreen1")
        frame2.place(x=570, y=80, width=400, height=440)

        Label(frame2, text="Developer - 2", font=("Times 25 bold underline"), bg = "springgreen1").place(x=100, y = 5)
        
        #dev_img_2 = Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\shubham.jpg")
        dev_img_2 = Image.open(r"E:/python/Face_Recognition_Attendace_System/images/shubham.jpg")
        dev_img_2 = dev_img_2.resize((150, 150), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(dev_img_2)
        dev_lbl_2 = Label(frame2, image=self.photoimg2)
        dev_lbl_2.place(x=120, y=65)
        
        dev_details_2 = Label(frame2, text="Name:\nCourse:\nBranch:\nSemester:\nContact:\n", bg = "springgreen1",
                                    fg = "darkblue", font=("Times 20 bold"))
        dev_details_2.place(x = 50, y = 250)

        dev_data_2 = Label(frame2, text="Shubham Saini\nB.Tech.\nIT\n7th\n+91 7669454417", bg = "springgreen1",
                                    fg = "red", font=("Times 20 bold"))
        dev_data_2.place(x = 170, y = 250)
        #=======================================================================================================

        # ======================================= Devloper-3 ==================================================
        frame3 = Frame(f_lbl, bd =2, bg = "Khaki")
        frame3.place(x=1040, y=80, width=400, height=440)

        Label(frame3, text="Developer - 3", font=("Times 25 bold underline"), bg = "Khaki").place(x=100, y = 5)
        
        #dev_img_3 = Image.open(r"D:\FINAL YEAR PROJECT\IMAGES\deepanshu.png")
        dev_img_3 = Image.open(r"E:/python/Face_Recognition_Attendace_System/images/deepanshu.png")
        dev_img_3 = dev_img_3.resize((150, 150), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(dev_img_3)
        dev_lbl_3 = Label(frame3, image=self.photoimg3)
        dev_lbl_3.place(x=120, y=65)
        
        dev_details_3 = Label(frame3, text="Name:\nCourse:\nBranch:\nSemester:\nContact:\n", bg = "Khaki",
                                    fg = "darkblue", font=("Times 20 bold"))
        dev_details_3.place(x = 40, y = 250)

        dev_data_3 = Label(frame3, text="Deepanshu Kumar\nB.Tech.\nIT\n7th\n+91 6399383578", bg = "Khaki",
                                    fg = "red", font=("Times 20 bold"))
        dev_data_3.place(x = 160, y = 250)
        #=======================================================================================================

if __name__=="__main__":
    root = Tk()    
    obj = Developer(root)
    root.mainloop()