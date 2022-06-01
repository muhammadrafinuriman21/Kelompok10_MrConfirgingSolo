from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

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
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="brown")
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
            "Mulai pakai MySQL"
            messagebox.showinfo("Success", "Register Successfully")




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()