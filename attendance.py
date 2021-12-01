from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition Attendance System")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # 1st image
        img_top=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\face.jpg")
        img_top=img_top.resize((1530,800),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=46,width=1530,height=800)

         #button
        b1_1=Button(f_lbl,text="Attendance",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="dark green",fg="white")
        b1_1.place(x=1018,y=580,width=210,height=50)

        #============================attendence======================================
    def mark_attendance(self,i,r,n,d):
        with open ("E:\python\Face_Recognition_Attendace_System\index.csv","r+",newline="\n") as f:
            myDataList=f.readlines()

            entry=[]
            for line in myDataList:
                entry=line.split((","))
                
                
            if(str(i[0]) not in entry) and (str(r[0]) not in entry) and (str(n[0]) not in entry) and (str(d[0]) not in entry):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")                   
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{i[0]},{r[0]},{n[0]},{d[0]},{dtString},{d1},preset\n")
            
                
                                       

                          #============================face recognition======================================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
             

            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300))) 
              
                conn=mysql.connector.connect(host = "localhost", username = "root", password = "root5", database = "face_recognizer")
                cur=conn.cursor()

                cur.execute("select Name from student where id="+str(id))
                n=cur.fetchone()
                #n="+".join(n)
                #n=str(n)

                cur.execute("select Roll from student where id="+str(id))
                r=cur.fetchone()
                #r="+".join(r)
                #n=str(r)

                cur.execute("select Dep from student where id="+str(id))
                d=cur.fetchone()
                #d="+".join(d)
                #d=str(d)

                cur.execute("select id from student where id="+str(id))
                i=cur.fetchone()
                #i="+".join(i)
                #i=str(i)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)


               
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)  

                coord=[x,y,w,h]

            return coord
                      
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf) 
            return img
            

        faceCascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("E:\python\Face_Recognition_Attendace_System\classifier.xml")
        video_cap=cv2.VideoCapture(0) 

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION",img)

            if cv2.waitKey(1)==13:

                break
        video_cap.release()
        cv2.destroyAllWindows()
            
         
if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()