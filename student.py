from tkinter import*
from tkinter import ttk,messagebox,filedialog
import sqlite3
import pandas

class studentClass:
    def __init__(self,root):
        self.root = root
        self.root.title("student Details")
        self.root.geometry("1500x610+10+140")
        self.root.resizable(False,False)
        self.root.config(bg='white')
        self.root.iconbitmap('image/student.ico')
        self.root.grab_set()
        self.root.focus_force()

        global con,cur
        con =sqlite3.connect(database='management.db')
        cur =con.cursor()

        # -------- Variable -------------
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_class = StringVar()
        self.var_admission_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pincode = StringVar()

        self.class_list = []
        self.get_class()

        # --------Title----------
        title = Label(self.root,text="Manage Student Deatils",bg="slateblue",fg="white",font=("goudy old style",30,"bold"))
        title.place(x=0,y=0,relwidth=1)

        # ------ Search frame ----------
        saerch_frame = LabelFrame(self.root, text="Search Student",bg="white",relief=RIDGE,font=("goudy old style",15,"bold"),bd=2)
        saerch_frame.place(x=800,y=60,height=100,width=690)

        # ------- Option---------
        cmb_search = ttk.Combobox(saerch_frame,values=("Select","Rollno","Name","Email","Contact","class","State","City","Pincode"),state="readonly",justify=CENTER,font=("times new roman",15,"bold"),textvariable=self.var_searchby)
        cmb_search.place(x=30,y=20,width=180)
        cmb_search.current(0)

        txt_search = Entry(saerch_frame,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_searchtxt)
        txt_search.place(x=260,y=20)

        search_btn = Button(saerch_frame,text='Search',cursor="hand2",bd=3,bg='#4caf50',font=("times new roman",20,"bold"),command=self.search)
        search_btn.place(x=520,y=10,height=40,width=140)

        # ----------Content---------------
        # ===================== col1 =====================
        lbl_rollno = Label(self.root,text="Roll No.",bg="white",font=("goudy old style",15,"bold"))
        lbl_rollno.place(x=30,y=70)

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

        txt_rollno = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_rollno)
        txt_rollno.place(x=130,y=70)

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

        # ================= col-2 =================

        lbl_class = Label(self.root,text="Select Class",bg="white",font=("goudy old style",15,"bold"))
        lbl_class.place(x=380,y=70)

        lbl_admission_type = Label(self.root,text="Admission Date",bg="white",font=("goudy old style",15,"bold"))
        lbl_admission_type.place(x=380,y=120)

        lbl_state = Label(self.root,text="State",bg="white",font=("goudy old style",15,"bold"))
        lbl_state.place(x=380,y=170)

        lbl_city = Label(self.root,text="City",bg="white",font=("goudy old style",15,"bold"))
        lbl_city.place(x=380,y=220)

        lbl_pincode = Label(self.root,text="Pin Code",bg="white",font=("goudy old style",15,"bold"))
        lbl_pincode.place(x=380,y=270)

        cmb_class = ttk.Combobox(self.root,textvariable=self.var_class,values=self.class_list,state="readonly",justify=CENTER,font=("times new roman",15,"bold"))
        cmb_class.place(x=560,y=70,width=205)
        cmb_class.current(0)


        txt_admission_date = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_admission_date)
        txt_admission_date.place(x=560,y=120)

        txt_state = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_state)
        txt_state.place(x=560,y=170)

        txt_city = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_city)
        txt_city.place(x=560,y=220)

        txt_pincode = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_pincode)
        txt_pincode.place(x=560,y=270)

        # ------------ row-4---------

        lbl_address = Label(self.root,text="Address",bg="white",font=("goudy old style",15,"bold"))
        lbl_address.place(x=30,y=370)

        self.txt_address = Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=130,y=370,height=100,width=400)


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
        student_frame = Frame(self.root,bd=3,relief=RIDGE)
        student_frame.place(x=800,y=170,width=690,height=400)

        scroll_x = Scrollbar(student_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(student_frame,orient=VERTICAL)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.studentTable = ttk.Treeview(student_frame,columns=("rollno","name","gender","contact","email","dob","class","admissiondate","state","city","pincode","address"),yscrollcommand=scroll_y,xscrollcommand=scroll_x)
        self.studentTable.pack(fill=BOTH,expand=1)

        scroll_x.config(command=self.studentTable.xview)
        scroll_y.config(command=self.studentTable.xview)

        self.studentTable.heading("rollno",text="Roll No.")
        self.studentTable.heading("name",text="Name")
        self.studentTable.heading("gender",text="Gender")
        self.studentTable.heading("contact",text="Contact")
        self.studentTable.heading("email",text="Email")
        self.studentTable.heading("dob",text="D.O.B")
        self.studentTable.heading("class",text="Class")
        self.studentTable.heading("admissiondate",text="Admission Date")
        self.studentTable.heading("state",text="State")
        self.studentTable.heading("city",text="City")
        self.studentTable.heading("pincode",text="Pin Code")
        self.studentTable.heading("address",text="Address")

        self.studentTable['show'] = "headings"

        self.studentTable.column("rollno",width=80)
        self.studentTable.column("name",width=150)
        self.studentTable.column("gender",width=80)
        self.studentTable.column("contact",width=100)
        self.studentTable.column("email",width=150)
        self.studentTable.column("dob",width=100)
        self.studentTable.column("class",width=80)
        self.studentTable.column("admissiondate",width=120)
        self.studentTable.column("state",width=100)
        self.studentTable.column("city",width=100)
        self.studentTable.column("pincode",width=100)
        self.studentTable.column("address",width=150)
        self.studentTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

# # ======================= FUNCTION  ============================
    def get_class(self):
        cur.execute('select cname from class')
        sup= cur.fetchall()
        self.class_list.append('Empty')
        if len(sup)>0:
            del self.class_list[:]
            self.class_list.append('Select')
            for i in sup:
                self.class_list.append(i[0])

    def exportdata(self):
        self.ask =messagebox.askyesno("Notification","Do you want to export the data in csv format ?",parent=self.root)
        # print(ask)
        if self.ask == True:
            file = filedialog.asksaveasfilename()
            self.records = self.studentTable.get_children()
            id,name,mobile,email,address,gender,dob,date,time=[],[],[],[],[],[],[],[],[]
            for record in self.records:
                self.content = self.studentTable.item(record)
                row = self.content['values']
                id.append(row[0]),name.append(row[1]),mobile.append(row[2]),email.append(row[3]),address.append(row[4]),gender.append(row[5]),
                dob.append(row[6]),date.append(row[7]),time.append(row[8])
            self.datacolumn = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Date','Time']
            self.dataframe = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,date,time)),columns=self.datacolumn)
            self.paths = r'{}.csv'.format(file)
            self.dataframe.to_csv(self.paths,index=False)
            messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(self.paths),parent=self.root)

    def save(self):
        try:
            if self.var_rollno.get() =='' or self.var_name.get() =='' or self.var_gender.get() =='Select' or self.var_contact.get() =='' or self.var_email.get() =='' or self.var_dob.get() =='' or self.var_class.get() =='Select' or self.var_admission_date.get() =='' or self.var_state.get() =='' or self.var_city.get() =='' or self.var_pincode.get()=='':
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select *from student where rollno=?",(self.var_rollno.get(),))
                row = cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error","This Student is already exists,try different id",parent=self.root)
                else:
                    cur.execute("Insert into  student (rollno,name,gender,contact,email,dob,class,admissiondate,state,city,pincode,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                         self.var_rollno.get(),
                         self.var_name.get(),
                         self.var_gender.get(),
                         self.var_contact.get(),
                         self.var_email.get(),
                         self.var_dob.get(),
                         self.var_class.get(),
                         self.var_admission_date.get(),
                         self.var_state.get(),
                         self.var_city.get(),
                         self.var_pincode.get(),
                         self.txt_address.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student is Added Successfully ",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def show(self):
        try:
            cur.execute("Select *from student")
            rows = cur.fetchall()
            self.studentTable.delete(* self.studentTable.get_children())
            for row in rows:
                self.studentTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def get_data(self,ev):
        f=self.studentTable.focus()
        content =( self.studentTable.item(f))
        row = content['values']
        self.var_rollno.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_contact.set(row[3])
        self.var_email.set(row[4])
        self.var_dob.set(row[5])
        self.var_class.set(row[6])
        self.var_admission_date.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pincode.set(row[10])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[11])

    def clear(self):
        self.var_rollno.set('')
        self.var_name.set('')
        self.var_gender.set('Select')
        self.var_contact.set('')
        self.var_email.set('')
        self.var_dob.set('')
        self.var_class.set('Select')
        self.var_admission_date.set('')
        self.var_state.set('')
        self.var_city.set('')
        self.var_pincode.set('')
        self.txt_address.delete('1.0',END)
        self.var_searchby.set('Select')
        self.var_searchtxt.set('')

    def delete(self):
        try:
            if self.var_rollno.get() =="":
                messagebox.showerror("Error","student must be required",parent=self.root)
            else:
                cur.execute("Select *from student where rollno=?",(self.var_rollno.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showinfo("Error","Invalid student Id",parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm','Do you really Want to Delete the record',parent=self.root)
                    if op == True:
                        cur.execute("delete from student where rollno =?",(self.var_rollno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete",f"student Id {str(self.var_rollno.get())} Deleted Successfully ",parent=self.root)
                        self.clear()
                        self.show()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def update(self):
        try:
            cur.execute("Select *from student where rollno=?",(self.var_rollno.get(),))
            row = cur.fetchone()
            if row ==None:
                messagebox.showinfo("Error","Invalid student Roll No",parent=self.root)
            else:
                cur.execute("update student set name=?,gender=?,contact=?,email=?,dob=?,class=?,admissiondate=?,state=?,city=?,pincode=?,address=? where rollno=?",(self.var_name.get(),
                         self.var_gender.get(),
                         self.var_contact.get(),
                         self.var_email.get(),
                         self.var_dob.get(),
                         self.var_class.get(),
                         self.var_admission_date.get(),
                         self.var_state.get(),
                         self.var_city.get(),
                         self.var_pincode.get(),
                         self.txt_address.get('1.0',END),
                         self.var_rollno.get()))
                con.commit()
                messagebox.showinfo("Success",f"student {str(self.var_rollno.get())} Updated Successfully ",parent=self.root)
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
                cur.execute("select * from student")
            else:
                cur.execute("select *from student where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.studentTable.delete(*self.studentTable.get_children())
                    for row in rows:
                        self.studentTable.insert('',END,values=row)
                    self.clear()
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)
        
if __name__ == "__main__":
    root = Tk()
    studentClass(root)
    root.mainloop()