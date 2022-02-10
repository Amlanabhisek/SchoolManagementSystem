from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox,ttk
import sqlite3

class detailsClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Course Details")
        self.root.geometry("1000x570+300+140")
        self.root.resizable(False,False)
        self.root.config(bg='white')
        self.root.iconbitmap('image/class.ico')
        self.root.grab_set()
        self.root.focus_force()

        global con,cur
        con =sqlite3.connect(database='management.db')
        cur =con.cursor()

        self.var_ans =StringVar()
        self.var_cid = StringVar()

        # --------Title----------
        title = Label(self.root,text="Manage Class Details",bg="slateblue2",fg="white",font=("goudy old style",30,"bold"))
        title.place(x=0,y=0,relwidth=1)

        # Image
        self.cat_image = Image.open('image/class.png')
        self.cat_image = self.cat_image.resize((400,400),Image.ANTIALIAS)
        self.cat_image = ImageTk.PhotoImage(self.cat_image)

        lbl_image = Label(self.root,image =self.cat_image,bd=0)
        lbl_image.place(x=540,y=100)

        # ======== Label & Entry field==========
        lbl_class = Label(self.root,text="Add New Class",bg="white",font=("goudy old style",17,"bold"))
        lbl_class.place(x=70,y=90)

        txt_sub_class = Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_ans)
        txt_sub_class.place(x=270,y=90)

        # ============= Button==============
        save_btn =Button(self.root,text='Save',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",20,"bold"),activeforeground="red",command=self.save)
        save_btn.place(x=60,y=150,height=40,width=120)

        delete_btn =Button(self.root,text='Delete',cursor="hand2",bd=3,bg='#f44336',font=("times new roman",20,"bold"),activeforeground="red",command=self.delete)
        delete_btn.place(x=210,y=150,height=40,width=120)

        update_btn =Button(self.root,text='Update',cursor="hand2",bd=3,bg='green3',font=("times new roman",20,"bold"),activeforeground="red",command=self.update)
        update_btn.place(x=350,y=150,height=40,width=120)

        search_btn =Button(self.root,text='Search',cursor="hand2",bd=3,bg='#2196f3',font=("times new roman",20,"bold"),activeforeground="red",command=self.Search)
        search_btn.place(x=140,y=210,height=40,width=120)

        clear_btn =Button(self.root,text='Clear',cursor="hand2",bd=3,bg='#607d8b',font=("times new roman",20,"bold"),activeforeground="red",command=self.clear)
        clear_btn.place(x=280,y=210,height=40,width=120)

        # =================show Class data==================
        class_data_frame= Frame(self.root,bd=3,relief=RIDGE)
        class_data_frame.place(x=50,y=280,width=420,height=250)

        ctitle = Label(class_data_frame,text="Class Deatils",bg="slateblue2",fg="white",font=("goudy old style",15,"bold"))
        ctitle.pack(fill=BOTH)

        scroll_x = Scrollbar(class_data_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(class_data_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.classTable = ttk.Treeview(class_data_frame,columns=("id","cname"),yscrollcommand=scroll_y)
        self.classTable.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.classTable.yview)

        self.classTable.heading("id",text="ID")
        self.classTable.heading("cname",text="Class Name")

        self.classTable['show'] = "headings"

        self.classTable.column("id",width=80)
        self.classTable.column("cname",width=150)
        self.classTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    # ======================= FUNCTION ======================

    def save(self):
        try:
            if self.var_ans.get() =='':
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from class where cname=?",(self.var_ans.get(),))
                row = cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error","This Class is already exists,try different",parent=self.root)
                else:
                    cur.execute("Insert into  class (cname) values(?)",(self.var_ans.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Class is Added Successfully ",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def delete(self):
        try:
            if self.var_ans.get() =="":
                messagebox.showerror("Error","class must be required",parent=self.root)
            else:
                cur.execute("Select * from class where cname=?",(self.var_ans.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showinfo("Error","Invalid class Id",parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm','Do you really Want to Delete the record',parent=self.root)
                    if op == True:
                        cur.execute("delete from class where cname =?",(self.var_ans.get(),))
                        con.commit()
                        messagebox.showinfo("Delete",f"class {str(self.var_ans.get())} Deleted Successfully ",parent=self.root)
                        self.clear()
                        self.show()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def update(self):
        try:
            if self.var_ans.get() =="":
                messagebox.showerror("Error","Class must be required",parent=self.root)
            else:
                cur.execute("Select * from class where cid=?",(self.var_cid.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showinfo("Error","Invalid Class Id",parent=self.root)
                else:
                    cur.execute("update class set cname=? where cid=?",(self.var_ans.get(),self.var_cid.get()))
                    con.commit()
                    messagebox.showinfo("Update",f"Class {str(self.var_ans.get())} Updated Successfully ",parent=self.root)
                    self.clear()
                    self.show()
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def clear(self):
        self.var_ans.set('')
        self.show()

    def show(self):
        try:
            cur.execute("Select *from class")
            rows = cur.fetchall()
            self.classTable.delete(* self.classTable.get_children())
            for row in rows:
                self.classTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def Search(self):
        try:
            if self.var_ans.get() =='':
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from class where cname=? ",(self.var_ans.get(),))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.classTable.delete(*self.classTable.get_children())
                    for row in rows:
                        self.classTable.insert('',END,values=row)
                    self.clear()
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f'Error due to: {str(e)}',parent=self.root)

    def get_data(self,ev):
        f=self.classTable.focus()
        content =(self.classTable.item(f))
        row = content['values']
        self.var_cid.set(row[0])
        self.var_ans.set(row[1])
        self.var_choice.set('Class')

if __name__ == "__main__":
    root = Tk()
    detailsClass(root)
    root.mainloop()