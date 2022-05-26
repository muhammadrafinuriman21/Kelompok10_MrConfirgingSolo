from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import os

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
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="brown")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


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
        registerbtn=Button(frame,command=self.login,text="New User Register",font=("times neew roman",10,"bold"), borderwidth=0,fg="white",bg="brown",activeforeground="white", activebackground="brown")
        registerbtn.place(x=167,y=430,width=160)
    
        # Forget Pass Button
        registerbtn=Button(frame,text="Forget Password",font=("times neew roman",10,"bold"), borderwidth=0,fg="white",bg="brown",activeforeground="white", activebackground="brown")
        registerbtn.place(x=162,y=450,width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All field required")
        elif self.txtuser.get()=="Rafi" and self.txtpass.get()=="Tamvan":
            messagebox.showinfo("Success", "Welcome to Mr. Conforging Solo")
        else:
            messagebox.showerror("Invalid", "Invalid Username and Password")
        
        '''
        sukses = False
        selflogin=open(file=r"C:\Hotel_Management_System\images\logindatabase.txt")
        for i in selflogin:
            a,b = i.split(",")
            b = b.strip()
            if (a=="username" and b=="password"):
                sukses == True
                break
        selflogin.close()
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All field required")
        elif self.txtuser.get()=="Rafi" and self.txtpass.get()=="Tamvan":
            messagebox.showinfo("Success", "Welcome to Mr. Conforging Solo")
        else:
            messagebox.showerror("Invalid", "Invalid Username and Password")
        '''

    def register(self):
        
        pass


        


    '''
    def login(self):
        sukses = False
        file = open("logindatabase.txt", "r")
        for i in file:
            a,b = i.split(",")
            b = b.strip()
            if (a==username and b==password):
                sukses = True
                break
        file.close()
        if sukses:
            messagebox.showinfo("Success", "Welcome to Mr. Conforging Solo")
        else:
            messagebox.showerror("Invalid", "Invalid Username and Password")
            
    def register(username, password):
        file = open("logindatabase.txt", "a")
        file.write("\n" + username + "," + password)

    def access(option):
        global username
        if (option == "login"):
            username = input("masukkan ID : ")
            password = input("masukkan password : ")
            login(username, password)
        else:
            print(" | Masukkan password Anda yang baru |")
            username = input("Masukkan ID : ")
            password = input("Masukkan password : ")
            register(username, password)
            print(" | Anda berhasil registrasi, silahkan masuk! | ")

    def begin():
        global option
        print("="*45)
        print(" | Selamat datang di MR. Conforging Solo | ")
        print("Masukkan 'login' jika anda sudah punya akun")
        print("Masukkan 'reg' jika anda belum punya akun")
        print("="*45)
        option = input("Silahkan masukkan (login/reg) : ")
        if (option != "login" and option != "reg"):
            begin()

    begin()
    access(option)
    '''



if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()