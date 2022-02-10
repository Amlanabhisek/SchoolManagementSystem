from tkinter import*
from tkinter import ttk,messagebox,filedialog
import sqlite3
import pandas

class teacherClass:
    def __init__(self,root):
        self.root = root
        self.root.title("teacher Details")
        self.root.geometry("1500x610+10+140")
        self.root.resizable(False,False)
        self.root.config(bg='white')
        self.root.iconbitmap('image/teacher.ico')
        self.root.grab_set()
        self.root.focus_force()

        global con,cur
        con =sqlite3.connect(database='management.db')
        cur =con.cursor()

        # -------- Variable -------------
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_tid = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_qualification = StringVar()
        self.var_doj = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pincode = StringVar()
        self.var_designation =StringVar()

        # --------Title----------
        title = Label(self.root,text="Manage Teacher Deatils",bg="slateblue",fg="white",font=("goudy old style",30,"bold"))
        title.place(x=0,y=0,relwidth=1)

        # ------ Search frame ----------
        saerch_frame = LabelFrame(self.root, text="Search Teacher",bg="white",relief=RIDGE,font=("goudy old style",15,"bold"),bd=2)
        saerch_frame.place(x=800,y=60,height=100,width=690)

        # ------- Option---------
        cmb_search = ttk.Combobox(saerch_frame,values=("Select","TID","Email","Name","Contact","Class","Qualification","DOJ","Pincode","State","City","Pincode"),state="readonly",justify=CENTER,font=("times new roman",15,"bold"),textvariable=self.var_searchby)
        cmb_search.place(x=30,y=20,width=180)
        cmb_search.current(0)

        txt_search = Entry(saerch_frame,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_searchtxt)
        txt_search.place(x=260,y=20)

        search_btn = Button(saerch_frame,text='Search',cursor="hand2",bd=3,bg='#4caf50',font=("times new roman",20,"bold"),command=self.search)
        search_btn.place(x=520,y=10,height=40,width=140)

        # ---------- Label & Entry Field ---------------
        # ===================== col1 =====================
        lbl_tid = Label(self.root,text="ID.",bg="white",font=("goudy old style",15,"bold"))
        lbl_tid.place(x=30,y=70)

        lbl_name = Label(self.root,text="Name",bg="white",font=("goudy old style",15,"bold"))
        lbl_name.place(x=30,y=120)

        lbl_gender = Label(self.root,text="Gender",bg="white",font=("goudy old style",15,"bold"))
        lbl_gender.place(x=30,y=170)

        lbl_contact = Label(self.root,text="Contact",bg="white",font=("goudy old style",15,"bold"))
        lbl_contact.place(x=30,y=220)

        lbl_dob = Label(self.root,text="D.O.B",bg="white",font=("goudy old style",15,"bold"))
        lbl_dob.place(x=30,y=270)

        lbl_email = Label(self.root,text="Email",bg="white",font=("goudy old style",15,"bold"))
        lbl_email.place(x=30,y=320)

        txt_tid = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_tid)
        txt_tid.place(x=130,y=70)

        txt_name = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_name)
        txt_name.place(x=130,y=120)

        cmb_gender = ttk.Combobox(self.root,values=("Select","Male","Female","Other"),state="readonly",justify=CENTER,font=("times new roman",15,"bold"),textvariable=self.var_gender)
        cmb_gender.place(x=130,y=170,width=205)
        cmb_gender.current(0)

        txt_contact = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_contact)
        txt_contact.place(x=130,y=220)

        txt_dob = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_dob)
        txt_dob.place(x=130,y=270)

        txt_email = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_email)
        txt_email.place(x=130,y=320)

        lbl_address = Label(self.root,text="Address",bg="white",font=("goudy old style",15,"bold"))
        lbl_address.place(x=30,y=370)

        self.txt_address = Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=130,y=370,height=100,width=400)

        # ================= col-2 =================

        lbl_course = Label(self.root,text="Qualification",bg="white",font=("goudy old style",15,"bold"))
        lbl_course.place(x=380,y=70)

        lbl_admission_type = Label(self.root,text="Joining Date",bg="white",font=("goudy old style",15,"bold"))
        lbl_admission_type.place(x=380,y=120)

        lbl_state = Label(self.root,text="State",bg="white",font=("goudy old style",15,"bold"))
        lbl_state.place(x=380,y=170)

        lbl_city = Label(self.root,text="City",bg="white",font=("goudy old style",15,"bold"))
        lbl_city.place(x=380,y=220)

        lbl_pincode = Label(self.root,text="Pin Code",bg="white",font=("goudy old style",15,"bold"))
        lbl_pincode.place(x=380,y=270)

        lbl_designation = Label(self.root,text="Designation",bg="white",font=("goudy old style",15,"bold"))
        lbl_designation.place(x=380,y=320)

        txt_qualification = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_qualification)
        txt_qualification.place(x=560,y=70)

        txt_doj = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_doj)
        txt_doj.place(x=560,y=120)

        txt_state = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_state)
        txt_state.place(x=560,y=170)

        txt_city = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_city)
        txt_city.place(x=560,y=220)

        txt_pincode = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_pincode)
        txt_pincode.place(x=560,y=270)

        txt_designation = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_designation)
        txt_designation.place(x=560,y=320)


        save_btn =Button(self.root,text='Save',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",20,"bold"),activeforeground="red",command=self.save)
        save_btn.place(x=90,y=490,height=40,width=120)

        delete_btn =Button(self.root,text='Delete',cursor="hand2",bd=3,bg='#f44336',font=("times new roman",20,"bold"),activeforeground="red",command=self.delete)
        delete_btn.place(x=260,y=490,height=40,width=120)

        update_btn =Button(self.root,text='Update',cursor="hand2",bd=3,bg='#4caf50',font=("times new roman",20,"bold"),activeforeground="red",command=self.update)
        update_btn.place(x=430,y=490,height=40,width=120)

        save_btn =Button(self.root,text='Export',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",20,"bold"),activeforeground="red",command=self.exportdata)
        save_btn.place(x=600,y=490,height=40,width=120)

        save_btn =Button(self.root,text='Show All',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",20,"bold"),activeforeground="red",command=self.show)
        save_btn.place(x=260,y=550,height=40,width=120)

        clear_btn =Button(self.root,text='Clear',cursor="hand2",bd=3,bg='#607d8b',font=("times new roman",20,"bold"),activeforeground="red",command=self.clear)
        clear_btn.place(x=430,y=550,height=40,width=120)

        # ------------- SHOW DATA ---------------
        teacher_frame = Frame(self.root,bd=3,relief=RIDGE)
        teacher_frame.place(x=800,y=170,width=690,height=400)

        scroll_x = Scrollbar(teacher_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(teacher_frame,orient=VERTICAL)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.teacherTable = ttk.Treeview(teacher_frame,columns=("tid","name","gender","contact","email","dob","qualification","doj","state","city","pincode","designation","address"),yscrollcommand=scroll_y,xscrollcommand=scroll_x)
        self.teacherTable.pack(fill=BOTH,expand=1)

        scroll_x.config(command=self.teacherTable.xview)
        scroll_y.config(command=self.teacherTable.xview)

        self.teacherTable.heading("tid",text="Teacher ID")
        self.teacherTable.heading("name",text="Name")
        self.teacherTable.heading("gender",text="Gender")
        self.teacherTable.heading("contact",text="Contact")
        self.teacherTable.heading("email",text="Email")
        self.teacherTable.heading("dob",text="D.O.B")
        self.teacherTable.heading("qualification",text="Qualification")
        self.teacherTable.heading("doj",text="D.O.J")
        self.teacherTable.heading("state",text="State")
        self.teacherTable.heading("city",text="City")
        self.teacherTable.heading("pincode",text="Pin Code")
        self.teacherTable.heading("designation",text="Designation")
        self.teacherTable.heading("address",text="Address")

        self.teacherTable['show'] = "headings"

        self.teacherTable.column("tid",width=80)
        self.teacherTable.column("name",width=150)
        self.teacherTable.column("gender",width=80)
        self.teacherTable.column("contact",width=100)
        self.teacherTable.column("email",width=150)
        self.teacherTable.column("dob",width=100)
        self.teacherTable.column("qualification",width=100)
        self.teacherTable.column("doj",width=100)
        self.teacherTable.column("state",width=100)
        self.teacherTable.column("city",width=100)
        self.teacherTable.column("pincode",width=100)
        self.teacherTable.column("designation",width=100)
        self.teacherTable.column("address",width=150)
        self.teacherTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

    # ========================== FUNCTION =================================
    def exportdata(self):
        self.ask =messagebox.askyesno("Notification","Do you want to export the data in csv format ?",parent=self.root)
        if self.ask == True:
            file = filedialog.asksaveasfilename()
            self.records = self.teacherTable.get_children()
            id,name,mobile,email,address,gender,dob,date,time=[],[],[],[],[],[],[],[],[]
            for record in self.records:
                self.content = self.teacherTable.item(record)
                row = self.content['values']
                id.append(row[0]),name.append(row[1]),mobile.append(row[2]),email.append(row[3]),address.append(row[4]),gender.append(row[5]),
                dob.append(row[6]),date.append(row[7]),time.append(row[8])
            self.datacolumn = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Date','Time']
            self.dataframe = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,date,time)),columns=self.datacolumn)
            self.paths = r'{}.csv'.format(file)
            self.dataframe.to_csv(self.paths,index=False)
            messagebox.showinfo('Success', 'Teacher data is Saved {}'.format(self.paths),parent=self.root)

    def save(self):
        try:
            if self.var_tid.get() =='' or self.var_name.get() =='' or self.var_gender.get() =='Select' or self.var_contact.get() =='' or self.var_email.get() =='' or self.var_dob.get() =='' or self.var_qualification.get() =='' or self.var_doj.get() =='' or self.var_state.get() =='' or self.var_city.get() =='' or self.var_pincode.get()=='':
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select *from teacher where tid=?",(self.var_tid.get(),))
                row = cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error","This teacher is already exists,try different id",parent=self.root)
                else:
                    cur.execute("Insert into  teacher (tid,name,gender,contact,email,dob,qualification,doj,state,city,pincode,designation,address) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                         self.var_tid.get(),
                         self.var_name.get(),
                         self.var_gender.get(),
                         self.var_contact.get(),
                         self.var_email.get(),
                         self.var_dob.get(),
                         self.var_qualification.get(),
                         self.var_doj.get(),
                         self.var_state.get(),
                         self.var_city.get(),
                         self.var_pincode.get(),
                         self.var_designation.get(),
                         self.txt_address.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Teacher is Added Successfully ",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def show(self):
        try:
            cur.execute("Select *from teacher")
            rows = cur.fetchall()
            self.teacherTable.delete(* self.teacherTable.get_children())
            for row in rows:
                self.teacherTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def get_data(self,ev):
        f=self.teacherTable.focus()
        content =( self.teacherTable.item(f))
        row = content['values']
        self.var_tid.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_contact.set(row[3])
        self.var_email.set(row[4])
        self.var_dob.set(row[5])
        self.var_qualification.set(row[6])
        self.var_doj.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pincode.set(row[10])
        self.var_designation.set(row[11])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[12])

    def clear(self):
        self.var_tid.set('')
        self.var_name.set('')
        self.var_gender.set('Select')
        self.var_contact.set('')
        self.var_email.set('')
        self.var_dob.set('')
        self.var_qualification.set('')
        self.var_doj.set('')
        self.var_state.set('')
        self.var_city.set('')
        self.var_pincode.set('')
        self.var_designation.set('')
        self.txt_address.delete('1.0',END)
        self.var_searchby.set('Select')
        self.var_searchtxt.set('')

    def delete(self):
        try:
            if self.var_tid.get() =="":
                messagebox.showerror("Error","Teacher must be required",parent=self.root)
            else:
                cur.execute("Select *from teacher where tid=?",(self.var_tid.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showinfo("Error","Invalid Teacher Id",parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm','Do you really Want to Delete the record',parent=self.root)
                    if op == True:
                        cur.execute("delete from teacher where tid =?",(self.var_tid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete",f"Teacher Id {str(self.var_tid.get())} Deleted Successfully ",parent=self.root)
                        self.clear()
                        self.show()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def update(self):
        try:
            cur.execute("Select *from teacher where tid=?",(self.var_tid.get(),))
            row = cur.fetchone()
            if row ==None:
                messagebox.showinfo("Error","Invalid Teacher Id",parent=self.root)
            else:
                cur.execute("update teacher set name=?,gender=?,contact=?,email=?,dob=?,qualification=?,doj=?,state=?,city=?,pincode=?,designation=?,address=? where tid =?",(self.var_name.get(),
                         self.var_gender.get(),
                         self.var_contact.get(),
                         self.var_email.get(),
                         self.var_dob.get(),
                         self.var_qualification.get(),
                         self.var_doj.get(),
                         self.var_state.get(),
                         self.var_city.get(),
                         self.var_pincode.get(),
                         self.var_designation.get(),
                         self.txt_address.get('1.0',END),
                         self.var_tid.get()))
                con.commit()
                messagebox.showinfo("Success",f"teacher Id {str(self.var_tid.get())} Updated Successfully ",parent=self.root)
                self.show()
                self.clear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def search(self):
        try:
            if self.var_searchby.get() =="Select":
                messagebox.showerror("Error","Search by option must be required",parent=self.root)
            elif  self.var_searchtxt.get() =="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
                cur.execute("select * from teacher")
            else:
                cur.execute("select *from teacher where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.teacherTable.delete(*self.teacherTable.get_children())
                    for row in rows:
                        self.teacherTable.insert('',END,values=row)
                    self.clear()
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)
        
if __name__ == "__main__":
    root = Tk()
    teacherClass(root)
    root.mainloop()