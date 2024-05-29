from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
from student import student
from attend import Attendance
import webbrowser
from app import app

class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")


        # first image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\face.jpg")
        img=img.resize((400,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)

        # second image
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\three.jpg")
        img1=img1.resize((600,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=600,height=130)

        # third image
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\college.jpg")
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
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM ", font=("times new roman",35,"bold",),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        
        
        
        #==================time=====================
        def time():
            string= strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
            
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time() 
             
        #student button
        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\Rahul.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        #first button
        b1=Button(bg_img,image=self.photoimg4,command=self.Student_Details,cursor="hand2")
        b1.place(x=200,y=75,width=200,height=200)

        b1_1=Button(bg_img,text="Student_Details",command=self.Student_Details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=250,width=200,height=30)


        #detect button
        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\face.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        #second button
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.app_data)
        b1.place(x=550,y=78,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.app_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=550,y=250,width=200,height=30)


        #Student Entry button
        img6=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\attendance.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        #Third button
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_attendance)
        b1.place(x=900,y=78,width=200,height=200)

        b1_1=Button(bg_img,text="Student Entry",cursor="hand2",command=self.open_attendance,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=900,y=250,width=200,height=30)        
        
        #Photo button
        img9=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\images.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        #Fifth button
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=200,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=485,width=200,height=30)
        
        #Attendance button
        img10=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\Attendance1.jpeg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        #Fifth button
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.attendance_data)
        b1.place(x=550,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=550,y=485,width=200,height=30)

        #Exit button
        img11=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face recognition\college images\exit.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        #Fifth button
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=900,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=900,y=485,width=200,height=30)
        
        
    def open_img(self):
        os.startfile(r"C:\Users\HP\OneDrive\Desktop\Face recognition\static\faces")  
        
    def open_attendance(self):
        os.startfile(r"C:\Users\HP\OneDrive\Desktop\Face recognition\Attendance")  
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this software",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
            
        
        
        # ==================================function buttons==============================================

    def Student_Details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)       
       
                   
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 
    
    def app_data(self):
        #url = "http://127.0.0.1:5000/"
        url="http://127.0.0.1:5000/"
        webbrowser.open(url)
        app.run(debug=True,port=5000)
        
  
        
        
    
    
        














        











if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()