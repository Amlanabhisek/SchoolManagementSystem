from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3

class view_resultClass:
    def __init__(self,root):
        self.root = root
        self.root.title("view_result")
        self.root.geometry("1140x600+300+140")
        self.root.resizable(False,False)
        self.root.config(bg='white')
        self.root.iconbitmap('image/viewresult.ico')
        self.root.grab_set()
        self.root.focus_force()

        # =========  Variable ===========
        self.var_rollno= StringVar()

        global con,cur
        con = sqlite3.connect(database='management.db')
        cur = con.cursor()

        # ========== title ============
        saerch_frame = Label(self.root, text="View Student Result",bg="cyan3",font=("goudy old style",25,"bold"))
        saerch_frame.place(x=0,y=0,height=50,relwidth=1)

        # entry field and label
        lbl_rollno = Label(self.root,text="Enter Roll No.",bg="white",font=("goudy old style",15,"bold"))
        lbl_rollno.place(x=370,y=80)

        txt_rollno= Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_rollno)
        txt_rollno.place(x=550,y=80)

        # ============= BUTTON =============
        Button(self.root,text='Show',cursor="hand2",bd=3,bg='green3',font=("times new roman",20,"bold"),activeforeground="red",command=self.show).place(x=320,y=140,height=40,width=110)
        Button(self.root,text='Delete',cursor="hand2",bd=3,bg='red',font=("times new roman",20,"bold"),activeforeground="red",command=self.delete).place(x=510,y=140,height=40,width=120)
        Button(self.root,text='Clear',cursor="hand2",bd=3,bg='SlateGray2',font=("times new roman",20,"bold"),activeforeground="red",command=self.clear).place(x=710,y=140,height=40,width=120)
        
        # ========== display result=========
        lbl_rollno = Label(self.root,text="Roll No \t :",bg="white",font=("goudy old style",15,"bold")).place(x=110,y=220)
        lbl_name = Label(self.root,text="Name\t :",bg="white",font=("goudy old style",15,"bold")).place(x=110,y=260)
        lbl_class = Label(self.root,text="Class \t :",bg="white",font=("goudy old style",15,"bold")).place(x=110,y=300)

        self.res_rollno = Label(self.root,bg="white",font=("goudy old style",15,"bold"))
        self.res_rollno.place(x=230,y=220)
        self.res_name = Label(self.root,bg="white",font=("goudy old style",15,"bold"))
        self.res_name.place(x=230,y=260)
        self.res_class = Label(self.root,bg="white",font=("goudy old style",15,"bold"))
        self.res_class.place(x=230,y=300)

        lbl_odia = Label(self.root,text="ODIA",bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE).place(x=30,y=350,width=120,height=60)
        lbl_eng = Label(self.root,text="ENGLISH",bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE).place(x=150,y=350,width=120,height=60)
        lbl_sans = Label(self.root,text="SANSKRIT",bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE).place(x=270,y=350,width=120,height=60)
        lbl_math = Label(self.root,text="MATH",bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE).place(x=390,y=350,width=120,height=60)
        lbl_gsc = Label(self.root,text="G.SCIENCE",bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE).place(x=510,y=350,width=120,height=60)
        lbl_ssc = Label(self.root,text="S.SCIENCE",bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE).place(x=630,y=350,width=120,height=60)
        lbl_total = Label(self.root,text="TOTAL",bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE).place(x=750,y=350,width=120,height=60)
        lbl_secured = Label(self.root,text="SECURED",bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE).place(x=870,y=350,width=120,height=60)
        lbl_percent = Label(self.root,text="PERCENT\n(%)",bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE).place(x=990,y=350,width=120,height=60)
        
        self.res_odia = Label(self.root,bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE)
        self.res_odia.place(x=30,y=410,width=120,height=60)
        self.res_eng = Label(self.root,bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE)
        self.res_eng.place(x=150,y=410,width=120,height=60)
        self.res_sans = Label(self.root,bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE)
        self.res_sans.place(x=270,y=410,width=120,height=60)
        self.res_math = Label(self.root,bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE)
        self.res_math.place(x=390,y=410,width=120,height=60)
        self.res_gsc = Label(self.root,bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE)
        self.res_gsc.place(x=510,y=410,width=120,height=60)
        self.res_ssc = Label(self.root,bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE)
        self.res_ssc.place(x=630,y=410,width=120,height=60)
        self.res_total = Label(self.root,bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE)
        self.res_total.place(x=750,y=410,width=120,height=60)
        self.res_secured = Label(self.root,bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE)
        self.res_secured.place(x=870,y=410,width=120,height=60)
        self.res_percent = Label(self.root,bg="white",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE)
        self.res_percent.place(x=990,y=410,width=120,height=60)

    # ======================= F U N C T I O N ============================

    def show(self):
        try:
            if self.var_rollno.get() == '':
                messagebox.showerror("Error","Enter Roll No. to display the result.",parent=self.root)
            else:
                cur.execute("Select * from result where rollno= ?",(self.var_rollno.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please Enter a Valid Roll No.",parent=self.root)
                else:
                    cur.execute("Select * from student where rollno=?",(self.var_rollno.get(),))
                    det = cur.fetchone()
                    if det!= None:
                        self.res_rollno.config(text=det[0])
                        self.res_name.config(text=det[1])
                        self.res_class.config(text=det[6])
                    cur.execute("Select * from result where rollno=?",(self.var_rollno.get(),))
                    row = cur.fetchone()
                    if row!= None:
                        self.res_odia.config(text=row[1])
                        self.res_eng.config(text=row[2])
                        self.res_sans.config(text=row[3])
                        self.res_math.config(text=row[4])
                        self.res_gsc.config(text=row[5])
                        self.res_ssc.config(text=row[6])
                        self.res_total.config(text=row[7])
                        self.res_secured.config(text=row[8])
                        self.res_percent.config(text=row[9]) 
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def clear(self):
        self.var_rollno.set('')
        self.res_rollno.config(text='')
        self.res_name.config(text='')
        self.res_class.config(text='')
        self.res_odia.config(text='')
        self.res_eng.config(text='')
        self.res_sans.config(text='')
        self.res_math.config(text='')
        self.res_gsc.config(text='')
        self.res_ssc.config(text='')
        self.res_total.config(text='')
        self.res_secured.config(text='')
        self.res_percent.config(text='')        

    def delete(self):
        try:
            if self.var_rollno.get() =="":
                messagebox.showerror("Error","First Show Result To Delete",parent=self.root)
            else:
                cur.execute("Select * from result where rollno=?",(self.var_rollno.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showinfo("Error","Invalid Roll No.",parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm','Do you really Want to Delete the record',parent=self.root)
                    if op == True:
                        cur.execute("delete from result where rollno=?",(self.var_rollno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete",f"Result Of {str(self.var_rollno.get())} Deleted Successfully ",parent=self.root)
                        self.clear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

if __name__ == "__main__":
    root = Tk()
    view_resultClass(root)
    root.mainloop()