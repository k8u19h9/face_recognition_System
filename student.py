from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import filedialog
import os


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        

        #===========================variables======================

        self.var_Dep=StringVar()
        self.var_Course=StringVar()
        self.var_Name=StringVar()
        self.var_father=StringVar()
        self.var_mother=StringVar()
        self.var_Session=StringVar()
        self.var_Sem=StringVar()
        self.var_Id=StringVar()
        self.var_Gender=StringVar()
        self.var_Phone_No=StringVar()
        self.var_DOB=StringVar()
        self.var_Email=StringVar()
        self.var_Address=StringVar()
        self.var_Teacher=StringVar()
    
        # first image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\student.jpg")
        img=img.resize((400,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)

        # second image
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\meeting.jpg")
        img1=img1.resize((600,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=600,height=130)

        # third image
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\class.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # background image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1366,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM ", font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1366,height=50)

        #============================================Frame============================================
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1330,height=650)

        #Left Label Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student_Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=550)

        img_left=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\class.jpg")
        img_left=img_left.resize((645,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=645,height=130)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=645,height=100)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",8,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Dep,font=("times new roman",8,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Vocational","IT","Commerce And Business Administration","Mathematics","Chemistry","Physical Education","Other")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course        
        course_label=Label(current_course_frame,text="Course",font=("times new roman",8,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_entry=ttk.Entry(current_course_frame,textvariable=self.var_Course,width=20,font=("times new roman",12,"bold"))
        course_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Session
        session_label=Label(current_course_frame,text="Session",font=("times new roman",8,"bold"),bg="white")
        session_label.grid(row=1,column=0,padx=10,sticky=W)

        session_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Session,font=("times new roman",8,"bold"),state="readonly",width=20)
        session_combo["values"]=("Select Session","2023-2024","2024-2025","2025-2026","2026-2027")
        session_combo.current(0)
        session_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",8,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Sem,font=("times new roman",8,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=240,width=645,height=250)

        #student id
        studentID_label=Label(class_student_frame,text="StudentID:",font=("times new roman",8,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=3,pady=3,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_Id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=3,pady=3,sticky=W)

        #student name
        student_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",8,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=3,pady=3,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_Name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=3,pady=3,sticky=W)

        #Father_Name
        Father_label=Label(class_student_frame,text="Father Name:",font=("times new roman",8,"bold"),bg="white")
        Father_label.grid(row=1,column=0,padx=3,pady=3,sticky=W)

        Father_entry=ttk.Entry(class_student_frame,textvariable=self.var_father,width=20,font=("times new roman",12,"bold"))
        Father_entry.grid(row=1,column=1,padx=3,pady=3,sticky=W)

        #Mother_Name
        Mother_label=Label(class_student_frame,text="Mother Name:",font=("times new roman",8,"bold"),bg="white")
        Mother_label.grid(row=1,column=2,padx=3,pady=3,sticky=W)

        Mother_entry=ttk.Entry(class_student_frame,textvariable=self.var_mother,width=20,font=("times new roman",12,"bold"))
        Mother_entry.grid(row=1,column=3,padx=3,pady=3,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",8,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=3,pady=3,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Gender,font=("times new roman",8,"bold"),state="readonly",width=24)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=3,pady=10,sticky=W)


        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",8,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=3,pady=3,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=3,pady=3,sticky=W)

        #EMail
        Email_label=Label(class_student_frame,text="EMail:",font=("times new roman",8,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=3,pady=3,sticky=W)

        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_Email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=3,pady=3,sticky=W)

        #phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",8,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=3,pady=3,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_Phone_No,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=3,pady=3,sticky=W)

        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",8,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=3,pady=3,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_Address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=3,pady=3,sticky=W)

        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",8,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=3,pady=3,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_Teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=3,pady=3,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0,padx=5,pady=3,sticky=W)

        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=5,column=1,padx=5,pady=3,sticky=W)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=1,y=190,width=800,height=35)

        #save button
        save_button=Button(btn_frame,text="Save",command=self.add_data,width=22,font=("times new roman",8,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        #Update button
        update_button=Button(btn_frame,text="Update",command=self.update_data,width=22,font=("times new roman",8,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

        #delete button
        delete_button=Button(btn_frame,text="Delete",command=self.delete_data,width=22,font=("times new roman",8,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)
        
        #Reset button
        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",8,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)
                
        #Right Label Frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student_Details",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=680,y=10,width=635,height=550)

        img_right=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\college.jpg")
        img_right=img_right.resize((645,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(RIGHT_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=620,height=130)

        # ==================Search System============================    

        search_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=128,width=619,height=50)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",10,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=3,pady=1,sticky=W)
        
        #search
        self.var_com_search=StringVar()      
    

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",8,"bold"),state="readonly",width=20)
        search_combo["values"]=("Student_Id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)
        
        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=3,padx=3,pady=0,sticky=W)
        
        

        #Search button
        search_button=Button(search_frame,command=self.search_data,text="Search",width=12,font=("times new roman",8,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=4,padx=4)

        #Show All button
        showAll_button=Button(search_frame,command=self.fetch_data,text="Show All",width=12,font=("times new roman",8,"bold"),bg="blue",fg="white")
        showAll_button.grid(row=0,column=5,padx=4)

        # ==================table frame=======================
        table_frame=Frame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=619,height=285)


        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Name","Father Name","Mother Name","Session","Sem","Id","Gender","Phone No","DOB","Email","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Father Name",text="Father Name")
        self.student_table.heading("Mother Name",text="Mother Name")
        self.student_table.heading("Session",text="Session")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="Student ID")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")        
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Father Name",width=100)
        self.student_table.column("Mother Name",width=100)
        self.student_table.column("Session",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)        
        self.student_table.column("Photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # =========================function declaration============================================================
    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_Dep.get(),
                                                                                            self.var_Course.get(),
                                                                                            self.var_Name.get(),
                                                                                            self.var_father.get(),
                                                                                            self.var_mother.get(),
                                                                                            self.var_Session.get(),
                                                                                            self.var_Sem.get(),
                                                                                            self.var_Id.get(),
                                                                                            self.var_Gender.get(),
                                                                                            self.var_Phone_No.get(),
                                                                                            self.var_DOB.get(),
                                                                                            self.var_Email.get(),
                                                                                            self.var_Address.get(),
                                                                                            self.var_Teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)    







    #==========================fetch data=================================================
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognizer")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()

         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close()

    #=====================================get cursor==================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Dep.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Name.set(data[2]),
        self.var_father.set(data[3]),
        self.var_mother.set(data[4]),
        self.var_Session.set(data[5]),
        self.var_Sem.set(data[6]),
        self.var_Id.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_Phone_No.set(data[9]),
        self.var_DOB.set(data[10]),
        self.var_Email.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_Teacher.set(data[13]),
        self.var_radio1.set(data[14])
            
    #update function
    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Name=%s,Father_Name=%s,Mother_Name=%s,Session=%s,Semester=%s,Gender=%s,Phone_No=%s,DOB=%s,Email=%s,Address=%s,Teacher=%s,PhotoSampleStatus=%s where Student_Id=%s",(
                                                                                                                                                                                                                                                 self.var_Dep.get(),
                                                                                                                                                                                                                                                 self.var_Course.get(),
                                                                                                                                                                                                                                                 self.var_Name.get(),
                                                                                                                                                                                                                                                 self.var_father.get(),
                                                                                                                                                                                                                                                 self.var_mother.get(),     
                                                                                                                                                                                                                                                 self.var_Session.get(),
                                                                                                                                                                                                                                                 self.var_Sem.get(),
                                                                                                                                                                                                                                                 self.var_Gender.get(),
                                                                                                                                                                                                                                                 self.var_Phone_No.get(),
                                                                                                                                                                                                                                                 self.var_DOB.get(),
                                                                                                                                                                                                                                                 self.var_Email.get(),
                                                                                                                                                                                                                                                 self.var_Address.get(),
                                                                                                                                                                                                                                                 self.var_Teacher.get(),
                                                                                                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                                                                                                 self.var_Id.get()                                    
                                                                                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update Completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        
                    
        
    #Delete function
    def delete_data(self):
        if self.var_Id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
                       
        
    #reset function
    def reset_data(self):
        self.var_Dep.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Name.set("")
        self.var_father.set("")
        self.var_mother.set("")
        self.var_Session.set("Select Session")
        self.var_Sem.set("Select Semester")
        self.var_Id.set("")
        self.var_Gender.set("Male")
        self.var_Phone_No.set("")
        self.var_DOB.set("")
        self.var_Email.set("")
        self.var_Address.set("")
        self.var_Teacher.set("")
        self.var_radio1.set("")
        
        
        
    # ===============search data=========================================
    
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select Option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student where " +str(self.var_com_search.get())+" LIKE '%" +str(self.var_search.get())+ "%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                        
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
                
                 
        
   

        
        
        
        
    

if __name__ == "__main__":
    root=Tk( )
    obj=student(root)
    root.mainloop()
