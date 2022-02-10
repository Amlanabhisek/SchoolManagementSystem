from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from teacher import teacherClass
from student import studentClass
from details import detailsClass
from viewresult import view_resultClass
from result import resultClass
from library import libraryClass
import sqlite3

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Inventory management System")
        self.root.geometry("1535x790+-10+0")
        self.root.resizable(False,False)
        self.root.config(bg='snow2')
        self.root.iconbitmap('image/school.ico')
        self.create_db()
    
        # -------TITLE------
        self.wel =Label(root,anchor=W,font=("times new roman",30,"bold"),bg="#010CA8")
        self.wel.place(x=0,y=0,relwidth=1,height=70)

        self.SliderLabel = Label(self.wel, text='Welcome To School Management System',font=("times new roman",25,"bold"),bg="#010CA8",fg='white',padx=20,justify=CENTER)
        self.SliderLabel.place(x=0,y=10,relwidth=1)

        # Clock
        self.lbl_clock=Label(self.wel,borderwidth=4,font=("Gintronic", 13, "bold"),bg="#010CA8",fg="white")
        self.lbl_clock.place(x=15,y=7)
        self.clockTick()

        self.menu_frame  = LabelFrame(self.root, text="Menus",bg="white",font=("goudy old style",20,"bold"),bd=2)
        self.menu_frame .place(x=20,y=80,height=110,width=1500)

        lbtn_course =Button(self.menu_frame,text='Teacher',cursor="hand2",bd=3,bg='royalblue1',font=("times new roman",20,"bold"),command=self.teacher).place(x= 20,y= 10,width=170,height=40)
        lbtn_student =Button(self.menu_frame,text='Student',cursor="hand2",bd=3,bg='royalblue1',font=("times new roman",20,"bold"),command=self.student).place(x=210,y=10,width=170,height=40)
        lbtn_student =Button(self.menu_frame,text='Library',cursor="hand2",bd=3,bg='royalblue1',font=("times new roman",20,"bold"),command=self.library).place(x=400,y=10,width=170,height=40)
        lbtn_resultt =Button(self.menu_frame,text='Result',cursor="hand2",bd=3,bg='royalblue1',font=("times new roman",20,"bold"),command=self.result).place(x=590,y=10,width=170,height=40)
        lbtn_view_result =Button(self.menu_frame,text='View Student Result',cursor="hand2",bd=3,bg='royalblue1',font=("times new roman",20,"bold"),command=self.view_result).place(x=780,y=10,width=310,height=40)
        lbtn_logout =Button(self.menu_frame,text='Course',cursor="hand2",bd=3,bg='royalblue1',font=("times new roman",20,"bold"),command=self.details).place(x=1110,y=10,width=170,height=40)
        lbtn_exit =Button(self.menu_frame,text='Exit',cursor="hand2",bd=3,bg='royalblue1',font=("times new roman",20,"bold"),command=self.exit).place(x= 1300,y=10,width=170,height=40)

        # Image
        self.cat_image = Image.open('image/bg.png')
        self.cat_image = self.cat_image.resize((1000,450),Image.ANTIALIAS)
        self.cat_image = ImageTk.PhotoImage(self.cat_image)

        lbl_image = Label(self.root,image =self.cat_image,bd=0)
        lbl_image.place(x=300,y=200)

        # details
        self.lbl_details =Label(self.root,bg='white')
        self.lbl_details.place(x=0,y=650,relwidth=1,height=200)

        self.lbl_teacher = Label(self.lbl_details, text="Total Teacher \n [0]",font=("goudy old style",20,"bold"),bg="seagreen",fg='white',bd=5,relief=RIDGE)
        self.lbl_teacher.place(x=50, y=20,height=90,width=270)
        self.lbl_student = Label(self.lbl_details, text="Total Student \n [0]",font=("goudy old style",20,"bold"),bg="seagreen3",fg='white',bd=5,relief=RIDGE)
        self.lbl_student.place(x=340, y=20,height=90,width=270)
        self.lbl_class = Label(self.lbl_details, text="Total Class \n [0]",font=("goudy old style",20,"bold"),bg="#ff5722",fg='white',bd=5,relief=RIDGE)
        self.lbl_class.place(x=630, y=20,height=90,width=270)
        self.lbl_result = Label(self.lbl_details, text="Total Result \n [0]",font=("goudy old style",20,"bold"),bg="#ff5722",fg='white',bd=5,relief=RIDGE)
        self.lbl_result.place(x=920, y=20,height=90,width=270)
        self.lbl_books = Label(self.lbl_details, text="Total Books \n [0]",font=("goudy old style",20,"bold"),bg="blue1",fg='white',bd=5,relief=RIDGE)
        self.lbl_books.place(x=1210, y=20,height=90,width=270)

        self.update_details()

    def teacher(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = teacherClass(self.new_win)

    def student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def view_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = view_resultClass(self.new_win)

    def details(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = detailsClass(self.new_win)

    def library(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = libraryClass(self.new_win)
       
    def exit(self):
        res = messagebox.askquestion("Confirm","Do you Want to exit ?")
        if res == 'yes':
            self.root.destroy()

    def update_details(self):
        try:
            self.con = sqlite3.connect(database='management.db')
            self.cur = self.con.cursor()
            self.cur.execute('select * from teacher')
            res = self.cur.fetchall()
            self.lbl_teacher.config(text=f'Total Teacher [{str(len(res))}]')

            self.cur.execute('select * from student')
            res = self.cur.fetchall()
            self.lbl_student.config(text=f'Total student [{str(len(res))}]')

            self.cur.execute('select * from class')
            res = self.cur.fetchall()
            self.lbl_class.config(text=f'Total class [{str(len(res))}]')

            self.cur.execute('select * from library')
            res = self.cur.fetchall()
            self.lbl_books.config(text=f'Total book [{str(len(res))}]')

            self.cur.execute('select * from result')
            res = self.cur.fetchall()
            self.lbl_result.config(text=f'Total result [{str(len(res))}]')
            self.lbl_result.after(200,self.update_details)
        except Exception as e:
            pass

    def clockTick(self):
        self.time_string=time.strftime('%H:%M:%S %p')
        self.date_string=time.strftime('%d:%m:%Y')
        self.lbl_clock.config(text='Date: '+self.date_string+"\n"+'Time: '+self.time_string)
        self.lbl_clock.after(200,self.clockTick)

    def create_db(self):
        self.con = sqlite3.connect(database=r'management.db')
        self.cur = self.con.cursor()

        # teacher table ( "teacherid","name","gender","contact","email","dob","qualification","joiningdate","state","city","pincode","designation","address")
        self.cur.execute("CREATE TABLE IF NOT EXISTS teacher(tid INTEGER PRIMARY KEY  AUTOINCREMENT,name text,gender text,contact text,email text,dob text,qualification text,doj text,state text,city text,pincode text,designation text,address texts)")
        self.con.commit()

        # # student table  ("rollno","name","gender","contact","email","dob","class","admissiondate","state","city","pincode","address")
        self.cur.execute("CREATE TABLE IF NOT EXISTS student(rollno INTEGER PRIMARY KEY  AUTOINCREMENT,name text,gender text,contact text,email text,dob text,class text,admissiondate text,state text,city text,pincode text,address texts)")
        self.con.commit()

        # class table
        self.cur.execute("CREATE TABLE IF NOT EXISTS class(cid INTEGER PRIMARY KEY  AUTOINCREMENT,cname text)")
        self.con.commit()

        # library table
        self.cur.execute("CREATE TABLE IF NOT EXISTS library(bno INTEGER PRIMARY KEY  AUTOINCREMENT,bname text,btype text,quantity integer,description text)")
        self.con.commit()

        # issue book table (ibno,ibname,srollno,sname,idate)
        self.cur.execute("CREATE TABLE IF NOT EXISTS issuebook(ibno INTEGER PRIMARY KEY  AUTOINCREMENT,ibname text,srollno text,sname text,idate integer)")
        self.con.commit()
        
        # result table
        self.cur.execute("CREATE TABLE IF NOT EXISTS result(rollno INTEGER PRIMARY KEY  AUTOINCREMENT,odia text,eng text,sans text,math text,gsc text,ssc text,total text,secured text,percentage text)")
        self.con.commit()

if __name__ == "__main__":
    root = Tk()
    IMS(root)
    root.mainloop()