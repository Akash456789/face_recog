from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET", font=("time new roman", 35, "bold"), bg="red" , fg="white",bd=4, relief=RIDGE)
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img=Image.open(r"E:/python/Face_Recognition_Attendace_System/images/train.jpg")
        #img=Image.open("D:/face_recon/images/pic2.png")
        img=img.resize((1530,370),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=45, width=1530, height=335)

        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("time new roman", 30, "bold"), bg="blue" , fg="white")
        b1_1.place(x=620,y=380,width=300,height=70)



        img1=Image.open(r"E:/python/Face_Recognition_Attendace_System/images/train1.jpg")
        #img=Image.open("D:/face_recon/images/pic2.png")
        img1=img1.resize((1530,355),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0,y=440, width=1530, height=355)

    def train_classifier(self):
        data_dir=("E:\python\Face_Recognition_Attendace_System\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("E:\python\Face_Recognition_Attendace_System\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

        

if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
