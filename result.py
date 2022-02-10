from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class resultClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Result")
        self.root.geometry("900x550+310+140")
        self.root.resizable(False,False)
        self.root.config(bg='white')
        self.root.iconbitmap('image/result.ico')
        self.root.grab_set()
        self.root.focus_force()

        self.var_rollno=StringVar()
        self.var_odia=StringVar()
        self.var_eng=StringVar()
        self.var_sans=StringVar()
        self.var_math=StringVar()
        self.var_gsc=StringVar()
        self.var_ssc=StringVar()

        global con,cur
        con = sqlite3.connect(database='management.db')
        cur = con.cursor()

        # ========== title ============
        saerch_frame = Label(self.root, text="Manage Student Result",bg="cyan3",font=("goudy old style",25,"bold"))
        saerch_frame.place(x=0,y=0,height=50,relwidth=1)

        # =========== Entry and Label =============
        lbl_rollno = Label(self.root,text="Roll No.",bg="white",font=("goudy old style",15,"bold"))
        lbl_rollno.place(x=30,y=70)

        lbl_odia = Label(self.root,text="Odia",bg="white",font=("goudy old style",15,"bold"))
        lbl_odia.place(x=30,y=120)

        lbl_eng = Label(self.root,text="English",bg="white",font=("goudy old style",15,"bold"))
        lbl_eng.place(x=30,y=170)

        lbl_sans = Label(self.root,text="Sanskrit/Hindi",bg="white",font=("goudy old style",15,"bold"))
        lbl_sans.place(x=30,y=220)

        lbl_math = Label(self.root,text="Mathematics",bg="white",font=("goudy old style",15,"bold"))
        lbl_math.place(x=30,y=270)

        lbl_gsc = Label(self.root,text="General Science",bg="white",font=("goudy old style",15,"bold"))
        lbl_gsc.place(x=30,y=320)

        lbl_ssc = Label(self.root,text="Social Science",bg="white",font=("goudy old style",15,"bold"))
        lbl_ssc.place(x=30,y=370)

        txt_rollno = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_rollno)
        txt_rollno.place(x=230,y=70)

        txt_odia = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_odia)
        txt_odia.place(x=230,y=120)

        txt_eng = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_eng)
        txt_eng.place(x=230,y=170)

        txt_sans = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_sans)
        txt_sans.place(x=230,y=220)

        txt_math = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_math)
        txt_math.place(x=230,y=270)

        txt_gsc = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_gsc)
        txt_gsc.place(x=230,y=320)

        txt_ssc = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_ssc)
        txt_ssc.place(x=230,y=370)

        # ============= Button==============
        save_btn =Button(self.root,text='Save',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",20,"bold"),activeforeground="red",command=self.save)
        save_btn.place(x=20,y=430,height=40,width=120)

        clear_btn =Button(self.root,text='Get Data',cursor="hand2",bd=3,bg='#607d8b',font=("times new roman",20,"bold"),activeforeground="red",command=self.get_date)
        clear_btn.place(x=160,y=430,height=40,width=120)

        save_btn =Button(self.root,text='Update',cursor="hand2",bd=3,bg='green3',font=("times new roman",20,"bold"),activeforeground="red",command=self.update)
        save_btn.place(x=300,y=430,height=40,width=120)

        clear_btn =Button(self.root,text='Clear',cursor="hand2",bd=3,bg='snow3',font=("times new roman",20,"bold"),activeforeground="red",command=self.clear)
        clear_btn.place(x=160,y=490,height=40,width=120)

        # ===== image ======
        self.cat_image2 = Image.open('image/result.jpeg')
        self.cat_image2 = self.cat_image2.resize((400,400),Image.ANTIALIAS)
        self.cat_image2 = ImageTk.PhotoImage(self.cat_image2)

        lbl_image2 = Label(self.root,image =self.cat_image2,bd=0)
        lbl_image2.place(x=470,y=100)

    # =========== FUNCTION =============
    
    def save(self):
        try:
            if self.var_rollno.get() =='' or self.var_odia.get() =='' or self.var_eng.get() =='' or self.var_sans.get() =='' or self.var_math.get() =='' or self.var_gsc.get() =='' or  self.var_ssc.get() =='':
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select *from student where rollno=?",(self.var_rollno.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","This Rollno is not exists,Please Enter a correct Roll No",parent=self.root)
                else:
                    cur.execute("Select * from result where rollno=?",(self.var_rollno.get(),))
                    row = cur.fetchone()
                    if row!= None:
                        messagebox.showerror("Error","This Rollno is already exists,try different",parent=self.root)
                    else:
                        self.secured = int(self.var_odia.get())+int(self.var_eng.get())+int(self.var_sans.get())+int(self.var_math.get())+ int(self.var_gsc.get())+int(self.var_ssc.get())
                        self.percent =(self.secured/6)
                        self.percent = round(self.percent,2)
                        self.total = 600
                        cur.execute("Insert into  result (rollno,odia,eng,sans,math,gsc,ssc,total,secured,percentage) values(?,?,?,?,?,?,?,?,?,?)",(
                            self.var_rollno.get(),
                            self.var_odia.get(),
                            self.var_eng.get(),
                            self.var_sans.get(),
                            self.var_math.get(),
                            self.var_gsc.get(),
                            self.var_ssc.get(),
                            self.total,
                            self.secured,
                            self.percent
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Result is Added Successfully ",parent=self.root)
                        self.clear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)
    def get_date(self):
        try:
            if self.var_rollno.get() == '':
                messagebox.showerror("Error","Enter Roll No. to display the result.",parent=self.root)
            else:
                cur.execute("Select * from result where rollno= ?",(self.var_rollno.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please Enter a Valid Roll No.",parent=self.root)
                else:
                    cur.execute("Select * from result where rollno=?",(self.var_rollno.get(),))
                    row = cur.fetchone()
                    if row!= None:
                        # self.var_rollno.set(row[0])
                        self.var_odia.set(row[1])
                        self.var_eng.set(row[2])
                        self.var_sans.set(row[3])
                        self.var_math.set(row[4])
                        self.var_gsc.set(row[5])
                        self.var_ssc.set(row[6])
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)
        
    def update(self):
        try:
            if self.var_rollno.get() =="":
                messagebox.showerror("Error","Roll No. must be required",parent=self.root)
            else:
                self.secured = int(self.var_odia.get())+int(self.var_eng.get())+int(self.var_sans.get())+int(self.var_math.get())+ int(self.var_gsc.get())+int(self.var_ssc.get())
                self.percent =(self.secured/6)
                self.percent = round(self.percent,2)
                self.total = 600
                cur.execute("update result set odia=?,eng=?,sans=?,math=?,gsc=?,ssc=?,total=?,secured=?,percentage=? where rollno=?",(
                            self.var_odia.get(),
                            self.var_eng.get(),
                            self.var_sans.get(),
                            self.var_math.get(),
                            self.var_gsc.get(),
                            self.var_ssc.get(),
                            self.total,
                            self.secured,
                            self.percent,
                         self.var_rollno.get()))
                con.commit()
                messagebox.showinfo("Success",f"student {str(self.var_rollno.get())} Updated Successfully ",parent=self.root)
                self.clear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def clear(self):
        self.var_rollno.set('')
        self.var_odia.set('')
        self.var_eng.set('')
        self.var_sans.set('')
        self.var_math.set('')
        self.var_gsc.set('')
        self.var_ssc.set('')

if __name__ == "__main__":
    root = Tk()
    resultClass(root)
    root.mainloop()