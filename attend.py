# import re
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Pannel")

        #-----------Variables-------------------
               
        self.var_attend_id=StringVar()
        self.var_attend_Name=StringVar()
        self.var_Date=StringVar()
        self.var_Father_Name=StringVar()
        self.var_Course=StringVar()
        self.var_sem=StringVar()
        self.var_status=StringVar()

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\Attendance1.jpeg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\bg.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        

        # ==================================Text boxes and Combo Boxes====================

        #Attendance id
        studentId_label = Label(left_frame,text="AttendanceId:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(left_frame,textvariable=self.var_attend_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Name
        student_roll_label = Label(left_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_attend_Name,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Father_Name
        student_name_label = Label(left_frame,text="Father Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_Father_Name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)


        #Semester
        time_label = Label(left_frame,text="Semester:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        semester_combo=ttk.Combobox(left_frame,font=("times new roman",13,"bold"),textvariable=self.var_sem,state="readonly",width=16)
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_Date,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        #Course
        course_label = Label(left_frame,text="Course:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        course_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        course_entry = ttk.Entry(left_frame,textvariable=self.var_Course,width=15,font=("verdana",12,"bold"))
        course_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_status,width=13,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        # ===============================Table Sql Data View==========================
        table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=150,width=635,height=310)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport_left = ttk.Treeview(table_frame,column=("attend_id","attend_Name","Date","Father_Name","Course","sem","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("attend_id",text="attend_id")
        self.attendanceReport_left.heading("attend_Name",text="attend_Name")
        self.attendanceReport_left.heading("Date",text="Date")
        self.attendanceReport_left.heading("Father_Name",text="Father_Name")
        self.attendanceReport_left.heading("Course",text="Course")
        self.attendanceReport_left.heading("sem",text="sem")
        self.attendanceReport_left.heading("status",text="status")
        self.attendanceReport_left["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport_left.column("attend_id",width=100)
        self.attendanceReport_left.column("attend_Name",width=100)
        self.attendanceReport_left.column("Date",width=100)
        self.attendanceReport_left.column("Father_Name",width=100)
        self.attendanceReport_left.column("Course",width=100)
        self.attendanceReport_left.column("sem",width=100)
        self.attendanceReport_left.column("status",width=100)
        
        self.attendanceReport_left.pack(fill=BOTH,expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
    

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #Improt button
        save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,command=self.action,text="Save",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)



        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=480)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("attend_id","attend_Name","Date","Father_Name","Course","sem","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("attend_id",text="attend_id")
        self.attendanceReport.heading("attend_Name",text="attend_Name")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Father_Name",text="Father_Name")
        self.attendanceReport.heading("Course",text="Course")
        self.attendanceReport.heading("sem",text="sem")
        self.attendanceReport.heading("status",text="status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("attend_id",width=100)
        self.attendanceReport.column("attend_Name",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Father_Name",width=100)
        self.attendanceReport.column("Course",width=100)
        self.attendanceReport.column("sem",width=100)
        self.attendanceReport.column("status",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
    # =================================update for mysql button================
    #Update button
        del_btn=Button(right_frame,command=self.update_data,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)
    #Delete button
        del_btn=Button(right_frame,command=self.delete_data,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)
        
    #fetch button
        del_btn=Button(right_frame,command=self.fetchCsv,text="FetchCsv",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)
    # ===============================update function for mysql database=================
    def update_data(self):
        if self.var_attend_id.get()=="" or self.var_Course.get=="" or self.var_attend_Name.get()=="" or self.var_Father_Name.get()=="" or self.var_Date.get()=="" or self.var_sem.get()=="" or self.var_status.get()=="status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="12345678",database="attendance")
                    mycursor = conn.cursor()
                    mycursor.execute("update attendance set attend_Name=%s,Date=%s,Father_Name=%s,Course=%s,sem=%s,status=%s where attend_id=%s",( 
                    self.var_attend_Name.get(),
                    self.var_Date.get(),
                    self.var_Father_Name.get(),
                    self.var_Course.get(),
                    self.var_sem.get(),
                    self.var_status.get(),
                    self.var_attend_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # =============================Delete Attendance form my sql============================
    def delete_data(self):
        if self.var_attend_id.get()=="":
            messagebox.showerror("Error","Attendance Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="12345678",database="attendance")
                    mycursor = conn.cursor() 
                    sql="delete from attendance where attend_id=%s"
                    val=(self.var_attend_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="12345678",database="attendance")
        mycursor = conn.cursor()

        mycursor.execute("select * from attendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============================Reset Data======================
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_Name.set("")
        self.var_Date.set("")
        self.var_Father_Name.set("")
        self.var_Course.set("")
        self.var_sem.set("")
        self.var_status.set("status")

    # =========================Fetch Data Import data ===============
    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
        
    def fetchCsv(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]

        self.var_attend_id.set(data[0]),
        self.var_attend_Name.set(data[1]),
        self.var_Date.set(data[2]),
        self.var_Father_Name.set(data[3]),
        self.var_Course.set(data[4]),
        self.var_sem.set(data[5]),
        self.var_status.set(data[6])  

     #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_attend_id.set(data[0]),
        self.var_attend_Name.set(data[1]),
        self.var_Date.set(data[2]),
        self.var_Father_Name.set(data[3]),
        self.var_Course.set(data[4]),
        self.var_sem.set(data[5]),
        self.var_status.set(data[6]) 
    #=========================================Update CSV============================

    # export upadte
    def action(self):
        if self.var_attend_id.get()=="" or self.var_Course.get=="" or self.var_attend_Name.get()=="" or self.var_Father_Name.get()=="" or self.var_Date.get()=="" or self.var_sem.get()=="" or self.var_status.get()=="status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="12345678",database="attendance")
                mycursor = conn.cursor()
                mycursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_attend_id.get(),
                self.var_attend_Name.get(),
                self.var_Date.get(),
                self.var_Father_Name.get(),
                self.var_Course.get(),
                self.var_sem.get(),
                self.var_status.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)






    








if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()