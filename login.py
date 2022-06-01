from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import datetime
import random, string
import pandas as pd


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root=root
        self.root.title("MR. CONFORGING SOLO")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\layarlogin.png")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="brown")
        frame.place(x=610,y=135,width=340,height=487)

        img1=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1= Label(image=self.photoimage1,bg="brown", borderwidth=0)
        lblimg1.place(x=730,y=140,width=100,height=100)

        get_str=Label(frame,text="Mr. Conforging Solo", font=("times new roman",20,"bold"),fg="white",bg="brown")
        get_str.place(x=50,y=100)


        # label
        email=lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="brown")
        email.place(x=70,y=155)

        self.txtemail=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtemail.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="brown")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        "============Icon Images================"
        img2=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2= Label(image=self.photoimage2,bg="brown", borderwidth=0)
        lblimg2.place(x=650,y=290,width=25,height=25)

        img3=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3= Label(image=self.photoimage3,bg="brown", borderwidth=0)
        lblimg3.place(x=650,y=360,width=25,height=25)

        # Login Button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times neew roman",15,"bold"), bd=3, relief=RIDGE,fg="white",bg="red",activeforeground="white", activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

         # Register Button
        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times neew roman",10,"bold"), borderwidth=0,fg="white",bg="brown",activeforeground="white", activebackground="brown")
        registerbtn.place(x=167,y=430,width=160)
    

    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    def login(self):
        userData = pd.read_csv('userdatabase.csv')
        df = pd.DataFrame(userData)
        if self.txtemail.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All field required")
        elif (len(df[(df.email == self.txtemail.get()) & (df.password == self.txtpass.get())]) > 0):
            messagebox.showinfo("Success", "Welcome to Mr. Conforging Solo")
            self.new_window=Toplevel(self.root)
            self.app=HotelManagementSystem(self.new_window)
        else:
            messagebox.showerror("Error", "Email atau Password Anda salah")    


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ==================== Variables ============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        # ==============bg image=================
        self.bg=ImageTk.PhotoImage(file=r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\layarlogin.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        # ==============left image=================
        self.bg1=ImageTk.PhotoImage(file=r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\pintuukirklasik.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        # ==============main frame=================
        frame=Frame(self.root,bg="brown")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE", font=("times new roman",20,"bold"),fg="white",bg="brown")
        register_lbl.place(x=20,y=20)

        # ================label and entry============

        #--------------------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="white",bg="brown")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="white",bg="brown")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
    
        #--------------------row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="white",bg="brown")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="brown")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # -------------------row3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="white",bg="brown")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="white",bg="brown")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        # --------------------row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="brown")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="white",bg="brown")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
            
        # =================checkbutton====================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        # ===================buttons=================
        img=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\register-now-button1.jpg")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="brown")
        b1.place(x=80,y=420,width=200)
        
        img1=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\login.jpg")
        img1=img1.resize((200,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="brown")
        b1.place(x=400,y=415,width=200)


    # =======================Function Declaration=====================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password Must Be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Please agree our terms and condition")
        else:
            newuser = {'firstname' : [self.fname_entry.get()],
                    'lastname' : [self.txt_lname.get()],
                    'contactno' : [self.txt_contact.get()],
                    'email' : [ self.txt_email.get()],
                    'selectsecurityquestion' : [self.combo_security_Q.get()],
                    'securityanswer' : [self.txt_security.get()],
                    'password' : [ self.txt_pswd.get()]}
            registeruser = pd.DataFrame(newuser)
            registeruser.to_csv('userdatabase.csv', mode='a', index=False, header=False)
            messagebox.showinfo("Success", "Register Successfully")


    def return_login(self):
        self.root.destroy()


class HotelManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # =========================ist img===============================
        img1 = Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\hotelmewah4.jpg")
        img1 = img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550, height=140)


         # =========================logo===============================
        img2 = Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\logobaru.png")
        img2 = img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230, height=140)


        # =============================title===========================
        lbl_title=Label(self.root,text="~  MR. CONFORGING SOLO  ~",font= ("times new roman",40,"bold"), bg="brown", fg="white", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)


        # ==========================main Frame=========================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        # ============================menu=============================
        lbl_menu=Label(main_frame,text="MENU",font= ("times new roman",20,"bold"), bg="red", fg="white", bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)


        # ===========================btn Frame=========================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="HOTEL A",width=20,command=self.cust_details,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="HOTEL B",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="HOTEL C",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="HOTEL D",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


        # ========================Right Side Image====================
        img3=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\slide5.jpg")
        img3 = img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)


        # ========================Down Image==========================
        img4=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\myh.jpg")
        img4 = img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\khana.jpg")
        img5 = img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)



class Cust_Win:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


         # =============================title===========================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font= ("times new roman",18,"bold"), bg="brown", fg="white", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)


        # =========================logo===============================
        img2 = Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\logobaru.png")
        img2 = img2.resize((70,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=6,width=70, height=40)

        # =================LabelFrame====================
        labelframeleft= LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font= ("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # =======================labels and entry=================
        # custRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29,state="readonly")
        enty_ref.grid(row=0,column=1)

        # cust name
        cname=Label(labelframeleft,font= ("arial",12,"bold"),text="Customer Name",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,font= ("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        # mother name
        lblmname=Label(labelframeleft,font= ("arial",12,"bold"),text="Mother Name: ",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        # gender combobox
        label_gender=Label(labelframeleft,font= ("arial",13,"bold"),text="Gender : ",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,font= ("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # postcode
        lblPostCode=Label(labelframeleft,font= ("arial",12,"bold"),text="PostCode : ",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,font= ("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        # mobilenumber
        lblMobile=Label(labelframeleft,font= ("arial",12,"bold"),text="Mobile : ",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,font= ("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        # email
        lblEmail=Label(labelframeleft,font= ("arial",12,"bold"),text="Email : ",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,font= ("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        # nationality
        lblNationality=Label(labelframeleft,font= ("arial",12,"bold"),text="Nationality : ",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        
        combo_Nationality=ttk.Combobox(labelframeleft,font= ("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indonesian","European","American")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        # id proof type combobox
        lblIdProof=Label(labelframeleft,font= ("arial",12,"bold"),text="ID Proof Type : ",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,font= ("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("KTP","SIM","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
        
        # id numnber
        lblIdNumber=Label(labelframeleft,font= ("arial",12,"bold"),text="Id Number : ",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font= ("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        # address
        lblAddress=Label(labelframeleft,font= ("arial",12,"bold"),text="Address : ",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,font= ("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)

        # =====================buttons===================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font= ("arial",11,"bold"),bg="gold",fg="black",width=10)
        btnAdd.grid(row=0, column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font= ("arial",11,"bold"),bg="gold",fg="black",width=10)
        btnUpdate.grid(row=0, column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font= ("arial",11,"bold"),bg="gold",fg="black",width=10)
        btnDelete.grid(row=0, column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font= ("arial",11,"bold"),bg="gold",fg="black",width=10)
        btnReset.grid(row=0, column=3,padx=1)

        # ==================tabel frame==================

        Tabel_Frame= LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font= ("times new roman",12,"bold"),padx=2)
        Tabel_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Tabel_Frame,font= ("arial",12,"bold"),text="Search By : ",bg="white",fg="red")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search=ttk.Combobox(Tabel_Frame,font= ("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        txtSearch=ttk.Entry(Tabel_Frame,font= ("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Tabel_Frame,text="Search",font= ("arial",11,"bold"),bg="gold",fg="black",width=10)
        btnSearch.grid(row=0, column=3,padx=1)

        btnShowAll=Button(Tabel_Frame,text="Show All",font= ("arial",11,"bold"),bg="gold",fg="black",width=10)
        btnShowAll.grid(row=0, column=4,padx=1)

        # ======================= Show Data Tabel =======================

        details_tabel=Frame(Tabel_Frame,bd=2,relief=RIDGE)
        details_tabel.place(x=0, y=50, width=860, height=350)

        scroll_x=ttk.Scrollbar(details_tabel,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_tabel,orient=VERTICAL)

        self.Cust_Details_Tabel=ttk.Treeview(details_tabel,column=("ref","name","mother","gender","post","mobile",
                                                                   "email","nationality","id proof","id number","address"),
                                                                   xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Tabel.xview)
        scroll_y.config(command=self.Cust_Details_Tabel.yview)

        self.Cust_Details_Tabel.heading("ref",text="Refer No")
        self.Cust_Details_Tabel.heading("name",text="Name")
        self.Cust_Details_Tabel.heading("mother",text="Mother Name")
        self.Cust_Details_Tabel.heading("gender",text="Gender")
        self.Cust_Details_Tabel.heading("post",text="PostCode")
        self.Cust_Details_Tabel.heading("mobile",text="Mobile")
        self.Cust_Details_Tabel.heading("email",text="Email")
        self.Cust_Details_Tabel.heading("nationality",text="Nationality")
        self.Cust_Details_Tabel.heading("id proof",text="Id Proof")
        self.Cust_Details_Tabel.heading("id number",text="Id Number")
        self.Cust_Details_Tabel.heading("address",text="Address")

        self.Cust_Details_Tabel["show"]="headings"


        self.Cust_Details_Tabel.column("ref",width=100)
        self.Cust_Details_Tabel.column("name",width=100)
        self.Cust_Details_Tabel.column("mother",width=100)
        self.Cust_Details_Tabel.column("gender",width=100)
        self.Cust_Details_Tabel.column("post",width=100)
        self.Cust_Details_Tabel.column("mobile",width=100)
        self.Cust_Details_Tabel.column("email",width=100)
        self.Cust_Details_Tabel.column("nationality",width=100)
        self.Cust_Details_Tabel.column("id proof",width=100)
        self.Cust_Details_Tabel.column("id number",width=100)
        self.Cust_Details_Tabel.column("address",width=100)

        self.Cust_Details_Tabel.pack(fill=BOTH,expand=1)


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.var_ref.get(),
                                                                    self.var_cust_name.get(),
                                                                    self.var_mother.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_post.get(),
                                                                    self.var_mobile.get(),
                                                                    self.var_email.get(),
                                                                    self.var_nationality.get(),
                                                                    self.var_id_proof.get(),
                                                                    self.var_address.get()
                                                                ))
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)




if __name__ == "__main__":
    main()