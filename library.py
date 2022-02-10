from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class libraryClass:
    def __init__(self,root):
        self.root = root
        self.root.title("library")
        self.root.geometry("1500x620+10+100")
        self.root.resizable(False,False)
        self.root.config(bg='white')
        self.root.iconbitmap('image/library.ico')
        self.root.grab_set()
        self.root.focus_force()
        
        # ========== Variable ==========
        self.var_bno =StringVar()
        self.var_bname =StringVar()
        self.var_btype=StringVar()
        self.var_quantity=StringVar()

        self.var_cid = StringVar()

        global con,cur
        con =sqlite3.connect(database='management.db')
        cur =con.cursor()

         # --------Title----------
        title = Label(self.root,text="Manage Book Details",bg="slateblue2",fg="white",font=("goudy old style",30,"bold"))
        title.place(x=0,y=0,relwidth=1)

        # ======== Label & Entry field==========
        self.manage_booke= Frame(self.root,bd=3,relief=RIDGE,bg='white')
        self.manage_booke.place(x=20,y=70,width=720,height=530)

        mtitle = Label(self.manage_booke,text="Add New Book",bg="slateblue2",fg="white",font=("goudy old style",15,"bold"))
        mtitle.pack(fill=X)

        lbl_bookno = Label(self.manage_booke,text="Book No.",bg="white",font=("goudy old style",17,"bold"))
        lbl_bookno.place(x=20,y=40)

        txt_bookno = Entry(self.manage_booke,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_bno)
        txt_bookno.place(x=20,y=80,width=180)

        lbl_book = Label(self.manage_booke,text="Book Name",bg="white",font=("goudy old style",17,"bold"))
        lbl_book.place(x=270,y=40)

        txt_book = Entry(self.manage_booke,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_bname)
        txt_book.place(x=270,y=80,width=180)

        lbl_book_type = Label(self.manage_booke,text="Book Type",bg="white",font=("goudy old style",17,"bold"))
        lbl_book_type.place(x=520,y=40)

        txt_book_type = Entry(self.manage_booke,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_btype)
        txt_book_type.place(x=520,y=80,width=180)


        lbl_quality = Label(self.manage_booke,text="Quantity",bg="white",font=("goudy old style",17,"bold"))
        lbl_quality.place(x=20,y=120)

        txt_quantity = Entry(self.manage_booke,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_quantity)
        txt_quantity.place(x=20,y=160,width=180)

        lbl_desc = Label(self.manage_booke,text="Description",bg="white",font=("goudy old style",17,"bold"))
        lbl_desc.place(x=220,y=120)

        self.txt_desc = Text(self.manage_booke,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_desc.place(x=350,y=120,height=65,width=350)

        # ============= Button==============
        save_btn =Button(self.manage_booke,text='Save',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",20,"bold"),activeforeground="red",command=self.save)
        save_btn.place(x=20,y=200,height=40,width=120)

        delete_btn =Button(self.manage_booke,text='Delete',cursor="hand2",bd=3,bg='#f44336',font=("times new roman",20,"bold"),activeforeground="red",command=self.delete)
        delete_btn.place(x=160,y=200,height=40,width=120)

        update_btn =Button(self.manage_booke,text='Update',cursor="hand2",bd=3,bg='green3',font=("times new roman",20,"bold"),activeforeground="red",command=self.update)
        update_btn.place(x=300,y=200,height=40,width=120)

        search_btn =Button(self.manage_booke,text='Search',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",20,"bold"),activeforeground="red",command=self.search)
        search_btn.place(x=440,y=200,height=40,width=120)

        clear_btn =Button(self.manage_booke,text='Clear',cursor="hand2",bd=3,bg='#607d8b',font=("times new roman",20,"bold"),activeforeground="red",command=self.clear)
        clear_btn.place(x=580,y=200,height=40,width=120)

        # =================show Book details==================
        self.manage_book_data= Frame(self.manage_booke,bd=3,relief=RIDGE)
        self.manage_book_data.place(x=0,y=250,relwidth=1,height=275)

        ctitle = Label(self.manage_book_data,text="Book Deatils",bg="slateblue2",fg="white",font=("goudy old style",15,"bold"))
        ctitle.pack(fill=BOTH)

        scroll_x = Scrollbar(self.manage_book_data,orient=HORIZONTAL)
        scroll_y = Scrollbar(self.manage_book_data,orient=VERTICAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.libraryTable = ttk.Treeview(self.manage_book_data,columns=("bno","bname","btype","quantity","description"),yscrollcommand=scroll_y,xscrollcommand=scroll_x)
        self.libraryTable.pack(fill=BOTH,expand=1)
        scroll_x.config(command=self.libraryTable.xview)
        scroll_y.config(command=self.libraryTable.yview)

        self.libraryTable.heading("bno",text="Book No.")
        self.libraryTable.heading("bname",text="Book Name")
        self.libraryTable.heading("btype",text="Book Type")
        self.libraryTable.heading("quantity",text="Quantity")
        self.libraryTable.heading("description",text="Description")
    
        self.libraryTable['show'] = "headings"

        self.libraryTable.column("bno",width=50)
        self.libraryTable.column("bname",width=120)
        self.libraryTable.column("btype",width=100)
        self.libraryTable.column("quantity",width=70)
        self.libraryTable.column("description",width=200)
        self.libraryTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        # ================================= ISSUE BOOK FRAME ===================================
        
        self.issue_book= Frame(self.root,bd=3,relief=RIDGE,bg='white')
        self.issue_book.place(x=760,y=70,width=720,height=530)

        self.var_ibno =StringVar()
        self.var_ibname =StringVar()
        self.var_srollno=StringVar()
        self.var_sname=StringVar()
        self.var_idate =StringVar()
        self.var_searchby =StringVar()
        self.var_searchtxt=StringVar()

        mtitle = Label(self.issue_book,text="Issue Book",bg="slateblue2",fg="white",font=("goudy old style",15,"bold"))
        mtitle.pack(fill=X)

        lbl_bookno = Label(self.issue_book,text="Book No.",bg="white",font=("goudy old style",17,"bold"))
        lbl_bookno.place(x=20,y=40)

        txt_bookno = Entry(self.issue_book,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_ibno)
        txt_bookno.place(x=190,y=40,width=150)

        lbl_book = Label(self.issue_book,text="Book Name",bg="white",font=("goudy old style",17,"bold"))
        lbl_book.place(x=360,y=40)

        txt_book = Entry(self.issue_book,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_ibname)
        txt_book.place(x=510,y=40,width=180)

        lbl_bookno = Label(self.issue_book,text="Student Roll No.",bg="white",font=("goudy old style",17,"bold"))
        lbl_bookno.place(x=20,y=80)

        txt_bookno = Entry(self.issue_book,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_srollno)
        txt_bookno.place(x=190,y=80,width=150)

        lbl_book = Label(self.issue_book,text="Student Name",bg="white",font=("goudy old style",17,"bold"))
        lbl_book.place(x=360,y=80)

        txt_book = Entry(self.issue_book,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_sname)
        txt_book.place(x=510,y=80,width=180)

        lbl_date = Label(self.issue_book,text="Issue Date",bg="white",font=("goudy old style",17,"bold"))
        lbl_date.place(x=20,y=120)

        txt_date = Entry(self.issue_book,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_idate)
        txt_date.place(x=20,y=160,width=150)

        # ================= Search Record ========================

        lbl_date = Label(self.issue_book,text="Search Record",bg="white",font=("goudy old style",17,"bold"))
        lbl_date.place(x=20,y=205)

        cmb_searchby = ttk.Combobox(self.issue_book,textvariable=self.var_searchby,values=('Select','Book Name','Roll No','Issue Date','Student Name'),state="readonly",justify=CENTER,font=("times new roman",15,"bold"))
        cmb_searchby.place(x=180,y=205,width=205)
        cmb_searchby.current(0)

        txt_searchtxt = Entry(self.issue_book,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_searchtxt)
        txt_searchtxt.place(x=410,y=205,width=150)

        # =================show issue Book details==================

        self.issue_book_data= Frame(self.issue_book,bd=3,relief=RIDGE)
        self.issue_book_data.place(x=0,y=250,relwidth=1,height=275)

        ctitle = Label(self.issue_book_data,text="Issue Book Deatils",bg="slateblue2",fg="white",font=("goudy old style",15,"bold"))
        ctitle.pack(fill=BOTH)

        scroll_x = Scrollbar(self.issue_book_data,orient=HORIZONTAL)
        scroll_y = Scrollbar(self.issue_book_data,orient=VERTICAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.issue_bookTable = ttk.Treeview(self.issue_book_data,columns=("ibno","ibname","srollno","sname","idate"),yscrollcommand=scroll_y,xscrollcommand=scroll_x)
        self.issue_bookTable.pack(fill=BOTH,expand=1)
        scroll_x.config(command=self.issue_bookTable.xview)
        scroll_y.config(command=self.issue_bookTable.yview)

        self.issue_bookTable.heading("ibno",text="Book No.")
        self.issue_bookTable.heading("ibname",text="Book Name")
        self.issue_bookTable.heading("srollno",text="Student Roll No.")
        self.issue_bookTable.heading("sname",text="Student Name")
        self.issue_bookTable.heading("idate",text="Issue date")

        self.issue_bookTable['show'] = "headings"

        self.issue_bookTable.column("ibno",width=50)
        self.issue_bookTable.column("ibname",width=120)
        self.issue_bookTable.column("srollno",width=70)
        self.issue_bookTable.column("sname",width=100)
        self.issue_bookTable.column("idate",width=100)

        # self.issue_bookTable.column("description",width=200)
        self.issue_bookTable.bind("<ButtonRelease-1>",self.get_issuedata)
        self.issueshow()

        # ============= Button==============
        save_btn =Button(self.issue_book,text='Save',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",20,"bold"),activeforeground="red",command=self.issuesave)
        save_btn.place(x=250,y=130,height=40,width=110)

        delete_btn =Button(self.issue_book,text='Delete',cursor="hand2",bd=3,bg='#f44336',font=("times new roman",20,"bold"),activeforeground="red",command=self.issuedelete)
        delete_btn.place(x=390,y=130,height=40,width=110)

        clear_btn =Button(self.issue_book,text='Clear',cursor="hand2",bd=3,bg='#607d8b',font=("times new roman",20,"bold"),activeforeground="red",command=self.issueclear)
        clear_btn.place(x=530,y=130,height=40,width=110)

        search_btn =Button(self.issue_book,text='Search',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",15,"bold"),activeforeground="red",command=self.issuesearch)
        search_btn.place(x=580,y=205,height=30,width=100)

    def issuesave(self):
        try:
            if self.var_ibno.get() =='' or self.var_ibname.get() =='' or self.var_srollno.get() =='' or self.var_sname.get() =='' or self.var_idate.get() =='':
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                if self.var_ibno.get() !='':
                    cur.execute("Select * from library where bno=? and bname=?",(self.var_ibno.get(),self.var_ibname.get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error","Invalid Book No. or Name ,Enter Correct Book No. and book Name",parent=self.root)
                    else:
                        if self.var_srollno.get() !='':
                            cur.execute("Select * from student where rollno=? and name=?",(self.var_srollno.get(),self.var_sname.get(),))
                            row = cur.fetchone()
                            if row == None:
                                messagebox.showerror("Error","Invalid Roll No. or Student Name,try different",parent=self.root)
                            else:
                                cur.execute("Select * from issuebook where ibno=? and srollno=?",(self.var_ibno.get(),self.var_srollno.get(),))
                                row = cur.fetchone()
                                print(row)
                                if row!= None:
                                    messagebox.showerror("Error","This Book No. is already Issued In This Roll No,try different",parent=self.root)
                                else:
                                    cur.execute("Insert into  issuebook (ibno,ibname,srollno,sname,idate) values(?,?,?,?,?)",(self.var_ibno.get(),self.var_ibname.get(),self.var_srollno.get(),self.var_sname.get(),self.var_idate.get()))
                                    con.commit()
                                    messagebox.showinfo("Success","Book has been issued Successfully ",parent=self.root)
                                    self.issueshow()
                                    self.issueclear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def issuedelete(self):
        try:
            if self.var_ibno.get() =="" or self.var_srollno.get() =='':
                messagebox.showerror("Error","Roll No. and Book No. must be required",parent=self.root)
            else:
                cur.execute("Select * from issuebook where ibno=? and srollno=?",(self.var_ibno.get(),self.var_srollno.get(),))
                # cur.execute("Select * from issuebook where srollno=?",(self.var_srollno.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showinfo("Error","Invalid Book No.",parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm','Do you really Want to Delete the record',parent=self.root)
                    if op == True:
                        cur.execute("delete from issuebook where srollno=? and ibno=?",(self.var_srollno.get(),self.var_ibno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete",f"Book No. {str(self.var_ibno.get())} issued with Roll no. {str(self.var_srollno.get())} Deleted Successfully ",parent=self.root)
                        self.issueclear()
                        self.issueshow()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def issuesearch(self):
        try:
            if self.var_searchby.get() =='Select' or self.var_searchtxt.get() =='':
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.var_searchby.get() =='Book Name':
                self.var_searchby.set('ibname')
                print(self.var_searchby.get())
                cur.execute("select * from issuebook where ibname=? ",(self.var_searchtxt.get(),))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.issue_bookTable.delete(*self.issue_bookTable.get_children())
                    for row in rows:
                        self.issue_bookTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            elif self.var_searchby.get() =='Roll No':
                cur.execute("select * from issuebook where srollno=? ",(self.var_searchtxt.get(),))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.issue_bookTable.delete(*self.issue_bookTable.get_children())
                    for row in rows:
                        self.issue_bookTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            elif self.var_searchby.get() =='Issue Date':
                cur.execute("select * from issuebook where idate=? ",(self.var_searchtxt.get(),))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.issue_bookTable.delete(*self.issue_bookTable.get_children())
                    for row in rows:
                        self.issue_bookTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            else:
                print(self.var_searchtxt.get())
                cur.execute("select * from issuebook where sname=? ",(self.var_searchtxt.get(),))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.issue_bookTable.delete(*self.issue_bookTable.get_children())
                    for row in rows:
                        self.issue_bookTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def issueclear(self):
        self.var_ibno.set('')
        self.var_ibname.set('')
        self.var_sname.set('')
        self.var_srollno.set('')
        self.var_idate.set('')
        self.var_searchby.set('Select')
        self.var_searchtxt.set('')
        self.issueshow()

    def get_issuedata(self,ev):
        f=self.issue_bookTable.focus()
        content =( self.issue_bookTable.item(f))
        row = content['values']
        self.var_ibno.set(row[0])
        self.var_ibname.set(row[1])
        self.var_srollno.set(row[2])
        self.var_sname.set(row[3])
        self.var_idate.set(row[4])

    def issueshow(self):
        try:
            cur.execute("Select * from issuebook")
            rows = cur.fetchall()
            self.issue_bookTable.delete(* self.issue_bookTable.get_children())
            for row in rows:
                self.issue_bookTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def save(self):
        try:
            if self.var_bno.get() =='' or self.var_bname.get() =='' or self.var_btype.get() =='' or self.var_quantity.get() =='':
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from library where bno=?",(self.var_bno.get(),))
                row = cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error","This Book No. is already exists,try different",parent=self.root)
                else:
                    cur.execute("Insert into  library (bno,bname,btype,quantity,description) values(?,?,?,?,?)",(
                         self.var_bno.get(),
                         self.var_bname.get(),
                         self.var_btype.get(),
                         self.var_quantity.get(),
                         self.txt_desc.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Book is Added Successfully ",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def show(self):
        try:
            cur.execute("Select * from library")
            rows = cur.fetchall()
            self.libraryTable.delete(* self.libraryTable.get_children())
            for row in rows:
                self.libraryTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def get_data(self,ev):
        f=self.libraryTable.focus()
        content =( self.libraryTable.item(f))
        row = content['values']
        self.var_bno.set(row[0])
        self.var_bname.set(row[1])
        self.var_btype.set(row[2])
        self.var_quantity.set(row[3])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[4])

    def clear(self):
        self.var_bno.set('')
        self.var_bname.set('')
        self.var_btype.set('')
        self.var_quantity.set('')
        self.txt_desc.delete('1.0',END)
        self.show()

    def delete(self):
        try:
            if self.var_bno.get() =="":
                messagebox.showerror("Error","library must be required",parent=self.root)
            else:
                cur.execute("Select * from library where bno=?",(self.var_bno.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showinfo("Error","Invalid Book No.",parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm','Do you really Want to Delete the record',parent=self.root)
                    if op == True:
                        cur.execute("delete from library where bno =?",(self.var_bno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete",f"Book No. {str(self.var_bno.get())} Deleted Successfully ",parent=self.root)
                        self.clear()
                        self.show()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def update(self):
        try:
            if self.var_bno.get() =='' or self.var_bname.get() =='' or self.var_btype.get() =='' or self.var_quantity.get() =='':
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from library where bno=?",(self.var_bno.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showinfo("Error","Invalid Book No",parent=self.root)
                else:
                    cur.execute("update library set bname=?,btype=?,quantity=?,description=? where bno=?",(
                            self.var_bname.get(),
                            self.var_btype.get(),
                            self.var_quantity.get(),
                            self.txt_desc.get('1.0',END),
                            self.var_bno.get()))
                    con.commit()
                    messagebox.showinfo("Success",f"Book No. {str(self.var_bno.get())} Updated Successfully ",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def search(self):
        try:
            if self.var_bname.get() =="":
                messagebox.showerror("Error","Book Name must be required",parent=self.root)
            else:
                cur.execute("select * from library where bname=? ",(self.var_bname.get(),))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.libraryTable.delete(*self.libraryTable.get_children())
                    for row in rows:
                        self.libraryTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

if __name__ == "__main__":
    root = Tk()
    libraryClass(root)
    root.mainloop()