from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        conn=mysql.connector.connect(host = "localhost", username = "root", password = "root5", database = "face_recognizer")
        cur=conn.cursor()
        cur.execute("select id from student order by id desc limit 1")
        
        max_id = cur.fetchone()
        next_id = ""
        if(max_id):
            next_id =max_id[0]+1
        else:
            curr=conn.cursor()
            curr.execute("SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'face_recognizer' AND TABLE_NAME = 'student'")
            new_id = curr.fetchone()
            next_id =new_id[0]

        print("max",next_id)
        
        # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

        self.var_std_id.set(str(next_id))
        #first image

        img=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\pic6.jpg")
        #img=Image.open(r"D:\face_recon\images\pic6.jpg")
        img=img.resize((550,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0, width=550, height=130)

        #second image

        img1=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\pic7.jpg")
        #img1=Image.open(r"D:\face_recon\images\pic7.jpg")
        img1=img1.resize((550,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=550,y=0, width=530, height=130)

        #thired image

        img2=Image.open("E:\python\Face_Recognition_Attendace_System\images\pic2.png")
        #img2=Image.open(r"D:\face_recon\images\pic2.png")
        img2=img2.resize((530,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000,y=0, width=530, height=130)

        #bg image
        img3=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\bgpic1.jpg")
        #img3=Image.open(r"D:\face_recon\images\bgpic1.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("time new roman", 35, "bold"), bg="red" , fg="white",bd=4, relief=RIDGE)
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img, bd=2)
        main_frame.place(y=46, width=1530,height=650)

        #left lable frame

        Left_frame=LabelFrame(main_frame,bd=2, relief=RIDGE,text="Student Details", font=("time new roman", 12, "bold"))
        Left_frame.place(x=10,y=10, width=765,height=580)

        img_left=Image.open("E:\python\Face_Recognition_Attendace_System\images\pic5.jpg")
        #img_left=Image.open(r"D:\face_recon\images\pic5.jpg")
        img_left=img_left.resize((750,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0, width=750, height=130)

        #current course information

        current_course_frame=LabelFrame(Left_frame,bd=2, relief=RIDGE,text="current course information", font=("time new roman", 12, "bold"))
        current_course_frame.place(x=5,y=135, width=720,height=125)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("time new roman", 12, "bold"))
        dep_label.grid(row=0,column=0, padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("time new roman", 13, "bold"), width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civli","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2, pady=10,sticky=W)

        #Course
        dep_label=Label(current_course_frame,text="Course",font=("time new roman", 12, "bold"))
        dep_label.grid(row=0,column=2, padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("time new roman", 13, "bold"), width=20)
        dep_combo["values"]=("Select Course","TE","FE","SE","BE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3, padx=2, pady=10,sticky=W)

        #YEAR

        year_label=Label(current_course_frame,text="Year",font=("time new roman", 12, "bold"))
        year_label.grid(row=1,column=0, padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("time new roman", 13, "bold"), width=20)
        dep_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1, padx=2, pady=10,sticky=W)

        #semester

        semester_label=Label(current_course_frame,text="Semester",font=("time new roman", 12, "bold"))
        semester_label.grid(row=1,column=2, padx=10, sticky=W)

        semester_combo=ttk.Combobox(current_course_frame, textvariable=self.var_semester,font=("time new roman", 13, "bold"), width=20)
        semester_combo["values"]=("Select Semester","1","2","3","4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=10,sticky=W)

        #class student information

        class_student_frame=LabelFrame(Left_frame,bd=2, relief=RIDGE,text="Class Student information", font=("time new roman", 12, "bold"))
        class_student_frame.place(x=5,y=250, width=720,height=300)

        #studentID

        studentId_label=Label(class_student_frame,text="StudentID:",font=("time new roman", 12, "bold"))
        studentId_label.grid(row=0,column=0, padx=10,pady=5, sticky=W)
        studentID_entry=ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20,font=("time new roman", 12, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #studentName
        studentname_label=Label(class_student_frame,text="Student Name:",font=("time new roman", 12, "bold"))
        studentname_label.grid(row=0,column=2, padx=10,pady=5, sticky=W)
        studentName_entry=ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20,font=("time new roman", 12, "bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Division:",font=("time new roman", 12, "bold"))
        class_div_label.grid(row=1,column=0, padx=10,pady=5, sticky=W)
        #class_div_entry=ttk.Entry(class_student_frame, textvariable=self.var_div, width=20,font=("time new roman", 12, "bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_student_frame, textvariable=self.var_div,font=("time new roman", 13, "bold"), width=18)
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)



        #roll_no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("time new roman", 12, "bold"))
        roll_no_label.grid(row=1,column=2, padx=10,pady=5, sticky=W)
        roll_no_entry=ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20,font=("time new roman", 12, "bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text="Gender:",font=("time new roman", 12, "bold"))
        gender_label.grid(row=2,column=0, padx=10,pady=5, sticky=W)
        gender_combo=ttk.Combobox(class_student_frame, textvariable=self.var_gender,font=("time new roman", 13, "bold"), width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1,padx=10,pady=5,sticky=W)



        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("time new roman", 12, "bold"))
        dob_label.grid(row=2,column=2, padx=10,pady=5, sticky=W)
        dob_entry=ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20,font=("time new roman", 12, "bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email

        email_label=Label(class_student_frame,text="Email:",font=("time new roman", 12, "bold"))
        email_label.grid(row=3,column=0, padx=10,pady=5, sticky=W)
        email_entry=ttk.Entry(class_student_frame, textvariable=self.var_email, width=20,font=("time new roman", 12, "bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone_no

        phone_label=Label(class_student_frame,text="Phone No:",font=("time new roman", 12, "bold"))
        phone_label.grid(row=3,column=2, padx=10,pady=5, sticky=W)
        phone_entry=ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20,font=("time new roman", 12, "bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Addreass

        address_label=Label(class_student_frame,text="Address:",font=("time new roman", 12, "bold"))
        address_label.grid(row=4,column=0, padx=10,pady=5, sticky=W)
        address_entry=ttk.Entry(class_student_frame, textvariable=self.var_address, width=20,font=("time new roman", 12, "bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name

        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("time new roman", 12, "bold"))
        teacher_label.grid(row=4,column=2, padx=10,pady=5, sticky=W)
        teacher_entry=ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20,font=("time new roman", 12, "bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio
        self.var_radio1 = StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="Take photo sample", value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="No photo sample", value="No")
        radionbtn2.grid(row=6,column=1)

        #buttons frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19)
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)


        take_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=39)
        take_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1,text="Update Photo Sample",font=("times new roman", 12, "bold"), bg="blue", fg="white", width=39)
        update_btn.grid(row=0,column=1)


        #right lable frame

        Right_frame=LabelFrame(main_frame,bd=2, relief=RIDGE,text="Student Details", font=("time new roman", 12, "bold"))
        Right_frame.place(x=750,y=10, width=765,height=580)

        img_right=Image.open(r"E:\python\Face_Recognition_Attendace_System\images\pic4.jpg")
        #img_right=Image.open(r"D:\face_recon\images\pic4.jpg")
        img_right=img_right.resize((750,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5,y=0, width=750, height=130)

        #serach system

        Search_frame=LabelFrame(Right_frame,bd=2, relief=RIDGE,text="Search System", font=("time new roman", 12, "bold"))
        Search_frame.place(x=5,y=135, width=750,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("time new roman", 12, "bold"),bg="red", fg="white")
        search_label.grid(row=0,column=0, padx=10,pady=5, sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("time new roman", 13, "bold"), width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1, padx=2, pady=10,sticky=W)

        phone_entry=ttk.Entry(Search_frame, width=15,font=("time new roman", 12, "bold"))
        phone_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",font=("times new roman", 12, "bold"), bg="blue", fg="white", width=10)
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",font=("times new roman", 12, "bold"), bg="blue", fg="white", width=10)
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame

        table_frame=Frame(Right_frame,bd=2, relief=RIDGE,bg="white")
        table_frame.place(x=5,y=210, width=750,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("id","course","dep","year","sem","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll no")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cusor)
        self.fetch_data()

    # ---------------------- function declaration---------------------
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are mandatory to fill.", parent = self.root)
        else:
            try:
                conn=mysql.connector.connect(host = "localhost", username = "root", password = "root5", database = "face_recognizer")
                cur=conn.cursor()
                id=0
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (id,self.var_course.get(),self.var_dep.get(),  self.var_year.get(), self.var_semester.get(),
                self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(),
                self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Students details has been added Successfully.", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host = "localhost", username = "root", password = "root5", database = "face_recognizer")
        cur=conn.cursor()
        cur.execute("select * from student")
        data = cur.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        #get cursor------------------
                
    def get_cusor(self, event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content["values"]
     
        self.var_std_id.set(data[0]),
        self.var_course.set(data[1]),
        self.var_dep.set(data[2]),
        
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_std_name.set(data[5]), 
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are mandatory to fill.", parent = self.root)
        else:
            try:
                Update =messagebox.askyesno("Update", "Do You want to update this student details.", parent = self.root)
                if Update > 0:
                    conn=mysql.connector.connect(host = "localhost", username = "root", password = "root5", database = "face_recognizer")
                    cur=conn.cursor()
                    cur.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where id=%s",
                    (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_name.get(),
                     self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(),self.var_email.get(),
                    self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get()))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success", "Student details update Successfully.", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student ID must be required.", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want this Student Data.", parent = self.root)
                if delete > 0:
                    conn=mysql.connector.connect(host = "localhost", username = "root", password = "root5", database = "face_recognizer")
                    cur=conn.cursor()
                    del_data = "delete from student where id=%s"
                    val = (self.var_std_id.get(),)
                    cur.execute(del_data, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted", "Successfully delete Student data.", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("") 
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are mandatory to fill.", parent = self.root)
        else:
            try:
                conn=mysql.connector.connect(host = "localhost", username = "root", password = "root5", database ="face_recognizer")
                cur=conn.cursor()
                cur.execute("select * from student")
                myresult = cur.fetchall()
                # id = 0
                for x in myresult:
                    # id+=1
                    id=self.var_std_id.get()
                    cur.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where id=%s",
                (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_name.get(),
                     self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(),self.var_email.get(),
                    self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get()))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                 
                # load face data from xml file
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scalling factor = 1.3
                    # minimum neighbot = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                        

                cap = cv2.VideoCapture(0)
                img_id =0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+= 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        #face_data_path = "D:/FINAL YEAR PROJECT/FACE DATA/stud."+str(id)+"."+str(img_id)+".jpg"
                        face_data_path ="E:\python\Face_Recognition_Attendace_System\data\student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(face_data_path,face_cropped(my_frame))
                        cv2.putText(face, str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Face Detection", "Generating Face data set Completed.")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()