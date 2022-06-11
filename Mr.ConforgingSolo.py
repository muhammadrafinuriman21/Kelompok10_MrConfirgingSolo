from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import datetime
import random,os,string
import pandas as pd
import tempfile
from time import strftime 
from datetime import datetime


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
        self.root.title("Mr. Conforging Solo")
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
        btn_frame.place(x=0,y=35,width=228,height=230)

        hotel1_btn=Button(btn_frame,text="SOLO PARAGON",width=20,command=self.SoloParagonHotel,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        hotel1_btn.grid(row=0,column=0,pady=1)

        hotel2_btn=Button(btn_frame,text="HOTEL 2",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        hotel2_btn.grid(row=1,column=0,pady=1)

        hotel3_btn=Button(btn_frame,text="HOTEL 3",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        hotel3_btn.grid(row=2,column=0,pady=1)

        hotel4_btn=Button(btn_frame,text="HOTEL 4",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        hotel4_btn.grid(row=3,column=0,pady=1)

        hotel5_btn=Button(btn_frame,text="HOTEL 5",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        hotel5_btn.grid(row=4,column=0,pady=1)

        exit_btn=Button(btn_frame,command=self.root.destroy,text="Exit",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        exit_btn.grid(row=5,column=0,pady=1)

        


        # ========================Right Side Image====================
        img3=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\slide5.jpg")
        img3 = img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)


        # ========================Down Image==========================
        
        img4=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\myh.jpg")
        img4 = img4.resize((260,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=260,width=230,height=170)
        
        img5=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\khana.jpg")
        img5 = img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)
    
    def SoloParagonHotel(self):
        self.new_window=Toplevel(self.root)
        self.app=Bill_App(self.new_window)
    
    
    



# Mulai sini Copy jadi 5 hotel
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Mr.Conforging Solo")


        # ================== Variables =======================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=IntVar()
        self.var_mobile.set("+62" + str())

        self.var_email=StringVar()
        self.var_provinsi=StringVar()
        self.var_id_type=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()

        self.var_roomtype=StringVar()
        self.var_roomprice=IntVar()
        self.var_quantity=IntVar()
        self.var_noofdays=IntVar()
        self.var_checkin=StringVar()
        self.var_earlycheckin=StringVar()
        self.var_latecheckout=StringVar()
        self.var_meal=StringVar()
        self.var_paymentmethod=StringVar()
        self.var_onlinepayment=StringVar()
        
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)

        self.search_bill=StringVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        # Var kamar jenis 1
        self.var_nomorkamarjenis1=StringVar()
        r=random.randint(0,101)
        self.var_nomorkamarjenis1.set(r)
        # Var kamar jenis 2
        self.var_nomorkamarjenis2=StringVar()
        s=random.randint(101,201)
        self.var_nomorkamarjenis2.set(s)
        # Var kamar jenis 3
        self.var_nomorkamarjenis3=StringVar()
        t=random.randint(201,301)
        self.var_nomorkamarjenis3.set(t)

        # Var Code Pembayaran
        self.var_codebayartunai=StringVar()
        u=random.randint(1000000000,9999999999)
        self.var_codebayartunai.set(u)









        # Reservation Room Type List
        self.RoomType=["Select Type","Single Room","Double Room","Luxury Room"]
        #self.RoomPrice=["Rp 500.000,-","Rp 1.000.000,-","Rp 2.000.000,-"]
        
        self.priceSingleRoom="Rp500.000,-"
        self.priceDoubleRoom="Rp1.000.000,-"
        self.priceLuxuryRoom="Rp2.000.000,-"

        self.price_SingleRoom=500000
        self.price_DoubleRoom=1000000
        self.price_LuxuryRoom=2000000
        '''
        # Quantity Room
        self.QuantityRoom=["Select Quantity","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
        self.Quantity1=1
        self.Quantity2=2
        self.Quantity3=3
        self.Quantity4=4
        self.Quantity5=5
        self.Quantity6=6
        self.Quantity7=7
        self.Quantity8=8
        self.Quantity9=9
        self.Quantity10=10
        self.Quantity11=11
        self.Quantity12=12
        self.Quantity13=13
        self.Quantity14=14
        self.Quantity15=15
        '''
        # Early Check In
        self.EarlyCheckInlist=["Select Time","09.00 WIB", "13.00 WIB"]
        self.EarlyCheckIn1="09.00 WIB"
        self.EarlyCheckIn2="13.00 WIB"

        # Late Check Out
        self.LateCheckOut=["Select Time","15.00 WIB", "18.00 WIB"]
        self.LateCheckOut1="15.00 WIB"
        self.LateCheckOut2="18.00 WIB"

        # Meal
        self.Meallist=["Select Meal","Breakfast","Lunch","Dinner"]
        self.Meal1="Breakfast"
        self.Meal2="Lunch"
        self.Meal3="Dinner"

        # Payment Method
        self.PaymentMethodlist=["Select Pay Method","Cash","Non-Cash"]
        self.PaymentMethod1="Cash"
        self.PaymentMethod2="Non-Cash"
        

        # Online Payment Method
        self.OnlinePaymentMethodlist=["Select Online Meth.","Credit Card","Debit Card","Gopay","OVO","ShoopePay","Dana"]
        self.OnlinePaymentMethodlist1="Credit Card"
        self.OnlinePaymentMethodlist2="Debit Card"
        self.OnlinePaymentMethodlist3="Gopay"
        self.OnlinePaymentMethodlist4="OVO"
        self.OnlinePaymentMethodlist5="ShoopePay"
        self.OnlinePaymentMethodlist6="Dana"            
        






        # Image 1
        img=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\SoloParagon1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        # Image 2
        img_1=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\SoloParagon2.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)

        # Image 3
        img_2=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\SoloParagon3.jpg")
        img_2=img_2.resize((550,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=550,height=130)



        lbl_title=Label(self.root,text="SOLO PARAGON HOTEL & RESIDENCES",font=("times new roman",35,"bold"),bg="brown",fg="white")
        lbl_title.place(x=0,y=130,width=1550,height=45)



        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(lbl_title,font=("times new roman",16,'bold'),background='brown',foreground='gold')
        lbl.place(x=0,y=0,width=120,height=45)
        time()




        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        # ==================Customer Label Frame======================
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details",font=("times new roman",12,"bold"),bg="white",fg="brown")
        Cust_Frame.place(x=10,y=5,width=355,height=360)
        # Cust Ref
        self.lblCustRef=Label(Cust_Frame,text="Customer Ref",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCustRef.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entryCustRef=ttk.Entry(Cust_Frame,textvariable=self.var_ref,font=("arial",10,"bold"),width=26)
        self.entryCustRef.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        #Cust Name
        self.lblCustName=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.var_cust_name,font=("arial",10,"bold"),width=26)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        #Cust Gender
        self.lblCustGender=Label(Cust_Frame,text="Gender",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCustGender.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.comboCustGender=ttk.Combobox(Cust_Frame,textvariable=self.var_gender,font=("arial",10,"bold"),width=23,state="readonly")
        self.comboCustGender["value"]=("","Male","Female","Other")
        self.comboCustGender.current(0)
        self.comboCustGender.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        #Cust PostCode
        self.lblCustPostCode=Label(Cust_Frame,text="PostCode",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCustPostCode.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        self.txtCustPostCode=ttk.Entry(Cust_Frame,textvariable=self.var_post,font=("arial",10,"bold"),width=26)
        self.txtCustPostCode.grid(row=3,column=1,sticky=W,padx=5,pady=2)
        #Cust Mobile
        self.lblCustMob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white",fg="brown")
        self.lblCustMob.grid(row=4,column=0,sticky=W,padx=5,pady=2)
        self.txtCustMob=ttk.Entry(Cust_Frame,textvariable=self.var_mobile,font=("times new roman",10,"bold"),width=26)
        self.txtCustMob.grid(row=4,column=1,sticky=W,padx=5,pady=2)
        #Cust Email
        self.lblCustEmail=Label(Cust_Frame,text="Email",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCustEmail.grid(row=5,column=0,sticky=W,padx=5,pady=2)
        self.txtCustEmail=ttk.Entry(Cust_Frame,textvariable=self.var_email,font=("arial",10,"bold"),width=26)
        self.txtCustEmail.grid(row=5,column=1,sticky=W,padx=5,pady=2)
        #Cust Provinsi
        self.lblCustProvinsi=Label(Cust_Frame,text="Provincial Origin",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCustProvinsi.grid(row=6,column=0,sticky=W,padx=5,pady=2)
        self.comboCustProvinsi=ttk.Combobox(Cust_Frame,textvariable=self.var_provinsi,font=("arial",10,"bold"),width=23,state="readonly")
        self.comboCustProvinsi["value"]=("","Aceh","Sumatera Utara","Sumatera Barat","Sumatera Selatan","Riau","Jambi","Bangka Belitung","Kepulauan Riau",
                           "Bengkulu","Lampung","Banten","DKI Jakarta","Jawa Barat","Jawa Tengah","Jawa Timur","DIY Yogyakarta","Bali",
                           "Nusa Tenggara Barat","Nusa Tenggara Timur","Kalimantan Barat","Kalimantan Selatan","Kalimantan Tengah",
                           "Kalimantan Timur","Kalimantan Utara","Sulawesi Utara","Sulawesi Tengah","Sulawesi Tenggara","Sulawesi Selatan",
                           "Sulawesi Barat","Maluku","Maluku Utara","Gorontalo","Papua","Papua Barat")
        self.comboCustProvinsi.current(0)
        self.comboCustProvinsi.grid(row=6,column=1,sticky=W,padx=5,pady=2)
        #Cust Id Type
        self.lblCustIdType=Label(Cust_Frame,text="ID Proof Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCustIdType.grid(row=7,column=0,sticky=W,padx=5,pady=2)
        self.comboCustIdType=ttk.Combobox(Cust_Frame,textvariable=self.var_id_type,font=("arial",10,"bold"),width=23,state="readonly")
        self.comboCustIdType["value"]=("","KTP","SIM","Passport")
        self.comboCustIdType.current(0)
        self.comboCustIdType.grid(row=7,column=1,sticky=W,padx=5,pady=2)
        #Cust Id Number
        self.lblCustIdNumber=Label(Cust_Frame,text="ID Number",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCustIdNumber.grid(row=8,column=0,sticky=W,padx=5,pady=2)
        self.txtCustIdNumber=ttk.Entry(Cust_Frame,textvariable=self.var_id_number,font=("arial",10,"bold"),width=26)
        self.txtCustIdNumber.grid(row=8,column=1,sticky=W,padx=5,pady=2)
        #Cust Address
        self.lblCustAddress=Label(Cust_Frame,text="Address",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCustAddress.grid(row=9,column=0,sticky=W,padx=5,pady=2)
        self.txtCustAddress=ttk.Entry(Cust_Frame,textvariable=self.var_address,font=("arial",10,"bold"),width=26)
        self.txtCustAddress.grid(row=9,column=1,sticky=W,padx=5,pady=2)


        # ======================Reservation Label Frame===========================
        Revervation_Frame=LabelFrame(Main_Frame,text="Room Reservation",font=("times new roman",12,"bold"),bg="white",fg="brown")
        Revervation_Frame.place(x=375,y=5,width=645,height=195)
        # Room Type
        self.lblRoomType=Label(Revervation_Frame,text="Room Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblRoomType.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.ComboRoomType=ttk.Combobox(Revervation_Frame,value=self.RoomType,textvariable=self.var_roomtype,font=("arial",10,"bold"),width=17,state="readonly")
        self.ComboRoomType.current(0)
        self.ComboRoomType.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.ComboRoomType.bind("<<ComboboxSelected>>",self.PriceRoomsType)
       
        # Room Price
        self.lblRoomPrice=Label(Revervation_Frame,text="Room Price",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblRoomPrice.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.ComboRoomPrice=ttk.Combobox(Revervation_Frame,textvariable=self.var_roomprice,font=("arial",10,"bold"),width=17,state="readonly")
        self.ComboRoomPrice.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        # Quantity Room
        self.lblQuantityRoom=Label(Revervation_Frame,text="Qty",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblQuantityRoom.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.txtQuantityRoom=ttk.Entry(Revervation_Frame,textvariable=self.var_quantity,font=("arial",10,"bold"),width=20)
        self.txtQuantityRoom.grid(row=2,column=1,sticky=W,padx=5,pady=2)
    
        # No Of Days
        self.lblNoOfDays=Label(Revervation_Frame,text="No Of Days",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblNoOfDays.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        self.txtNoOfDays=ttk.Entry(Revervation_Frame,textvariable=self.var_noofdays,font=("arial",10,"bold"),width=20)
        self.txtNoOfDays.grid(row=3,column=1,sticky=W,padx=5,pady=2)
        # Check-In
        self.lblCheckIn=Label(Revervation_Frame,text="Check-In Date",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblCheckIn.grid(row=4,column=0,sticky=W,padx=5,pady=2)
        self.txtCheckIn=ttk.Entry(Revervation_Frame,textvariable=self.var_checkin,font=("arial",10,"bold"),width=20)
        self.txtCheckIn.grid(row=4,column=1,sticky=W,padx=5,pady=2)
        # Early Check-In
        self.lblEarlyCheckIn=Label(Revervation_Frame,text="Earliest Check-In",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblEarlyCheckIn.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        self.ComboEarlyCheckIn=ttk.Combobox(Revervation_Frame,value=self.EarlyCheckInlist,textvariable=self.var_earlycheckin,font=("arial",10,"bold"),width=19,state="readonly")
        self.ComboEarlyCheckIn.current(0)
        self.ComboEarlyCheckIn.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        self.ComboEarlyCheckIn.bind("<<ComboboxSelected>>",self.LateCheckOut_Add)
        # Late Check-Out
        self.lblLateCheckOut=Label(Revervation_Frame,text="Late Check-Out",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblLateCheckOut.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        self.ComboLateCheckOut=ttk.Combobox(Revervation_Frame,textvariable=self.var_latecheckout,font=("arial",10,"bold"),width=19,state="readonly")
        self.ComboLateCheckOut.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        self.ComboLateCheckOut.bind("<<ComboboxSelected>>",self.Meal_Add)
        # Meal
        self.lblMeal=Label(Revervation_Frame,text="Meal",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblMeal.grid(row=2,column=2,sticky=W,padx=5,pady=2)
        self.ComboMeal=ttk.Combobox(Revervation_Frame,textvariable=self.var_meal,font=("arial",10,"bold"),width=19,state="readonly")
        self.ComboMeal.grid(row=2,column=3,sticky=W,padx=5,pady=2)
        self.ComboMeal.bind("<<ComboboxSelected>>",self.PaymentMethod_Add)
        # Payment Method
        self.lblPaymentMethod=Label(Revervation_Frame,text="Payment Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblPaymentMethod.grid(row=3,column=2,sticky=W,padx=5,pady=2)
        self.ComboPaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_paymentmethod,font=("arial",10,"bold"),width=19,state="readonly")
        self.ComboPaymentMethod.grid(row=3,column=3,sticky=W,padx=5,pady=2)
        self.ComboPaymentMethod.bind("<<ComboboxSelected>>",self.OnlinePaymentMethod_Add)
        # Online Pay Method
        self.lblOnlinePaymentMethod=Label(Revervation_Frame,text="Online Pay Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblOnlinePaymentMethod.grid(row=4,column=2,sticky=W,padx=5,pady=2)
        self.ComboOnlinePaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_onlinepayment,font=("arial",10,"bold"),width=19,state="readonly")
        self.ComboOnlinePaymentMethod.grid(row=4,column=3,sticky=W,padx=5,pady=2)


        # =====================Middle Frame 1 =================================
        MiddleFrame1=Frame(Main_Frame,bd=10)
        MiddleFrame1.place(x=10,y=370,width=1010,height=400)
        
        # Image 1
        img12=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\SoloParagon5.jpg")
        img12=img12.resize((505,400),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame1,image=self.photoimg12)
        lbl_img12.place(x=-8,y=-8,width=505,height=130)

        # Image 2
        img13=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\SoloParagon2.jpg")
        img13=img13.resize((505,400),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)
        
        lbl_img13=Label(MiddleFrame1,image=self.photoimg13)
        lbl_img13.place(x=505,y=-8,width=505,height=130)


        # =====================Middle Frame 2 =================================
        MiddleFrame2=Frame(Main_Frame,bd=10)
        MiddleFrame2.place(x=375,y=208,width=645,height=156)
        
        # Foto Tabel Facilities
        img14=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\SoloParagon6.png")
        img14=img14.resize((645,156),Image.ANTIALIAS)
        self.photoimg14=ImageTk.PhotoImage(img14)

        lbl_img14=Label(MiddleFrame2,image=self.photoimg14)
        lbl_img14.place(x=-10,y=-10,width=645,height=156)
        
        '''
        img_1=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\SoloParagon2.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)
        '''
        # ====================== Search =====================================
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1050,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)
        


        # ====================== Right Frame Bill Area ======================
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="brown")
        RightLabelFrame.place(x=1030,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        # ======================Bill Counter Label Frame===========================
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="brown")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)
        # Sub Total
        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.txtSubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=24)
        self.txtSubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        # Gov Tax
        self.lblGovTax=Label(Bottom_Frame,text="Gov Tax",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblGovTax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.txtGovTax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=24)
        self.txtGovTax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        # Amount Total
        self.lblAmount=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)
        self.lblAmount.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.txtAmount=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24)
        self.txtAmount.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        # ================ Button Frame =========================
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)
        # Btn Add To Cart
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0,padx=1)
        global datakamar,jumlahkamar,lamamenginap,totalhargakamar,hargahargakamardipesan

        datakamar=[]
        jumlahkamar=[]
        lamamenginap=[]
        hargahargakamardipesan=[]
        totalhargakamar=[]
        # Btn Generate
        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnGenerate_bill.grid(row=0,column=1,padx=1)
        # Btn Save Bill
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)
        # Btn Print
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)
        # Btn Clear
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)
        # Btn Back
        self.BtnBack=Button(Btn_Frame,command=self.root.destroy,height=2,text="Back",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnBack.grid(row=0,column=5)
        self.welcome()

        self.l=[]



    # ============================= FUNCTION DECLARATION ==============================

    def AddItem(self):
        Tax=1
        self.n=self.var_roomprice.get()
        self.m=self.var_quantity.get()*self.n
        self.o=self.var_noofdays.get()*self.m
        self.l.append(self.o)
        if self.var_roomtype.get()=="Select Type":
            messagebox.showerror("Error","Please Select The Room Type Name")
            self.new_window=Toplevel(self.root)
            self.app=Bill_App(self.new_window)
        else:
            self.textarea.insert(END,f"\n {self.var_roomtype.get()}\t\t{self.var_quantity.get()}\t          {self.var_noofdays.get()}\t\t        {self.o}")
            self.sub_total.set(str('Rp.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rp.%.2f'%((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))
            self.total.set(str('Rp.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))))
            datakamar.append(self.var_roomtype.get())
            jumlahkamar.append(self.var_quantity.get())
            lamamenginap.append(self.var_noofdays.get())
            totalhargakamar.append(self.o)
            hargahargakamardipesan.append(self.var_roomprice.get())


    def gen_bill(self):
        if self.var_roomtype.get()=="Select Type":
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")
            self.new_window=Toplevel(self.root)
            self.app=Bill_App(self.new_window)
        if self.var_paymentmethod.get()=="Select Pay Method":
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")
            self.new_window=Toplevel(self.root)
            self.app=Bill_App(self.new_window)
        else:
            text=self.textarea.get(20.0,(24.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"==================================================")
            self.textarea.insert(END,"\n ~ ADDITIONAL INFORMATION ~\n")
            self.textarea.insert(END,f"\n Check-In Date\t\t\t: {self.var_checkin.get()}")
            if self.var_earlycheckin.get()=="Select Time":
                messagebox.showerror("Error","Please Select Earliest Check-In Time")
                self.new_window=Toplevel(self.root)
                self.app=Bill_App(self.new_window)
            else:
                self.textarea.insert(END,f"\n Earliest Check-In Date\t\t\t: {self.var_earlycheckin.get()}")
            if self.var_latecheckout.get()=="Select Time":
                messagebox.showerror("Error","Please Select Check-Out Time")
                self.new_window=Toplevel(self.root)
                self.app=Bill_App(self.new_window)
            else:
                self.textarea.insert(END,f"\n Late Check-Out\t\t\t: {self.var_latecheckout.get()}")
            if self.var_meal.get()=="Select Meal":
                messagebox.showerror("Error","Please Select Meal")
                self.new_window=Toplevel(self.root)
                self.app=Bill_App(self.new_window)
            else:
                self.textarea.insert(END,f"\n Meal\t\t\t: {self.var_meal.get()}")
            if self.var_paymentmethod.get()=="Cash":
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")
            if self.var_paymentmethod.get()=="Non-Cash":
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")
                self.textarea.insert(END,f"\n Online Payment Method\t\t\t: {self.var_onlinepayment.get()}")
            self.textarea.insert(END,"\n==================================================")
            # self.textarea.insert(END,f"\n Time Generate Bill\t\t\t: {global.time.get()}")
            if self.var_onlinepayment.get()=="Credit Card":
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")
            if self.var_onlinepayment.get()=="Debit Card":
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")
            self.textarea.insert(END,f"\n Sub Amount\t\t\t: {self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount\t\t\t: {self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount\t\t\t: {self.total.get()}")
            self.textarea.insert(END,"\n==================================================")
            newcustomer = {'Bill Number' : [str(self.bill_no.get())],
                'Cust Ref' : [self.entryCustRef.get()],
                'Cust Name' : [self.txtCustName.get()],
                'Cust Gender' : [self.comboCustGender.get()],
                'Cust PostCode' : [self.txtCustPostCode.get()],
                'Cust Mobile' : [self.txtCustMob.get()],
                'Cust Email' : [self.txtCustEmail.get()],
                'Cust Provinsi' : [self.comboCustProvinsi.get()],
                'Cust ID Type' : [self.comboCustProvinsi.get()],
                'Cust Address' : [self.txtCustAddress.get()],
                'Room Type' : [datakamar],
                'Room Price' : [hargahargakamardipesan],
                'Quantity Room' : [jumlahkamar],
                'No of Days' : [lamamenginap],
                'Total Harga Kamar' : [totalhargakamar],
                'Check-In' : [self.txtCheckIn.get()],
                'Early Check-In' : [self.ComboEarlyCheckIn.get()],
                'Late Check-Out' : [self.ComboLateCheckOut.get()],
                'Meal' : [self.ComboMeal.get()],
                'Payment Method' : [self.ComboPaymentMethod.get()],
                'Online Pay Method' : [self.ComboOnlinePaymentMethod.get()],
                'Payment Code' : [self.var_codebayartunai.get()]}
            userpemesan = pd.DataFrame(newcustomer)
            userpemesan.to_csv('pemesanankamarsoloparagon.csv', mode='a', index=False, header=False)
            

    

    def save_bill(self):
        if self.var_roomtype.get()=="Select Type":
            messagebox.showerror("Error","Please CLick Generate Bill")
            self.new_window=Toplevel(self.root)
            self.app=Bill_App(self.new_window)
        else:
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
            if op>0:
                self.bill_data=self.textarea.get(1.0,END)
                f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
                f1.write(self.bill_data)
                op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Successfully!")
                f1.close()

    
    def iprint(self):
        if self.var_roomtype.get()=="Select Type":
            messagebox.showerror("Error","Please CLick Generate Bill")
            self.new_window=Toplevel(self.root)
            self.app=Bill_App(self.new_window)
        else:
            q=self.textarea.get(1.0,"end-1c")
            filename=tempfile.mktemp('.txt')
            open(filename,'w').write(q)
            os.startfile(filename,"print")
    

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error","Invalid Bill No.")
    

    def clear(self):
        self.textarea.delete(1.0,END)
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_cust_name.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_provinsi.set("")
        self.var_id_type.set("")
        self.var_id_number.set("")
        self.var_address.set("")
        self.var_roomtype.set("")
        self.var_roomprice.set(0)
        self.var_quantity.set(0)
        self.var_noofdays.set(0)
        self.var_checkin.set("")
        self.var_earlycheckin.set("")
        self.var_latecheckout.set("")
        self.var_paymentmethod.set("")
        self.var_onlinepayment.set(0)
        z=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()
        






    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t ~ WELCOME TO MR.CONFORGING SOLO ~\n")
        self.textarea.insert(END,f"\n Bill Number\t\t\t: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Ref\t\t\t: {self.var_ref.get()}")
        self.textarea.insert(END,f"\n Customer Name\t\t\t: {self.var_cust_name.get()}")
        self.textarea.insert(END,f"\n Gender\t\t\t: {self.var_gender.get()}")
        self.textarea.insert(END,f"\n PostCode\t\t\t: {self.var_post.get()}")
        self.textarea.insert(END,f"\n Mobil No.\t\t\t: {self.var_mobile.get()}")
        self.textarea.insert(END,f"\n Email\t\t\t: {self.var_email.get()}")
        self.textarea.insert(END,f"\n Provincial Origin\t\t\t: {self.var_provinsi.get()}")
        self.textarea.insert(END,f"\n ID Proof Type\t\t\t: {self.var_id_type.get()}")
        self.textarea.insert(END,f"\n ID Number\t\t\t: {self.var_id_number.get()}")
        self.textarea.insert(END,f"\n Address\t\t\t: {self.var_address.get()}")

        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,'\t\t\t "SOLO PARAGON HOTEL & RESIDENCES"\n')
        self.textarea.insert(END,'\n  Jl. Dr. Sutomo, Mangkubumen, Kec. Banjarsari, Kota Surakarta\n')
        self.textarea.insert(END,f"\n  Room Type\t\tQuantity\t          No of Days\t\t        Room Price")
        self.textarea.insert(END,"\n==================================================")

    
    def PriceRoomsType(self,event=""):
        if self.ComboRoomType.get()=="Single Room":
            self.ComboRoomPrice.config(value=self.price_SingleRoom)
            self.ComboRoomPrice.current(0)
            self.var_quantity.set(1)
            self.var_noofdays.set(1)
        if self.ComboRoomType.get()=="Double Room":
            self.ComboRoomPrice.config(value=self.price_DoubleRoom)
            self.ComboRoomPrice.current(0)
            self.var_quantity.set(1)
            self.var_noofdays.set(1)
        if self.ComboRoomType.get()=="Luxury Room":
            self.ComboRoomPrice.config(value=self.price_LuxuryRoom)
            self.ComboRoomPrice.current(0)
            self.var_quantity.set(1)
            self.var_noofdays.set(1)
    

    
    def LateCheckOut_Add(self,event=""):
        if self.ComboEarlyCheckIn.get()=="09.00 WIB":
            self.ComboLateCheckOut.config(value=self.LateCheckOut)
            self.ComboLateCheckOut.current(0)
            self.var_quantity.set(1)
        if self.ComboEarlyCheckIn.get()=="13.00 WIB":
            self.ComboLateCheckOut.config(value=self.LateCheckOut)
            self.ComboLateCheckOut.current(0)
    
    def Meal_Add(self,event=""):
        if self.ComboLateCheckOut.get()=="15.00 WIB":
            self.ComboMeal.config(value=self.Meallist)
            self.ComboMeal.current(0)
        if self.ComboLateCheckOut.get()=="18.00 WIB":
            self.ComboMeal.config(value=self.Meallist)
            self.ComboMeal.current(0)

    def PaymentMethod_Add(self,event=""):
        if self.ComboMeal.get()=="Breakfast":
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)
            self.ComboPaymentMethod.current(0)
        if self.ComboMeal.get()=="Lunch":
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)
            self.ComboPaymentMethod.current(0)
        if self.ComboMeal.get()=="Dinner":
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)
            self.ComboPaymentMethod.current(0)

    def OnlinePaymentMethod_Add(self,event=""):
        if self.ComboPaymentMethod.get()=="Non-Cash":
            self.ComboOnlinePaymentMethod.config(value=self.OnlinePaymentMethodlist)
            self.ComboOnlinePaymentMethod.current(0)
        
    

    




if __name__ == "__main__":
    main()