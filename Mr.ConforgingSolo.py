from tkinter import*                                    # Untuk mengimpor semua modul yang ada pada Tkinter 
from tkinter import messagebox                          # Untuk membuat messagebox dengan Tkinter berupa memunculkan jendela kecil
from PIL import Image, ImageTk   #pip install pillow    # PIL (Python Imaging Library) adalah library open source untuk memanipulasi file gambar (PNG, JPG/JPEG) dan mengimport gambar dari luar agar bisa dibca oleh python                        
from tkinter import ttk                                 # Untuk import fungsi scroll bar                                         
import random,os                                        # Untuk membuat angka random pada nomor bill dan nomor ref pelanggan
import pandas as pd                                     # Untuk membuat, membaca, dan mengedit csv 
import tempfile                                         # Digunakan pada tombol print bill untuk membuat file sementara bentuk txt agar bisa dibaca dalam waktu sementara jadi sat program jalan ngesave saat program tidak jalan tidak ngesave 
from time import strftime                               # Untuk mengubah objek tanggal menjadi string yang mudah dibaca dan membaca dari waktu laptop
                                        


def main():                                             # Mendefinisikan Fungsi main untuk membuat window utama yaitu Login Window
    global win
    win=Tk()                                            # win adalah variabelnya, Tk adalah Tkinter untuk TopLevel agar muncul paling atas 
    Login_Window(win)                                   # Login_Window adalah class pertama dan masuk ke screen win 
    win.mainloop()                                      # Untuk memanggil mainloop Tkinter dan programnya melakukan looping (terus memproses) agar window tidka langsung menutup saat dipanggil


class Login_Window:                                     # Membuat class berisi gabungan dari beberapa fungsi untuk user melakukan login 
    def __init__(self, root):                           # Mendefinisikan fungsi dalam class dengan nama __init__ dengan parameternya harus "self" (merujuk pada objek class) dan ada parameter tambahan yaitu "root"
                                                            # Fungsi parameter self : untuk merepresentasikan setiap objek yang dibuat pada class yang memiliki atribut yang berbeda-beda dalam class yang sama
        self.root=root                                  # Membuat properti root dengan sintaks self.root dan memberikan nilai dari root
        self.root.title("MR. CONFORGING SOLO")          # Membuat judul window dengan nama Mr.Conforging  Solo 
        self.root.geometry("1550x800+0+0")              # Membuat ukuran window login panjang 1550 pixel, lebar 800 pixel, bergeser 0 pixel dari sumbu X, bergeser 0 pixel dari sumbu Y 

        self.bg=ImageTk.PhotoImage(file=r"images\layarlogin.png")      # Mengisi layar frame dengan foto bernama layarlogin.png
        lbl_bg=Label(self.root,image=self.bg)           # Mengatur posisi foto layarlogin.png 
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)    # Dengan koordinat x=0, y=0, relative posisi window dengan lebar 1 dan tinggi 1   
        
        frame=Frame(self.root,bg="brown")               # Membuat frame baru berwarna coklat
        frame.place(x=610,y=135,width=340,height=487)   # Dengan posisi terhadap sumbu x = 610 dan terhadap sumbu y = 135, dengan lebar 340 pixel dan tinggi 487 pixel
        
        img1=Image.open(r"images\LoginIconAppl.png")   # mendefinisikan img1 adalah variabel untuk mengupload gambar LoginIconAppl.png
        img1=img1.resize((100,100),Image.ANTIALIAS)                         # Mengatur ukuran img1 menjadi 100 x 100 pixel dan disimpan dalam img1
        self.photoimage1=ImageTk.PhotoImage(img1)                           # Mendefinisikan parameter photoimage1 yang membuka img1 pada tkinter
        lblimg1= Label(image=self.photoimage1,bg="brown", borderwidth=0)    # Membuat background img1 berwarna coklat dan tanpa border
        lblimg1.place(x=730,y=140,width=100,height=100)                     # Mengatur posisi img1

        get_str=Label(frame,text="Mr. Conforging Solo", font=("times new roman",20,"bold"),fg="white",bg="brown")   # Membuat tulisan Mr.Conforging Solo dengan font, warna tulisan, dan bg yang kita tentukan sendiri
        get_str.place(x=50,y=100)                       # Mengatur lokasi ditempatkannya tulisan
        

        # -----------------LABEL
        ## Label Email Untuk Login
        email=lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="brown")    # Membuat tulisan Email dengan font dan warna yang disesuaikan
        email.place(x=70,y=155)                                                                         # Mengatur posisi tulisan Email
        self.txtemail=ttk.Entry(frame,font=("times new roman",15,"bold"))                               # Membuat kotak isian sebagai tempat input untuk email user
        self.txtemail.place(x=40,y=180,width=270)                                                       # Mengatur posisi dan lebar dari kotak isian
        
        # Label Password untuk Login
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="brown")  # Membuat tulisan Password dengan font dan warna yang disesuaikan
        password.place(x=70,y=225)                                                                          # Mengatur posisi tulisan Password
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))                                    # Membuat kotak isian sebagai tempat input untuk password user
        self.txtpass.place(x=40,y=250,width=270)                                                            # Mengatur posisi dan lebar dari kotak isian
        
        "============Icon Images================"
        img2=Image.open(r"images\LoginIconAppl.png")   # Menginput foto sebelum tulisan Email dengan variabelnya img2
        img2=img2.resize((25,25),Image.ANTIALIAS)                                                           # Mengatur ukuran img2
        self.photoimage2=ImageTk.PhotoImage(img2)                                                           # Mendefinisikan parameter photoimage2 yang membuka img2 pada tkinter
        lblimg2= Label(image=self.photoimage2,bg="brown", borderwidth=0)                                    # Membuat background img2 berwarna coklat dan tanpa border 
        lblimg2.place(x=650,y=290,width=25,height=25)                                                       # Mengatur posisi img2
        
        img3=Image.open(r"images\lock-512.png")        # Menginput foto sebelum tulisan Password dengan variabelnya img3
        img3=img3.resize((25,25),Image.ANTIALIAS)                                                           # Mengatur ukuran img3
        self.photoimage3=ImageTk.PhotoImage(img3)                                                           # Mendefinisikan parameter photoimage3 yang membuka img2 pada tkinter
        lblimg3= Label(image=self.photoimage3,bg="brown", borderwidth=0)                                    # Membuat background img3 berwarna coklat dan tanpa border
        lblimg3.place(x=650,y=360,width=25,height=25)                                                       # Mengatur posisi img3
        
        # --------------- BUTTON            # Bagian TOMBOL
        # Login Button                      # Tombol untuk login user
        loginbtn=Button(frame,command=self.login,text="Login",font=("times neew roman",15,"bold"), bd=3, relief=RIDGE,fg="white",bg="red",activeforeground="white", activebackground="red")     # Membuat tombol login user bertuliskan "Login" dengan warna yang disesuaikan
        loginbtn.place(x=110,y=300,width=120,height=35)         # Mengatur dimensi dan lokasi dari tombol Login pada frame login                                                                                                                             

         # Register Button                  # Tombol untuk register user
        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times neew roman",10,"bold"), borderwidth=0,fg="white",bg="brown",activeforeground="white", activebackground="brown")     # Membuat tombol login user bertuliskan "Register" dengan warna yang disesuaikan
        registerbtn.place(x=167,y=430,width=160)                # # Mengatur dimensi dan lokasi dari tombol Register pada frame login
    


    def register_window(self):                          # Membuat fungsi register window yang mana ketika user klik tombol "New User Register" frame register akan menumpuk di atas frame login menggunakan TopLevel setelah membaca class register
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)              
    
    def login(self):                                                # Membuat fungsi login window yang mana ketika user klik tombol "Login" frame HotelManagementSystem akan menumpuk di atas frame login menggunakan TopLevel setelah membaca class HotelManagementSystem                               
        userData = pd.read_csv('userdatabase.csv')                  # Membuat variabel userData untuk melakukan read file userdatabase.csv
        df = pd.DataFrame(userData)                                 # Membuat variabel df untuk mengakses data pada variabel userData
        if self.txtemail.get()=="" or self.txtpass.get()=="":       # Membuat decision untuk perintah error bila saat user klik tombol login tanpa memasukkan input apapun  
            messagebox.showerror("Error", "All field required")     # Menampilkan messagebox error
        elif (len(df[(df.email == self.txtemail.get()) & (df.password == self.txtpass.get())]) > 0):        # Membuat decision untuk perintah berhasil login bila username dan password ada pada file userdatabase.csv
            messagebox.showinfo("Success", "Welcome to Mr. Conforging Solo")                                # Menampilkan messagebox sukses login
            self.new_window=Toplevel(self.root)                                                             # Memunculkan frame window baru
            self.app=HotelManagementSystem(self.new_window)
                                                             # Yakni memunculkan frame pada class HotelManagementSystem 
        else:                                                                           # Membuat decision untuk perintah error bila username atau password yang dimasukkan salah atau tidak ada pada file userdatabase.csv 
            messagebox.showerror("Error", "Email atau Password Anda salah")             # Menampilkan messagebox error berupa info email atau password yang dimasukkan keliru        

class Register:                                                 # Membuat class berisi gabungan dari beberapa fungsi untuk user melakukan registrasi 
    def __init__(self,root):                                    # Mendefinisikan fungsi dalam class dengan nama __init__ dengan parameternya harus "self" (merujuk pada objek class) dan ada parameter tambahan yaitu "root"                                   
        self.root=root                                          # Membuat properti root dengan sintaks self.root dan memberikan nilai dari root
        self.root.title("Register")                             # Membuat judul window dengan nama Register
        self.root.geometry("1600x900+0+0")                      # Membuat ukuran window register panjang 1600 pixel, lebar 900 pixel, bergeser 0 pixel dari sumbu X, bergeser 0 pixel dari sumbu Y 

        # ==================== Variables ============           # Variabel-variabel yang ada pada class Register
        self.var_fname=StringVar()                              # Membuat variabel firstname dengan jenis datanya string
        self.var_lname=StringVar()                              # Membuat variabel lastname dengan jenis datanya string
        self.var_contact=StringVar()                            # Membuat variabel nomor HP dengan jenis datanya string
        self.var_email=StringVar()                              # Membuat variabel email dengan jenis datanya string
        self.var_securityQ=StringVar()                          # Membuat variabel Sequrity Question dengan jenis datanya string
        self.var_SecurityA=StringVar()                          # Membuat variabel Sequrity Answer dengan jenis datanya string 
        self.var_pass=StringVar()                               # Membuat variabel password dengan jenis datanya string
        self.var_confpass=StringVar()                           # Membuat variabel konfirmasi password dengan jenis datanya string


        # ==============Foto Utama Frame Register=================               
        self.bg=ImageTk.PhotoImage(file=r"images\layarlogin.png")      # Mengisi layar frame dengan foto bernama layarlogin.png
        bg_lbl=Label(self.root,image=self.bg)                   # Mengatur posisi foto layarlogin.png
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)            # Dengan koordinat x=0, y=0, relative posisi window dengan lebar 1 dan tinggi 1


        # ==============Foto Hiasan Pintu================
        self.bg1=ImageTk.PhotoImage(file=r"images\pintuukirklasik.jpg")    # Mengisi layar frame dengan foto bernama pintu ukir klasik.png
        left_lbl=Label(self.root,image=self.bg1)                # Mengatur posisi foto pintuukirklasik.png
        left_lbl.place(x=50,y=100,width=470,height=550)         # Dengan koordinat x = 50, y = 100, lebar foto = 470 pixel, dan tinggi = 550 pixel

        # ==============main frame Registrasi=================
        frame=Frame(self.root,bg="brown")                       # Membuat Frame Utama untuk registrasi
        frame.place(x=520,y=100,width=800,height=550)           # Dengan koordinat x = 520, y = 100, dengan lebar frame = 800 pixel, dan tinggi 550 pixel

        register_lbl=Label(frame,text="REGISTER HERE", font=("times new roman",20,"bold"),fg="white",bg="brown")    # Membuat tulisan label bertuliskan "REGISTER HERE" dengan format tulisan yang disesuaikan
        register_lbl.place(x=20,y=20)                           # Dengan koordinat x = 20 pixel dan y = 20 pixel

        # ================label and entry============
        #--------------------row1
        # First Name User
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="white",bg="brown")   # Membuat label tulisan "First Name"
        fname.place(x=50,y=100)                                                                         # Dengan koordinat x=50 pixel dan y=100 pixxel
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))       # Membuat kotak isian sebagai tempat user menuliskan nama depannya
        self.fname_entry.place(x=50,y=130,width=250)                                                    # Dengan koordinat dan lebar yang disesuaikan
        
        # Last Name User
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="white",bg="brown")   # Membuat label tulisan "Last Name"
        l_name.place(x=370,y=100)                                                                       # Dengan koordinat x=370 pixel dan y=100
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))         # Membuat kotak isian sebagai tempat user menuliskan nama belakang
        self.txt_lname.place(x=370,y=130,width=250)                                                     # Dengan koordinat dan lebar yang disesuaikan
        
        #--------------------row2
        # Contact Number User
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="white",bg="brown")     # Membuat label tulisan "Contact No" 
        contact.place(x=50,y=170)                                                                           # Dengan koordinat x=50 pixel dan y=170 pixel
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))         # Membuat kotak isian sebagai tempat user menuliskan nomor HP user
        self.txt_contact.place(x=50,y=200,width=250)                                                        # Dengan koordinat dan lebar yang disesuaikan

        # Email User
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="brown")        # Membuat label tulisan "Email"
        email.place(x=370,y=170)                                                                        # Dengan koordinat x=370 pixel dan y=170 pixel
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))         # Membuat kotak isian sebagai tempat user menuliskan email user
        self.txt_email.place(x=370,y=200,width=250)                                                     # Dengan koordinat dan lebar yang disesuaikan 

        # -------------------row3
        # Select Security Question 
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="white",bg="brown")    # Membuat label tulisan "Select Security Question"
        security_Q.place(x=50,y=240)                                                                                        # Dengan koordinat x=50 dan y=240
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")   # Membuat opsi pilihan menggunakan combobox dengan font yang disesuaikan
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")                            # Mendefinisikan values yang akan muncul pada combobox
        self.combo_security_Q.place(x=50,y=270,width=250)       # Dengan koordinat combobox yang disesuaikan
        self.combo_security_Q.current(0)                        # Mengatur saat program dijalankan dan membuka frame register combobox otomatis mengisi value index 0 yakni "Select"

        # Security Answer
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="white",bg="brown")     # Membuat label tulisan "Security Answer"
        security_A.place(x=370,y=240)                                                                               # Dengan koordinat x=370 pixel dan y=240 pixel
        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))              # Membuat kotak isian sebagai tempat user menuliskan jawaban dari sequrity yang dipilih
        self.txt_security.place(x=370,y=270,width=250)                                                              # Dengan koordinat dan lebar yang disesuaikan

        # --------------------row4
        # Password
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="brown")      # Membuat label tulisan "Password"
        pswd.place(x=50,y=310)                                                                          # Dengan koordinat x=50 pixel dan y=310 pixel
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))           # Membuat kotak isian sebagai tempat user menuliskan password
        self.txt_pswd.place(x=50,y=340,width=250)                                                       # Dengan koordinat dan lebar yang disesuaikan

        # Confirm Password
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="white",bg="brown")  # Membuat label tulisan "Confirm Password"
        confirm_pswd.place(x=370,y=310)                                                                             # Dengan koordinat yang disesuaikan 
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))           # Membuat kotak isian sebagai tempat user menuliskan password yang sebelumnya
        self.txt_confirm_pswd.place(x=370,y=340,width=250)                                                          # Dengan koordinat dan lebar yang disesuaikan
        
            
        # =================checkbutton====================      # Membuat tombol centang (Check Button)
        self.var_check=IntVar()                                 # Mendefinisikan menjadi variabel integer
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)  # Membuat check button 
        self.checkbtn.place(x=50,y=380)                                                                                                                         # Dengan koordinat yang disesuaikan

        # ===================buttons=================
        img=Image.open(r"images\register-now-button1.jpg")     # Menginput gambar "register-now-button1.jpg"
        img=img.resize((200,55),Image.ANTIALIAS)        # Mengubah ukuran foto register dengan dimensi yang disesuaikan
        self.photoimage=ImageTk.PhotoImage(img)         # Menginput gambar ke Tkinter pada frame register
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="brown")    # Menjadikan foto sebelumnya menjadi button
        b1.place(x=80,y=420,width=200)                  # Mengatur posisi gambar yang telah menjadi button dengan koordinat dan lebar yang disesuaikan
        
        img1=Image.open(r"images\login.jpg")   # Menginput gambar "login.jpg" 
        img1=img1.resize((200,100),Image.ANTIALIAS)                                                 # Mengubah ukuran foto login now dengan dimensi foto yang disesuaikan
        self.photoimage1=ImageTk.PhotoImage(img1)                                                   # Menginput gambar ke Tkinter pada frame register
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="brown")    # Menjadikan foto sebelumnya menjadi button
        b1.place(x=400,y=415,width=200)                 # Mengatur posisi gambar yang telah menjadi button dengan koordinat dan lebar yang disesuaikan


    # =======================Function Declaration=====================      # Bagian Fungsi-Fungsi
    def register_data(self):                                                                            # Membuat fungsi bernama register_data dengan parameter self
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":  # Membuat decision bila data first name/email/security masih belum terisi atau masih bertuliskan "Select"
            messagebox.showerror("Error", "All fields are required")                                    # Memunculkan notifikasi error dan meminta untuk memasukkan data-data tersebut
        elif self.var_pass.get()!=self.var_confpass.get():                              # Membuat decision bila value password dan confirm password berbeda
            messagebox.showerror("Error", "Password & Confirm Password Must Be Same")   # Memunculkan notifikasi error dan meminta untuk memasukkan data yang sama agar dapat lanjut registrasi
        elif self.var_check.get()==0:                                               # Membuat decision bila tidak mencentang kotak ceklis
            messagebox.showerror("Error", "Please agree our terms and condition")   # Memunculkan notifikasi error dan meminta untuk menceklis kotak isian 
        else:                                                                           # Membuat decision selain syarat sebelumnya
            newuser = {'firstname' : [self.fname_entry.get()],                          # Membuat variabel newuser yang berisi data dictionary dengan kata kunci dan valuenya mendapatkan nilai kata kunci tersebut
                    'lastname' : [self.txt_lname.get()],
                    'contactno' : [self.txt_contact.get()],
                    'email' : [ self.txt_email.get()],
                    'selectsecurityquestion' : [self.combo_security_Q.get()],
                    'securityanswer' : [self.txt_security.get()],
                    'password' : [ self.txt_pswd.get()]}
            registeruser = pd.DataFrame(newuser)                                            # Membuat variabel registeruser yang menghubungkan dengan pandas
            registeruser.to_csv('userdatabase.csv', mode='a', index=False, header=False)    # Memasukkan data ke csv 
            messagebox.showinfo("Success", "Register Successfully")                         # Memunculkan notifikasi "Register Successfully"
            self.root.destroy()


    def return_login(self):             # Membuat fungsi return_login dengan parameter self agar ketika user klik tombol register atau login now
        self.root.destroy()             # akan menghilangkan frame register sehingga kembali ke frame login user





class HotelManagementSystem:                        # Membuat class berisi gabungan dari beberapa fungsi untuk user melakukan pemilihan dari pilihan hotel yang tersedia  
    def __init__(self, root):                       # Mendefinisikan fungsi dalam class dengan nama __init__ dengan parameternya harus "self" (merujuk pada objek class) dan ada parameter tambahan yaitu "root"
        self.root=root                              # Membuat properti root dengan sintaks self.root dan memberikan nilai dari root
        self.root.title("Mr. Conforging Solo")      # Membuat judul window dengan nama Mr.Conforging Solo
        self.root.geometry("1550x800+0+0")          # Membuat ukuran window pilihan hotel dengan panjang 1550 pixel, lebar 800 pixel, bergeser 0 pixel dari sumbu X, bergeser 0 pixel dari sumbu Y 
    
        # =========================Gambar foto paling atas===============================
        img1 = Image.open(r"images\hotelmewah4.jpg")   # Menginput gambar "hotelmewah4.jpg"
        img1 = img1.resize((1550,140),Image.ANTIALIAS)                                                      # Mengubah dimensi ukuran gambar "hotelmewah4.jpg" menjadi 1550 x 140 pixel
        self.photoimg1=ImageTk.PhotoImage(img1)                                                             # Menginput gambar ke Tkinter pada frame Mr.Conforging Solo
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)                                      # Mengatur format foto yang disesuaikan
        lblimg.place(x=0,y=0,width=1550, height=140)                                                        # Mengatur posisi gambar pada frame dengan jarak terhadap sumbu x dan y adalah 0 pixel dan panjang lebar disesuaikan
 
         # =========================logo===============================
        img2 = Image.open(r"images\logobaru.png")      # Menginput gambar "logobaru.png"
        img2 = img2.resize((230,140),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg2=ImageTk.PhotoImage(img2)                                                             # Menginput gambar ke Tkinter pada frame Mr.Conforging Solo 
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)                                      # Mengatur format foto yang disesuaikan
        lblimg.place(x=0,y=0,width=230, height=140)                                                         # Mengatur posisi gambar pada frame dengan jarak terhadap sumbu x dan y adalah 0 pixel dan panjang lebar disesuaikan

        # =============================title===========================
        lbl_title=Label(self.root,text="~  MR. CONFORGING SOLO  ~",font= ("times new roman",40,"bold"), bg="brown", fg="white", bd=4,relief=RIDGE)  # Membuat label bertuliskan Mr.Conforging Solo dengan font dan format yang disesuaikan
        lbl_title.place(x=0, y=140, width=1550, height=50)              # Mengatur posisi label dengan koordinat yang disesuaikan

        # ==========================main Frame=========================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)                   # Membuat main_frame pada frame Mr.Conforging Solo
        main_frame.place(x=0,y=190,width=1550,height=620)               # Mengatur dimensi main_frame 

        # ========= Kotak Tulisan Menu ===========
        lbl_menu=Label(main_frame,text="MENU",font= ("times new roman",20,"bold"), bg="red", fg="white", bd=4,relief=RIDGE)     # Membuat label tulisan "MENU" dengan font dan format yang disesuaikan 
        lbl_menu.place(x=0, y=0, width=230)                             # Mengatur posisi dan lebar label


        # =========================== Frame Tombol-Tombol=========================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)               # Membuat frame untuk tombol-tombol pada frame Mr.Conforging Solo
        btn_frame.place(x=0,y=35,width=228,height=230)              # Mengatur posisi dan dimensi frame tombol

        hotel1_btn=Button(btn_frame,text="SOLO PARAGON",width=20,command=self.SoloParagonHotel,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")     # Membuat tombol 1 untuk masuk ke frame SoloParagonHotel
        hotel1_btn.grid(row=0,column=0,pady=1)          # Mengatur posisi tombol hotel 1

        hotel2_btn=Button(btn_frame,text="THE ALANA SOLO",width=20,command=self.TheAlanaSolo,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        hotel2_btn.grid(row=1,column=0,pady=1)          # Mengatur posisi tombol hotel 2

        hotel3_btn=Button(btn_frame,text="NOVOTEL SOLO",width=20,command=self.NovotelSolo,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        hotel3_btn.grid(row=2,column=0,pady=1)          # Mengatur posisi tombol hotel 3

        hotel4_btn=Button(btn_frame,text="ASTON SOLO HOTEL",width=20,command=self.AstonSolo,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        hotel4_btn.grid(row=3,column=0,pady=1)          # Mengatur posisi tombol hotel 4

        hotel5_btn=Button(btn_frame,text="HOTEL 5",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")
        hotel5_btn.grid(row=4,column=0,pady=1)          # Mengatur posisi tombol hotel 5

        exit_btn=Button(btn_frame,command=self.root.destroy,text="Exit",width=20,font= ("times new roman",14,"bold"), bg="brown", fg="white",bd=0,cursor="hand1")       # Membuat tombol exit untuk keluar dari frame Mr.Conforging Solo dan kembali ke frame login 
        exit_btn.grid(row=5,column=0,pady=1)            # Mengatur posisi tombol Exit

        


        # ======================== Foto Tengah ====================
        img3=Image.open(r"images\slide5.jpg")      # Menginput gambar "slide5.jpg"
        img3 = img3.resize((1310,590),Image.ANTIALIAS)                                                  # Mengubah dimensi ukuran gambar
        self.photoimg3=ImageTk.PhotoImage(img3)                                                         # Menginput gambar ke Tkinter pada frame Mr.Conforging Solo
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)                                # Mengatur format foto yang disesuaikan
        lblimg1.place(x=225,y=0,width=1310,height=590)                                                  # Mengatur posisi gambar pada frame dengan jarak terhadap sumbu x=225 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan


        # ======================== Foto Hiasan Pinggir Kiri ==========================
        # Foto hiasan 1
        img4=Image.open(r"images\myh.jpg")         # Menginput gambar "myh.jpg"
        img4 = img4.resize((260,170),Image.ANTIALIAS)                                                   # Mengubah dimensi ukuran gambar
        self.photoimg4=ImageTk.PhotoImage(img4)                                                         # Menginput gambar ke Tkinter pada frame Mr.Conforging Solo
        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)                                # Mengatur format foto yang disesuaikan
        lblimg1.place(x=0,y=260,width=230,height=170)                                                   # Mengatur posisi gambar pada frame dengan jarak terhadap sumbu x=0 pixel, sumbu y=260 pixel, dan panjang lebar disesuaikan
        
        # Foto Hiasan 2 
        img5=Image.open(r"images\khana.jpg")       # Menginput gambar "khana.jpg"
        img5 = img5.resize((230,190),Image.ANTIALIAS)                                                   # Mengubah dimensi ukuran gambar
        self.photoimg5=ImageTk.PhotoImage(img5)                                                         # Menginput gambar ke Tkinter pada frame Mr.Conforging Solo
        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)                                # Mengatur format foot yang disesuaikan
        lblimg1.place(x=0,y=420,width=230,height=190)                                                   # Mengatur gambar pada frame dengan jarak terhadap sumbu x=0 pixel, sumbu y=420 pixel, dan panjang lebar disesuaikan
    
    def SoloParagonHotel(self):                             # Membuat fungsi SoloParagonHotel dengan parameter self agar saat user klik tombol Solo Paragon
        self.new_window=Toplevel(self.root)                 # Maka frame Bill_App1 akan menutupi frame sebelumnya menggunakan Toplevel
        self.app=Bill_App1(self.new_window)                 # Membuka frame baru untuk Bill_App1

    def TheAlanaSolo(self):                             # Membuat fungsi SoloParagonHotel dengan parameter self agar saat user klik tombol Solo Paragon
        self.new_window=Toplevel(self.root)                 # Maka frame Bill_App1 akan menutupi frame sebelumnya menggunakan Toplevel
        self.app=Bill_App2(self.new_window)                 # Membuka frame baru untuk Bill_App2

    def NovotelSolo(self):                             # Membuat fungsi SoloParagonHotel dengan parameter self agar saat user klik tombol Solo Paragon
        self.new_window=Toplevel(self.root)                 # Maka frame Bill_App1 akan menutupi frame sebelumnya menggunakan Toplevel
        self.app=Bill_App3(self.new_window)                 # Membuka frame baru untuk Bill_App3  

    def AstonSolo(self):                             # Membuat fungsi SoloParagonHotel dengan parameter self agar saat user klik tombol Solo Paragon
        self.new_window=Toplevel(self.root)                 # Maka frame Bill_App1 akan menutupi frame sebelumnya menggunakan Toplevel
        self.app=Bill_App4(self.new_window)                 # Membuka frame baru untuk Bill_App4          
  
    
    



# Mulai sini Copy jadi 5 hotel
class Bill_App1:                                                                        # Membuat class berisi gabungan dari beberapa fungsi untuk user melakukan pemesanan kamar dan mendapatkan bill di Hotel Solo Paragon
    def __init__(self,root):                                                            # Mendefinisikan fungsi dalam class dengan nama __init__ dengan parameternya harus "self" (merujuk pada objek class) dan ada parameter tambahan yaitu "root"
        self.root=root                                                                  # Membuat properti root dengan sintaks self.root dan memberikan nilai dari root
        self.root.geometry("1530x800+0+0")                                              # Membuat ukuran window billing hotel dengan panjang 1530 pixel, lebar 800 pixel, bergeser 0 pixel dari sumbu X, bergeser 0 pixel dari sumbu Y 
        self.root.title("Billing Mr.Conforging Solo")                                   # Membuat judul window dengan nama Billing Mr.Conforging Solo


        # ================== Variables =======================
        self.var_ref=StringVar()                            # Membuat variabel var_ref dengan parameternya self dengan jenis datanya String
        x=random.randint(1000,9999)                             # Membuat variabel x untuk random angka mulai dari 1000 sampai 9999-1 
        self.var_ref.set(str(x))                                # Melakukan set untuk var_ref agar angka random muncul otomatis

        self.var_cust_name=StringVar()                      # Membuat variabel var_cust_name dengan parameternya self dengan jenis datanya String
        self.var_gender=StringVar()                         # Membuat variabel var_gender dengan parameternya self dengan jenis datanya String
        self.var_post=StringVar()                           # Membuat variabel var_post dengan parameternya self dengan jenis datanya String
        self.var_mobile=IntVar()                            # Membuat variabel var_mobile dengan parameternya self dengan jenis datanya Integer
        self.var_mobile.set("+62" + str())                      # Melakukan set untuk var_mobile agar diawal otomatis terisi "+62"

        self.var_email=StringVar()                          # Membuat variabel var_email dengan parameternya self dengan jenis datanya String
        self.var_provinsi=StringVar()                       # Membuat variabel var_provinsi dengan parameternya self dengan jenis datanya String
        self.var_id_type=StringVar()                        # Membuat variabel var_id_type dengan parameternya self dengan jenis datanya String
        self.var_id_number=StringVar()                      # Membuat variabel var_id_number dengan parameternya self dengan jenis datanya String
        self.var_address=StringVar()                        # Membuat variabel var_address dengan parameternya self dengan jenis datanya String

        self.var_roomtype=StringVar()                       # Membuat variabel var_roomtype dengan parameternya self dengan jenis datanya String
        self.var_roomprice=IntVar()                         # Membuat variabel var_roomprice dengan parameternya self dengan jenis datanya Integer
        self.var_quantity=IntVar()                          # Membuat variabel var_quantity dengan parameternya self dengan jenis datanya Integer
        self.var_noofdays=IntVar()                          # Membuat variabel var_noofdays dengan parameternya self dengan jenis datanya Integer
        self.var_checkin=StringVar()                        # Membuat variabel var_checkin dengan parameternya self dengan jenis datanya String
        self.var_earlycheckin=StringVar()                   # Membuat variabel var_earlycheckin dengan parameternya self dengan jenis datanya String
        self.var_latecheckout=StringVar()                   # Membuat variabel var_latecheckout dengan parameternya self dengan jenis datanya String
        self.var_meal=StringVar()                           # Membuat variabel var_meal dengan parameternya self dengan jenis datanya String
        self.var_paymentmethod=StringVar()                  # Membuat variabel var_paymentmethod dengan parameternya self dengan jenis datanya String
        self.var_onlinepayment=StringVar()                  # Membuat variabel var_onlinepayment dengan parameternya self dengan jenis datanya String
        
        self.bill_no=StringVar()                            # Membuat variabel bill_no dengan parameternya self dengan jenis datanya String
        z=random.randint(1000,9999)                             # Membuat variabel z untuk random angka mulai dari 1000 sampai 9999-1
        self.bill_no.set(z)                                     # Melakukan set untuk var_ref agar angka random muncul otomatis

        self.search_bill=StringVar()                        # Membuat variabel search_bill dengan parameternya self dengan jenis datanya String               
        self.sub_total=StringVar()                          # Membuat variabel sub_total dengan parameternya self dengan jenis datanya String
        self.tax_input=StringVar()                          # Membuat variabel tax_input dengan parameternya self dengan jenis datanya String
        self.total=StringVar()                              # Membuat variabel total dengan parameternya self dengan jenis datanya String

        # Var Code Pembayaran
        self.var_codebayartunai=StringVar()                                         # Membuat variabel var_codebayartunai dengan parameternya self dengan jenis datanya String
        u=random.randint(1000000000,9999999999)                                         # Membuat variabel u untuk random angka mulai dari 1000000000 sampai 9999999999-1
        self.var_codebayartunai.set(u)                                                  # Melakukan set untuk var_codebayartunai agar angka random muncul otomatis

        # Reservation Room Type List
        self.RoomType=["Select Type","Suite 2 Bedrooms","Deluxe Room","Superior Room","Executive Room"]     # Membuat data list RoomType dengan parameter self
        self.price_Suite2Bedrooms=1091698                                                # Membuat variabel price_Suite2Bedrooms dengan parameter self bernilai 1091698
        self.price_DeluxeRoom=558178                                                     # Membuat variabel price_DeluxeRoom dengan parameter self bernilai 558178
        self.price_SuperiorRoom=499999                                                   # Membuat variabel price_SuperiorRoom dengan parameter self bernilai 499999 
        self.price_ExecutiveRoom=852629                                                  # Membuat variabel price_ExecutiveRoom dengan parameter self bernilai 852629
        
        # Early Check In                                    
        self.EarlyCheckInlist=["Select Time","09.00 WIB", "13.00 WIB"]              # Membuat data list EarlyCheckInlist dengan parameter self
        self.EarlyCheckIn1="09.00 WIB"                                              # Membuat variabel EarlyCheckIn1 dengan parameter self bernilai 09.00 WIB
        self.EarlyCheckIn2="13.00 WIB"                                              # Membuat variabel EarlyCheckIn2 dengan parameter self bernilai 13.00 WIB

        # Late Check Out
        self.LateCheckOut=["Select Time","15.00 WIB", "18.00 WIB"]                  # Membuat data list LateCheckOut dengan parameter self
        self.LateCheckOut1="15.00 WIB"                                              # Membuat variabel LateCheckOut1 dengan parameter self bernilai 15.00 WIB
        self.LateCheckOut2="18.00 WIB"                                              # Membuat variabel LateCheckOut2 dengan parameter self bernilai 18.00 WIB

        # Meal
        self.Meallist=["Select Meal","Breakfast","Lunch","Dinner"]                  # Membuat data list Meallist dengan parameter self
        self.Meal1="Breakfast"                                                      # Membuat variabel Meal1 dengan parameter self bernilai Breakfast
        self.Meal2="Lunch"                                                          # Membuat variabel Meal2 dengan parameter self bernilai Lunch
        self.Meal3="Dinner"                                                         # Membuat variabel Meal3 dengan parameter self bernilai Dinner

        # Payment Method
        self.PaymentMethodlist=["Select Pay Method","Cash","Non-Cash"]              # Membuat data list PaymentMethodlist dengan parameter self
        self.PaymentMethod1="Cash"                                                  # Membuat variabel PaymentMethod1 dengan parameter self bernilai Cash
        self.PaymentMethod2="Non-Cash"                                              # Membuat variabel PaymentMethod2 dengan parameter self bernilai Non-Cash
        

        # Online Payment Method
        self.OnlinePaymentMethodlist=["Select Online Meth.","Credit Card","Debit Card","Gopay","OVO","ShoopePay","Dana"]    # Membuat data list OnlinePaymentMethodlist dengan parameter self
        self.OnlinePaymentMethodlist1="Credit Card"                                 # Membuat variabel OnlinePaymentMethodlist1 dengan parameter self bernilai Credir Card
        self.OnlinePaymentMethodlist2="Debit Card"                                  # Membuat variabel OnlinePaymentMethodlist2 dengan parameter self bernilai Debit Card
        self.OnlinePaymentMethodlist3="Gopay"                                       # Membuat variabel OnlinePaymentMethodlist3 dengan parameter self bernilai Gopay
        self.OnlinePaymentMethodlist4="OVO"                                         # Membuat variabel OnlinePaymentMethodlist4 dengan parameter self bernilai OVO
        self.OnlinePaymentMethodlist5="ShoopePay"                                   # Membuat variabel OnlinePaymentMethodlist5 dengan parameter self bernilai ShoopePay
        self.OnlinePaymentMethodlist6="Dana"                                        # Membuat variabel OnlinePaymentMethodlist6 dengan parameter self bernilai Dana
        
        # Foto Atas Kiri
        img=Image.open(r"images\SoloParagon1.jpg")     # Menginput gambar "SoloParagon1.jpg"
        img=img.resize((500,130),Image.ANTIALIAS)                                                           # Mengubah dimensi ukuran gambar
        self.photoimg=ImageTk.PhotoImage(img)                                                               # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img=Label(self.root,image=self.photoimg)                                                        # Mengatur format foto yang disesuaikan
        lbl_img.place(x=0,y=0,width=500,height=130)                                                         # Mengatur gambar pada frame dengan jarak terhadap sumbu x=0 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan
        
        # Foto Atas Tengah
        img_1=Image.open(r"images\SoloParagon2.jpg")   # Menginput gambar "SoloParagon2.jpg"
        img_1=img_1.resize((500,130),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg_1=ImageTk.PhotoImage(img_1)                                                           # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img_1=Label(self.root,image=self.photoimg_1)                                                    # Mengatur format foto yang disesuaikan
        lbl_img_1.place(x=500,y=0,width=500,height=130)                                                     # Mengatur gambar pada frame dengan jarak terhadap sumbu x=500 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan
        
        # Foto Atas Kanan
        img_2=Image.open(r"images\SoloParagon3.jpg")   # Menginput gambar "SoloParagon3.jpg"
        img_2=img_2.resize((550,130),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg_2=ImageTk.PhotoImage(img_2)                                                           # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img_2=Label(self.root,image=self.photoimg_2)                                                    # Mengatur format foto yang disesuaikan
        lbl_img_2.place(x=1000,y=0,width=550,height=130)                                                    # Mengatur gambar pada frame dengan jarak terhadap sumbu x=1000 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan

        # Membuat label tulisan Nama Hotel
        lbl_title=Label(self.root,text="SOLO PARAGON HOTEL & RESIDENCES",font=("times new roman",35,"bold"),bg="brown",fg="white")  # Membuat label bertuliskan Nama Hotel dengan font dan format yang disesuaikan
        lbl_title.place(x=0,y=130,width=1550,height=45)                                                     # Mengatur posisi label dengan koordinat yang disesuaikan
        
        def time():                                 # Membuat fungsi time untuk waktu terkini
            string=strftime('%H:%M:%S %p')          # Membuat variabel bernama string yang bernilai fungsi strtime dengan value Jam,Menit,Detik,Am/Pm
            lbl.config(text=string)                 # Mengubah text pada lbl menjadi string
            lbl.after(1000,time)                    # Mmebuat label lbl dengan method after dengan value 1000 sampai time
        
        lbl=Label(lbl_title,font=("times new roman",16,'bold'),background='brown',foreground='gold')    # menjadikan lbl menjadi label dengan font dan warna yang disesuaikan 
        lbl.place(x=0,y=0,width=120,height=45)                                                          # mengatur posisi label waktu
        time()                                                                                          # Mengembalikan fungsi time
        
        # ===== Main Frame =====
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")               # Membuat frame utama dengan format dan warna yang disesuaikan
        Main_Frame.place(x=0,y=175,width=1530,height=620)                       # Mengatur koordinat dan ukuran frame utama
        
        # ==================Customer Label Frame======================          # Membuat Frame Data Diri Pemesan Kamar
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details",font=("times new roman",12,"bold"),bg="white",fg="brown")  # Membuat frame kotak bingkai bertuliskan "Customer Details" dengan format dan warna yang disesuaikan 
        Cust_Frame.place(x=10,y=5,width=355,height=360)                                                                     # Mengatur posisi frame kotak bingkai 
        # Cust Ref
        self.lblCustRef=Label(Cust_Frame,text="Customer Ref",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)       # Membuat label tulisan Customer Ref dengan format dan warna tulisan yang disesuaikan
        self.lblCustRef.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.entryCustRef=ttk.Entry(Cust_Frame,textvariable=self.var_ref,font=("arial",10,"bold"),width=26)             # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.entryCustRef.grid(row=0,column=1,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi Entry
        #Cust Name
        self.lblCustName=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)     # Membuat label tulisan Customer Name dengan format dan warna tulisan yang disesuaikan
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                    # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.var_cust_name,font=("arial",10,"bold"),width=26)        # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                    # Mengatur grid/posisi Entry
        #Cust Gender
        self.lblCustGender=Label(Cust_Frame,text="Gender",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)          # Membuat label tulisan Gender dengan format dan warna tulisan yang disesuaikan
        self.lblCustGender.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustGender=ttk.Combobox(Cust_Frame,textvariable=self.var_gender,font=("arial",10,"bold"),width=23,state="readonly")   # Membuat Combobox Gender
        self.comboCustGender["value"]=("","Male","Female","Other")                                                                      # Dengan membuat beberapa value
        self.comboCustGender.current(0)                                                                                                 # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustGender.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust PostCode
        self.lblCustPostCode=Label(Cust_Frame,text="PostCode",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)      # Membuat label tulisan PostCode dengan format dan warna tulisan yang disesuaikan 
        self.lblCustPostCode.grid(row=3,column=0,sticky=W,padx=5,pady=2)                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustPostCode=ttk.Entry(Cust_Frame,textvariable=self.var_post,font=("arial",10,"bold"),width=26)         # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustPostCode.grid(row=3,column=1,sticky=W,padx=5,pady=2)                                                # Mengatur grid/posisi Entry
        #Cust Mobile
        self.lblCustMob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat label tulisan CustMobile dengan format dan warna tulisan yang disesuaikan
        self.lblCustMob.grid(row=4,column=0,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustMob=ttk.Entry(Cust_Frame,textvariable=self.var_mobile,font=("times new roman",10,"bold"),width=26)  # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustMob.grid(row=4,column=1,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi Entry
        #Cust Email
        self.lblCustEmail=Label(Cust_Frame,text="Email",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)            # Membuat label tulisan Email dengan format dan warna tulisan yang disesuaikan
        self.lblCustEmail.grid(row=5,column=0,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustEmail=ttk.Entry(Cust_Frame,textvariable=self.var_email,font=("arial",10,"bold"),width=26)           # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustEmail.grid(row=5,column=1,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi Entry
        #Cust Provinsi
        self.lblCustProvinsi=Label(Cust_Frame,text="Provincial Origin",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                                     # Membuat label tulisan Provincial Origin dengan format dan warna tulisan yang disesuaikan
        self.lblCustProvinsi.grid(row=6,column=0,sticky=W,padx=5,pady=2)                                                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustProvinsi=ttk.Combobox(Cust_Frame,textvariable=self.var_provinsi,font=("arial",10,"bold"),width=23,state="readonly")                       # Membuat Combobox Provinsi 
        self.comboCustProvinsi["value"]=("","Aceh","Sumatera Utara","Sumatera Barat","Sumatera Selatan","Riau","Jambi","Bangka Belitung","Kepulauan Riau",      # Dengan membuat value nama-nama provinsi di Indonesia
                           "Bengkulu","Lampung","Banten","DKI Jakarta","Jawa Barat","Jawa Tengah","Jawa Timur","DIY Yogyakarta","Bali",
                           "Nusa Tenggara Barat","Nusa Tenggara Timur","Kalimantan Barat","Kalimantan Selatan","Kalimantan Tengah",
                           "Kalimantan Timur","Kalimantan Utara","Sulawesi Utara","Sulawesi Tengah","Sulawesi Tenggara","Sulawesi Selatan",
                           "Sulawesi Barat","Maluku","Maluku Utara","Gorontalo","Papua","Papua Barat")
        self.comboCustProvinsi.current(0)                                                                                                                       # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustProvinsi.grid(row=6,column=1,sticky=W,padx=5,pady=2)                                                                                      # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust Id Type
        self.lblCustIdType=Label(Cust_Frame,text="ID Proof Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                       # Membuat label tulisan ID Proof Type dengan format dan warna tulisan yang disesuaikan
        self.lblCustIdType.grid(row=7,column=0,sticky=W,padx=5,pady=2)                                                                      # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustIdType=ttk.Combobox(Cust_Frame,textvariable=self.var_id_type,font=("arial",10,"bold"),width=23,state="readonly")      # Membuat Combobox ID Proof Type
        self.comboCustIdType["value"]=("","KTP","SIM","Passport")                                                                           # Dengan membuat beberapa value 
        self.comboCustIdType.current(0)                                                                                                     # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustIdType.grid(row=7,column=1,sticky=W,padx=5,pady=2)                                                                    # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust Id Number
        self.lblCustIdNumber=Label(Cust_Frame,text="ID Number",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)             # Membuat label tulisan ID Number dengan format dan warna tulisan yang disesuaikan
        self.lblCustIdNumber.grid(row=8,column=0,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustIdNumber=ttk.Entry(Cust_Frame,textvariable=self.var_id_number,font=("arial",10,"bold"),width=26)            # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustIdNumber.grid(row=8,column=1,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi Entry
        #Cust Address
        self.lblCustAddress=Label(Cust_Frame,text="Address",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                # Membuat label tulisan Address dengan format dan warna tulisan yang disesuaikan
        self.lblCustAddress.grid(row=9,column=0,sticky=W,padx=5,pady=2)                                                         # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustAddress=ttk.Entry(Cust_Frame,textvariable=self.var_address,font=("arial",10,"bold"),width=26)               # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustAddress.grid(row=9,column=1,sticky=W,padx=5,pady=2)                                                         # Mengatur grid/posisi Entry

        
        # ======================Reservation Label Frame===========================          # Membuat Frame Reservasi Kamar
        Revervation_Frame=LabelFrame(Main_Frame,text="Room Reservation",font=("times new roman",12,"bold"),bg="white",fg="brown")   # Membuat frame kotak bingkai bertuliskan "Room Reservation" dengan format dan warna yang disesuaikan
        Revervation_Frame.place(x=375,y=5,width=645,height=195)                                                                     # Mengatur posisi frame kotak bingkai
        # Room Type
        self.lblRoomType=Label(Revervation_Frame,text="Room Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)              # Membuat label tulisan Room Type dengan format dan warna tulisan yang disesuaikan
        self.lblRoomType.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboRoomType=ttk.Combobox(Revervation_Frame,value=self.RoomType,textvariable=self.var_roomtype,font=("arial",10,"bold"),width=17,state="readonly")    # Membuat Combobox Tipe Kamar
        self.ComboRoomType.current(0)                                                   # Dengan melakukan set daat program dijalankan otomatis memunculkan value index 0 pada combobox
        self.ComboRoomType.grid(row=0,column=1,sticky=W,padx=5,pady=2)                  # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboRoomType.bind("<<ComboboxSelected>>",self.PriceRoomsType)             # Mengatur menggunakan method bind agar user dapat memiliki value combobos sesuai keinginan dari pilihan value yang tersedia 
                                                                                            # Sekaligus saat user memilih value tertentu maka value Room Price, Quantity, dan No of Days otomatis terisi suatu value
                                                                                            # Dan data Room Price, Quantity, dan No of Days hanya dapat diisi user setelah memilih Room Type
        # Room Price
        self.lblRoomPrice=Label(Revervation_Frame,text="Room Price",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)        # Membuat label tulisan Room Price dengan format dan warna tulisan yang disesuaikan
        self.lblRoomPrice.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                           # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboRoomPrice=ttk.Combobox(Revervation_Frame,textvariable=self.var_roomprice,font=("arial",10,"bold"),width=17,state="readonly")  # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data 
        self.ComboRoomPrice.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                                         # Mengatur grid/posisi Entry
        # Quantity Room
        self.lblQuantityRoom=Label(Revervation_Frame,text="Qty",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)            # Membuat label tulisan QTY dengan format dan warna tulisan yang disesuaikan            
        self.lblQuantityRoom.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtQuantityRoom=ttk.Entry(Revervation_Frame,textvariable=self.var_quantity,font=("arial",10,"bold"),width=20)      # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data 
        self.txtQuantityRoom.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi Entry
        # No Of Days
        self.lblNoOfDays=Label(Revervation_Frame,text="No Of Days",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)         # Membuat label tulisan No of Days dengan format dan warna tulisan yang disesuaikan
        self.lblNoOfDays.grid(row=3,column=0,sticky=W,padx=5,pady=2)                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtNoOfDays=ttk.Entry(Revervation_Frame,textvariable=self.var_noofdays,font=("arial",10,"bold"),width=20)          # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtNoOfDays.grid(row=3,column=1,sticky=W,padx=5,pady=2)                                                            # Mengatur grid/posisi Entry
        # Check-In
        self.lblCheckIn=Label(Revervation_Frame,text="Check-In Date",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)       # Membuat label tulisan Check-In Date dengan format dan warna tulisan yang disesuaikan
        self.lblCheckIn.grid(row=4,column=0,sticky=W,padx=5,pady=2)                                                             # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCheckIn=ttk.Entry(Revervation_Frame,textvariable=self.var_checkin,font=("arial",10,"bold"),width=20)            # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCheckIn.grid(row=4,column=1,sticky=W,padx=5,pady=2)                                                             # Mengatur grid/posisi Entry
        # Early Check-In
        self.lblEarlyCheckIn=Label(Revervation_Frame,text="Earliest Check-In",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                                                  # Membuat label tulisan Early Check-In dengan format dan warna tulisan yang disesuaikan
        self.lblEarlyCheckIn.grid(row=0,column=2,sticky=W,padx=5,pady=2)                                                                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboEarlyCheckIn=ttk.Combobox(Revervation_Frame,value=self.EarlyCheckInlist,textvariable=self.var_earlycheckin,font=("arial",10,"bold"),width=19,state="readonly")    # Membuat Combobox pilihan Early Check-In
        self.ComboEarlyCheckIn.current(0)                                                                                       # Dengan melakukan set daat program dijalankan otomatis memunculkan value index 0 pada combobox 
        self.ComboEarlyCheckIn.grid(row=0,column=3,sticky=W,padx=5,pady=2)                                                      # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboEarlyCheckIn.bind("<<ComboboxSelected>>",self.LateCheckOut_Add)                                               # Mengatur menggunakan method bind agar user dapat memiliki value combobos sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                    # Dan data Late Check-Out hanya dapat diisi user setelah memilih Early Chech-In
        # Late Check-Out
        self.lblLateCheckOut=Label(Revervation_Frame,text="Late Check-Out",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                         # Membuat label tulisan Latest Check-Out dengan format dan warna tulisan yang disesuaikan
        self.lblLateCheckOut.grid(row=1,column=2,sticky=W,padx=5,pady=2)                                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboLateCheckOut=ttk.Combobox(Revervation_Frame,textvariable=self.var_latecheckout,font=("arial",10,"bold"),width=19,state="readonly")    # Membuat Combobox pilihan Latest Check-Out 
        self.ComboLateCheckOut.grid(row=1,column=3,sticky=W,padx=5,pady=2)                                                                              # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboLateCheckOut.bind("<<ComboboxSelected>>",self.Meal_Add)                                                                               # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                            # Dan data Meal hanya dapat diisi user setelah memilih Latest Check-Out
        # Meal
        self.lblMeal=Label(Revervation_Frame,text="Meal",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                               # Membuat label tulisan Meal dengan format dan warna tulisan yang disesuaikan
        self.lblMeal.grid(row=2,column=2,sticky=W,padx=5,pady=2)                                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboMeal=ttk.Combobox(Revervation_Frame,textvariable=self.var_meal,font=("arial",10,"bold"),width=19,state="readonly")        # Membuat Combobox pilihan Meal
        self.ComboMeal.grid(row=2,column=3,sticky=W,padx=5,pady=2)                                                                          # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboMeal.bind("<<ComboboxSelected>>",self.PaymentMethod_Add)                                                                  # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                # Dan data Payment Moethod hanya dapat diisi user setelah memilih Meal
        # Payment Method
        self.lblPaymentMethod=Label(Revervation_Frame,text="Payment Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                            # Membuat label tulisan Payment Method dengan format dan warna tulisan yang disesuaikan
        self.lblPaymentMethod.grid(row=3,column=2,sticky=W,padx=5,pady=2)                                                                                   # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboPaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_paymentmethod,font=("arial",10,"bold"),width=19,state="readonly")      # Membuat Combobox pilihan Payment Method
        self.ComboPaymentMethod.grid(row=3,column=3,sticky=W,padx=5,pady=2)                                                                                 # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboPaymentMethod.bind("<<ComboboxSelected>>",self.OnlinePaymentMethod_Add)                                                                   # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                                # Dan data Online Payment Method hanya dapat diisi bila user memilih payment method "Non-Cash"
        # Online Pay Method
        self.lblOnlinePaymentMethod=Label(Revervation_Frame,text="Online Pay Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                           # Membuat label tulisan Online Payment Method dengan format dan warna tulisan yang disesuaikan
        self.lblOnlinePaymentMethod.grid(row=4,column=2,sticky=W,padx=5,pady=2)                                                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboOnlinePaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_onlinepayment,font=("arial",10,"bold"),width=19,state="readonly")        # Membuat Combobox pilihan Payment Method
        self.ComboOnlinePaymentMethod.grid(row=4,column=3,sticky=W,padx=5,pady=2)                                                                                   # Mengatur grid/posisi combobox dari baris dan kolomnya
                                                                                                                                                                        # Mengatur menggunakan readonly agar user tidak dapat menghapus value combobox sesuai keinginan dari pilihan value yang tersedia
        
        # =====================Foto bawah =================================
        MiddleFrame1=Frame(Main_Frame,bd=10)                        # Membuat frame baru untuk foto hiasan dan info tambahan
        MiddleFrame1.place(x=10,y=370,width=1010,height=400)        # Mengatur koordinat frame
        
        # Foto hiasan kiri
        img12=Image.open(r"images\SoloParagon5.jpg")                                                        # Menginput gambar "SoloParagon3.jpg"
        img12=img12.resize((505,400),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg12=ImageTk.PhotoImage(img12)                                                           # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img12=Label(MiddleFrame1,image=self.photoimg12)                                                 # Mengatur format foto yang disesuaikan
        lbl_img12.place(x=-8,y=-8,width=505,height=130)                                                     # Mengatur gambar pada frame dengan jarak terhadap sumbu x=-8 pixel, sumbu y=-8 pixel, dan panjang lebar disesuaikan
        # Foto hiasan kanan
        img13=Image.open(r"images\SoloParagon2.jpg")                                    # Menginput gambar "SoloParagon2.jpg"
        img13=img13.resize((505,400),Image.ANTIALIAS)                                   # Mengubah dimensi ukuran gambar
        self.photoimg13=ImageTk.PhotoImage(img13)                                       # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img13=Label(MiddleFrame1,image=self.photoimg13)                             # Mengatur format foto yang disesuaikan
        lbl_img13.place(x=505,y=-8,width=505,height=130)                                # Mengatur gambar pada frame dengan jarak terhadap sumbu x=505 pixel, sumbu y=-8 pixel, dan panjang lebar disesuaikan
        

        # ===================== Foto Tengah =================================
        MiddleFrame2=Frame(Main_Frame,bd=10)                    # Membuat frame baru untuk foto keterangan fasilitas kamar
        MiddleFrame2.place(x=375,y=208,width=645,height=156)    # Mengatur koordinat frame
        # Foto Tabel Facilities
        img14=Image.open(r"images\SoloParagon6.png")                    # Menginput gambar "SoloParagon2.jpg"
        img14=img14.resize((645,156),Image.ANTIALIAS)                   # Mengubah dimensi ukuran gambar
        self.photoimg14=ImageTk.PhotoImage(img14)                       # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img14=Label(MiddleFrame2,image=self.photoimg14)             # Mengatur format foto yang disesuaikan
        lbl_img14.place(x=-10,y=-10,width=645,height=156)               # Mengatur gambar pada frame dengan jarak terhadap sumbu x=-10 pixel, sumbu y=-10 pixel, dan panjang lebar disesuaikan
        
        
        # ====================== Search Bill =====================================
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")          # Membuat frame baru untuk search bill
        Search_Frame.place(x=1050,y=15,width=500,height=40)     # Mengatur koordinat frame

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")                # Membuat label tulisan Bill Number dengan format dan warna tulisan yang disesuaikan
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)                                                               # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)   # Membuat Entry pada frame search bill yang digunakan sebagai tempat user memasukkan data 
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)                                                      # Mengatur grid/posisi Entry
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")     # Membuat tombol search bill untuk membuka bill yang telah tersimpan dan dibuka pada frame bill Solo Paragon Hotel 
        self.BtnSearch.grid(row=0,column=2)                                                                             # Mengatur posisi tombol search bill
        
        # ====================== Right Frame Bill Area ======================
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat frame baru untuk bill area dengan format yang disesuaikan
        RightLabelFrame.place(x=1030,y=45,width=480,height=440)                                                             # Mengatur koordinat dan ukuran frame

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)                                                                         # Membuat scrollbar arah vertikal
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))     # Membuat text area yang dapat discroll dengan format yang disesuaikan
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # ====================== Bill Counter Label Frame ===========================           # Tabel perhitungan harga total kamar, pajak, dan total biaya
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat tabel perhitungan harga total kamar, pajak, dan total biaya
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)                                     # Mengatur posisi dan ukuran frame
        # Sub Total
        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                   # Membuat label tulisan Sub Total dengan format dan warna tulisan yang disesuaikan
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtSubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=24,state="readonly")     # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan sub total
        self.txtSubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi Entry
        # Gov Tax
        self.lblGovTax=Label(Bottom_Frame,text="Gov Tax",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                       # Membuat label tulisan Gov Total dengan format dan warna tulisan yang disesuaikan
        self.lblGovTax.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtGovTax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=24,state="readonly")       # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan pajak total
        self.txtGovTax.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi Entry
        # Amount Total
        self.lblAmount=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                         # Membuat label tulisan Amount Total dengan format dan warna tulisan yang disesuaikan
        self.lblAmount.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtAmount=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24,state="readonly")           # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan total biaya
        self.txtAmount.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi Entry


        # ================ Button Frame =========================   # Frame Berbagai Tombol
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")               # Membuat frame baru untuk tombol Add to chart, Generate Bill, Print, Clear, Back
        Btn_Frame.place(x=320,y=0)                                  # Mengatur posisi frame tombol-tombol
        
        # Btn Add To Cart
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")     # Membuat tombol Add to chart dengan format dan warna yang disesuaikan
        self.BtnAddToCart.grid(row=0,column=0,padx=1)                                               # Mengatur posisi tombol Add to chart
        global datakamar,jumlahkamar,lamamenginap,totalhargakamar,hargahargakamardipesan            # Menjadikan variabel datakamar,jumlahkamar,lamamenginap,totalhargakamar,hargahargakamardipesan  
        datakamar=[]                                                # Menjadikan variabel datakamar menjadi data list
        jumlahkamar=[]                                              # Menjadikan variabel jumlahkamar menjadi data list
        lamamenginap=[]                                             # Menjadikan variabel lamamenginap menjadi data list
        hargahargakamardipesan=[]                                   # Menjadikan variabel hargahargakamardipesan menjadi data list
        totalhargakamar=[]                                          # Menjadikan variabel totalhargakamar menjadi data list
        # Btn Generate
        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")  # Membuat tombol Generate Bill dengan format dan warna yang disesuaikan
        self.BtnGenerate_bill.grid(row=0,column=1,padx=1)                                           # Mengatur posisi tombol Generate Bill
        # Btn Save Bill
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")      # Membuat tombol Save Bill dengan format dan warna yang disesuaikan
        self.BtnSave.grid(row=0,column=2)                                                           # Mengatur posisi tombol Generate Bill
        # Btn Print
        self.BtnPrint=Button(Btn_Frame,command=self.printbill,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")    # Membuat tombol Print Bill dengan format dan warna yang disesuaikan
        self.BtnPrint.grid(row=0,column=3)                                                          # Mengatur posisi tombol Print Bill
        # Btn Clear
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")      # Membuat tombol Clear Bill dengan format dan warna yang disesuaikan
        self.BtnClear.grid(row=0,column=4)                                                          # Mengatur posisi tombol Clear Bill
        # Btn Back
        self.BtnBack=Button(Btn_Frame,command=self.root.destroy,height=2,text="Back",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")    # Membuat tombol Back dengan format dan warna yang disesuaikan
        self.BtnBack.grid(row=0,column=5)                                                           # Mengatur posisi tombol Back
        self.welcome()                      # Memanggil nama fungsi welcome setelah klik tombol Add to cart
        self.l=[]                           # Memanggil variabel l setelah klik tombol Add to cart agar memulai perhitungan dan memunculkan nominal pada frame bill counting


    # ============================= FUNCTION DECLARATION ==============================
    def AddItem(self):                                                          # Membuat fungsi AddItem dengan parameter self
        Tax=1                                                                   # Melakukan pemisalan Tax=1
        self.n=self.var_roomprice.get()                                         # membuat variabel self.n yang nantinya akan berisi nilai dari variabel harga kamar
        self.m=self.var_quantity.get()*self.n                                   # membuat variabel self.m yang nantinya akan berisi nilai hasil perkalian harga kamar * jumlah kamar
        self.o=self.var_noofdays.get()*self.m                                   # membuat variabel self.o yang nantinya akan berisi nilai hasil dari harga kamar * jumlah kamar * lama menginap
        self.l.append(self.o)                                                   # membuat variabel self.l yang nantinya akan berisi nilai dari self.o dan penambahannya
        if self.var_roomtype.get()=="Select Type":                                      # Membuat decision bila user klik tombol Add to cart namun belum memilih tipe kamar
            messagebox.showerror("Error","Please Select The Room Type Name")            # Maka akan muncul notiifikasi error dan meminta untuk memilih tipe kamar
            self.new_window=Toplevel(self.root)                                         # Lalu akan memunculkan layar baru dengan Toplevel
            self.app=Bill_App1(self.new_window)                                         # Membuka kembali window Bill_App1
        else:                                                                                   # Membuat decision lain (bila user memilih tipe kamar)
            self.textarea.insert(END,f"\n {self.var_roomtype.get()}\t\t{self.var_quantity.get()}\t          {self.var_noofdays.get()}\t\t        {self.o}")     # Menginput dan memunculkan data tipe kamar,jumlah,lama menginap, dan total harga kamar pada frame bill text area
            self.sub_total.set(str('Rp.%.2f'%(sum(self.l))))                                                                    # Menghitung dan memunculkan nilai subtotal setelah dilakukan perhitungan pada frame Bill Counting
            self.tax_input.set(str('Rp.%.2f'%((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))                         # Menghitung dan memunculkan nilai pajak setelah dilakukan perhitungan pada frame Bill Counting
            self.total.set(str('Rp.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))))         # Menghitung dan memunculkan nilai total setelah dilakukan perhitungan pada frame Bill Counting
            datakamar.append(self.var_roomtype.get())                       # Memasukkan data tipe kamar ke data listnya dan memasukkan ke csv
            jumlahkamar.append(self.var_quantity.get())                     # Memasukkan data jumlah kamar ke data listnya dan memasukkan ke csv
            lamamenginap.append(self.var_noofdays.get())                    # Memasukkan data lama menginap ke data listnya dan memasukkan ke csv
            totalhargakamar.append(self.o)                                  # Memasukkan data totalhargakamar ke data listnya dan memasukkan ke csv
            hargahargakamardipesan.append(self.var_roomprice.get())         # Memasukkan data harga-harga kamar ke data listnya dan memasukkan ke csv

    def gen_bill(self):                                                                             # Membuat fungsi gen_bil untuk generate bill dengan parameter self
        if self.var_roomtype.get()=="Select Type":                                                  # Membuat decision saat user klik tombol generate bill namun belum memilih tipe kamar
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")       # Maka akan memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                                     # Membuka kembali window Bill
            self.app=Bill_App1(self.new_window)
        if self.var_paymentmethod.get()=="Select Pay Method":                                       # Membuat decision saat user klik tombol generate bill namun belum memilih jenis metode pembayaran
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")       # Maka akan memunculkan notiifikasi error 
            self.new_window=Toplevel(self.root)                                                     # Membuka kembali window Bill
            self.app=Bill_App1(self.new_window)
        else:
            text=self.textarea.get(20.0,(24.0+float(len(self.l))))                                              # membuat variabel text yang akan mengambil data pada baris 20.0 sampai 24.0+len(self.l)
            self.welcome()                                                                                      # Mengisi value pada self.welcome (data pemesan dan informasi hasil biaya)
            self.textarea.insert(END,text)                                                                      # Memasukkan ke textarea setelah data paling akhir dari text area                                                                  
            self.textarea.insert(END,"==================================================")                      
            self.textarea.insert(END,"\n ~ ADDITIONAL INFORMATION ~\n")
            self.textarea.insert(END,f"\n Check-In Date\t\t\t: {self.var_checkin.get()}")           # Memasukkan data Check-In Date ke text area
            if self.var_earlycheckin.get()=="Select Time":                                          # Decision saat belum memilih Early Check-In
                messagebox.showerror("Error","Please Select Earliest Check-In Time")                # Muncul notifikasi error
                self.new_window=Toplevel(self.root)                                             # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App1(self.new_window)                                             # Membukanya adalah window Bill_App1
            else:
                self.textarea.insert(END,f"\n Earliest Check-In Date\t\t\t: {self.var_earlycheckin.get()}")     # Memasukkan data Earlist Check-In ke text area
            
            if self.var_latecheckout.get()=="Select Time":                          # Decision saat belum memilih late check-out
                messagebox.showerror("Error","Please Select Check-Out Time")        # Muncul notifikasi error
                self.new_window=Toplevel(self.root)                                 # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App1(self.new_window)                                 # Membukanya adalah window Bill_App1
            else:
                self.textarea.insert(END,f"\n Late Check-Out\t\t\t: {self.var_latecheckout.get()}")     # Memasukkan data Late Check-Out ke text area
            
            if self.var_meal.get()=="Select Meal":                          # Decision saat belum memilih Meal
                messagebox.showerror("Error","Please Select Meal")          # Muncul notifikasi error  
                self.new_window=Toplevel(self.root)                         # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App1(self.new_window)                         # Membukanya adalah window Bill_App1
            else:
                self.textarea.insert(END,f"\n Meal\t\t\t: {self.var_meal.get()}")   # Memasukkan data Meal ke text area
            
            if self.var_paymentmethod.get()=="Cash":                                                    # Decision saat memilih cash
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")    # Memasukkan data Payment Method ke text area
            
            if self.var_paymentmethod.get()=="Non-Cash":                                                        # Decision saat memilih Non-cash
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")            # Memasukkan data Payment Method ke text area
                self.textarea.insert(END,f"\n Online Payment Method\t\t\t: {self.var_onlinepayment.get()}")     # Memasukkan data Online Payment Method ke text area
            self.textarea.insert(END,"\n==================================================")
            
            if self.var_onlinepayment.get()=="Credit Card":                                                 # Decision saat memilih Credit Card
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")           # Memasukkan data No.rek CV Conforging ke text area
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")         # Memasukkan data Code bayar ke text area
            if self.var_onlinepayment.get()=="Debit Card":                                              # Decision saat memilih Credit Card
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")       # Memasukkan data No.rek CV Conforging ke text area
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")     # Memasukkan data Code bayar ke text area
            self.textarea.insert(END,f"\n Sub Amount\t\t\t: {self.sub_total.get()}")            # Memasukkan data Sub Amount ke text area
            self.textarea.insert(END,f"\n Tax Amount\t\t\t: {self.tax_input.get()}")            # Memasukkan data Tax Amount ke text area
            self.textarea.insert(END,f"\n Total Amount\t\t\t: {self.total.get()}")              # Memasukkan data Total Amount ke text area
            self.textarea.insert(END,"\n==================================================")
            newcustomer = {'Bill Number' : [str(self.bill_no.get())],                           # Membuat variabel newcustomer yang berisi data dictionary dengan kata kunci dan valuenya mendapatkan nilai kata kunci tersebut
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
            userpemesan = pd.DataFrame(newcustomer)                                                         # Membuat variabel newcustomer yang menghubungkan dengan pandas
            userpemesan.to_csv('pemesanankamarsoloparagon.csv', mode='a', index=False, header=False)        # Memasukkan data ke csv
            
    def save_bill(self):                                                    # Membuat fungsi save_bill dengan parameter self agar bill dapat disimpan user
        if self.var_roomtype.get()=="Select Type":                                      # Membuat decision bila user belum memilih jenis kamar
            messagebox.showerror("Error","Please CLick Generate Bill")                  # Akan Memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                         # Lalu akan membuka windows baru dengan toplevel
            self.app=Bill_App1(self.new_window)                                         # windownya adalah Bill_App1
        else:
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")         # Memunculkan messagebox untuk meminta user memilih ya atau tidak
            if op:                                                                                    # Membuat situasi jika user pilih ya save bill  
                self.bill_data=self.textarea.get(1.0,END)                                             # Mendapatkan nilai dari baris 1 sampai akhir dalam bill
                f1=open('bills/'+str(self.bill_no.get())+".txt",'w')                                  # Membuka file bills.txt dan memanggil nomor bill lalu menggunakan parameter mode 'w' untuk mereplace file dan diganti dengan yang baru ditulis
                f1.write(self.bill_data)                                                                # Masukkan data pada file bills.txt
                op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Successfully!")     # Membuat notifikasi bila bill dengan nomor tertentu berhasil disimpan
                f1.close()                                                                              # Menutup file bills.txt agar menjamin bahwa file akan tetap ditutup walaupun ada error sebelumnya
 
    def printbill(self):                                                                   # Membuat fungsi print bill dengan parameter self agar user dapat melakukan print bill
        if self.var_roomtype.get()=="Select Type":                              # Membuat decision jika user belum memilih jenis kamar
            messagebox.showerror("Error","Please CLick Generate Bill")          # Memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                 # Memunculkan windows baru dengan TopLevel
            self.app=Bill_App1(self.new_window)                                 # Windownya adalah Bill_App1
        else:
            q=self.textarea.get(1.0,"end-1c")                   # Mengambil data pada keseluruhan bill
            filename=tempfile.mktemp('.txt')                    # Menggunakan modul tempfile (TemporaryFile) untuk file sementara
            open(filename,'w').write(q)                         # Merename nama file
            os.startfile(filename,"print")                      # Melakukan proses printing
    
    def find_bill(self):                                        # Membuat  fungsi find_bill dengan parameter self 
        found="no"                                              # membuat acuan awal found="no"
        for i in os.listdir("bills/"):                          # membuat looping bila i ada dalam os.listdir (fungsi individual) 
            if i.split('.')[0]==self.search_bill.get():         # bila data momor bill yang dimasukkan user = nomor bill yang sudah pernah disave sebelumnya
                f1=open(f'bills/{i}','r')                       # Maka akan membuka folder bills
                self.textarea.delete(1.0,END)                   # dan menghapus semua valuenya
                for d in f1:                                        # looping bila d ada pada salah satu file di folser bills
                    self.textarea.insert(END,d)                     # maka akan memasukkan data-data value pada frame bill
                f1.close()                                          # Menutup file agar lebih aman
                found="yes"                                         # menjadikan found menjadi bernilai yes
        if found=="no":                                         # jika tidak ditemukan nomor bill
            messagebox.showerror("Error","Invalid Bill No.")    # maka akan muncul messagebox error
            self.new_window=Toplevel(self.root)                 # membuka window baru dengan toplevel agar berada di posisi paling atas
            self.app=Bill_App1(self.new_window)                 # windownya adalah Bill_app1

    def clear(self):                                    # Membuat fungsi clear bill dengan parameter self
        self.textarea.delete(1.0,END)                   # Menghapus semua value dalam frame bill
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))                        # Dan mengganti dengan nomor kode baru
        self.var_cust_name.set("")                      # Menjadikan Cust name menjadi kosong kembali
        self.var_gender.set("")                         # Menjadikan Cust gender menjadi kosong kembali
        self.var_post.set("")                           # Menjadikan Cust post code menjadi kosong kembali
        self.var_mobile.set(+62)                        # Menjadikan Cust mobile menjadi kosong kembali
        self.var_email.set("")                          # Menjadikan Cust email menjadi kosong kembali
        self.var_provinsi.set("")                       # Menjadikan Cust provinsi menjadi kosong kembali
        self.var_id_type.set("")                        # Menjadikan Cust idItype menjadi kosong kembali
        self.var_id_number.set(0)                       # Menjadikan Cust id number menjadi kosong kembali
        self.var_address.set("")                        # Menjadikan Cust addres menjadi kosong kembali
        self.var_roomtype.set("")                       # Menjadikan room type menjadi kosong kembali
        self.var_roomprice.set(0)                       # Menjadikan room price menjadi kosong kembali
        self.var_quantity.set(0)                        # Menjadikan quantity room menjadi kosong kembali
        self.var_noofdays.set(0)                        # Menjadikan lama menginap menjadi kosong kembali
        self.var_checkin.set("")                        # Menjadikan data checkin menjadi kosong kembali
        self.var_earlycheckin.set("")                   # Menjadikan data early checkin menjadi kosong kembali
        self.var_latecheckout.set("")                   # Menjadikan data latest cehckout menjadi kosong kembali
        self.var_paymentmethod.set("")                  # Menjadikan onlinepayment menjadi kosong kembali
        self.var_onlinepayment.set("")                  # Menjadikan online payment menjadi kosong kembali
        z=random.randint(2000,9999)                     
        self.bill_no.set(str(x))                        # Melakukan set nomor bill yang baru
        self.search_bill.set("")                        # Menjadikan data search bill menjadi kosong kembali
        self.l=[0]                                      # Menjadikan rumus perhitungan menjadi kosong kembali
        self.total.set(0)                               # Menjadikan value total biaya menjadi kosong kembali 
        self.sub_total.set(0)                           # Menjadikan value sub total menjadi kosong kembali
        self.tax_input.set(0)                           # Menjadikan value biaya tax menjadi kosong kembali
        self.welcome()                                  # Memasukkan kembali variabel-variabel template pada frame  
        
    def welcome(self):                                                                                  # Membuat fungsi welcome dengan parameter self untuk sebagai template awal yang muncul pada frame bill dengan datanya sendiri masih kosong
        self.textarea.delete(1.0,END)                                                                   # Menghapus semua value pada variabel menjadi nol/kosong
        self.textarea.insert(END,"\t ~ WELCOME TO MR.CONFORGING SOLO ~\n")                              # Menampilkan judul pada bill frame
        self.textarea.insert(END,f"\n Bill Number\t\t\t: {self.bill_no.get()}")                         # Menampilkan bill number pada bill frame
        self.textarea.insert(END,f"\n Customer Ref\t\t\t: {self.var_ref.get()}")                        # Menampilkan customer ref pada bill frame
        self.textarea.insert(END,f"\n Customer Name\t\t\t: {self.var_cust_name.get()}")                 # Menampilkan customer name pada bill frame
        self.textarea.insert(END,f"\n Gender\t\t\t: {self.var_gender.get()}")                           # Menampilkan cust gender pada bill frame
        self.textarea.insert(END,f"\n PostCode\t\t\t: {self.var_post.get()}")                           # Menampilkan postcode pada bill frame
        self.textarea.insert(END,f"\n Mobil No.\t\t\t: {self.var_mobile.get()}")                        # Menampilkan mobile number cust pada bill frame
        self.textarea.insert(END,f"\n Email\t\t\t: {self.var_email.get()}")                             # Menampilkan cust email pada bill frame
        self.textarea.insert(END,f"\n Provincial Origin\t\t\t: {self.var_provinsi.get()}")              # Menampilkan cust provincial origin pada bill frame
        self.textarea.insert(END,f"\n ID Proof Type\t\t\t: {self.var_id_type.get()}")                   # Menampilkan tipe Id Proof pada bill frame
        self.textarea.insert(END,f"\n ID Number\t\t\t: {self.var_id_number.get()}")                     # Menampilkan nomor id cust pada bill frame
        self.textarea.insert(END,f"\n Address\t\t\t: {self.var_address.get()}")                         # Menampilkan address pada bill frame

        self.textarea.insert(END,"\n==================================================")                        # Variasi Bill
        self.textarea.insert(END,'\t\t\t "SOLO PARAGON HOTEL & RESIDENCES"\n')                                  # Menampilkan keterangan nama hotel
        self.textarea.insert(END,'\n  Jl. Dr. Sutomo, Mangkubumen, Kec. Banjarsari, Kota Surakarta\n')          # Menampilkan keterangan alamat hotel
        self.textarea.insert(END,f"\n  Room Type\t\tQuantity\t          No of Days\t\t        Room Price")      # Menampilkan keterangan Jenis kamar,jumlah,lama menginap, dan total harga kamar 
        self.textarea.insert(END,"\n==================================================")                        # Variasi bill
   
    def PriceRoomsType(self,event=""):                                              # Membuat fungsi PriceRoomsType dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboRoomType.get()=="Suite 2 Bedrooms":                            # Membuat decision bila memilih kamar jenis 1 
            self.ComboRoomPrice.config(value=self.price_Suite2Bedrooms)             # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 1
            self.ComboRoomPrice.current(0)                                          # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Deluxe Room":                     # Membuat decision bila memilih kamar jenis 2        
            self.ComboRoomPrice.config(value=self.price_DeluxeRoom)     # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 2
            self.ComboRoomPrice.current(0)                              # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                    # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                    # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Superior Room":                           # Membuat decision bila memilih kamar jenis 3
            self.ComboRoomPrice.config(value=self.price_SuperiorRoom)           # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 3
            self.ComboRoomPrice.current(0)                                      # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                            # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                            # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Executive Room":                                   # Membuat decision bila memilih kamar jenis 4
            self.ComboRoomPrice.config(value=self.price_ExecutiveRoom)                   # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 4
            self.ComboRoomPrice.current(0)                                               # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                     # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                     # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        
    def LateCheckOut_Add(self,event=""):                                    # Membuat fungsi LateCheckOut_Add dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu 
        if self.ComboEarlyCheckIn.get()=="09.00 WIB":                       # Membuat decision bila memilih waktu 09.00 WIB di early checkin
            self.ComboLateCheckOut.config(value=self.LateCheckOut)          # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel latecheckout
            self.ComboLateCheckOut.current(0)                               # Meng set late checkout otomatis membaca index 0                        
        if self.ComboEarlyCheckIn.get()=="13.00 WIB":                   # Membuat decision bila memilih waktu 13.00 WIB di early checkin
            self.ComboLateCheckOut.config(value=self.LateCheckOut)      # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel latecheckout
            self.ComboLateCheckOut.current(0)                           # Meng set late checkout otomatis membaca index 0
    
    def Meal_Add(self,event=""):                             # Membuat fungsi Meal dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu    
        if self.ComboLateCheckOut.get()=="15.00 WIB":           # Membuat decision bila memilih waktu 15.00 WIB di late checkout
            self.ComboMeal.config(value=self.Meallist)          # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel meallist
            self.ComboMeal.current(0)                           # Meng set meal otomatis membaca index 0
        if self.ComboLateCheckOut.get()=="18.00 WIB":               # Membuat decision bila memilih waktu 18.00 WIB di late checkout
            self.ComboMeal.config(value=self.Meallist)              # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel meallist
            self.ComboMeal.current(0)                               # Meng set meal otomatis membaca index 0

    def PaymentMethod_Add(self,event=""):                                   # Membuat fungsi PaymentMethod dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboMeal.get()=="Breakfast":                               # Membuat decision bila memilih waktu breakfast di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)    # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                              # Meng set paymentmethod otomatis membaca index 0
        if self.ComboMeal.get()=="Lunch":                                           # Membuat decision bila memilih waktu lunch di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)            # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                                      # Meng set paymentmethod otomatis membaca index 0
        if self.ComboMeal.get()=="Dinner":                                      # Membuat decision bila memilih waktu dinner di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)        # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                                  # Meng set paymentmethod otomatis membaca index 0

    def OnlinePaymentMethod_Add(self,event=""):                                         # Membuat fungsi OnlinePaymentMethod dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboPaymentMethod.get()=="Non-Cash":                                   # Membuat decision bila memilih Non-Cash di Payment method
            self.ComboOnlinePaymentMethod.config(value=self.OnlinePaymentMethodlist)    # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel OnlinePaymentMethodlist
            self.ComboOnlinePaymentMethod.current(0)                                    # Meng set onlinepaymentmethod otomatis membaca index 0

# HOTEL ALANA
class Bill_App2:                                                                        # Membuat class berisi gabungan dari beberapa fungsi untuk user melakukan pemesanan kamar dan mendapatkan bill di Hotel Alana
    def __init__(self,root):                                                            # Mendefinisikan fungsi dalam class dengan nama __init__ dengan parameternya harus "self" (merujuk pada objek class) dan ada parameter tambahan yaitu "root"
        self.root=root                                                                  # Membuat properti root dengan sintaks self.root dan memberikan nilai dari root
        self.root.geometry("1530x800+0+0")                                              # Membuat ukuran window billing hotel dengan panjang 1530 pixel, lebar 800 pixel, bergeser 0 pixel dari sumbu X, bergeser 0 pixel dari sumbu Y 
        self.root.title("Billing Mr.Conforging Solo")                                   # Membuat judul window dengan nama Billing Mr.Conforging Solo


        # ================== Variables =======================
        self.var_ref=StringVar()                            # Membuat variabel var_ref dengan parameternya self dengan jenis datanya String
        x=random.randint(1000,9999)                             # Membuat variabel x untuk random angka mulai dari 1000 sampai 9999-1 
        self.var_ref.set(str(x))                                # Melakukan set untuk var_ref agar angka random muncul otomatis

        self.var_cust_name=StringVar()                      # Membuat variabel var_cust_name dengan parameternya self dengan jenis datanya String
        self.var_gender=StringVar()                         # Membuat variabel var_gender dengan parameternya self dengan jenis datanya String
        self.var_post=StringVar()                           # Membuat variabel var_post dengan parameternya self dengan jenis datanya String
        self.var_mobile=IntVar()                            # Membuat variabel var_mobile dengan parameternya self dengan jenis datanya Integer
        self.var_mobile.set("+62" + str())                      # Melakukan set untuk var_mobile agar diawal otomatis terisi "+62"

        self.var_email=StringVar()                          # Membuat variabel var_email dengan parameternya self dengan jenis datanya String
        self.var_provinsi=StringVar()                       # Membuat variabel var_provinsi dengan parameternya self dengan jenis datanya String
        self.var_id_type=StringVar()                        # Membuat variabel var_id_type dengan parameternya self dengan jenis datanya String
        self.var_id_number=StringVar()                      # Membuat variabel var_id_number dengan parameternya self dengan jenis datanya String
        self.var_address=StringVar()                        # Membuat variabel var_address dengan parameternya self dengan jenis datanya String

        self.var_roomtype=StringVar()                       # Membuat variabel var_roomtype dengan parameternya self dengan jenis datanya String
        self.var_roomprice=IntVar()                         # Membuat variabel var_roomprice dengan parameternya self dengan jenis datanya Integer
        self.var_quantity=IntVar()                          # Membuat variabel var_quantity dengan parameternya self dengan jenis datanya Integer
        self.var_noofdays=IntVar()                          # Membuat variabel var_noofdays dengan parameternya self dengan jenis datanya Integer
        self.var_checkin=StringVar()                        # Membuat variabel var_checkin dengan parameternya self dengan jenis datanya String
        self.var_earlycheckin=StringVar()                   # Membuat variabel var_earlycheckin dengan parameternya self dengan jenis datanya String
        self.var_latecheckout=StringVar()                   # Membuat variabel var_latecheckout dengan parameternya self dengan jenis datanya String
        self.var_meal=StringVar()                           # Membuat variabel var_meal dengan parameternya self dengan jenis datanya String
        self.var_paymentmethod=StringVar()                  # Membuat variabel var_paymentmethod dengan parameternya self dengan jenis datanya String
        self.var_onlinepayment=StringVar()                  # Membuat variabel var_onlinepayment dengan parameternya self dengan jenis datanya String
        
        self.bill_no=StringVar()                            # Membuat variabel bill_no dengan parameternya self dengan jenis datanya String
        z=random.randint(1000,9999)                             # Membuat variabel z untuk random angka mulai dari 1000 sampai 9999-1
        self.bill_no.set(z)                                     # Melakukan set untuk var_ref agar angka random muncul otomatis

        self.search_bill=StringVar()                        # Membuat variabel search_bill dengan parameternya self dengan jenis datanya String               
        self.sub_total=StringVar()                          # Membuat variabel sub_total dengan parameternya self dengan jenis datanya String
        self.tax_input=StringVar()                          # Membuat variabel tax_input dengan parameternya self dengan jenis datanya String
        self.total=StringVar()                              # Membuat variabel total dengan parameternya self dengan jenis datanya String

        # Var Code Pembayaran
        self.var_codebayartunai=StringVar()                                         # Membuat variabel var_codebayartunai dengan parameternya self dengan jenis datanya String
        u=random.randint(1000000000,9999999999)                                         # Membuat variabel u untuk random angka mulai dari 1000000000 sampai 9999999999-1
        self.var_codebayartunai.set(u)                                                  # Melakukan set untuk var_codebayartunai agar angka random muncul otomatis

        # Reservation Room Type List
        self.RoomType=["Select Type","Superior Room","Deluxe Room","Superior Family Room","Deluxe Family","Junior Suite","Presidents Suite"]     # Membuat data list RoomType dengan parameter self
        self.price_SuperiorRoom=592200                                                       # Membuat variabel price_Suite2Bedrooms dengan parameter self bernilai 1091698
        self.price_DeluxeRoom=815341                                                         # Membuat variabel price_DeluxeRoom dengan parameter self bernilai 558178
        self.price_SuperiorFamilyRoom=904851                                                 # Membuat variabel price_SuperiorRoom dengan parameter self bernilai 499999 
        self.price_DeluxeFamily=912035                                                       # Membuat variabel price_ExecutiveRoom dengan parameter self bernilai 852629
        self.price_JuniorSuite=1484762
        self.price_PresidentsSuite=2526084

        # Early Check In                                    
        self.EarlyCheckInlist=["Select Time","09.00 WIB", "13.00 WIB"]              # Membuat data list EarlyCheckInlist dengan parameter self
        self.EarlyCheckIn1="09.00 WIB"                                              # Membuat variabel EarlyCheckIn1 dengan parameter self bernilai 09.00 WIB
        self.EarlyCheckIn2="13.00 WIB"                                              # Membuat variabel EarlyCheckIn2 dengan parameter self bernilai 13.00 WIB

        # Late Check Out
        self.LateCheckOut=["Select Time","15.00 WIB", "18.00 WIB"]                  # Membuat data list LateCheckOut dengan parameter self
        self.LateCheckOut1="15.00 WIB"                                              # Membuat variabel LateCheckOut1 dengan parameter self bernilai 15.00 WIB
        self.LateCheckOut2="18.00 WIB"                                              # Membuat variabel LateCheckOut2 dengan parameter self bernilai 18.00 WIB

        # Meal
        self.Meallist=["Select Meal","Breakfast","Lunch","Dinner"]                  # Membuat data list Meallist dengan parameter self
        self.Meal1="Breakfast"                                                      # Membuat variabel Meal1 dengan parameter self bernilai Breakfast
        self.Meal2="Lunch"                                                          # Membuat variabel Meal2 dengan parameter self bernilai Lunch
        self.Meal3="Dinner"                                                         # Membuat variabel Meal3 dengan parameter self bernilai Dinner

        # Payment Method
        self.PaymentMethodlist=["Select Pay Method","Cash","Non-Cash"]              # Membuat data list PaymentMethodlist dengan parameter self
        self.PaymentMethod1="Cash"                                                  # Membuat variabel PaymentMethod1 dengan parameter self bernilai Cash
        self.PaymentMethod2="Non-Cash"                                              # Membuat variabel PaymentMethod2 dengan parameter self bernilai Non-Cash
        

        # Online Payment Method
        self.OnlinePaymentMethodlist=["Select Online Meth.","Credit Card","Debit Card","Gopay","OVO","ShoopePay","Dana"]    # Membuat data list OnlinePaymentMethodlist dengan parameter self
        self.OnlinePaymentMethodlist1="Credit Card"                                 # Membuat variabel OnlinePaymentMethodlist1 dengan parameter self bernilai Credir Card
        self.OnlinePaymentMethodlist2="Debit Card"                                  # Membuat variabel OnlinePaymentMethodlist2 dengan parameter self bernilai Debit Card
        self.OnlinePaymentMethodlist3="Gopay"                                       # Membuat variabel OnlinePaymentMethodlist3 dengan parameter self bernilai Gopay
        self.OnlinePaymentMethodlist4="OVO"                                         # Membuat variabel OnlinePaymentMethodlist4 dengan parameter self bernilai OVO
        self.OnlinePaymentMethodlist5="ShoopePay"                                   # Membuat variabel OnlinePaymentMethodlist5 dengan parameter self bernilai ShoopePay
        self.OnlinePaymentMethodlist6="Dana"                                        # Membuat variabel OnlinePaymentMethodlist6 dengan parameter self bernilai Dana
        
        # Foto Atas Kiri
        img=Image.open(r"images\Alana1.jpg")     # Menginput gambar "Alana1.jpg"
        img=img.resize((500,130),Image.ANTIALIAS)                                                           # Mengubah dimensi ukuran gambar
        self.photoimg=ImageTk.PhotoImage(img)                                                               # Menginput gambar ke Tkinter pada frame Billing Alana Hotel
        lbl_img=Label(self.root,image=self.photoimg)                                                        # Mengatur format foto yang disesuaikan
        lbl_img.place(x=0,y=0,width=500,height=130)                                                         # Mengatur gambar pada frame dengan jarak terhadap sumbu x=0 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan
        
        # Foto Atas Tengah
        img_1=Image.open(r"images\Alana2.jpg")   # Menginput gambar "Alana2.jpg"
        img_1=img_1.resize((500,130),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg_1=ImageTk.PhotoImage(img_1)                                                           # Menginput gambar ke Tkinter pada frame Billing Alana Hotel
        lbl_img_1=Label(self.root,image=self.photoimg_1)                                                    # Mengatur format foto yang disesuaikan
        lbl_img_1.place(x=500,y=0,width=500,height=130)                                                     # Mengatur gambar pada frame dengan jarak terhadap sumbu x=500 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan
        
        # Foto Atas Kanan
        img_2=Image.open(r"images\Alana3.jpg")   # Menginput gambar "Alana3.jpg"
        img_2=img_2.resize((550,130),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg_2=ImageTk.PhotoImage(img_2)                                                           # Menginput gambar ke Tkinter pada frame Billing Alana Hotel
        lbl_img_2=Label(self.root,image=self.photoimg_2)                                                    # Mengatur format foto yang disesuaikan
        lbl_img_2.place(x=1000,y=0,width=550,height=130)                                                    # Mengatur gambar pada frame dengan jarak terhadap sumbu x=1000 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan

        # Membuat label tulisan Nama Hotel
        lbl_title=Label(self.root,text="THE ALANA HOTEL AND CONVENTION CENTER SOLO",font=("times new roman",35,"bold"),bg="brown",fg="white")  # Membuat label bertuliskan Nama Hotel dengan font dan format yang disesuaikan
        lbl_title.place(x=0,y=130,width=1550,height=45)                                                     # Mengatur posisi label dengan koordinat yang disesuaikan
        
        def time():                                 # Membuat fungsi time untuk waktu terkini
            string=strftime('%H:%M:%S %p')          # Membuat variabel bernama string yang bernilai fungsi strtime dengan value Jam,Menit,Detik,Am/Pm
            lbl.config(text=string)                 # Mengubah text pada lbl menjadi string
            lbl.after(1000,time)                    # Mmebuat label lbl dengan method after dengan value 1000 sampai time
        
        lbl=Label(lbl_title,font=("times new roman",16,'bold'),background='brown',foreground='gold')    # menjadikan lbl menjadi label dengan font dan warna yang disesuaikan 
        lbl.place(x=0,y=0,width=120,height=45)                                                          # mengatur posisi label waktu
        time()                                                                                          # Mengembalikan fungsi time
        
        # ===== Main Frame =====
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")               # Membuat frame utama dengan format dan warna yang disesuaikan
        Main_Frame.place(x=0,y=175,width=1530,height=620)                       # Mengatur koordinat dan ukuran frame utama
        
        # ==================Customer Label Frame======================          # Membuat Frame Data Diri Pemesan Kamar
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details",font=("times new roman",12,"bold"),bg="white",fg="brown")  # Membuat frame kotak bingkai bertuliskan "Customer Details" dengan format dan warna yang disesuaikan 
        Cust_Frame.place(x=10,y=5,width=355,height=360)                                                                     # Mengatur posisi frame kotak bingkai 
        # Cust Ref
        self.lblCustRef=Label(Cust_Frame,text="Customer Ref",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)       # Membuat label tulisan Customer Ref dengan format dan warna tulisan yang disesuaikan
        self.lblCustRef.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.entryCustRef=ttk.Entry(Cust_Frame,textvariable=self.var_ref,font=("arial",10,"bold"),width=26)             # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.entryCustRef.grid(row=0,column=1,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi Entry
        #Cust Name
        self.lblCustName=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)     # Membuat label tulisan Customer Name dengan format dan warna tulisan yang disesuaikan
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                    # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.var_cust_name,font=("arial",10,"bold"),width=26)        # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                    # Mengatur grid/posisi Entry
        #Cust Gender
        self.lblCustGender=Label(Cust_Frame,text="Gender",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)          # Membuat label tulisan Gender dengan format dan warna tulisan yang disesuaikan
        self.lblCustGender.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustGender=ttk.Combobox(Cust_Frame,textvariable=self.var_gender,font=("arial",10,"bold"),width=23,state="readonly")   # Membuat Combobox Gender
        self.comboCustGender["value"]=("","Male","Female","Other")                                                                      # Dengan membuat beberapa value
        self.comboCustGender.current(0)                                                                                                 # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustGender.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust PostCode
        self.lblCustPostCode=Label(Cust_Frame,text="PostCode",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)      # Membuat label tulisan PostCode dengan format dan warna tulisan yang disesuaikan 
        self.lblCustPostCode.grid(row=3,column=0,sticky=W,padx=5,pady=2)                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustPostCode=ttk.Entry(Cust_Frame,textvariable=self.var_post,font=("arial",10,"bold"),width=26)         # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustPostCode.grid(row=3,column=1,sticky=W,padx=5,pady=2)                                                # Mengatur grid/posisi Entry
        #Cust Mobile
        self.lblCustMob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat label tulisan CustMobile dengan format dan warna tulisan yang disesuaikan
        self.lblCustMob.grid(row=4,column=0,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustMob=ttk.Entry(Cust_Frame,textvariable=self.var_mobile,font=("times new roman",10,"bold"),width=26)  # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustMob.grid(row=4,column=1,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi Entry
        #Cust Email
        self.lblCustEmail=Label(Cust_Frame,text="Email",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)            # Membuat label tulisan Email dengan format dan warna tulisan yang disesuaikan
        self.lblCustEmail.grid(row=5,column=0,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustEmail=ttk.Entry(Cust_Frame,textvariable=self.var_email,font=("arial",10,"bold"),width=26)           # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustEmail.grid(row=5,column=1,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi Entry
        #Cust Provinsi
        self.lblCustProvinsi=Label(Cust_Frame,text="Provincial Origin",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                                     # Membuat label tulisan Provincial Origin dengan format dan warna tulisan yang disesuaikan
        self.lblCustProvinsi.grid(row=6,column=0,sticky=W,padx=5,pady=2)                                                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustProvinsi=ttk.Combobox(Cust_Frame,textvariable=self.var_provinsi,font=("arial",10,"bold"),width=23,state="readonly")                       # Membuat Combobox Provinsi 
        self.comboCustProvinsi["value"]=("","Aceh","Sumatera Utara","Sumatera Barat","Sumatera Selatan","Riau","Jambi","Bangka Belitung","Kepulauan Riau",      # Dengan membuat value nama-nama provinsi di Indonesia
                           "Bengkulu","Lampung","Banten","DKI Jakarta","Jawa Barat","Jawa Tengah","Jawa Timur","DIY Yogyakarta","Bali",
                           "Nusa Tenggara Barat","Nusa Tenggara Timur","Kalimantan Barat","Kalimantan Selatan","Kalimantan Tengah",
                           "Kalimantan Timur","Kalimantan Utara","Sulawesi Utara","Sulawesi Tengah","Sulawesi Tenggara","Sulawesi Selatan",
                           "Sulawesi Barat","Maluku","Maluku Utara","Gorontalo","Papua","Papua Barat")
        self.comboCustProvinsi.current(0)                                                                                                                       # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustProvinsi.grid(row=6,column=1,sticky=W,padx=5,pady=2)                                                                                      # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust Id Type
        self.lblCustIdType=Label(Cust_Frame,text="ID Proof Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                       # Membuat label tulisan ID Proof Type dengan format dan warna tulisan yang disesuaikan
        self.lblCustIdType.grid(row=7,column=0,sticky=W,padx=5,pady=2)                                                                      # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustIdType=ttk.Combobox(Cust_Frame,textvariable=self.var_id_type,font=("arial",10,"bold"),width=23,state="readonly")      # Membuat Combobox ID Proof Type
        self.comboCustIdType["value"]=("","KTP","SIM","Passport")                                                                           # Dengan membuat beberapa value 
        self.comboCustIdType.current(0)                                                                                                     # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustIdType.grid(row=7,column=1,sticky=W,padx=5,pady=2)                                                                    # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust Id Number
        self.lblCustIdNumber=Label(Cust_Frame,text="ID Number",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)             # Membuat label tulisan ID Number dengan format dan warna tulisan yang disesuaikan
        self.lblCustIdNumber.grid(row=8,column=0,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustIdNumber=ttk.Entry(Cust_Frame,textvariable=self.var_id_number,font=("arial",10,"bold"),width=26)            # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustIdNumber.grid(row=8,column=1,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi Entry
        #Cust Address
        self.lblCustAddress=Label(Cust_Frame,text="Address",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                # Membuat label tulisan Address dengan format dan warna tulisan yang disesuaikan
        self.lblCustAddress.grid(row=9,column=0,sticky=W,padx=5,pady=2)                                                         # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustAddress=ttk.Entry(Cust_Frame,textvariable=self.var_address,font=("arial",10,"bold"),width=26)               # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustAddress.grid(row=9,column=1,sticky=W,padx=5,pady=2)                                                         # Mengatur grid/posisi Entry

        
        # ======================Reservation Label Frame===========================          # Membuat Frame Reservasi Kamar
        Revervation_Frame=LabelFrame(Main_Frame,text="Room Reservation",font=("times new roman",12,"bold"),bg="white",fg="brown")   # Membuat frame kotak bingkai bertuliskan "Room Reservation" dengan format dan warna yang disesuaikan
        Revervation_Frame.place(x=375,y=5,width=645,height=195)                                                                     # Mengatur posisi frame kotak bingkai
        # Room Type
        self.lblRoomType=Label(Revervation_Frame,text="Room Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)              # Membuat label tulisan Room Type dengan format dan warna tulisan yang disesuaikan
        self.lblRoomType.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboRoomType=ttk.Combobox(Revervation_Frame,value=self.RoomType,textvariable=self.var_roomtype,font=("arial",10,"bold"),width=17,state="readonly")    # Membuat Combobox Tipe Kamar
        self.ComboRoomType.current(0)                                                   # Dengan melakukan set daat program dijalankan otomatis memunculkan value index 0 pada combobox
        self.ComboRoomType.grid(row=0,column=1,sticky=W,padx=5,pady=2)                  # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboRoomType.bind("<<ComboboxSelected>>",self.PriceRoomsType)             # Mengatur menggunakan method bind agar user dapat memiliki value combobos sesuai keinginan dari pilihan value yang tersedia 
                                                                                            # Sekaligus saat user memilih value tertentu maka value Room Price, Quantity, dan No of Days otomatis terisi suatu value
                                                                                            # Dan data Room Price, Quantity, dan No of Days hanya dapat diisi user setelah memilih Room Type
        # Room Price
        self.lblRoomPrice=Label(Revervation_Frame,text="Room Price",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)        # Membuat label tulisan Room Price dengan format dan warna tulisan yang disesuaikan
        self.lblRoomPrice.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                           # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboRoomPrice=ttk.Combobox(Revervation_Frame,textvariable=self.var_roomprice,font=("arial",10,"bold"),width=17,state="readonly")  # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data 
        self.ComboRoomPrice.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                                         # Mengatur grid/posisi Entry
        # Quantity Room
        self.lblQuantityRoom=Label(Revervation_Frame,text="Qty",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)            # Membuat label tulisan QTY dengan format dan warna tulisan yang disesuaikan            
        self.lblQuantityRoom.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtQuantityRoom=ttk.Entry(Revervation_Frame,textvariable=self.var_quantity,font=("arial",10,"bold"),width=20)      # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data 
        self.txtQuantityRoom.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi Entry
        # No Of Days
        self.lblNoOfDays=Label(Revervation_Frame,text="No Of Days",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)         # Membuat label tulisan No of Days dengan format dan warna tulisan yang disesuaikan
        self.lblNoOfDays.grid(row=3,column=0,sticky=W,padx=5,pady=2)                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtNoOfDays=ttk.Entry(Revervation_Frame,textvariable=self.var_noofdays,font=("arial",10,"bold"),width=20)          # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtNoOfDays.grid(row=3,column=1,sticky=W,padx=5,pady=2)                                                            # Mengatur grid/posisi Entry
        # Check-In
        self.lblCheckIn=Label(Revervation_Frame,text="Check-In Date",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)       # Membuat label tulisan Check-In Date dengan format dan warna tulisan yang disesuaikan
        self.lblCheckIn.grid(row=4,column=0,sticky=W,padx=5,pady=2)                                                             # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCheckIn=ttk.Entry(Revervation_Frame,textvariable=self.var_checkin,font=("arial",10,"bold"),width=20)            # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCheckIn.grid(row=4,column=1,sticky=W,padx=5,pady=2)                                                             # Mengatur grid/posisi Entry
        # Early Check-In
        self.lblEarlyCheckIn=Label(Revervation_Frame,text="Earliest Check-In",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                                                  # Membuat label tulisan Early Check-In dengan format dan warna tulisan yang disesuaikan
        self.lblEarlyCheckIn.grid(row=0,column=2,sticky=W,padx=5,pady=2)                                                                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboEarlyCheckIn=ttk.Combobox(Revervation_Frame,value=self.EarlyCheckInlist,textvariable=self.var_earlycheckin,font=("arial",10,"bold"),width=19,state="readonly")    # Membuat Combobox pilihan Early Check-In
        self.ComboEarlyCheckIn.current(0)                                                                                       # Dengan melakukan set daat program dijalankan otomatis memunculkan value index 0 pada combobox 
        self.ComboEarlyCheckIn.grid(row=0,column=3,sticky=W,padx=5,pady=2)                                                      # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboEarlyCheckIn.bind("<<ComboboxSelected>>",self.LateCheckOut_Add)                                               # Mengatur menggunakan method bind agar user dapat memiliki value combobos sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                    # Dan data Late Check-Out hanya dapat diisi user setelah memilih Early Chech-In
        # Late Check-Out
        self.lblLateCheckOut=Label(Revervation_Frame,text="Late Check-Out",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                         # Membuat label tulisan Latest Check-Out dengan format dan warna tulisan yang disesuaikan
        self.lblLateCheckOut.grid(row=1,column=2,sticky=W,padx=5,pady=2)                                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboLateCheckOut=ttk.Combobox(Revervation_Frame,textvariable=self.var_latecheckout,font=("arial",10,"bold"),width=19,state="readonly")    # Membuat Combobox pilihan Latest Check-Out 
        self.ComboLateCheckOut.grid(row=1,column=3,sticky=W,padx=5,pady=2)                                                                              # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboLateCheckOut.bind("<<ComboboxSelected>>",self.Meal_Add)                                                                               # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                            # Dan data Meal hanya dapat diisi user setelah memilih Latest Check-Out
        # Meal
        self.lblMeal=Label(Revervation_Frame,text="Meal",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                               # Membuat label tulisan Meal dengan format dan warna tulisan yang disesuaikan
        self.lblMeal.grid(row=2,column=2,sticky=W,padx=5,pady=2)                                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboMeal=ttk.Combobox(Revervation_Frame,textvariable=self.var_meal,font=("arial",10,"bold"),width=19,state="readonly")        # Membuat Combobox pilihan Meal
        self.ComboMeal.grid(row=2,column=3,sticky=W,padx=5,pady=2)                                                                          # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboMeal.bind("<<ComboboxSelected>>",self.PaymentMethod_Add)                                                                  # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                # Dan data Payment Moethod hanya dapat diisi user setelah memilih Meal
        # Payment Method
        self.lblPaymentMethod=Label(Revervation_Frame,text="Payment Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                            # Membuat label tulisan Payment Method dengan format dan warna tulisan yang disesuaikan
        self.lblPaymentMethod.grid(row=3,column=2,sticky=W,padx=5,pady=2)                                                                                   # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboPaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_paymentmethod,font=("arial",10,"bold"),width=19,state="readonly")      # Membuat Combobox pilihan Payment Method
        self.ComboPaymentMethod.grid(row=3,column=3,sticky=W,padx=5,pady=2)                                                                                 # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboPaymentMethod.bind("<<ComboboxSelected>>",self.OnlinePaymentMethod_Add)                                                                   # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                                # Dan data Online Payment Method hanya dapat diisi bila user memilih payment method "Non-Cash"
        # Online Pay Method
        self.lblOnlinePaymentMethod=Label(Revervation_Frame,text="Online Pay Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                           # Membuat label tulisan Online Payment Method dengan format dan warna tulisan yang disesuaikan
        self.lblOnlinePaymentMethod.grid(row=4,column=2,sticky=W,padx=5,pady=2)                                                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboOnlinePaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_onlinepayment,font=("arial",10,"bold"),width=19,state="readonly")        # Membuat Combobox pilihan Payment Method
        self.ComboOnlinePaymentMethod.grid(row=4,column=3,sticky=W,padx=5,pady=2)                                                                                   # Mengatur grid/posisi combobox dari baris dan kolomnya
                                                                                                                                                                        # Mengatur menggunakan readonly agar user tidak dapat menghapus value combobox sesuai keinginan dari pilihan value yang tersedia
        
        # =====================Foto bawah =================================
        MiddleFrame1=Frame(Main_Frame,bd=10)                        # Membuat frame baru untuk foto hiasan dan info tambahan
        MiddleFrame1.place(x=10,y=370,width=1010,height=400)        # Mengatur koordinat frame
        
        # Foto hiasan kiri
        img12=Image.open(r"images\Alana4.jpg")                                                        # Menginput gambar "Alana3.jpg"
        img12=img12.resize((505,400),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg12=ImageTk.PhotoImage(img12)                                                           # Menginput gambar ke Tkinter pada frame Billing Alana Hotel
        lbl_img12=Label(MiddleFrame1,image=self.photoimg12)                                                 # Mengatur format foto yang disesuaikan
        lbl_img12.place(x=-8,y=-8,width=505,height=130)                                                     # Mengatur gambar pada frame dengan jarak terhadap sumbu x=-8 pixel, sumbu y=-8 pixel, dan panjang lebar disesuaikan
        # Foto hiasan kanan
        img13=Image.open(r"images\Alana5.jpg")                                    # Menginput gambar "Alana2.jpg"
        img13=img13.resize((505,400),Image.ANTIALIAS)                                   # Mengubah dimensi ukuran gambar
        self.photoimg13=ImageTk.PhotoImage(img13)                                       # Menginput gambar ke Tkinter pada frame Billing Alana Hotel
        lbl_img13=Label(MiddleFrame1,image=self.photoimg13)                             # Mengatur format foto yang disesuaikan
        lbl_img13.place(x=505,y=-8,width=505,height=130)                                # Mengatur gambar pada frame dengan jarak terhadap sumbu x=505 pixel, sumbu y=-8 pixel, dan panjang lebar disesuaikan
        

        # ===================== Foto Tengah =================================
        MiddleFrame2=Frame(Main_Frame,bd=10)                    # Membuat frame baru untuk foto keterangan fasilitas kamar
        MiddleFrame2.place(x=375,y=208,width=645,height=156)    # Mengatur koordinat frame
        # Foto Tabel Facilities
        img14=Image.open(r"images\Alana6.png")                    # Menginput gambar "Alana2.jpg"
        img14=img14.resize((645,156),Image.ANTIALIAS)                   # Mengubah dimensi ukuran gambar
        self.photoimg14=ImageTk.PhotoImage(img14)                       # Menginput gambar ke Tkinter pada frame Billing Alana Hotel
        lbl_img14=Label(MiddleFrame2,image=self.photoimg14)             # Mengatur format foto yang disesuaikan
        lbl_img14.place(x=-10,y=-10,width=645,height=156)               # Mengatur gambar pada frame dengan jarak terhadap sumbu x=-10 pixel, sumbu y=-10 pixel, dan panjang lebar disesuaikan
        
        
        # ====================== Search Bill =====================================
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")          # Membuat frame baru untuk search bill
        Search_Frame.place(x=1050,y=15,width=500,height=40)     # Mengatur koordinat frame

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")                # Membuat label tulisan Bill Number dengan format dan warna tulisan yang disesuaikan
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)                                                               # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)   # Membuat Entry pada frame search bill yang digunakan sebagai tempat user memasukkan data 
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)                                                      # Mengatur grid/posisi Entry
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")     # Membuat tombol search bill untuk membuka bill yang telah tersimpan dan dibuka pada frame bill Alana Hotel 
        self.BtnSearch.grid(row=0,column=2)                                                                             # Mengatur posisi tombol search bill
        
        # ====================== Right Frame Bill Area ======================
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat frame baru untuk bill area dengan format yang disesuaikan
        RightLabelFrame.place(x=1030,y=45,width=480,height=440)                                                             # Mengatur koordinat dan ukuran frame

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)                                                                         # Membuat scrollbar arah vertikal
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))     # Membuat text area yang dapat discroll dengan format yang disesuaikan
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # ====================== Bill Counter Label Frame ===========================           # Tabel perhitungan harga total kamar, pajak, dan total biaya
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat tabel perhitungan harga total kamar, pajak, dan total biaya
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)                                     # Mengatur posisi dan ukuran frame
        # Sub Total
        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                   # Membuat label tulisan Sub Total dengan format dan warna tulisan yang disesuaikan
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtSubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=24,state="readonly")     # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan sub total
        self.txtSubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi Entry
        # Gov Tax
        self.lblGovTax=Label(Bottom_Frame,text="Gov Tax",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                       # Membuat label tulisan Gov Total dengan format dan warna tulisan yang disesuaikan
        self.lblGovTax.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtGovTax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=24,state="readonly")       # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan pajak total
        self.txtGovTax.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi Entry
        # Amount Total
        self.lblAmount=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                         # Membuat label tulisan Amount Total dengan format dan warna tulisan yang disesuaikan
        self.lblAmount.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtAmount=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24,state="readonly")           # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan total biaya
        self.txtAmount.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi Entry


        # ================ Button Frame =========================   # Frame Berbagai Tombol
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")               # Membuat frame baru untuk tombol Add to chart, Generate Bill, Print, Clear, Back
        Btn_Frame.place(x=320,y=0)                                  # Mengatur posisi frame tombol-tombol
        
        # Btn Add To Cart
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")     # Membuat tombol Add to chart dengan format dan warna yang disesuaikan
        self.BtnAddToCart.grid(row=0,column=0,padx=1)                                               # Mengatur posisi tombol Add to chart
        global datakamar,jumlahkamar,lamamenginap,totalhargakamar,hargahargakamardipesan            # Menjadikan variabel datakamar,jumlahkamar,lamamenginap,totalhargakamar,hargahargakamardipesan  
        datakamar=[]                                                # Menjadikan variabel datakamar menjadi data list
        jumlahkamar=[]                                              # Menjadikan variabel jumlahkamar menjadi data list
        lamamenginap=[]                                             # Menjadikan variabel lamamenginap menjadi data list
        hargahargakamardipesan=[]                                   # Menjadikan variabel hargahargakamardipesan menjadi data list
        totalhargakamar=[]                                          # Menjadikan variabel totalhargakamar menjadi data list
        # Btn Generate
        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")  # Membuat tombol Generate Bill dengan format dan warna yang disesuaikan
        self.BtnGenerate_bill.grid(row=0,column=1,padx=1)                                           # Mengatur posisi tombol Generate Bill
        # Btn Save Bill
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")      # Membuat tombol Save Bill dengan format dan warna yang disesuaikan
        self.BtnSave.grid(row=0,column=2)                                                           # Mengatur posisi tombol Generate Bill
        # Btn Print
        self.BtnPrint=Button(Btn_Frame,command=self.printbill,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")    # Membuat tombol Print Bill dengan format dan warna yang disesuaikan
        self.BtnPrint.grid(row=0,column=3)                                                          # Mengatur posisi tombol Print Bill
        # Btn Clear
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")      # Membuat tombol Clear Bill dengan format dan warna yang disesuaikan
        self.BtnClear.grid(row=0,column=4)                                                          # Mengatur posisi tombol Clear Bill
        # Btn Back
        self.BtnBack=Button(Btn_Frame,command=self.root.destroy,height=2,text="Back",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")    # Membuat tombol Back dengan format dan warna yang disesuaikan
        self.BtnBack.grid(row=0,column=5)                                                           # Mengatur posisi tombol Back
        self.welcome()                      # Memanggil nama fungsi welcome setelah klik tombol Add to cart
        self.l=[]                           # Memanggil variabel l setelah klik tombol Add to cart agar memulai perhitungan dan memunculkan nominal pada frame bill counting


    # ============================= FUNCTION DECLARATION ==============================
    def AddItem(self):                                                          # Membuat fungsi AddItem dengan parameter self
        Tax=1                                                                   # Melakukan pemisalan Tax=1
        self.n=self.var_roomprice.get()                                         # membuat variabel self.n yang nantinya akan berisi nilai dari variabel harga kamar
        self.m=self.var_quantity.get()*self.n                                   # membuat variabel self.m yang nantinya akan berisi nilai hasil perkalian harga kamar * jumlah kamar
        self.o=self.var_noofdays.get()*self.m                                   # membuat variabel self.o yang nantinya akan berisi nilai hasil dari harga kamar * jumlah kamar * lama menginap
        self.l.append(self.o)                                                   # membuat variabel self.l yang nantinya akan berisi nilai dari self.o dan penambahannya
        if self.var_roomtype.get()=="Select Type":                                      # Membuat decision bila user klik tombol Add to cart namun belum memilih tipe kamar
            messagebox.showerror("Error","Please Select The Room Type Name")            # Maka akan muncul notiifikasi error dan meminta untuk memilih tipe kamar
            self.new_window=Toplevel(self.root)                                         # Lalu akan memunculkan layar baru dengan Toplevel
            self.app=Bill_App2(self.new_window)                                         # Membuka kembali window Bill_App2
        else:                                                                                   # Membuat decision lain (bila user memilih tipe kamar)
            self.textarea.insert(END,f"\n {self.var_roomtype.get()}\t\t{self.var_quantity.get()}\t          {self.var_noofdays.get()}\t\t        {self.o}")     # Menginput dan memunculkan data tipe kamar,jumlah,lama menginap, dan total harga kamar pada frame bill text area
            self.sub_total.set(str('Rp.%.2f'%(sum(self.l))))                                                                    # Menghitung dan memunculkan nilai subtotal setelah dilakukan perhitungan pada frame Bill Counting
            self.tax_input.set(str('Rp.%.2f'%((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))                         # Menghitung dan memunculkan nilai pajak setelah dilakukan perhitungan pada frame Bill Counting
            self.total.set(str('Rp.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))))         # Menghitung dan memunculkan nilai total setelah dilakukan perhitungan pada frame Bill Counting
            datakamar.append(self.var_roomtype.get())                       # Memasukkan data tipe kamar ke data listnya dan memasukkan ke csv
            jumlahkamar.append(self.var_quantity.get())                     # Memasukkan data jumlah kamar ke data listnya dan memasukkan ke csv
            lamamenginap.append(self.var_noofdays.get())                    # Memasukkan data lama menginap ke data listnya dan memasukkan ke csv
            totalhargakamar.append(self.o)                                  # Memasukkan data totalhargakamar ke data listnya dan memasukkan ke csv
            hargahargakamardipesan.append(self.var_roomprice.get())         # Memasukkan data harga-harga kamar ke data listnya dan memasukkan ke csv

    def gen_bill(self):                                                                             # Membuat fungsi gen_bil untuk generate bill dengan parameter self
        if self.var_roomtype.get()=="Select Type":                                                  # Membuat decision saat user klik tombol generate bill namun belum memilih tipe kamar
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")       # Maka akan memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                                     # Membuka kembali window Bill
            self.app=Bill_App2(self.new_window)
        if self.var_paymentmethod.get()=="Select Pay Method":                                       # Membuat decision saat user klik tombol generate bill namun belum memilih jenis metode pembayaran
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")       # Maka akan memunculkan notiifikasi error 
            self.new_window=Toplevel(self.root)                                                     # Membuka kembali window Bill
            self.app=Bill_App2(self.new_window)
        else:
            text=self.textarea.get(20.0,(24.0+float(len(self.l))))                                              # membuat variabel text yang akan mengambil data pada baris 20.0 sampai 24.0+len(self.l)
            self.welcome()                                                                                      # Mengisi value pada self.welcome (data pemesan dan informasi hasil biaya)
            self.textarea.insert(END,text)                                                                      # Memasukkan ke textarea setelah data paling akhir dari text area                                                                  
            self.textarea.insert(END,"==================================================")                      
            self.textarea.insert(END,"\n ~ ADDITIONAL INFORMATION ~\n")
            self.textarea.insert(END,f"\n Check-In Date\t\t\t: {self.var_checkin.get()}")           # Memasukkan data Check-In Date ke text area
            if self.var_earlycheckin.get()=="Select Time":                                          # Decision saat belum memilih Early Check-In
                messagebox.showerror("Error","Please Select Earliest Check-In Time")                # Muncul notifikasi error
                self.new_window=Toplevel(self.root)                                             # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App2(self.new_window)                                             # Membukanya adalah window Bill_App2
            else:
                self.textarea.insert(END,f"\n Earliest Check-In Date\t\t\t: {self.var_earlycheckin.get()}")     # Memasukkan data Earlist Check-In ke text area
            
            if self.var_latecheckout.get()=="Select Time":                          # Decision saat belum memilih late check-out
                messagebox.showerror("Error","Please Select Check-Out Time")        # Muncul notifikasi error
                self.new_window=Toplevel(self.root)                                 # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App2(self.new_window)                                 # Membukanya adalah window Bill_App2
            else:
                self.textarea.insert(END,f"\n Late Check-Out\t\t\t: {self.var_latecheckout.get()}")     # Memasukkan data Late Check-Out ke text area
            
            if self.var_meal.get()=="Select Meal":                          # Decision saat belum memilih Meal
                messagebox.showerror("Error","Please Select Meal")          # Muncul notifikasi error  
                self.new_window=Toplevel(self.root)                         # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App2(self.new_window)                         # Membukanya adalah window Bill_App2
            else:
                self.textarea.insert(END,f"\n Meal\t\t\t: {self.var_meal.get()}")   # Memasukkan data Meal ke text area
            
            if self.var_paymentmethod.get()=="Cash":                                                    # Decision saat memilih cash
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")    # Memasukkan data Payment Method ke text area
            
            if self.var_paymentmethod.get()=="Non-Cash":                                                        # Decision saat memilih Non-cash
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")            # Memasukkan data Payment Method ke text area
                self.textarea.insert(END,f"\n Online Payment Method\t\t\t: {self.var_onlinepayment.get()}")     # Memasukkan data Online Payment Method ke text area
            self.textarea.insert(END,"\n==================================================")
            
            if self.var_onlinepayment.get()=="Credit Card":                                                 # Decision saat memilih Credit Card
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")           # Memasukkan data No.rek CV Conforging ke text area
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")         # Memasukkan data Code bayar ke text area
            if self.var_onlinepayment.get()=="Debit Card":                                              # Decision saat memilih Credit Card
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")       # Memasukkan data No.rek CV Conforging ke text area
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")     # Memasukkan data Code bayar ke text area
            self.textarea.insert(END,f"\n Sub Amount\t\t\t: {self.sub_total.get()}")            # Memasukkan data Sub Amount ke text area
            self.textarea.insert(END,f"\n Tax Amount\t\t\t: {self.tax_input.get()}")            # Memasukkan data Tax Amount ke text area
            self.textarea.insert(END,f"\n Total Amount\t\t\t: {self.total.get()}")              # Memasukkan data Total Amount ke text area
            self.textarea.insert(END,"\n==================================================")
            newcustomer = {'Bill Number' : [str(self.bill_no.get())],                           # Membuat variabel newcustomer yang berisi data dictionary dengan kata kunci dan valuenya mendapatkan nilai kata kunci tersebut
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
            userpemesan = pd.DataFrame(newcustomer)                                                         # Membuat variabel newcustomer yang menghubungkan dengan pandas
            userpemesan.to_csv('pemesanankamarthealanahotelandconventioncentersolo.csv', mode='a', index=False, header=False)        # Memasukkan data ke csv
            
    def save_bill(self):                                                    # Membuat fungsi save_bill dengan parameter self agar bill dapat disimpan user
        if self.var_roomtype.get()=="Select Type":                                      # Membuat decision bila user belum memilih jenis kamar
            messagebox.showerror("Error","Please CLick Generate Bill")                  # Akan Memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                         # Lalu akan membuka windows baru dengan toplevel
            self.app=Bill_App2(self.new_window)                                         # windownya adalah Bill_App2
        else:
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")         # Memunculkan messagebox untuk meminta user memilih ya atau tidak
            if op:                                                                                    # Membuat situasi jika user pilih ya save bill  
                self.bill_data=self.textarea.get(1.0,END)                                             # Mendapatkan nilai dari baris 1 sampai akhir dalam bill
                f1=open('bills/'+str(self.bill_no.get())+".txt",'w')                                  # Membuka file bills.txt dan memanggil nomor bill lalu menggunakan parameter mode 'w' untuk mereplace file dan diganti dengan yang baru ditulis
                f1.write(self.bill_data)                                                                # Masukkan data pada file bills.txt
                op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Successfully!")     # Membuat notifikasi bila bill dengan nomor tertentu berhasil disimpan
                f1.close()                                                                              # Menutup file bills.txt agar menjamin bahwa file akan tetap ditutup walaupun ada error sebelumnya
 
    def printbill(self):                                                                   # Membuat fungsi print bill dengan parameter self agar user dapat melakukan print bill
        if self.var_roomtype.get()=="Select Type":                              # Membuat decision jika user belum memilih jenis kamar
            messagebox.showerror("Error","Please CLick Generate Bill")          # Memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                 # Memunculkan windows baru dengan TopLevel
            self.app=Bill_App2(self.new_window)                                 # Windownya adalah Bill_App2
        else:
            q=self.textarea.get(1.0,"end-1c")                   # Mengambil data pada keseluruhan bill
            filename=tempfile.mktemp('.txt')                    # Menggunakan modul tempfile (TemporaryFile) untuk file sementara
            open(filename,'w').write(q)                         # Merename nama file
            os.startfile(filename,"print")                      # Melakukan proses printing
    
    def find_bill(self):                                        # Membuat  fungsi find_bill dengan parameter self 
        found="no"                                              # membuat acuan awal found="no"
        for i in os.listdir("bills/"):                          # membuat looping bila i ada dalam os.listdir (fungsi individual) 
            if i.split('.')[0]==self.search_bill.get():         # bila data momor bill yang dimasukkan user = nomor bill yang sudah pernah disave sebelumnya
                f1=open(f'bills/{i}','r')                       # Maka akan membuka folder bills
                self.textarea.delete(1.0,END)                   # dan menghapus semua valuenya
                for d in f1:                                        # looping bila d ada pada salah satu file di folser bills
                    self.textarea.insert(END,d)                     # maka akan memasukkan data-data value pada frame bill
                f1.close()                                          # Menutup file agar lebih aman
                found="yes"                                         # menjadikan found menjadi bernilai yes
        if found=="no":                                         # jika tidak ditemukan nomor bill
            messagebox.showerror("Error","Invalid Bill No.")    # maka akan muncul messagebox error
            self.new_window=Toplevel(self.root)                 # membuka window baru dengan toplevel agar berada di posisi paling atas
            self.app=Bill_App2(self.new_window)                 # windownya adalah Bill_App2

    def clear(self):                                    # Membuat fungsi clear bill dengan parameter self
        self.textarea.delete(1.0,END)                   # Menghapus semua value dalam frame bill
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))                        # Dan mengganti dengan nomor kode baru
        self.var_cust_name.set("")                      # Menjadikan Cust name menjadi kosong kembali
        self.var_gender.set("")                         # Menjadikan Cust gender menjadi kosong kembali
        self.var_post.set("")                           # Menjadikan Cust post code menjadi kosong kembali
        self.var_mobile.set(+62)                        # Menjadikan Cust mobile menjadi kosong kembali
        self.var_email.set("")                          # Menjadikan Cust email menjadi kosong kembali
        self.var_provinsi.set("")                       # Menjadikan Cust provinsi menjadi kosong kembali
        self.var_id_type.set("")                        # Menjadikan Cust idItype menjadi kosong kembali
        self.var_id_number.set(0)                       # Menjadikan Cust id number menjadi kosong kembali
        self.var_address.set("")                        # Menjadikan Cust addres menjadi kosong kembali
        self.var_roomtype.set("")                       # Menjadikan room type menjadi kosong kembali
        self.var_roomprice.set(0)                       # Menjadikan room price menjadi kosong kembali
        self.var_quantity.set(0)                        # Menjadikan quantity room menjadi kosong kembali
        self.var_noofdays.set(0)                        # Menjadikan lama menginap menjadi kosong kembali
        self.var_checkin.set("")                        # Menjadikan data checkin menjadi kosong kembali
        self.var_earlycheckin.set("")                   # Menjadikan data early checkin menjadi kosong kembali
        self.var_latecheckout.set("")                   # Menjadikan data latest cehckout menjadi kosong kembali
        self.var_paymentmethod.set("")                  # Menjadikan onlinepayment menjadi kosong kembali
        self.var_onlinepayment.set("")                  # Menjadikan online payment menjadi kosong kembali
        z=random.randint(2000,9999)                     
        self.bill_no.set(str(x))                        # Melakukan set nomor bill yang baru
        self.search_bill.set("")                        # Menjadikan data search bill menjadi kosong kembali
        self.l=[0]                                      # Menjadikan rumus perhitungan menjadi kosong kembali
        self.total.set(0)                               # Menjadikan value total biaya menjadi kosong kembali 
        self.sub_total.set(0)                           # Menjadikan value sub total menjadi kosong kembali
        self.tax_input.set(0)                           # Menjadikan value biaya tax menjadi kosong kembali
        self.welcome()                                  # Memasukkan kembali variabel-variabel template pada frame  
        
    def welcome(self):                                                                                  # Membuat fungsi welcome dengan parameter self untuk sebagai template awal yang muncul pada frame bill dengan datanya sendiri masih kosong
        self.textarea.delete(1.0,END)                                                                   # Menghapus semua value pada variabel menjadi nol/kosong
        self.textarea.insert(END,"\t ~ WELCOME TO MR.CONFORGING SOLO ~\n")                              # Menampilkan judul pada bill frame
        self.textarea.insert(END,f"\n Bill Number\t\t\t: {self.bill_no.get()}")                         # Menampilkan bill number pada bill frame
        self.textarea.insert(END,f"\n Customer Ref\t\t\t: {self.var_ref.get()}")                        # Menampilkan customer ref pada bill frame
        self.textarea.insert(END,f"\n Customer Name\t\t\t: {self.var_cust_name.get()}")                 # Menampilkan customer name pada bill frame
        self.textarea.insert(END,f"\n Gender\t\t\t: {self.var_gender.get()}")                           # Menampilkan cust gender pada bill frame
        self.textarea.insert(END,f"\n PostCode\t\t\t: {self.var_post.get()}")                           # Menampilkan postcode pada bill frame
        self.textarea.insert(END,f"\n Mobil No.\t\t\t: {self.var_mobile.get()}")                        # Menampilkan mobile number cust pada bill frame
        self.textarea.insert(END,f"\n Email\t\t\t: {self.var_email.get()}")                             # Menampilkan cust email pada bill frame
        self.textarea.insert(END,f"\n Provincial Origin\t\t\t: {self.var_provinsi.get()}")              # Menampilkan cust provincial origin pada bill frame
        self.textarea.insert(END,f"\n ID Proof Type\t\t\t: {self.var_id_type.get()}")                   # Menampilkan tipe Id Proof pada bill frame
        self.textarea.insert(END,f"\n ID Number\t\t\t: {self.var_id_number.get()}")                     # Menampilkan nomor id cust pada bill frame
        self.textarea.insert(END,f"\n Address\t\t\t: {self.var_address.get()}")                         # Menampilkan address pada bill frame

        self.textarea.insert(END,"\n==================================================")                        # Variasi Bill
        self.textarea.insert(END,'\t\t\t "THE ALANA HOTEL AND CONVENTION CENTER SOLO"\n')                                  # Menampilkan keterangan nama hotel
        self.textarea.insert(END,'\n  Jl. Adi Sucipto, Colomadu, Karanganyar, Kec. Colomadu, Kota Surakarta\n')          # Menampilkan keterangan alamat hotel
        self.textarea.insert(END,f"\n  Room Type\t\tQuantity\t          No of Days\t\t        Room Price")      # Menampilkan keterangan Jenis kamar,jumlah,lama menginap, dan total harga kamar 
        self.textarea.insert(END,"\n==================================================")                        # Variasi bill
   
    def PriceRoomsType(self,event=""):                                              # Membuat fungsi PriceRoomsType dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboRoomType.get()=="Superior Room":                            # Membuat decision bila memilih kamar jenis 1 
            self.ComboRoomPrice.config(value=self.price_SuperiorRoom)             # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 1
            self.ComboRoomPrice.current(0)                                          # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Deluxe Room":                     # Membuat decision bila memilih kamar jenis 2        
            self.ComboRoomPrice.config(value=self.price_DeluxeRoom)     # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 2
            self.ComboRoomPrice.current(0)                              # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                    # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                    # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Superior Family Room":                           # Membuat decision bila memilih kamar jenis 3
            self.ComboRoomPrice.config(value=self.price_SuperiorFamilyRoom)           # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 3
            self.ComboRoomPrice.current(0)                                      # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                            # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                            # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Deluxe Family":                                   # Membuat decision bila memilih kamar jenis 4
            self.ComboRoomPrice.config(value=self.price_DeluxeFamily)                   # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 4
            self.ComboRoomPrice.current(0)                                               # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                     # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                     # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Junior Suite":                     # Membuat decision bila memilih kamar jenis 2        
            self.ComboRoomPrice.config(value=self.price_JuniorSuite)     # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 2
            self.ComboRoomPrice.current(0)                              # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                    # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1) 
        if self.ComboRoomType.get()=="Presidents Suite":                     # Membuat decision bila memilih kamar jenis 2        
            self.ComboRoomPrice.config(value=self.price_PresidentsSuite)     # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 2
            self.ComboRoomPrice.current(0)                              # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                    # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)

    def LateCheckOut_Add(self,event=""):                                    # Membuat fungsi LateCheckOut_Add dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu 
        if self.ComboEarlyCheckIn.get()=="09.00 WIB":                       # Membuat decision bila memilih waktu 09.00 WIB di early checkin
            self.ComboLateCheckOut.config(value=self.LateCheckOut)          # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel latecheckout
            self.ComboLateCheckOut.current(0)                               # Meng set late checkout otomatis membaca index 0                        
        if self.ComboEarlyCheckIn.get()=="13.00 WIB":                   # Membuat decision bila memilih waktu 13.00 WIB di early checkin
            self.ComboLateCheckOut.config(value=self.LateCheckOut)      # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel latecheckout
            self.ComboLateCheckOut.current(0)                           # Meng set late checkout otomatis membaca index 0
    
    def Meal_Add(self,event=""):                             # Membuat fungsi Meal dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu    
        if self.ComboLateCheckOut.get()=="15.00 WIB":           # Membuat decision bila memilih waktu 15.00 WIB di late checkout
            self.ComboMeal.config(value=self.Meallist)          # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel meallist
            self.ComboMeal.current(0)                           # Meng set meal otomatis membaca index 0
        if self.ComboLateCheckOut.get()=="18.00 WIB":               # Membuat decision bila memilih waktu 18.00 WIB di late checkout
            self.ComboMeal.config(value=self.Meallist)              # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel meallist
            self.ComboMeal.current(0)                               # Meng set meal otomatis membaca index 0

    def PaymentMethod_Add(self,event=""):                                   # Membuat fungsi PaymentMethod dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboMeal.get()=="Breakfast":                               # Membuat decision bila memilih waktu breakfast di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)    # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                              # Meng set paymentmethod otomatis membaca index 0
        if self.ComboMeal.get()=="Lunch":                                           # Membuat decision bila memilih waktu lunch di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)            # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                                      # Meng set paymentmethod otomatis membaca index 0
        if self.ComboMeal.get()=="Dinner":                                      # Membuat decision bila memilih waktu dinner di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)        # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                                  # Meng set paymentmethod otomatis membaca index 0

    def OnlinePaymentMethod_Add(self,event=""):                                         # Membuat fungsi OnlinePaymentMethod dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboPaymentMethod.get()=="Non-Cash":                                   # Membuat decision bila memilih Non-Cash di Payment method
            self.ComboOnlinePaymentMethod.config(value=self.OnlinePaymentMethodlist)    # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel OnlinePaymentMethodlist
            self.ComboOnlinePaymentMethod.current(0)                                    # Meng set onlinepaymentmethod otomatis membaca index 0    

# NOVOTEL SOLO HOTEL
class Bill_App3:                                                                        # Membuat class berisi gabungan dari beberapa fungsi untuk user melakukan pemesanan kamar dan mendapatkan bill di Hotel Solo Paragon
    def __init__(self,root):                                                            # Mendefinisikan fungsi dalam class dengan nama __init__ dengan parameternya harus "self" (merujuk pada objek class) dan ada parameter tambahan yaitu "root"
        self.root=root                                                                  # Membuat properti root dengan sintaks self.root dan memberikan nilai dari root
        self.root.geometry("1530x800+0+0")                                              # Membuat ukuran window billing hotel dengan panjang 1530 pixel, lebar 800 pixel, bergeser 0 pixel dari sumbu X, bergeser 0 pixel dari sumbu Y 
        self.root.title("Billing Mr.Conforging Solo")                                   # Membuat judul window dengan nama Billing Mr.Conforging Solo


        # ================== Variables =======================
        self.var_ref=StringVar()                            # Membuat variabel var_ref dengan parameternya self dengan jenis datanya String
        x=random.randint(1000,9999)                             # Membuat variabel x untuk random angka mulai dari 1000 sampai 9999-1 
        self.var_ref.set(str(x))                                # Melakukan set untuk var_ref agar angka random muncul otomatis

        self.var_cust_name=StringVar()                      # Membuat variabel var_cust_name dengan parameternya self dengan jenis datanya String
        self.var_gender=StringVar()                         # Membuat variabel var_gender dengan parameternya self dengan jenis datanya String
        self.var_post=StringVar()                           # Membuat variabel var_post dengan parameternya self dengan jenis datanya String
        self.var_mobile=IntVar()                            # Membuat variabel var_mobile dengan parameternya self dengan jenis datanya Integer
        self.var_mobile.set("+62" + str())                      # Melakukan set untuk var_mobile agar diawal otomatis terisi "+62"

        self.var_email=StringVar()                          # Membuat variabel var_email dengan parameternya self dengan jenis datanya String
        self.var_provinsi=StringVar()                       # Membuat variabel var_provinsi dengan parameternya self dengan jenis datanya String
        self.var_id_type=StringVar()                        # Membuat variabel var_id_type dengan parameternya self dengan jenis datanya String
        self.var_id_number=StringVar()                      # Membuat variabel var_id_number dengan parameternya self dengan jenis datanya String
        self.var_address=StringVar()                        # Membuat variabel var_address dengan parameternya self dengan jenis datanya String

        self.var_roomtype=StringVar()                       # Membuat variabel var_roomtype dengan parameternya self dengan jenis datanya String
        self.var_roomprice=IntVar()                         # Membuat variabel var_roomprice dengan parameternya self dengan jenis datanya Integer
        self.var_quantity=IntVar()                          # Membuat variabel var_quantity dengan parameternya self dengan jenis datanya Integer
        self.var_noofdays=IntVar()                          # Membuat variabel var_noofdays dengan parameternya self dengan jenis datanya Integer
        self.var_checkin=StringVar()                        # Membuat variabel var_checkin dengan parameternya self dengan jenis datanya String
        self.var_earlycheckin=StringVar()                   # Membuat variabel var_earlycheckin dengan parameternya self dengan jenis datanya String
        self.var_latecheckout=StringVar()                   # Membuat variabel var_latecheckout dengan parameternya self dengan jenis datanya String
        self.var_meal=StringVar()                           # Membuat variabel var_meal dengan parameternya self dengan jenis datanya String
        self.var_paymentmethod=StringVar()                  # Membuat variabel var_paymentmethod dengan parameternya self dengan jenis datanya String
        self.var_onlinepayment=StringVar()                  # Membuat variabel var_onlinepayment dengan parameternya self dengan jenis datanya String
        
        self.bill_no=StringVar()                            # Membuat variabel bill_no dengan parameternya self dengan jenis datanya String
        z=random.randint(1000,9999)                             # Membuat variabel z untuk random angka mulai dari 1000 sampai 9999-1
        self.bill_no.set(z)                                     # Melakukan set untuk var_ref agar angka random muncul otomatis

        self.search_bill=StringVar()                        # Membuat variabel search_bill dengan parameternya self dengan jenis datanya String               
        self.sub_total=StringVar()                          # Membuat variabel sub_total dengan parameternya self dengan jenis datanya String
        self.tax_input=StringVar()                          # Membuat variabel tax_input dengan parameternya self dengan jenis datanya String
        self.total=StringVar()                              # Membuat variabel total dengan parameternya self dengan jenis datanya String

        # Var Code Pembayaran
        self.var_codebayartunai=StringVar()                                         # Membuat variabel var_codebayartunai dengan parameternya self dengan jenis datanya String
        u=random.randint(1000000000,9999999999)                                         # Membuat variabel u untuk random angka mulai dari 1000000000 sampai 9999999999-1
        self.var_codebayartunai.set(u)                                                  # Melakukan set untuk var_codebayartunai agar angka random muncul otomatis

        # Reservation Room Type List
        self.RoomType=["Select Type","Superior Twin Room","Executive Room Double Bed","Executive Room","Superior Family Room"]     # Membuat data list RoomType dengan parameter self
        self.price_SuperiorrTwinRoom=471000                                                # Membuat variabel price_Suite2Bedrooms dengan parameter self bernilai 1091698
        self.price_SuperiorRoomDoubleBed=471000                                                     # Membuat variabel price_DeluxeRoom dengan parameter self bernilai 558178
        self.price_ExecutiveRoom=621000                                                   # Membuat variabel price_SuperiorRoom dengan parameter self bernilai 499999 
        self.price_SuperiorFamilyRoom=746000                                                  # Membuat variabel price_ExecutiveRoom dengan parameter self bernilai 852629
        
        # Early Check In                                    
        self.EarlyCheckInlist=["Select Time","09.00 WIB", "13.00 WIB"]              # Membuat data list EarlyCheckInlist dengan parameter self
        self.EarlyCheckIn1="09.00 WIB"                                              # Membuat variabel EarlyCheckIn1 dengan parameter self bernilai 09.00 WIB
        self.EarlyCheckIn2="13.00 WIB"                                              # Membuat variabel EarlyCheckIn2 dengan parameter self bernilai 13.00 WIB

        # Late Check Out
        self.LateCheckOut=["Select Time","15.00 WIB", "18.00 WIB"]                  # Membuat data list LateCheckOut dengan parameter self
        self.LateCheckOut1="15.00 WIB"                                              # Membuat variabel LateCheckOut1 dengan parameter self bernilai 15.00 WIB
        self.LateCheckOut2="18.00 WIB"                                              # Membuat variabel LateCheckOut2 dengan parameter self bernilai 18.00 WIB

        # Meal
        self.Meallist=["Select Meal","Breakfast","Lunch","Dinner"]                  # Membuat data list Meallist dengan parameter self
        self.Meal1="Breakfast"                                                      # Membuat variabel Meal1 dengan parameter self bernilai Breakfast
        self.Meal2="Lunch"                                                          # Membuat variabel Meal2 dengan parameter self bernilai Lunch
        self.Meal3="Dinner"                                                         # Membuat variabel Meal3 dengan parameter self bernilai Dinner

        # Payment Method
        self.PaymentMethodlist=["Select Pay Method","Cash","Non-Cash"]              # Membuat data list PaymentMethodlist dengan parameter self
        self.PaymentMethod1="Cash"                                                  # Membuat variabel PaymentMethod1 dengan parameter self bernilai Cash
        self.PaymentMethod2="Non-Cash"                                              # Membuat variabel PaymentMethod2 dengan parameter self bernilai Non-Cash
        

        # Online Payment Method
        self.OnlinePaymentMethodlist=["Select Online Meth.","Credit Card","Debit Card","Gopay","OVO","ShoopePay","Dana"]    # Membuat data list OnlinePaymentMethodlist dengan parameter self
        self.OnlinePaymentMethodlist1="Credit Card"                                 # Membuat variabel OnlinePaymentMethodlist1 dengan parameter self bernilai Credir Card
        self.OnlinePaymentMethodlist2="Debit Card"                                  # Membuat variabel OnlinePaymentMethodlist2 dengan parameter self bernilai Debit Card
        self.OnlinePaymentMethodlist3="Gopay"                                       # Membuat variabel OnlinePaymentMethodlist3 dengan parameter self bernilai Gopay
        self.OnlinePaymentMethodlist4="OVO"                                         # Membuat variabel OnlinePaymentMethodlist4 dengan parameter self bernilai OVO
        self.OnlinePaymentMethodlist5="ShoopePay"                                   # Membuat variabel OnlinePaymentMethodlist5 dengan parameter self bernilai ShoopePay
        self.OnlinePaymentMethodlist6="Dana"                                        # Membuat variabel OnlinePaymentMethodlist6 dengan parameter self bernilai Dana
        
        # Foto Atas Kiri
        img=Image.open(r"images\Novotel1.jpg")     # Menginput gambar "SoloParagon1.jpg"
        img=img.resize((500,130),Image.ANTIALIAS)                                                           # Mengubah dimensi ukuran gambar
        self.photoimg=ImageTk.PhotoImage(img)                                                               # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img=Label(self.root,image=self.photoimg)                                                        # Mengatur format foto yang disesuaikan
        lbl_img.place(x=0,y=0,width=500,height=130)                                                         # Mengatur gambar pada frame dengan jarak terhadap sumbu x=0 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan
        
        # Foto Atas Tengah
        img_1=Image.open(r"images\Novotel2.jpg")   # Menginput gambar "SoloParagon2.jpg"
        img_1=img_1.resize((500,130),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg_1=ImageTk.PhotoImage(img_1)                                                           # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img_1=Label(self.root,image=self.photoimg_1)                                                    # Mengatur format foto yang disesuaikan
        lbl_img_1.place(x=500,y=0,width=500,height=130)                                                     # Mengatur gambar pada frame dengan jarak terhadap sumbu x=500 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan
        
        # Foto Atas Kanan
        img_2=Image.open(r"images\Novotel3.jpg")   # Menginput gambar "SoloParagon3.jpg"
        img_2=img_2.resize((550,130),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg_2=ImageTk.PhotoImage(img_2)                                                           # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img_2=Label(self.root,image=self.photoimg_2)                                                    # Mengatur format foto yang disesuaikan
        lbl_img_2.place(x=1000,y=0,width=550,height=130)                                                    # Mengatur gambar pada frame dengan jarak terhadap sumbu x=1000 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan

        # Membuat label tulisan Nama Hotel
        lbl_title=Label(self.root,text="NOVOTEL SOLO HOTEL",font=("times new roman",35,"bold"),bg="brown",fg="white")  # Membuat label bertuliskan Nama Hotel dengan font dan format yang disesuaikan
        lbl_title.place(x=0,y=130,width=1550,height=45)                                                     # Mengatur posisi label dengan koordinat yang disesuaikan
        
        def time():                                 # Membuat fungsi time untuk waktu terkini
            string=strftime('%H:%M:%S %p')          # Membuat variabel bernama string yang bernilai fungsi strtime dengan value Jam,Menit,Detik,Am/Pm
            lbl.config(text=string)                 # Mengubah text pada lbl menjadi string
            lbl.after(1000,time)                    # Mmebuat label lbl dengan method after dengan value 1000 sampai time
        
        lbl=Label(lbl_title,font=("times new roman",16,'bold'),background='brown',foreground='gold')    # menjadikan lbl menjadi label dengan font dan warna yang disesuaikan 
        lbl.place(x=0,y=0,width=120,height=45)                                                          # mengatur posisi label waktu
        time()                                                                                          # Mengembalikan fungsi time
        
        # ===== Main Frame =====
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")               # Membuat frame utama dengan format dan warna yang disesuaikan
        Main_Frame.place(x=0,y=175,width=1530,height=620)                       # Mengatur koordinat dan ukuran frame utama
        
        # ==================Customer Label Frame======================          # Membuat Frame Data Diri Pemesan Kamar
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details",font=("times new roman",12,"bold"),bg="white",fg="brown")  # Membuat frame kotak bingkai bertuliskan "Customer Details" dengan format dan warna yang disesuaikan 
        Cust_Frame.place(x=10,y=5,width=355,height=360)                                                                     # Mengatur posisi frame kotak bingkai 
        # Cust Ref
        self.lblCustRef=Label(Cust_Frame,text="Customer Ref",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)       # Membuat label tulisan Customer Ref dengan format dan warna tulisan yang disesuaikan
        self.lblCustRef.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.entryCustRef=ttk.Entry(Cust_Frame,textvariable=self.var_ref,font=("arial",10,"bold"),width=26)             # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.entryCustRef.grid(row=0,column=1,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi Entry
        #Cust Name
        self.lblCustName=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)     # Membuat label tulisan Customer Name dengan format dan warna tulisan yang disesuaikan
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                    # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.var_cust_name,font=("arial",10,"bold"),width=26)        # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                    # Mengatur grid/posisi Entry
        #Cust Gender
        self.lblCustGender=Label(Cust_Frame,text="Gender",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)          # Membuat label tulisan Gender dengan format dan warna tulisan yang disesuaikan
        self.lblCustGender.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustGender=ttk.Combobox(Cust_Frame,textvariable=self.var_gender,font=("arial",10,"bold"),width=23,state="readonly")   # Membuat Combobox Gender
        self.comboCustGender["value"]=("","Male","Female","Other")                                                                      # Dengan membuat beberapa value
        self.comboCustGender.current(0)                                                                                                 # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustGender.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust PostCode
        self.lblCustPostCode=Label(Cust_Frame,text="PostCode",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)      # Membuat label tulisan PostCode dengan format dan warna tulisan yang disesuaikan 
        self.lblCustPostCode.grid(row=3,column=0,sticky=W,padx=5,pady=2)                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustPostCode=ttk.Entry(Cust_Frame,textvariable=self.var_post,font=("arial",10,"bold"),width=26)         # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustPostCode.grid(row=3,column=1,sticky=W,padx=5,pady=2)                                                # Mengatur grid/posisi Entry
        #Cust Mobile
        self.lblCustMob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat label tulisan CustMobile dengan format dan warna tulisan yang disesuaikan
        self.lblCustMob.grid(row=4,column=0,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustMob=ttk.Entry(Cust_Frame,textvariable=self.var_mobile,font=("times new roman",10,"bold"),width=26)  # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustMob.grid(row=4,column=1,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi Entry
        #Cust Email
        self.lblCustEmail=Label(Cust_Frame,text="Email",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)            # Membuat label tulisan Email dengan format dan warna tulisan yang disesuaikan
        self.lblCustEmail.grid(row=5,column=0,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustEmail=ttk.Entry(Cust_Frame,textvariable=self.var_email,font=("arial",10,"bold"),width=26)           # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustEmail.grid(row=5,column=1,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi Entry
        #Cust Provinsi
        self.lblCustProvinsi=Label(Cust_Frame,text="Provincial Origin",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                                     # Membuat label tulisan Provincial Origin dengan format dan warna tulisan yang disesuaikan
        self.lblCustProvinsi.grid(row=6,column=0,sticky=W,padx=5,pady=2)                                                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustProvinsi=ttk.Combobox(Cust_Frame,textvariable=self.var_provinsi,font=("arial",10,"bold"),width=23,state="readonly")                       # Membuat Combobox Provinsi 
        self.comboCustProvinsi["value"]=("","Aceh","Sumatera Utara","Sumatera Barat","Sumatera Selatan","Riau","Jambi","Bangka Belitung","Kepulauan Riau",      # Dengan membuat value nama-nama provinsi di Indonesia
                           "Bengkulu","Lampung","Banten","DKI Jakarta","Jawa Barat","Jawa Tengah","Jawa Timur","DIY Yogyakarta","Bali",
                           "Nusa Tenggara Barat","Nusa Tenggara Timur","Kalimantan Barat","Kalimantan Selatan","Kalimantan Tengah",
                           "Kalimantan Timur","Kalimantan Utara","Sulawesi Utara","Sulawesi Tengah","Sulawesi Tenggara","Sulawesi Selatan",
                           "Sulawesi Barat","Maluku","Maluku Utara","Gorontalo","Papua","Papua Barat")
        self.comboCustProvinsi.current(0)                                                                                                                       # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustProvinsi.grid(row=6,column=1,sticky=W,padx=5,pady=2)                                                                                      # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust Id Type
        self.lblCustIdType=Label(Cust_Frame,text="ID Proof Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                       # Membuat label tulisan ID Proof Type dengan format dan warna tulisan yang disesuaikan
        self.lblCustIdType.grid(row=7,column=0,sticky=W,padx=5,pady=2)                                                                      # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustIdType=ttk.Combobox(Cust_Frame,textvariable=self.var_id_type,font=("arial",10,"bold"),width=23,state="readonly")      # Membuat Combobox ID Proof Type
        self.comboCustIdType["value"]=("","KTP","SIM","Passport")                                                                           # Dengan membuat beberapa value 
        self.comboCustIdType.current(0)                                                                                                     # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustIdType.grid(row=7,column=1,sticky=W,padx=5,pady=2)                                                                    # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust Id Number
        self.lblCustIdNumber=Label(Cust_Frame,text="ID Number",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)             # Membuat label tulisan ID Number dengan format dan warna tulisan yang disesuaikan
        self.lblCustIdNumber.grid(row=8,column=0,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustIdNumber=ttk.Entry(Cust_Frame,textvariable=self.var_id_number,font=("arial",10,"bold"),width=26)            # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustIdNumber.grid(row=8,column=1,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi Entry
        #Cust Address
        self.lblCustAddress=Label(Cust_Frame,text="Address",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                # Membuat label tulisan Address dengan format dan warna tulisan yang disesuaikan
        self.lblCustAddress.grid(row=9,column=0,sticky=W,padx=5,pady=2)                                                         # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustAddress=ttk.Entry(Cust_Frame,textvariable=self.var_address,font=("arial",10,"bold"),width=26)               # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustAddress.grid(row=9,column=1,sticky=W,padx=5,pady=2)                                                         # Mengatur grid/posisi Entry

        
        # ======================Reservation Label Frame===========================          # Membuat Frame Reservasi Kamar
        Revervation_Frame=LabelFrame(Main_Frame,text="Room Reservation",font=("times new roman",12,"bold"),bg="white",fg="brown")   # Membuat frame kotak bingkai bertuliskan "Room Reservation" dengan format dan warna yang disesuaikan
        Revervation_Frame.place(x=375,y=5,width=645,height=195)                                                                     # Mengatur posisi frame kotak bingkai
        # Room Type
        self.lblRoomType=Label(Revervation_Frame,text="Room Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)              # Membuat label tulisan Room Type dengan format dan warna tulisan yang disesuaikan
        self.lblRoomType.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboRoomType=ttk.Combobox(Revervation_Frame,value=self.RoomType,textvariable=self.var_roomtype,font=("arial",10,"bold"),width=17,state="readonly")    # Membuat Combobox Tipe Kamar
        self.ComboRoomType.current(0)                                                   # Dengan melakukan set daat program dijalankan otomatis memunculkan value index 0 pada combobox
        self.ComboRoomType.grid(row=0,column=1,sticky=W,padx=5,pady=2)                  # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboRoomType.bind("<<ComboboxSelected>>",self.PriceRoomsType)             # Mengatur menggunakan method bind agar user dapat memiliki value combobos sesuai keinginan dari pilihan value yang tersedia 
                                                                                            # Sekaligus saat user memilih value tertentu maka value Room Price, Quantity, dan No of Days otomatis terisi suatu value
                                                                                            # Dan data Room Price, Quantity, dan No of Days hanya dapat diisi user setelah memilih Room Type
        # Room Price
        self.lblRoomPrice=Label(Revervation_Frame,text="Room Price",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)        # Membuat label tulisan Room Price dengan format dan warna tulisan yang disesuaikan
        self.lblRoomPrice.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                           # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboRoomPrice=ttk.Combobox(Revervation_Frame,textvariable=self.var_roomprice,font=("arial",10,"bold"),width=17,state="readonly")  # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data 
        self.ComboRoomPrice.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                                         # Mengatur grid/posisi Entry
        # Quantity Room
        self.lblQuantityRoom=Label(Revervation_Frame,text="Qty",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)            # Membuat label tulisan QTY dengan format dan warna tulisan yang disesuaikan            
        self.lblQuantityRoom.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtQuantityRoom=ttk.Entry(Revervation_Frame,textvariable=self.var_quantity,font=("arial",10,"bold"),width=20)      # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data 
        self.txtQuantityRoom.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi Entry
        # No Of Days
        self.lblNoOfDays=Label(Revervation_Frame,text="No Of Days",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)         # Membuat label tulisan No of Days dengan format dan warna tulisan yang disesuaikan
        self.lblNoOfDays.grid(row=3,column=0,sticky=W,padx=5,pady=2)                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtNoOfDays=ttk.Entry(Revervation_Frame,textvariable=self.var_noofdays,font=("arial",10,"bold"),width=20)          # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtNoOfDays.grid(row=3,column=1,sticky=W,padx=5,pady=2)                                                            # Mengatur grid/posisi Entry
        # Check-In
        self.lblCheckIn=Label(Revervation_Frame,text="Check-In Date",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)       # Membuat label tulisan Check-In Date dengan format dan warna tulisan yang disesuaikan
        self.lblCheckIn.grid(row=4,column=0,sticky=W,padx=5,pady=2)                                                             # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCheckIn=ttk.Entry(Revervation_Frame,textvariable=self.var_checkin,font=("arial",10,"bold"),width=20)            # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCheckIn.grid(row=4,column=1,sticky=W,padx=5,pady=2)                                                             # Mengatur grid/posisi Entry
        # Early Check-In
        self.lblEarlyCheckIn=Label(Revervation_Frame,text="Earliest Check-In",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                                                  # Membuat label tulisan Early Check-In dengan format dan warna tulisan yang disesuaikan
        self.lblEarlyCheckIn.grid(row=0,column=2,sticky=W,padx=5,pady=2)                                                                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboEarlyCheckIn=ttk.Combobox(Revervation_Frame,value=self.EarlyCheckInlist,textvariable=self.var_earlycheckin,font=("arial",10,"bold"),width=19,state="readonly")    # Membuat Combobox pilihan Early Check-In
        self.ComboEarlyCheckIn.current(0)                                                                                       # Dengan melakukan set daat program dijalankan otomatis memunculkan value index 0 pada combobox 
        self.ComboEarlyCheckIn.grid(row=0,column=3,sticky=W,padx=5,pady=2)                                                      # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboEarlyCheckIn.bind("<<ComboboxSelected>>",self.LateCheckOut_Add)                                               # Mengatur menggunakan method bind agar user dapat memiliki value combobos sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                    # Dan data Late Check-Out hanya dapat diisi user setelah memilih Early Chech-In
        # Late Check-Out
        self.lblLateCheckOut=Label(Revervation_Frame,text="Late Check-Out",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                         # Membuat label tulisan Latest Check-Out dengan format dan warna tulisan yang disesuaikan
        self.lblLateCheckOut.grid(row=1,column=2,sticky=W,padx=5,pady=2)                                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboLateCheckOut=ttk.Combobox(Revervation_Frame,textvariable=self.var_latecheckout,font=("arial",10,"bold"),width=19,state="readonly")    # Membuat Combobox pilihan Latest Check-Out 
        self.ComboLateCheckOut.grid(row=1,column=3,sticky=W,padx=5,pady=2)                                                                              # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboLateCheckOut.bind("<<ComboboxSelected>>",self.Meal_Add)                                                                               # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                            # Dan data Meal hanya dapat diisi user setelah memilih Latest Check-Out
        # Meal
        self.lblMeal=Label(Revervation_Frame,text="Meal",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                               # Membuat label tulisan Meal dengan format dan warna tulisan yang disesuaikan
        self.lblMeal.grid(row=2,column=2,sticky=W,padx=5,pady=2)                                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboMeal=ttk.Combobox(Revervation_Frame,textvariable=self.var_meal,font=("arial",10,"bold"),width=19,state="readonly")        # Membuat Combobox pilihan Meal
        self.ComboMeal.grid(row=2,column=3,sticky=W,padx=5,pady=2)                                                                          # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboMeal.bind("<<ComboboxSelected>>",self.PaymentMethod_Add)                                                                  # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                # Dan data Payment Moethod hanya dapat diisi user setelah memilih Meal
        # Payment Method
        self.lblPaymentMethod=Label(Revervation_Frame,text="Payment Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                            # Membuat label tulisan Payment Method dengan format dan warna tulisan yang disesuaikan
        self.lblPaymentMethod.grid(row=3,column=2,sticky=W,padx=5,pady=2)                                                                                   # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboPaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_paymentmethod,font=("arial",10,"bold"),width=19,state="readonly")      # Membuat Combobox pilihan Payment Method
        self.ComboPaymentMethod.grid(row=3,column=3,sticky=W,padx=5,pady=2)                                                                                 # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboPaymentMethod.bind("<<ComboboxSelected>>",self.OnlinePaymentMethod_Add)                                                                   # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                                # Dan data Online Payment Method hanya dapat diisi bila user memilih payment method "Non-Cash"
        # Online Pay Method
        self.lblOnlinePaymentMethod=Label(Revervation_Frame,text="Online Pay Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                           # Membuat label tulisan Online Payment Method dengan format dan warna tulisan yang disesuaikan
        self.lblOnlinePaymentMethod.grid(row=4,column=2,sticky=W,padx=5,pady=2)                                                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboOnlinePaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_onlinepayment,font=("arial",10,"bold"),width=19,state="readonly")        # Membuat Combobox pilihan Payment Method
        self.ComboOnlinePaymentMethod.grid(row=4,column=3,sticky=W,padx=5,pady=2)                                                                                   # Mengatur grid/posisi combobox dari baris dan kolomnya
                                                                                                                                                                        # Mengatur menggunakan readonly agar user tidak dapat menghapus value combobox sesuai keinginan dari pilihan value yang tersedia
        
        # =====================Foto bawah =================================
        MiddleFrame1=Frame(Main_Frame,bd=10)                        # Membuat frame baru untuk foto hiasan dan info tambahan
        MiddleFrame1.place(x=10,y=370,width=1010,height=400)        # Mengatur koordinat frame
        
        # Foto hiasan kiri
        img12=Image.open(r"images\Novotel4.jpg")                                                        # Menginput gambar "SoloParagon3.jpg"
        img12=img12.resize((505,400),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg12=ImageTk.PhotoImage(img12)                                                           # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img12=Label(MiddleFrame1,image=self.photoimg12)                                                 # Mengatur format foto yang disesuaikan
        lbl_img12.place(x=-8,y=-8,width=505,height=130)                                                     # Mengatur gambar pada frame dengan jarak terhadap sumbu x=-8 pixel, sumbu y=-8 pixel, dan panjang lebar disesuaikan
        # Foto hiasan kanan
        img13=Image.open(r"images\Novotel5.jpg")                                    # Menginput gambar "SoloParagon2.jpg"
        img13=img13.resize((505,400),Image.ANTIALIAS)                                   # Mengubah dimensi ukuran gambar
        self.photoimg13=ImageTk.PhotoImage(img13)                                       # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img13=Label(MiddleFrame1,image=self.photoimg13)                             # Mengatur format foto yang disesuaikan
        lbl_img13.place(x=505,y=-8,width=505,height=130)                                # Mengatur gambar pada frame dengan jarak terhadap sumbu x=505 pixel, sumbu y=-8 pixel, dan panjang lebar disesuaikan
        

        # ===================== Foto Tengah =================================
        MiddleFrame2=Frame(Main_Frame,bd=10)                    # Membuat frame baru untuk foto keterangan fasilitas kamar
        MiddleFrame2.place(x=375,y=208,width=645,height=156)    # Mengatur koordinat frame
        # Foto Tabel Facilities
        img14=Image.open(r"images\Novotel6.png")                    # Menginput gambar "SoloParagon2.jpg"
        img14=img14.resize((645,156),Image.ANTIALIAS)                   # Mengubah dimensi ukuran gambar
        self.photoimg14=ImageTk.PhotoImage(img14)                       # Menginput gambar ke Tkinter pada frame Billing Solo Paragon Hotel
        lbl_img14=Label(MiddleFrame2,image=self.photoimg14)             # Mengatur format foto yang disesuaikan
        lbl_img14.place(x=-10,y=-10,width=645,height=156)               # Mengatur gambar pada frame dengan jarak terhadap sumbu x=-10 pixel, sumbu y=-10 pixel, dan panjang lebar disesuaikan
        
        
        # ====================== Search Bill =====================================
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")          # Membuat frame baru untuk search bill
        Search_Frame.place(x=1050,y=15,width=500,height=40)     # Mengatur koordinat frame

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")                # Membuat label tulisan Bill Number dengan format dan warna tulisan yang disesuaikan
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)                                                               # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)   # Membuat Entry pada frame search bill yang digunakan sebagai tempat user memasukkan data 
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)                                                      # Mengatur grid/posisi Entry
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")     # Membuat tombol search bill untuk membuka bill yang telah tersimpan dan dibuka pada frame bill Solo Paragon Hotel 
        self.BtnSearch.grid(row=0,column=2)                                                                             # Mengatur posisi tombol search bill
        
        # ====================== Right Frame Bill Area ======================
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat frame baru untuk bill area dengan format yang disesuaikan
        RightLabelFrame.place(x=1030,y=45,width=480,height=440)                                                             # Mengatur koordinat dan ukuran frame

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)                                                                         # Membuat scrollbar arah vertikal
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))     # Membuat text area yang dapat discroll dengan format yang disesuaikan
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # ====================== Bill Counter Label Frame ===========================           # Tabel perhitungan harga total kamar, pajak, dan total biaya
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat tabel perhitungan harga total kamar, pajak, dan total biaya
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)                                     # Mengatur posisi dan ukuran frame
        # Sub Total
        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                   # Membuat label tulisan Sub Total dengan format dan warna tulisan yang disesuaikan
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtSubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=24,state="readonly")     # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan sub total
        self.txtSubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi Entry
        # Gov Tax
        self.lblGovTax=Label(Bottom_Frame,text="Gov Tax",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                       # Membuat label tulisan Gov Total dengan format dan warna tulisan yang disesuaikan
        self.lblGovTax.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtGovTax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=24,state="readonly")       # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan pajak total
        self.txtGovTax.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi Entry
        # Amount Total
        self.lblAmount=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                         # Membuat label tulisan Amount Total dengan format dan warna tulisan yang disesuaikan
        self.lblAmount.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtAmount=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24,state="readonly")           # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan total biaya
        self.txtAmount.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi Entry


        # ================ Button Frame =========================   # Frame Berbagai Tombol
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")               # Membuat frame baru untuk tombol Add to chart, Generate Bill, Print, Clear, Back
        Btn_Frame.place(x=320,y=0)                                  # Mengatur posisi frame tombol-tombol
        
        # Btn Add To Cart
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")     # Membuat tombol Add to chart dengan format dan warna yang disesuaikan
        self.BtnAddToCart.grid(row=0,column=0,padx=1)                                               # Mengatur posisi tombol Add to chart
        global datakamar,jumlahkamar,lamamenginap,totalhargakamar,hargahargakamardipesan            # Menjadikan variabel datakamar,jumlahkamar,lamamenginap,totalhargakamar,hargahargakamardipesan  
        datakamar=[]                                                # Menjadikan variabel datakamar menjadi data list
        jumlahkamar=[]                                              # Menjadikan variabel jumlahkamar menjadi data list
        lamamenginap=[]                                             # Menjadikan variabel lamamenginap menjadi data list
        hargahargakamardipesan=[]                                   # Menjadikan variabel hargahargakamardipesan menjadi data list
        totalhargakamar=[]                                          # Menjadikan variabel totalhargakamar menjadi data list
        # Btn Generate
        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")  # Membuat tombol Generate Bill dengan format dan warna yang disesuaikan
        self.BtnGenerate_bill.grid(row=0,column=1,padx=1)                                           # Mengatur posisi tombol Generate Bill
        # Btn Save Bill
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")      # Membuat tombol Save Bill dengan format dan warna yang disesuaikan
        self.BtnSave.grid(row=0,column=2)                                                           # Mengatur posisi tombol Generate Bill
        # Btn Print
        self.BtnPrint=Button(Btn_Frame,command=self.printbill,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")    # Membuat tombol Print Bill dengan format dan warna yang disesuaikan
        self.BtnPrint.grid(row=0,column=3)                                                          # Mengatur posisi tombol Print Bill
        # Btn Clear
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")      # Membuat tombol Clear Bill dengan format dan warna yang disesuaikan
        self.BtnClear.grid(row=0,column=4)                                                          # Mengatur posisi tombol Clear Bill
        # Btn Back
        self.BtnBack=Button(Btn_Frame,command=self.root.destroy,height=2,text="Back",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")    # Membuat tombol Back dengan format dan warna yang disesuaikan
        self.BtnBack.grid(row=0,column=5)                                                           # Mengatur posisi tombol Back
        self.welcome()                      # Memanggil nama fungsi welcome setelah klik tombol Add to cart
        self.l=[]                           # Memanggil variabel l setelah klik tombol Add to cart agar memulai perhitungan dan memunculkan nominal pada frame bill counting


    # ============================= FUNCTION DECLARATION ==============================
    def AddItem(self):                                                          # Membuat fungsi AddItem dengan parameter self
        Tax=1                                                                   # Melakukan pemisalan Tax=1
        self.n=self.var_roomprice.get()                                         # membuat variabel self.n yang nantinya akan berisi nilai dari variabel harga kamar
        self.m=self.var_quantity.get()*self.n                                   # membuat variabel self.m yang nantinya akan berisi nilai hasil perkalian harga kamar * jumlah kamar
        self.o=self.var_noofdays.get()*self.m                                   # membuat variabel self.o yang nantinya akan berisi nilai hasil dari harga kamar * jumlah kamar * lama menginap
        self.l.append(self.o)                                                   # membuat variabel self.l yang nantinya akan berisi nilai dari self.o dan penambahannya
        if self.var_roomtype.get()=="Select Type":                                      # Membuat decision bila user klik tombol Add to cart namun belum memilih tipe kamar
            messagebox.showerror("Error","Please Select The Room Type Name")            # Maka akan muncul notiifikasi error dan meminta untuk memilih tipe kamar
            self.new_window=Toplevel(self.root)                                         # Lalu akan memunculkan layar baru dengan Toplevel
            self.app=Bill_App3(self.new_window)                                         # Membuka kembali window Bill_App3
        else:                                                                                   # Membuat decision lain (bila user memilih tipe kamar)
            self.textarea.insert(END,f"\n {self.var_roomtype.get()}\t\t{self.var_quantity.get()}\t          {self.var_noofdays.get()}\t\t        {self.o}")     # Menginput dan memunculkan data tipe kamar,jumlah,lama menginap, dan total harga kamar pada frame bill text area
            self.sub_total.set(str('Rp.%.2f'%(sum(self.l))))                                                                    # Menghitung dan memunculkan nilai subtotal setelah dilakukan perhitungan pada frame Bill Counting
            self.tax_input.set(str('Rp.%.2f'%((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))                         # Menghitung dan memunculkan nilai pajak setelah dilakukan perhitungan pada frame Bill Counting
            self.total.set(str('Rp.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))))         # Menghitung dan memunculkan nilai total setelah dilakukan perhitungan pada frame Bill Counting
            datakamar.append(self.var_roomtype.get())                       # Memasukkan data tipe kamar ke data listnya dan memasukkan ke csv
            jumlahkamar.append(self.var_quantity.get())                     # Memasukkan data jumlah kamar ke data listnya dan memasukkan ke csv
            lamamenginap.append(self.var_noofdays.get())                    # Memasukkan data lama menginap ke data listnya dan memasukkan ke csv
            totalhargakamar.append(self.o)                                  # Memasukkan data totalhargakamar ke data listnya dan memasukkan ke csv
            hargahargakamardipesan.append(self.var_roomprice.get())         # Memasukkan data harga-harga kamar ke data listnya dan memasukkan ke csv

    def gen_bill(self):                                                                             # Membuat fungsi gen_bil untuk generate bill dengan parameter self
        if self.var_roomtype.get()=="Select Type":                                                  # Membuat decision saat user klik tombol generate bill namun belum memilih tipe kamar
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")       # Maka akan memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                                     # Membuka kembali window Bill
            self.app=Bill_App3(self.new_window)
        if self.var_paymentmethod.get()=="Select Pay Method":                                       # Membuat decision saat user klik tombol generate bill namun belum memilih jenis metode pembayaran
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")       # Maka akan memunculkan notiifikasi error 
            self.new_window=Toplevel(self.root)                                                     # Membuka kembali window Bill
            self.app=Bill_App3(self.new_window)
        else:
            text=self.textarea.get(20.0,(24.0+float(len(self.l))))                                              # membuat variabel text yang akan mengambil data pada baris 20.0 sampai 24.0+len(self.l)
            self.welcome()                                                                                      # Mengisi value pada self.welcome (data pemesan dan informasi hasil biaya)
            self.textarea.insert(END,text)                                                                      # Memasukkan ke textarea setelah data paling akhir dari text area                                                                  
            self.textarea.insert(END,"==================================================")                      
            self.textarea.insert(END,"\n ~ ADDITIONAL INFORMATION ~\n")
            self.textarea.insert(END,f"\n Check-In Date\t\t\t: {self.var_checkin.get()}")           # Memasukkan data Check-In Date ke text area
            if self.var_earlycheckin.get()=="Select Time":                                          # Decision saat belum memilih Early Check-In
                messagebox.showerror("Error","Please Select Earliest Check-In Time")                # Muncul notifikasi error
                self.new_window=Toplevel(self.root)                                             # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App3(self.new_window)                                             # Membukanya adalah window Bill_App3
            else:
                self.textarea.insert(END,f"\n Earliest Check-In Date\t\t\t: {self.var_earlycheckin.get()}")     # Memasukkan data Earlist Check-In ke text area
            
            if self.var_latecheckout.get()=="Select Time":                          # Decision saat belum memilih late check-out
                messagebox.showerror("Error","Please Select Check-Out Time")        # Muncul notifikasi error
                self.new_window=Toplevel(self.root)                                 # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App3(self.new_window)                                 # Membukanya adalah window Bill_App3
            else:
                self.textarea.insert(END,f"\n Late Check-Out\t\t\t: {self.var_latecheckout.get()}")     # Memasukkan data Late Check-Out ke text area
            
            if self.var_meal.get()=="Select Meal":                          # Decision saat belum memilih Meal
                messagebox.showerror("Error","Please Select Meal")          # Muncul notifikasi error  
                self.new_window=Toplevel(self.root)                         # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App3(self.new_window)                         # Membukanya adalah window Bill_App3
            else:
                self.textarea.insert(END,f"\n Meal\t\t\t: {self.var_meal.get()}")   # Memasukkan data Meal ke text area
            
            if self.var_paymentmethod.get()=="Cash":                                                    # Decision saat memilih cash
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")    # Memasukkan data Payment Method ke text area
            
            if self.var_paymentmethod.get()=="Non-Cash":                                                        # Decision saat memilih Non-cash
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")            # Memasukkan data Payment Method ke text area
                self.textarea.insert(END,f"\n Online Payment Method\t\t\t: {self.var_onlinepayment.get()}")     # Memasukkan data Online Payment Method ke text area
            self.textarea.insert(END,"\n==================================================")
            
            if self.var_onlinepayment.get()=="Credit Card":                                                 # Decision saat memilih Credit Card
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")           # Memasukkan data No.rek CV Conforging ke text area
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")         # Memasukkan data Code bayar ke text area
            if self.var_onlinepayment.get()=="Debit Card":                                              # Decision saat memilih Credit Card
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")       # Memasukkan data No.rek CV Conforging ke text area
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")     # Memasukkan data Code bayar ke text area
            self.textarea.insert(END,f"\n Sub Amount\t\t\t: {self.sub_total.get()}")            # Memasukkan data Sub Amount ke text area
            self.textarea.insert(END,f"\n Tax Amount\t\t\t: {self.tax_input.get()}")            # Memasukkan data Tax Amount ke text area
            self.textarea.insert(END,f"\n Total Amount\t\t\t: {self.total.get()}")              # Memasukkan data Total Amount ke text area
            self.textarea.insert(END,"\n==================================================")
            newcustomer = {'Bill Number' : [str(self.bill_no.get())],                           # Membuat variabel newcustomer yang berisi data dictionary dengan kata kunci dan valuenya mendapatkan nilai kata kunci tersebut
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
            userpemesan = pd.DataFrame(newcustomer)                                                         # Membuat variabel newcustomer yang menghubungkan dengan pandas
            userpemesan.to_csv('pemesanankamarnovotelsolohotel.csv', mode='a', index=False, header=False)        # Memasukkan data ke csv
            
    def save_bill(self):                                                    # Membuat fungsi save_bill dengan parameter self agar bill dapat disimpan user
        if self.var_roomtype.get()=="Select Type":                                      # Membuat decision bila user belum memilih jenis kamar
            messagebox.showerror("Error","Please CLick Generate Bill")                  # Akan Memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                         # Lalu akan membuka windows baru dengan toplevel
            self.app=Bill_App3(self.new_window)                                         # windownya adalah Bill_App3
        else:
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")         # Memunculkan messagebox untuk meminta user memilih ya atau tidak
            if op:                                                                                    # Membuat situasi jika user pilih ya save bill  
                self.bill_data=self.textarea.get(1.0,END)                                             # Mendapatkan nilai dari baris 1 sampai akhir dalam bill
                f1=open('bills/'+str(self.bill_no.get())+".txt",'w')                                  # Membuka file bills.txt dan memanggil nomor bill lalu menggunakan parameter mode 'w' untuk mereplace file dan diganti dengan yang baru ditulis
                f1.write(self.bill_data)                                                                # Masukkan data pada file bills.txt
                op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Successfully!")     # Membuat notifikasi bila bill dengan nomor tertentu berhasil disimpan
                f1.close()                                                                              # Menutup file bills.txt agar menjamin bahwa file akan tetap ditutup walaupun ada error sebelumnya
 
    def printbill(self):                                                                   # Membuat fungsi print bill dengan parameter self agar user dapat melakukan print bill
        if self.var_roomtype.get()=="Select Type":                              # Membuat decision jika user belum memilih jenis kamar
            messagebox.showerror("Error","Please CLick Generate Bill")          # Memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                 # Memunculkan windows baru dengan TopLevel
            self.app=Bill_App3(self.new_window)                                 # Windownya adalah Bill_App3
        else:
            q=self.textarea.get(1.0,"end-1c")                   # Mengambil data pada keseluruhan bill
            filename=tempfile.mktemp('.txt')                    # Menggunakan modul tempfile (TemporaryFile) untuk file sementara
            open(filename,'w').write(q)                         # Merename nama file
            os.startfile(filename,"print")                      # Melakukan proses printing
    
    def find_bill(self):                                        # Membuat  fungsi find_bill dengan parameter self 
        found="no"                                              # membuat acuan awal found="no"
        for i in os.listdir("bills/"):                          # membuat looping bila i ada dalam os.listdir (fungsi individual) 
            if i.split('.')[0]==self.search_bill.get():         # bila data momor bill yang dimasukkan user = nomor bill yang sudah pernah disave sebelumnya
                f1=open(f'bills/{i}','r')                       # Maka akan membuka folder bills
                self.textarea.delete(1.0,END)                   # dan menghapus semua valuenya
                for d in f1:                                        # looping bila d ada pada salah satu file di folser bills
                    self.textarea.insert(END,d)                     # maka akan memasukkan data-data value pada frame bill
                f1.close()                                          # Menutup file agar lebih aman
                found="yes"                                         # menjadikan found menjadi bernilai yes
        if found=="no":                                         # jika tidak ditemukan nomor bill
            messagebox.showerror("Error","Invalid Bill No.")    # maka akan muncul messagebox error
            self.new_window=Toplevel(self.root)                 # membuka window baru dengan toplevel agar berada di posisi paling atas
            self.app=Bill_App3(self.new_window)                 # windownya adalah Bill_App3

    def clear(self):                                    # Membuat fungsi clear bill dengan parameter self
        self.textarea.delete(1.0,END)                   # Menghapus semua value dalam frame bill
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))                        # Dan mengganti dengan nomor kode baru
        self.var_cust_name.set("")                      # Menjadikan Cust name menjadi kosong kembali
        self.var_gender.set("")                         # Menjadikan Cust gender menjadi kosong kembali
        self.var_post.set("")                           # Menjadikan Cust post code menjadi kosong kembali
        self.var_mobile.set(+62)                        # Menjadikan Cust mobile menjadi kosong kembali
        self.var_email.set("")                          # Menjadikan Cust email menjadi kosong kembali
        self.var_provinsi.set("")                       # Menjadikan Cust provinsi menjadi kosong kembali
        self.var_id_type.set("")                        # Menjadikan Cust idItype menjadi kosong kembali
        self.var_id_number.set(0)                       # Menjadikan Cust id number menjadi kosong kembali
        self.var_address.set("")                        # Menjadikan Cust addres menjadi kosong kembali
        self.var_roomtype.set("")                       # Menjadikan room type menjadi kosong kembali
        self.var_roomprice.set(0)                       # Menjadikan room price menjadi kosong kembali
        self.var_quantity.set(0)                        # Menjadikan quantity room menjadi kosong kembali
        self.var_noofdays.set(0)                        # Menjadikan lama menginap menjadi kosong kembali
        self.var_checkin.set("")                        # Menjadikan data checkin menjadi kosong kembali
        self.var_earlycheckin.set("")                   # Menjadikan data early checkin menjadi kosong kembali
        self.var_latecheckout.set("")                   # Menjadikan data latest cehckout menjadi kosong kembali
        self.var_paymentmethod.set("")                  # Menjadikan onlinepayment menjadi kosong kembali
        self.var_onlinepayment.set("")                  # Menjadikan online payment menjadi kosong kembali
        z=random.randint(2000,9999)                     
        self.bill_no.set(str(x))                        # Melakukan set nomor bill yang baru
        self.search_bill.set("")                        # Menjadikan data search bill menjadi kosong kembali
        self.l=[0]                                      # Menjadikan rumus perhitungan menjadi kosong kembali
        self.total.set(0)                               # Menjadikan value total biaya menjadi kosong kembali 
        self.sub_total.set(0)                           # Menjadikan value sub total menjadi kosong kembali
        self.tax_input.set(0)                           # Menjadikan value biaya tax menjadi kosong kembali
        self.welcome()                                  # Memasukkan kembali variabel-variabel template pada frame  
        
    def welcome(self):                                                                                  # Membuat fungsi welcome dengan parameter self untuk sebagai template awal yang muncul pada frame bill dengan datanya sendiri masih kosong
        self.textarea.delete(1.0,END)                                                                   # Menghapus semua value pada variabel menjadi nol/kosong
        self.textarea.insert(END,"\t ~ WELCOME TO MR.CONFORGING SOLO ~\n")                              # Menampilkan judul pada bill frame
        self.textarea.insert(END,f"\n Bill Number\t\t\t: {self.bill_no.get()}")                         # Menampilkan bill number pada bill frame
        self.textarea.insert(END,f"\n Customer Ref\t\t\t: {self.var_ref.get()}")                        # Menampilkan customer ref pada bill frame
        self.textarea.insert(END,f"\n Customer Name\t\t\t: {self.var_cust_name.get()}")                 # Menampilkan customer name pada bill frame
        self.textarea.insert(END,f"\n Gender\t\t\t: {self.var_gender.get()}")                           # Menampilkan cust gender pada bill frame
        self.textarea.insert(END,f"\n PostCode\t\t\t: {self.var_post.get()}")                           # Menampilkan postcode pada bill frame
        self.textarea.insert(END,f"\n Mobil No.\t\t\t: {self.var_mobile.get()}")                        # Menampilkan mobile number cust pada bill frame
        self.textarea.insert(END,f"\n Email\t\t\t: {self.var_email.get()}")                             # Menampilkan cust email pada bill frame
        self.textarea.insert(END,f"\n Provincial Origin\t\t\t: {self.var_provinsi.get()}")              # Menampilkan cust provincial origin pada bill frame
        self.textarea.insert(END,f"\n ID Proof Type\t\t\t: {self.var_id_type.get()}")                   # Menampilkan tipe Id Proof pada bill frame
        self.textarea.insert(END,f"\n ID Number\t\t\t: {self.var_id_number.get()}")                     # Menampilkan nomor id cust pada bill frame
        self.textarea.insert(END,f"\n Address\t\t\t: {self.var_address.get()}")                         # Menampilkan address pada bill frame

        self.textarea.insert(END,"\n==================================================")                        # Variasi Bill
        self.textarea.insert(END,'\t\t\t "NOVOTEL SOLO HOTEL"\n')                                  # Menampilkan keterangan nama hotel
        self.textarea.insert(END,'\n  Jl. Slamet Riyadi No. 272, Kec. Banjarsari, Kota Surakarta, 57131 \n')          # Menampilkan keterangan alamat hotel
        self.textarea.insert(END,f"\n  Room Type\t\tQuantity\t          No of Days\t\t        Room Price")      # Menampilkan keterangan Jenis kamar,jumlah,lama menginap, dan total harga kamar 
        self.textarea.insert(END,"\n==================================================")                        # Variasi bill
   
    def PriceRoomsType(self,event=""):                                              # Membuat fungsi PriceRoomsType dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboRoomType.get()=="Superior Twin Room":                            # Membuat decision bila memilih kamar jenis 1 
            self.ComboRoomPrice.config(value=self.price_SuperiorrTwinRoom)             # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 1
            self.ComboRoomPrice.current(0)                                          # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                 # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Executive Room Double Bed":                     # Membuat decision bila memilih kamar jenis 2        
            self.ComboRoomPrice.config(value=self.price_SuperiorRoomDoubleBed)     # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 2
            self.ComboRoomPrice.current(0)                              # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                    # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                    # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Executive Room":                           # Membuat decision bila memilih kamar jenis 3
            self.ComboRoomPrice.config(value=self.price_ExecutiveRoom)           # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 3
            self.ComboRoomPrice.current(0)                                      # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                            # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                            # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Superior Family Room":                                   # Membuat decision bila memilih kamar jenis 4
            self.ComboRoomPrice.config(value=self.price_SuperiorFamilyRoom)                   # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 4
            self.ComboRoomPrice.current(0)                                               # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                     # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                     # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        
    def LateCheckOut_Add(self,event=""):                                    # Membuat fungsi LateCheckOut_Add dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu 
        if self.ComboEarlyCheckIn.get()=="09.00 WIB":                       # Membuat decision bila memilih waktu 09.00 WIB di early checkin
            self.ComboLateCheckOut.config(value=self.LateCheckOut)          # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel latecheckout
            self.ComboLateCheckOut.current(0)                               # Meng set late checkout otomatis membaca index 0                        
        if self.ComboEarlyCheckIn.get()=="13.00 WIB":                   # Membuat decision bila memilih waktu 13.00 WIB di early checkin
            self.ComboLateCheckOut.config(value=self.LateCheckOut)      # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel latecheckout
            self.ComboLateCheckOut.current(0)                           # Meng set late checkout otomatis membaca index 0
    
    def Meal_Add(self,event=""):                             # Membuat fungsi Meal dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu    
        if self.ComboLateCheckOut.get()=="15.00 WIB":           # Membuat decision bila memilih waktu 15.00 WIB di late checkout
            self.ComboMeal.config(value=self.Meallist)          # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel meallist
            self.ComboMeal.current(0)                           # Meng set meal otomatis membaca index 0
        if self.ComboLateCheckOut.get()=="18.00 WIB":               # Membuat decision bila memilih waktu 18.00 WIB di late checkout
            self.ComboMeal.config(value=self.Meallist)              # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel meallist
            self.ComboMeal.current(0)                               # Meng set meal otomatis membaca index 0

    def PaymentMethod_Add(self,event=""):                                   # Membuat fungsi PaymentMethod dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboMeal.get()=="Breakfast":                               # Membuat decision bila memilih waktu breakfast di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)    # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                              # Meng set paymentmethod otomatis membaca index 0
        if self.ComboMeal.get()=="Lunch":                                           # Membuat decision bila memilih waktu lunch di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)            # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                                      # Meng set paymentmethod otomatis membaca index 0
        if self.ComboMeal.get()=="Dinner":                                      # Membuat decision bila memilih waktu dinner di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)        # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                                  # Meng set paymentmethod otomatis membaca index 0

    def OnlinePaymentMethod_Add(self,event=""):                                         # Membuat fungsi OnlinePaymentMethod dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboPaymentMethod.get()=="Non-Cash":                                   # Membuat decision bila memilih Non-Cash di Payment method
            self.ComboOnlinePaymentMethod.config(value=self.OnlinePaymentMethodlist)    # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel OnlinePaymentMethodlist
            self.ComboOnlinePaymentMethod.current(0)                                    # Meng set onlinepaymentmethod otomatis membaca index 0

# ASTON HOTEL 
class Bill_App4:                                                                        # Membuat class berisi gabungan dari beberapa fungsi untuk user melakukan pemesanan kamar dan mendapatkan bill di Aston Hotel Solo
    def __init__(self,root):                                                            # Mendefinisikan fungsi dalam class dengan nama __init__ dengan parameternya harus "self" (merujuk pada objek class) dan ada parameter tambahan yaitu "root"
        self.root=root                                                                  # Membuat properti root dengan sintaks self.root dan memberikan nilai dari root
        self.root.geometry("1530x800+0+0")                                              # Membuat ukuran window billing hotel dengan panjang 1530 pixel, lebar 800 pixel, bergeser 0 pixel dari sumbu X, bergeser 0 pixel dari sumbu Y 
        self.root.title("Billing Mr.Conforging Solo")                                   # Membuat judul window dengan nama Billing Mr.Conforging Solo


        # ================== Variables =======================
        self.var_ref=StringVar()                            # Membuat variabel var_ref dengan parameternya self dengan jenis datanya String
        x=random.randint(1000,9999)                             # Membuat variabel x untuk random angka mulai dari 1000 sampai 9999-1 
        self.var_ref.set(str(x))                                # Melakukan set untuk var_ref agar angka random muncul otomatis

        self.var_cust_name=StringVar()                      # Membuat variabel var_cust_name dengan parameternya self dengan jenis datanya String
        self.var_gender=StringVar()                         # Membuat variabel var_gender dengan parameternya self dengan jenis datanya String
        self.var_post=StringVar()                           # Membuat variabel var_post dengan parameternya self dengan jenis datanya String
        self.var_mobile=IntVar()                            # Membuat variabel var_mobile dengan parameternya self dengan jenis datanya Integer
        self.var_mobile.set("+62" + str())                      # Melakukan set untuk var_mobile agar diawal otomatis terisi "+62"

        self.var_email=StringVar()                          # Membuat variabel var_email dengan parameternya self dengan jenis datanya String
        self.var_provinsi=StringVar()                       # Membuat variabel var_provinsi dengan parameternya self dengan jenis datanya String
        self.var_id_type=StringVar()                        # Membuat variabel var_id_type dengan parameternya self dengan jenis datanya String
        self.var_id_number=StringVar()                      # Membuat variabel var_id_number dengan parameternya self dengan jenis datanya String
        self.var_address=StringVar()                        # Membuat variabel var_address dengan parameternya self dengan jenis datanya String

        self.var_roomtype=StringVar()                       # Membuat variabel var_roomtype dengan parameternya self dengan jenis datanya String
        self.var_roomprice=IntVar()                         # Membuat variabel var_roomprice dengan parameternya self dengan jenis datanya Integer
        self.var_quantity=IntVar()                          # Membuat variabel var_quantity dengan parameternya self dengan jenis datanya Integer
        self.var_noofdays=IntVar()                          # Membuat variabel var_noofdays dengan parameternya self dengan jenis datanya Integer
        self.var_checkin=StringVar()                        # Membuat variabel var_checkin dengan parameternya self dengan jenis datanya String
        self.var_earlycheckin=StringVar()                   # Membuat variabel var_earlycheckin dengan parameternya self dengan jenis datanya String
        self.var_latecheckout=StringVar()                   # Membuat variabel var_latecheckout dengan parameternya self dengan jenis datanya String
        self.var_meal=StringVar()                           # Membuat variabel var_meal dengan parameternya self dengan jenis datanya String
        self.var_paymentmethod=StringVar()                  # Membuat variabel var_paymentmethod dengan parameternya self dengan jenis datanya String
        self.var_onlinepayment=StringVar()                  # Membuat variabel var_onlinepayment dengan parameternya self dengan jenis datanya String
        
        self.bill_no=StringVar()                            # Membuat variabel bill_no dengan parameternya self dengan jenis datanya String
        z=random.randint(1000,9999)                             # Membuat variabel z untuk random angka mulai dari 1000 sampai 9999-1
        self.bill_no.set(z)                                     # Melakukan set untuk var_ref agar angka random muncul otomatis

        self.search_bill=StringVar()                        # Membuat variabel search_bill dengan parameternya self dengan jenis datanya String               
        self.sub_total=StringVar()                          # Membuat variabel sub_total dengan parameternya self dengan jenis datanya String
        self.tax_input=StringVar()                          # Membuat variabel tax_input dengan parameternya self dengan jenis datanya String
        self.total=StringVar()                              # Membuat variabel total dengan parameternya self dengan jenis datanya String

        # Var Code Pembayaran
        self.var_codebayartunai=StringVar()                                         # Membuat variabel var_codebayartunai dengan parameternya self dengan jenis datanya String
        u=random.randint(1000000000,9999999999)                                         # Membuat variabel u untuk random angka mulai dari 1000000000 sampai 9999999999-1
        self.var_codebayartunai.set(u)                                                  # Melakukan set untuk var_codebayartunai agar angka random muncul otomatis

        # Reservation Room Type List
        self.RoomType=["Select Type","Superior Double","Superior Twin","Superior Triple","Deluxe Room","Suite Room","Corner Suite"]     # Membuat data list RoomType dengan parameter self
        self.price_SuperiorDouble=553719                                                # Membuat variabel price_SuperiorDouble dengan parameter self bernilai 553719
        self.price_SuperiorTwin=553719                                                     # Membuat variabel price_SuperiorTwin dengan parameter self bernilai 553719
        self.price_SuperiorTriple=619835                                                   # Membuat variabel price_SuperiorTriple dengan parameter self bernilai 619835 
        self.price_DeluxeRoom=661157                                                  # Membuat variabel price_DeluxeRoom dengan parameter self bernilai 661157
        self.price_SuiteRoom=1264463                                                  # Membuat variabel price_SuiteRomm dengan parameter self bernilai 1264463
        self.price_CornerSuite=1330579                                                  # Membuat variabel price_CornerSuite dengan parameter self bernilai 1330579
        
        # Early Check In                                    
        self.EarlyCheckInlist=["Select Time","09.00 WIB", "13.00 WIB"]              # Membuat data list EarlyCheckInlist dengan parameter self
        self.EarlyCheckIn1="09.00 WIB"                                              # Membuat variabel EarlyCheckIn1 dengan parameter self bernilai 09.00 WIB
        self.EarlyCheckIn2="13.00 WIB"                                              # Membuat variabel EarlyCheckIn2 dengan parameter self bernilai 13.00 WIB

        # Late Check Out
        self.LateCheckOut=["Select Time","15.00 WIB", "18.00 WIB"]                  # Membuat data list LateCheckOut dengan parameter self
        self.LateCheckOut1="15.00 WIB"                                              # Membuat variabel LateCheckOut1 dengan parameter self bernilai 15.00 WIB
        self.LateCheckOut2="18.00 WIB"                                              # Membuat variabel LateCheckOut2 dengan parameter self bernilai 18.00 WIB

        # Meal
        self.Meallist=["Select Meal","Breakfast","Lunch","Dinner"]                  # Membuat data list Meallist dengan parameter self
        self.Meal1="Breakfast"                                                      # Membuat variabel Meal1 dengan parameter self bernilai Breakfast
        self.Meal2="Lunch"                                                          # Membuat variabel Meal2 dengan parameter self bernilai Lunch
        self.Meal3="Dinner"                                                         # Membuat variabel Meal3 dengan parameter self bernilai Dinner

        # Payment Method
        self.PaymentMethodlist=["Select Pay Method","Cash","Non-Cash"]              # Membuat data list PaymentMethodlist dengan parameter self
        self.PaymentMethod1="Cash"                                                  # Membuat variabel PaymentMethod1 dengan parameter self bernilai Cash
        self.PaymentMethod2="Non-Cash"                                              # Membuat variabel PaymentMethod2 dengan parameter self bernilai Non-Cash
        

        # Online Payment Method
        self.OnlinePaymentMethodlist=["Select Online Meth.","Credit Card","Debit Card","Gopay","OVO","ShoopePay","Dana"]    # Membuat data list OnlinePaymentMethodlist dengan parameter self
        self.OnlinePaymentMethodlist1="Credit Card"                                 # Membuat variabel OnlinePaymentMethodlist1 dengan parameter self bernilai Credir Card
        self.OnlinePaymentMethodlist2="Debit Card"                                  # Membuat variabel OnlinePaymentMethodlist2 dengan parameter self bernilai Debit Card
        self.OnlinePaymentMethodlist3="Gopay"                                       # Membuat variabel OnlinePaymentMethodlist3 dengan parameter self bernilai Gopay
        self.OnlinePaymentMethodlist4="OVO"                                         # Membuat variabel OnlinePaymentMethodlist4 dengan parameter self bernilai OVO
        self.OnlinePaymentMethodlist5="ShoopePay"                                   # Membuat variabel OnlinePaymentMethodlist5 dengan parameter self bernilai ShoopePay
        self.OnlinePaymentMethodlist6="Dana"                                        # Membuat variabel OnlinePaymentMethodlist6 dengan parameter self bernilai Dana
        
        # Foto Atas Kiri
        img=Image.open(r"images\aston1.webp")     # Menginput gambar "SoloParagon1.jpg"
        img=img.resize((500,130),Image.ANTIALIAS)                                                           # Mengubah dimensi ukuran gambar
        self.photoimg=ImageTk.PhotoImage(img)                                                               # Menginput gambar ke Tkinter pada frame Billing Aston Solo Hotel
        lbl_img=Label(self.root,image=self.photoimg)                                                        # Mengatur format foto yang disesuaikan
        lbl_img.place(x=0,y=0,width=500,height=130)                                                         # Mengatur gambar pada frame dengan jarak terhadap sumbu x=0 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan
        
        # Foto Atas Tengah
        img_1=Image.open(r"images\aston2.webp")   # Menginput gambar "SoloParagon2.jpg"
        img_1=img_1.resize((500,130),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg_1=ImageTk.PhotoImage(img_1)                                                           # Menginput gambar ke Tkinter pada frame Billing Aston Solo Hotel
        lbl_img_1=Label(self.root,image=self.photoimg_1)                                                    # Mengatur format foto yang disesuaikan
        lbl_img_1.place(x=500,y=0,width=500,height=130)                                                     # Mengatur gambar pada frame dengan jarak terhadap sumbu x=500 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan
        
        # Foto Atas Kanan
        img_2=Image.open(r"images\aston3.webp")   # Menginput gambar "SoloParagon3.jpg"
        img_2=img_2.resize((550,130),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg_2=ImageTk.PhotoImage(img_2)                                                           # Menginput gambar ke Tkinter pada frame Billing Aston Solo Hotel
        lbl_img_2=Label(self.root,image=self.photoimg_2)                                                    # Mengatur format foto yang disesuaikan
        lbl_img_2.place(x=1000,y=0,width=550,height=130)                                                    # Mengatur gambar pada frame dengan jarak terhadap sumbu x=1000 pixel, sumbu y=0 pixel, dan panjang lebar disesuaikan

        # Membuat label tulisan Nama Hotel
        lbl_title=Label(self.root,text="ASTON SOLO HOTEL",font=("times new roman",35,"bold"),bg="brown",fg="white")  # Membuat label bertuliskan Nama Hotel dengan font dan format yang disesuaikan
        lbl_title.place(x=0,y=130,width=1550,height=45)                                                     # Mengatur posisi label dengan koordinat yang disesuaikan
        
        def time():                                 # Membuat fungsi time untuk waktu terkini
            string=strftime('%H:%M:%S %p')          # Membuat variabel bernama string yang bernilai fungsi strtime dengan value Jam,Menit,Detik,Am/Pm
            lbl.config(text=string)                 # Mengubah text pada lbl menjadi string
            lbl.after(1000,time)                    # Mmebuat label lbl dengan method after dengan value 1000 sampai time
        
        lbl=Label(lbl_title,font=("times new roman",16,'bold'),background='brown',foreground='gold')    # menjadikan lbl menjadi label dengan font dan warna yang disesuaikan 
        lbl.place(x=0,y=0,width=120,height=45)                                                          # mengatur posisi label waktu
        time()                                                                                          # Mengembalikan fungsi time
        
        # ===== Main Frame =====
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")               # Membuat frame utama dengan format dan warna yang disesuaikan
        Main_Frame.place(x=0,y=175,width=1530,height=620)                       # Mengatur koordinat dan ukuran frame utama
        
        # ==================Customer Label Frame======================          # Membuat Frame Data Diri Pemesan Kamar
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details",font=("times new roman",12,"bold"),bg="white",fg="brown")  # Membuat frame kotak bingkai bertuliskan "Customer Details" dengan format dan warna yang disesuaikan 
        Cust_Frame.place(x=10,y=5,width=355,height=360)                                                                     # Mengatur posisi frame kotak bingkai 
        # Cust Ref
        self.lblCustRef=Label(Cust_Frame,text="Customer Ref",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)       # Membuat label tulisan Customer Ref dengan format dan warna tulisan yang disesuaikan
        self.lblCustRef.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.entryCustRef=ttk.Entry(Cust_Frame,textvariable=self.var_ref,font=("arial",10,"bold"),width=26)             # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.entryCustRef.grid(row=0,column=1,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi Entry
        #Cust Name
        self.lblCustName=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)     # Membuat label tulisan Customer Name dengan format dan warna tulisan yang disesuaikan
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                    # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.var_cust_name,font=("arial",10,"bold"),width=26)        # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                    # Mengatur grid/posisi Entry
        #Cust Gender
        self.lblCustGender=Label(Cust_Frame,text="Gender",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)          # Membuat label tulisan Gender dengan format dan warna tulisan yang disesuaikan
        self.lblCustGender.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustGender=ttk.Combobox(Cust_Frame,textvariable=self.var_gender,font=("arial",10,"bold"),width=23,state="readonly")   # Membuat Combobox Gender
        self.comboCustGender["value"]=("","Male","Female","Other")                                                                      # Dengan membuat beberapa value
        self.comboCustGender.current(0)                                                                                                 # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustGender.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust PostCode
        self.lblCustPostCode=Label(Cust_Frame,text="PostCode",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)      # Membuat label tulisan PostCode dengan format dan warna tulisan yang disesuaikan 
        self.lblCustPostCode.grid(row=3,column=0,sticky=W,padx=5,pady=2)                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustPostCode=ttk.Entry(Cust_Frame,textvariable=self.var_post,font=("arial",10,"bold"),width=26)         # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustPostCode.grid(row=3,column=1,sticky=W,padx=5,pady=2)                                                # Mengatur grid/posisi Entry
        #Cust Mobile
        self.lblCustMob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat label tulisan CustMobile dengan format dan warna tulisan yang disesuaikan
        self.lblCustMob.grid(row=4,column=0,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustMob=ttk.Entry(Cust_Frame,textvariable=self.var_mobile,font=("times new roman",10,"bold"),width=26)  # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustMob.grid(row=4,column=1,sticky=W,padx=5,pady=2)                                                     # Mengatur grid/posisi Entry
        #Cust Email
        self.lblCustEmail=Label(Cust_Frame,text="Email",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)            # Membuat label tulisan Email dengan format dan warna tulisan yang disesuaikan
        self.lblCustEmail.grid(row=5,column=0,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustEmail=ttk.Entry(Cust_Frame,textvariable=self.var_email,font=("arial",10,"bold"),width=26)           # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustEmail.grid(row=5,column=1,sticky=W,padx=5,pady=2)                                                   # Mengatur grid/posisi Entry
        #Cust Provinsi
        self.lblCustProvinsi=Label(Cust_Frame,text="Provincial Origin",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                                     # Membuat label tulisan Provincial Origin dengan format dan warna tulisan yang disesuaikan
        self.lblCustProvinsi.grid(row=6,column=0,sticky=W,padx=5,pady=2)                                                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustProvinsi=ttk.Combobox(Cust_Frame,textvariable=self.var_provinsi,font=("arial",10,"bold"),width=23,state="readonly")                       # Membuat Combobox Provinsi 
        self.comboCustProvinsi["value"]=("","Aceh","Sumatera Utara","Sumatera Barat","Sumatera Selatan","Riau","Jambi","Bangka Belitung","Kepulauan Riau",      # Dengan membuat value nama-nama provinsi di Indonesia
                           "Bengkulu","Lampung","Banten","DKI Jakarta","Jawa Barat","Jawa Tengah","Jawa Timur","DIY Yogyakarta","Bali",
                           "Nusa Tenggara Barat","Nusa Tenggara Timur","Kalimantan Barat","Kalimantan Selatan","Kalimantan Tengah",
                           "Kalimantan Timur","Kalimantan Utara","Sulawesi Utara","Sulawesi Tengah","Sulawesi Tenggara","Sulawesi Selatan",
                           "Sulawesi Barat","Maluku","Maluku Utara","Gorontalo","Papua","Papua Barat")
        self.comboCustProvinsi.current(0)                                                                                                                       # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustProvinsi.grid(row=6,column=1,sticky=W,padx=5,pady=2)                                                                                      # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust Id Type
        self.lblCustIdType=Label(Cust_Frame,text="ID Proof Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                       # Membuat label tulisan ID Proof Type dengan format dan warna tulisan yang disesuaikan
        self.lblCustIdType.grid(row=7,column=0,sticky=W,padx=5,pady=2)                                                                      # Mengatur grid/posisi tulisan baris dan kolomnya
        self.comboCustIdType=ttk.Combobox(Cust_Frame,textvariable=self.var_id_type,font=("arial",10,"bold"),width=23,state="readonly")      # Membuat Combobox ID Proof Type
        self.comboCustIdType["value"]=("","KTP","SIM","Passport")                                                                           # Dengan membuat beberapa value 
        self.comboCustIdType.current(0)                                                                                                     # Dengan melakukan set saat program jalan otomatis menampilkan index 0
        self.comboCustIdType.grid(row=7,column=1,sticky=W,padx=5,pady=2)                                                                    # Mengatur grid/posisi combobox dari baris dan kolomnya
        #Cust Id Number
        self.lblCustIdNumber=Label(Cust_Frame,text="ID Number",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)             # Membuat label tulisan ID Number dengan format dan warna tulisan yang disesuaikan
        self.lblCustIdNumber.grid(row=8,column=0,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustIdNumber=ttk.Entry(Cust_Frame,textvariable=self.var_id_number,font=("arial",10,"bold"),width=26)            # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustIdNumber.grid(row=8,column=1,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi Entry
        #Cust Address
        self.lblCustAddress=Label(Cust_Frame,text="Address",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                # Membuat label tulisan Address dengan format dan warna tulisan yang disesuaikan
        self.lblCustAddress.grid(row=9,column=0,sticky=W,padx=5,pady=2)                                                         # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCustAddress=ttk.Entry(Cust_Frame,textvariable=self.var_address,font=("arial",10,"bold"),width=26)               # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCustAddress.grid(row=9,column=1,sticky=W,padx=5,pady=2)                                                         # Mengatur grid/posisi Entry

        
        # ======================Reservation Label Frame===========================          # Membuat Frame Reservasi Kamar
        Revervation_Frame=LabelFrame(Main_Frame,text="Room Reservation",font=("times new roman",12,"bold"),bg="white",fg="brown")   # Membuat frame kotak bingkai bertuliskan "Room Reservation" dengan format dan warna yang disesuaikan
        Revervation_Frame.place(x=375,y=5,width=645,height=195)                                                                     # Mengatur posisi frame kotak bingkai
        # Room Type
        self.lblRoomType=Label(Revervation_Frame,text="Room Type",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)              # Membuat label tulisan Room Type dengan format dan warna tulisan yang disesuaikan
        self.lblRoomType.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboRoomType=ttk.Combobox(Revervation_Frame,value=self.RoomType,textvariable=self.var_roomtype,font=("arial",10,"bold"),width=17,state="readonly")    # Membuat Combobox Tipe Kamar
        self.ComboRoomType.current(0)                                                   # Dengan melakukan set daat program dijalankan otomatis memunculkan value index 0 pada combobox
        self.ComboRoomType.grid(row=0,column=1,sticky=W,padx=5,pady=2)                  # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboRoomType.bind("<<ComboboxSelected>>",self.PriceRoomsType)             # Mengatur menggunakan method bind agar user dapat memiliki value combobos sesuai keinginan dari pilihan value yang tersedia 
                                                                                            # Sekaligus saat user memilih value tertentu maka value Room Price, Quantity, dan No of Days otomatis terisi suatu value
                                                                                            # Dan data Room Price, Quantity, dan No of Days hanya dapat diisi user setelah memilih Room Type
        # Room Price
        self.lblRoomPrice=Label(Revervation_Frame,text="Room Price",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)        # Membuat label tulisan Room Price dengan format dan warna tulisan yang disesuaikan
        self.lblRoomPrice.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                           # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboRoomPrice=ttk.Combobox(Revervation_Frame,textvariable=self.var_roomprice,font=("arial",10,"bold"),width=17,state="readonly")  # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data 
        self.ComboRoomPrice.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                                         # Mengatur grid/posisi Entry
        # Quantity Room
        self.lblQuantityRoom=Label(Revervation_Frame,text="Qty",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)            # Membuat label tulisan QTY dengan format dan warna tulisan yang disesuaikan            
        self.lblQuantityRoom.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtQuantityRoom=ttk.Entry(Revervation_Frame,textvariable=self.var_quantity,font=("arial",10,"bold"),width=20)      # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data 
        self.txtQuantityRoom.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                        # Mengatur grid/posisi Entry
        # No Of Days
        self.lblNoOfDays=Label(Revervation_Frame,text="No Of Days",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)         # Membuat label tulisan No of Days dengan format dan warna tulisan yang disesuaikan
        self.lblNoOfDays.grid(row=3,column=0,sticky=W,padx=5,pady=2)                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtNoOfDays=ttk.Entry(Revervation_Frame,textvariable=self.var_noofdays,font=("arial",10,"bold"),width=20)          # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtNoOfDays.grid(row=3,column=1,sticky=W,padx=5,pady=2)                                                            # Mengatur grid/posisi Entry
        # Check-In
        self.lblCheckIn=Label(Revervation_Frame,text="Check-In Date",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)       # Membuat label tulisan Check-In Date dengan format dan warna tulisan yang disesuaikan
        self.lblCheckIn.grid(row=4,column=0,sticky=W,padx=5,pady=2)                                                             # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtCheckIn=ttk.Entry(Revervation_Frame,textvariable=self.var_checkin,font=("arial",10,"bold"),width=20)            # Membuat Entry pada frame data diri pemesan yang digunakan sebagai tempat user memasukkan data
        self.txtCheckIn.grid(row=4,column=1,sticky=W,padx=5,pady=2)                                                             # Mengatur grid/posisi Entry
        # Early Check-In
        self.lblEarlyCheckIn=Label(Revervation_Frame,text="Earliest Check-In",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                                                  # Membuat label tulisan Early Check-In dengan format dan warna tulisan yang disesuaikan
        self.lblEarlyCheckIn.grid(row=0,column=2,sticky=W,padx=5,pady=2)                                                                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboEarlyCheckIn=ttk.Combobox(Revervation_Frame,value=self.EarlyCheckInlist,textvariable=self.var_earlycheckin,font=("arial",10,"bold"),width=19,state="readonly")    # Membuat Combobox pilihan Early Check-In
        self.ComboEarlyCheckIn.current(0)                                                                                       # Dengan melakukan set daat program dijalankan otomatis memunculkan value index 0 pada combobox 
        self.ComboEarlyCheckIn.grid(row=0,column=3,sticky=W,padx=5,pady=2)                                                      # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboEarlyCheckIn.bind("<<ComboboxSelected>>",self.LateCheckOut_Add)                                               # Mengatur menggunakan method bind agar user dapat memiliki value combobos sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                    # Dan data Late Check-Out hanya dapat diisi user setelah memilih Early Chech-In
        # Late Check-Out
        self.lblLateCheckOut=Label(Revervation_Frame,text="Late Check-Out",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                         # Membuat label tulisan Latest Check-Out dengan format dan warna tulisan yang disesuaikan
        self.lblLateCheckOut.grid(row=1,column=2,sticky=W,padx=5,pady=2)                                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboLateCheckOut=ttk.Combobox(Revervation_Frame,textvariable=self.var_latecheckout,font=("arial",10,"bold"),width=19,state="readonly")    # Membuat Combobox pilihan Latest Check-Out 
        self.ComboLateCheckOut.grid(row=1,column=3,sticky=W,padx=5,pady=2)                                                                              # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboLateCheckOut.bind("<<ComboboxSelected>>",self.Meal_Add)                                                                               # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                            # Dan data Meal hanya dapat diisi user setelah memilih Latest Check-Out
        # Meal
        self.lblMeal=Label(Revervation_Frame,text="Meal",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                               # Membuat label tulisan Meal dengan format dan warna tulisan yang disesuaikan
        self.lblMeal.grid(row=2,column=2,sticky=W,padx=5,pady=2)                                                                            # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboMeal=ttk.Combobox(Revervation_Frame,textvariable=self.var_meal,font=("arial",10,"bold"),width=19,state="readonly")        # Membuat Combobox pilihan Meal
        self.ComboMeal.grid(row=2,column=3,sticky=W,padx=5,pady=2)                                                                          # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboMeal.bind("<<ComboboxSelected>>",self.PaymentMethod_Add)                                                                  # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                # Dan data Payment Moethod hanya dapat diisi user setelah memilih Meal
        # Payment Method
        self.lblPaymentMethod=Label(Revervation_Frame,text="Payment Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                            # Membuat label tulisan Payment Method dengan format dan warna tulisan yang disesuaikan
        self.lblPaymentMethod.grid(row=3,column=2,sticky=W,padx=5,pady=2)                                                                                   # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboPaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_paymentmethod,font=("arial",10,"bold"),width=19,state="readonly")      # Membuat Combobox pilihan Payment Method
        self.ComboPaymentMethod.grid(row=3,column=3,sticky=W,padx=5,pady=2)                                                                                 # Mengatur grid/posisi combobox dari baris dan kolomnya
        self.ComboPaymentMethod.bind("<<ComboboxSelected>>",self.OnlinePaymentMethod_Add)                                                                   # Mengatur menggunakan method bind agar user dapat memiliki value combobox sesuai keinginan dari pilihan value yang tersedia
                                                                                                                                                                # Dan data Online Payment Method hanya dapat diisi bila user memilih payment method "Non-Cash"
        # Online Pay Method
        self.lblOnlinePaymentMethod=Label(Revervation_Frame,text="Online Pay Method",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                           # Membuat label tulisan Online Payment Method dengan format dan warna tulisan yang disesuaikan
        self.lblOnlinePaymentMethod.grid(row=4,column=2,sticky=W,padx=5,pady=2)                                                                                     # Mengatur grid/posisi tulisan baris dan kolomnya
        self.ComboOnlinePaymentMethod=ttk.Combobox(Revervation_Frame,textvariable=self.var_onlinepayment,font=("arial",10,"bold"),width=19,state="readonly")        # Membuat Combobox pilihan Payment Method
        self.ComboOnlinePaymentMethod.grid(row=4,column=3,sticky=W,padx=5,pady=2)                                                                                   # Mengatur grid/posisi combobox dari baris dan kolomnya
                                                                                                                                                                        # Mengatur menggunakan readonly agar user tidak dapat menghapus value combobox sesuai keinginan dari pilihan value yang tersedia
        
        # =====================Foto bawah =================================
        MiddleFrame1=Frame(Main_Frame,bd=10)                        # Membuat frame baru untuk foto hiasan dan info tambahan
        MiddleFrame1.place(x=10,y=370,width=1010,height=400)        # Mengatur koordinat frame
        
        # Foto hiasan kiri
        img12=Image.open(r"images\aston4.jpg")                                                        # Menginput gambar "SoloParagon3.jpg"
        img12=img12.resize((505,400),Image.ANTIALIAS)                                                       # Mengubah dimensi ukuran gambar
        self.photoimg12=ImageTk.PhotoImage(img12)                                                           # Menginput gambar ke Tkinter pada frame Billing Aston Solo Hotel
        lbl_img12=Label(MiddleFrame1,image=self.photoimg12)                                                 # Mengatur format foto yang disesuaikan
        lbl_img12.place(x=-8,y=-8,width=505,height=130)                                                     # Mengatur gambar pada frame dengan jarak terhadap sumbu x=-8 pixel, sumbu y=-8 pixel, dan panjang lebar disesuaikan
        # Foto hiasan kanan
        img13=Image.open(r"images\aston5.webp")                                    # Menginput gambar "SoloParagon2.jpg"
        img13=img13.resize((505,400),Image.ANTIALIAS)                                   # Mengubah dimensi ukuran gambar
        self.photoimg13=ImageTk.PhotoImage(img13)                                       # Menginput gambar ke Tkinter pada frame Billing Aston Solo Hotel
        lbl_img13=Label(MiddleFrame1,image=self.photoimg13)                             # Mengatur format foto yang disesuaikan
        lbl_img13.place(x=505,y=-8,width=505,height=130)                                # Mengatur gambar pada frame dengan jarak terhadap sumbu x=505 pixel, sumbu y=-8 pixel, dan panjang lebar disesuaikan
        

        # ===================== Foto Tengah =================================
        MiddleFrame2=Frame(Main_Frame,bd=10)                    # Membuat frame baru untuk foto keterangan fasilitas kamar
        MiddleFrame2.place(x=375,y=208,width=645,height=156)    # Mengatur koordinat frame
        # Foto Tabel Facilities
        img14=Image.open(r"images\aston6.png")                    # Menginput gambar "SoloParagon2.jpg"
        img14=img14.resize((645,156),Image.ANTIALIAS)                   # Mengubah dimensi ukuran gambar
        self.photoimg14=ImageTk.PhotoImage(img14)                       # Menginput gambar ke Tkinter pada frame Billing Aston Solo Hotel
        lbl_img14=Label(MiddleFrame2,image=self.photoimg14)             # Mengatur format foto yang disesuaikan
        lbl_img14.place(x=-10,y=-10,width=645,height=156)               # Mengatur gambar pada frame dengan jarak terhadap sumbu x=-10 pixel, sumbu y=-10 pixel, dan panjang lebar disesuaikan
        
        
        # ====================== Search Bill =====================================
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")          # Membuat frame baru untuk search bill
        Search_Frame.place(x=1050,y=15,width=500,height=40)     # Mengatur koordinat frame

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")                # Membuat label tulisan Bill Number dengan format dan warna tulisan yang disesuaikan
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)                                                               # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)   # Membuat Entry pada frame search bill yang digunakan sebagai tempat user memasukkan data 
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)                                                      # Mengatur grid/posisi Entry
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")     # Membuat tombol search bill untuk membuka bill yang telah tersimpan dan dibuka pada frame bill Aston Solo Hotel 
        self.BtnSearch.grid(row=0,column=2)                                                                             # Mengatur posisi tombol search bill
        
        # ====================== Right Frame Bill Area ======================
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat frame baru untuk bill area dengan format yang disesuaikan
        RightLabelFrame.place(x=1030,y=45,width=480,height=440)                                                             # Mengatur koordinat dan ukuran frame

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)                                                                         # Membuat scrollbar arah vertikal
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))     # Membuat text area yang dapat discroll dengan format yang disesuaikan
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # ====================== Bill Counter Label Frame ===========================           # Tabel perhitungan harga total kamar, pajak, dan total biaya
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="brown")    # Membuat tabel perhitungan harga total kamar, pajak, dan total biaya
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)                                     # Mengatur posisi dan ukuran frame
        # Sub Total
        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                   # Membuat label tulisan Sub Total dengan format dan warna tulisan yang disesuaikan
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtSubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=24,state="readonly")     # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan sub total
        self.txtSubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)                                                                # Mengatur grid/posisi Entry
        # Gov Tax
        self.lblGovTax=Label(Bottom_Frame,text="Gov Tax",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                       # Membuat label tulisan Gov Total dengan format dan warna tulisan yang disesuaikan
        self.lblGovTax.grid(row=1,column=0,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtGovTax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=24,state="readonly")       # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan pajak total
        self.txtGovTax.grid(row=1,column=1,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi Entry
        # Amount Total
        self.lblAmount=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",fg="brown",bd=4)                         # Membuat label tulisan Amount Total dengan format dan warna tulisan yang disesuaikan
        self.lblAmount.grid(row=2,column=0,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi tulisan baris dan kolomnya
        self.txtAmount=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24,state="readonly")           # Membuat Entry pada frame bill counter yang digunakan sebagai tempat menampilkan nominal hasil perhitungan total biaya
        self.txtAmount.grid(row=2,column=1,sticky=W,padx=5,pady=2)                                                                  # Mengatur grid/posisi Entry


        # ================ Button Frame =========================   # Frame Berbagai Tombol
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")               # Membuat frame baru untuk tombol Add to chart, Generate Bill, Print, Clear, Back
        Btn_Frame.place(x=320,y=0)                                  # Mengatur posisi frame tombol-tombol
        
        # Btn Add To Cart
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")     # Membuat tombol Add to chart dengan format dan warna yang disesuaikan
        self.BtnAddToCart.grid(row=0,column=0,padx=1)                                               # Mengatur posisi tombol Add to chart
        global datakamar,jumlahkamar,lamamenginap,totalhargakamar,hargahargakamardipesan            # Menjadikan variabel datakamar,jumlahkamar,lamamenginap,totalhargakamar,hargahargakamardipesan  
        datakamar=[]                                                # Menjadikan variabel datakamar menjadi data list
        jumlahkamar=[]                                              # Menjadikan variabel jumlahkamar menjadi data list
        lamamenginap=[]                                             # Menjadikan variabel lamamenginap menjadi data list
        hargahargakamardipesan=[]                                   # Menjadikan variabel hargahargakamardipesan menjadi data list
        totalhargakamar=[]                                          # Menjadikan variabel totalhargakamar menjadi data list
        # Btn Generate
        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")  # Membuat tombol Generate Bill dengan format dan warna yang disesuaikan
        self.BtnGenerate_bill.grid(row=0,column=1,padx=1)                                           # Mengatur posisi tombol Generate Bill
        # Btn Save Bill
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")      # Membuat tombol Save Bill dengan format dan warna yang disesuaikan
        self.BtnSave.grid(row=0,column=2)                                                           # Mengatur posisi tombol Generate Bill
        # Btn Print
        self.BtnPrint=Button(Btn_Frame,command=self.printbill,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")    # Membuat tombol Print Bill dengan format dan warna yang disesuaikan
        self.BtnPrint.grid(row=0,column=3)                                                          # Mengatur posisi tombol Print Bill
        # Btn Clear
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")      # Membuat tombol Clear Bill dengan format dan warna yang disesuaikan
        self.BtnClear.grid(row=0,column=4)                                                          # Mengatur posisi tombol Clear Bill
        # Btn Back
        self.BtnBack=Button(Btn_Frame,command=self.root.destroy,height=2,text="Back",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")    # Membuat tombol Back dengan format dan warna yang disesuaikan
        self.BtnBack.grid(row=0,column=5)                                                           # Mengatur posisi tombol Back
        self.welcome()                      # Memanggil nama fungsi welcome setelah klik tombol Add to cart
        self.l=[]                           # Memanggil variabel l setelah klik tombol Add to cart agar memulai perhitungan dan memunculkan nominal pada frame bill counting


    # ============================= FUNCTION DECLARATION ==============================
    def AddItem(self):                                                          # Membuat fungsi AddItem dengan parameter self
        Tax=1                                                                   # Melakukan pemisalan Tax=1
        self.n=self.var_roomprice.get()                                         # membuat variabel self.n yang nantinya akan berisi nilai dari variabel harga kamar
        self.m=self.var_quantity.get()*self.n                                   # membuat variabel self.m yang nantinya akan berisi nilai hasil perkalian harga kamar * jumlah kamar
        self.o=self.var_noofdays.get()*self.m                                   # membuat variabel self.o yang nantinya akan berisi nilai hasil dari harga kamar * jumlah kamar * lama menginap
        self.l.append(self.o)                                                   # membuat variabel self.l yang nantinya akan berisi nilai dari self.o dan penambahannya
        if self.var_roomtype.get()=="Select Type":                                      # Membuat decision bila user klik tombol Add to cart namun belum memilih tipe kamar
            messagebox.showerror("Error","Please Select The Room Type Name")            # Maka akan muncul notiifikasi error dan meminta untuk memilih tipe kamar
            self.new_window=Toplevel(self.root)                                         # Lalu akan memunculkan layar baru dengan Toplevel
            self.app=Bill_App4(self.new_window)                                         # Membuka kembali window Bill_App4
        else:                                                                                   # Membuat decision lain (bila user memilih tipe kamar)
            self.textarea.insert(END,f"\n {self.var_roomtype.get()}\t\t{self.var_quantity.get()}\t          {self.var_noofdays.get()}\t\t        {self.o}")     # Menginput dan memunculkan data tipe kamar,jumlah,lama menginap, dan total harga kamar pada frame bill text area
            self.sub_total.set(str('Rp.%.2f'%(sum(self.l))))                                                                    # Menghitung dan memunculkan nilai subtotal setelah dilakukan perhitungan pada frame Bill Counting
            self.tax_input.set(str('Rp.%.2f'%((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))                         # Menghitung dan memunculkan nilai pajak setelah dilakukan perhitungan pada frame Bill Counting
            self.total.set(str('Rp.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.var_roomprice.get()))*Tax)/100)))))         # Menghitung dan memunculkan nilai total setelah dilakukan perhitungan pada frame Bill Counting
            datakamar.append(self.var_roomtype.get())                       # Memasukkan data tipe kamar ke data listnya dan memasukkan ke csv
            jumlahkamar.append(self.var_quantity.get())                     # Memasukkan data jumlah kamar ke data listnya dan memasukkan ke csv
            lamamenginap.append(self.var_noofdays.get())                    # Memasukkan data lama menginap ke data listnya dan memasukkan ke csv
            totalhargakamar.append(self.o)                                  # Memasukkan data totalhargakamar ke data listnya dan memasukkan ke csv
            hargahargakamardipesan.append(self.var_roomprice.get())         # Memasukkan data harga-harga kamar ke data listnya dan memasukkan ke csv

    def gen_bill(self):                                                                             # Membuat fungsi gen_bil untuk generate bill dengan parameter self
        if self.var_roomtype.get()=="Select Type":                                                  # Membuat decision saat user klik tombol generate bill namun belum memilih tipe kamar
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")       # Maka akan memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                                     # Membuka kembali window Bill
            self.app=Bill_App4(self.new_window)
        if self.var_paymentmethod.get()=="Select Pay Method":                                       # Membuat decision saat user klik tombol generate bill namun belum memilih jenis metode pembayaran
            messagebox.showerror("Error","Please Add to Cart Room and Choose Method Payment")       # Maka akan memunculkan notiifikasi error 
            self.new_window=Toplevel(self.root)                                                     # Membuka kembali window Bill
            self.app=Bill_App4(self.new_window)
        else:
            text=self.textarea.get(20.0,(24.0+float(len(self.l))))                                              # membuat variabel text yang akan mengambil data pada baris 20.0 sampai 24.0+len(self.l)
            self.welcome()                                                                                      # Mengisi value pada self.welcome (data pemesan dan informasi hasil biaya)
            self.textarea.insert(END,text)                                                                      # Memasukkan ke textarea setelah data paling akhir dari text area                                                                  
            self.textarea.insert(END,"==================================================")                      
            self.textarea.insert(END,"\n ~ ADDITIONAL INFORMATION ~\n")
            self.textarea.insert(END,f"\n Check-In Date\t\t\t: {self.var_checkin.get()}")           # Memasukkan data Check-In Date ke text area
            if self.var_earlycheckin.get()=="Select Time":                                          # Decision saat belum memilih Early Check-In
                messagebox.showerror("Error","Please Select Earliest Check-In Time")                # Muncul notifikasi error
                self.new_window=Toplevel(self.root)                                             # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App4(self.new_window)                                             # Membukanya adalah window Bill_App4
            else:
                self.textarea.insert(END,f"\n Earliest Check-In Date\t\t\t: {self.var_earlycheckin.get()}")     # Memasukkan data Earlist Check-In ke text area
            
            if self.var_latecheckout.get()=="Select Time":                          # Decision saat belum memilih late check-out
                messagebox.showerror("Error","Please Select Check-Out Time")        # Muncul notifikasi error
                self.new_window=Toplevel(self.root)                                 # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App4(self.new_window)                                 # Membukanya adalah window Bill_App4
            else:
                self.textarea.insert(END,f"\n Late Check-Out\t\t\t: {self.var_latecheckout.get()}")     # Memasukkan data Late Check-Out ke text area
            
            if self.var_meal.get()=="Select Meal":                          # Decision saat belum memilih Meal
                messagebox.showerror("Error","Please Select Meal")          # Muncul notifikasi error  
                self.new_window=Toplevel(self.root)                         # Membuka new window dengan toplevel agar posisi paling atas
                self.app=Bill_App4(self.new_window)                         # Membukanya adalah window Bill_App4
            else:
                self.textarea.insert(END,f"\n Meal\t\t\t: {self.var_meal.get()}")   # Memasukkan data Meal ke text area
            
            if self.var_paymentmethod.get()=="Cash":                                                    # Decision saat memilih cash
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")    # Memasukkan data Payment Method ke text area
            
            if self.var_paymentmethod.get()=="Non-Cash":                                                        # Decision saat memilih Non-cash
                self.textarea.insert(END,f"\n Payment Method\t\t\t: {self.var_paymentmethod.get()}")            # Memasukkan data Payment Method ke text area
                self.textarea.insert(END,f"\n Online Payment Method\t\t\t: {self.var_onlinepayment.get()}")     # Memasukkan data Online Payment Method ke text area
            self.textarea.insert(END,"\n==================================================")
            
            if self.var_onlinepayment.get()=="Credit Card":                                                 # Decision saat memilih Credit Card
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")           # Memasukkan data No.rek CV Conforging ke text area
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")         # Memasukkan data Code bayar ke text area
            if self.var_onlinepayment.get()=="Debit Card":                                              # Decision saat memilih Credit Card
                self.textarea.insert(END,"\n Transfer to rek. number 2168329 a.n. CV Conforging")       # Memasukkan data No.rek CV Conforging ke text area
                self.textarea.insert(END,f"\n Payment Code\t\t\t: {self.var_codebayartunai.get()}")     # Memasukkan data Code bayar ke text area
            self.textarea.insert(END,f"\n Sub Amount\t\t\t: {self.sub_total.get()}")            # Memasukkan data Sub Amount ke text area
            self.textarea.insert(END,f"\n Tax Amount\t\t\t: {self.tax_input.get()}")            # Memasukkan data Tax Amount ke text area
            self.textarea.insert(END,f"\n Total Amount\t\t\t: {self.total.get()}")              # Memasukkan data Total Amount ke text area
            self.textarea.insert(END,"\n==================================================")
            newcustomer = {'Bill Number' : [str(self.bill_no.get())],                           # Membuat variabel newcustomer yang berisi data dictionary dengan kata kunci dan valuenya mendapatkan nilai kata kunci tersebut
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
            userpemesan = pd.DataFrame(newcustomer)                                                         # Membuat variabel newcustomer yang menghubungkan dengan pandas
            userpemesan.to_csv('pemesanankamaraston.csv', mode='a', index=False, header=False)        # Memasukkan data ke csv
            
    def save_bill(self):                                                    # Membuat fungsi save_bill dengan parameter self agar bill dapat disimpan user
        if self.var_roomtype.get()=="Select Type":                                      # Membuat decision bila user belum memilih jenis kamar
            messagebox.showerror("Error","Please CLick Generate Bill")                  # Akan Memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                         # Lalu akan membuka windows baru dengan toplevel
            self.app=Bill_App4(self.new_window)                                         # windownya adalah Bill_App4
        else:
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")         # Memunculkan messagebox untuk meminta user memilih ya atau tidak
            if op:                                                                                    # Membuat situasi jika user pilih ya save bill  
                self.bill_data=self.textarea.get(1.0,END)                                             # Mendapatkan nilai dari baris 1 sampai akhir dalam bill
                f1=open('bills/'+str(self.bill_no.get())+".txt",'w')                                  # Membuka file bills.txt dan memanggil nomor bill lalu menggunakan parameter mode 'w' untuk mereplace file dan diganti dengan yang baru ditulis
                f1.write(self.bill_data)                                                                # Masukkan data pada file bills.txt
                op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Successfully!")     # Membuat notifikasi bila bill dengan nomor tertentu berhasil disimpan
                f1.close()                                                                              # Menutup file bills.txt agar menjamin bahwa file akan tetap ditutup walaupun ada error sebelumnya
 
    def printbill(self):                                                                   # Membuat fungsi print bill dengan parameter self agar user dapat melakukan print bill
        if self.var_roomtype.get()=="Select Type":                              # Membuat decision jika user belum memilih jenis kamar
            messagebox.showerror("Error","Please CLick Generate Bill")          # Memunculkan notifikasi error
            self.new_window=Toplevel(self.root)                                 # Memunculkan windows baru dengan TopLevel
            self.app=Bill_App4(self.new_window)                                 # Windownya adalah Bill_App4
        else:
            q=self.textarea.get(1.0,"end-1c")                   # Mengambil data pada keseluruhan bill
            filename=tempfile.mktemp('.txt')                    # Menggunakan modul tempfile (TemporaryFile) untuk file sementara
            open(filename,'w').write(q)                         # Merename nama file
            os.startfile(filename,"print")                      # Melakukan proses printing
    
    def find_bill(self):                                        # Membuat  fungsi find_bill dengan parameter self 
        found="no"                                              # membuat acuan awal found="no"
        for i in os.listdir("bills/"):                          # membuat looping bila i ada dalam os.listdir (fungsi individual) 
            if i.split('.')[0]==self.search_bill.get():         # bila data momor bill yang dimasukkan user = nomor bill yang sudah pernah disave sebelumnya
                f1=open(f'bills/{i}','r')                       # Maka akan membuka folder bills
                self.textarea.delete(1.0,END)                   # dan menghapus semua valuenya
                for d in f1:                                        # looping bila d ada pada salah satu file di folser bills
                    self.textarea.insert(END,d)                     # maka akan memasukkan data-data value pada frame bill
                f1.close()                                          # Menutup file agar lebih aman
                found="yes"                                         # menjadikan found menjadi bernilai yes
        if found=="no":                                         # jika tidak ditemukan nomor bill
            messagebox.showerror("Error","Invalid Bill No.")    # maka akan muncul messagebox error
            self.new_window=Toplevel(self.root)                 # membuka window baru dengan toplevel agar berada di posisi paling atas
            self.app=Bill_App4(self.new_window)                 # windownya adalah Bill_App4

    def clear(self):                                    # Membuat fungsi clear bill dengan parameter self
        self.textarea.delete(1.0,END)                   # Menghapus semua value dalam frame bill
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))                        # Dan mengganti dengan nomor kode baru
        self.var_cust_name.set("")                      # Menjadikan Cust name menjadi kosong kembali
        self.var_gender.set("")                         # Menjadikan Cust gender menjadi kosong kembali
        self.var_post.set("")                           # Menjadikan Cust post code menjadi kosong kembali
        self.var_mobile.set(+62)                        # Menjadikan Cust mobile menjadi kosong kembali
        self.var_email.set("")                          # Menjadikan Cust email menjadi kosong kembali
        self.var_provinsi.set("")                       # Menjadikan Cust provinsi menjadi kosong kembali
        self.var_id_type.set("")                        # Menjadikan Cust idItype menjadi kosong kembali
        self.var_id_number.set(0)                       # Menjadikan Cust id number menjadi kosong kembali
        self.var_address.set("")                        # Menjadikan Cust addres menjadi kosong kembali
        self.var_roomtype.set("")                       # Menjadikan room type menjadi kosong kembali
        self.var_roomprice.set(0)                       # Menjadikan room price menjadi kosong kembali
        self.var_quantity.set(0)                        # Menjadikan quantity room menjadi kosong kembali
        self.var_noofdays.set(0)                        # Menjadikan lama menginap menjadi kosong kembali
        self.var_checkin.set("")                        # Menjadikan data checkin menjadi kosong kembali
        self.var_earlycheckin.set("")                   # Menjadikan data early checkin menjadi kosong kembali
        self.var_latecheckout.set("")                   # Menjadikan data latest cehckout menjadi kosong kembali
        self.var_paymentmethod.set("")                  # Menjadikan onlinepayment menjadi kosong kembali
        self.var_onlinepayment.set("")                  # Menjadikan online payment menjadi kosong kembali
        z=random.randint(2000,9999)                     
        self.bill_no.set(str(x))                        # Melakukan set nomor bill yang baru
        self.search_bill.set("")                        # Menjadikan data search bill menjadi kosong kembali
        self.l=[0]                                      # Menjadikan rumus perhitungan menjadi kosong kembali
        self.total.set(0)                               # Menjadikan value total biaya menjadi kosong kembali 
        self.sub_total.set(0)                           # Menjadikan value sub total menjadi kosong kembali
        self.tax_input.set(0)                           # Menjadikan value biaya tax menjadi kosong kembali
        self.welcome()                                  # Memasukkan kembali variabel-variabel template pada frame  
        
    def welcome(self):                                                                                  # Membuat fungsi welcome dengan parameter self untuk sebagai template awal yang muncul pada frame bill dengan datanya sendiri masih kosong
        self.textarea.delete(1.0,END)                                                                   # Menghapus semua value pada variabel menjadi nol/kosong
        self.textarea.insert(END,"\t ~ WELCOME TO MR.CONFORGING SOLO ~\n")                              # Menampilkan judul pada bill frame
        self.textarea.insert(END,f"\n Bill Number\t\t\t: {self.bill_no.get()}")                         # Menampilkan bill number pada bill frame
        self.textarea.insert(END,f"\n Customer Ref\t\t\t: {self.var_ref.get()}")                        # Menampilkan customer ref pada bill frame
        self.textarea.insert(END,f"\n Customer Name\t\t\t: {self.var_cust_name.get()}")                 # Menampilkan customer name pada bill frame
        self.textarea.insert(END,f"\n Gender\t\t\t: {self.var_gender.get()}")                           # Menampilkan cust gender pada bill frame
        self.textarea.insert(END,f"\n PostCode\t\t\t: {self.var_post.get()}")                           # Menampilkan postcode pada bill frame
        self.textarea.insert(END,f"\n Mobil No.\t\t\t: {self.var_mobile.get()}")                        # Menampilkan mobile number cust pada bill frame
        self.textarea.insert(END,f"\n Email\t\t\t: {self.var_email.get()}")                             # Menampilkan cust email pada bill frame
        self.textarea.insert(END,f"\n Provincial Origin\t\t\t: {self.var_provinsi.get()}")              # Menampilkan cust provincial origin pada bill frame
        self.textarea.insert(END,f"\n ID Proof Type\t\t\t: {self.var_id_type.get()}")                   # Menampilkan tipe Id Proof pada bill frame
        self.textarea.insert(END,f"\n ID Number\t\t\t: {self.var_id_number.get()}")                     # Menampilkan nomor id cust pada bill frame
        self.textarea.insert(END,f"\n Address\t\t\t: {self.var_address.get()}")                         # Menampilkan address pada bill frame

        self.textarea.insert(END,"\n==================================================")                        # Variasi Bill
        self.textarea.insert(END,'\t\t\t "ASTON SOLO HOTEL"\n')                                  # Menampilkan keterangan nama hotel
        self.textarea.insert(END,'\n  Jl. Slamet Riyadi No.373, Sondakan, Kec. Laweyan, Kota Surakarta\n')          # Menampilkan keterangan alamat hotel
        self.textarea.insert(END,f"\n  Room Type\t\tQuantity\t          No of Days\t\t        Room Price")      # Menampilkan keterangan Jenis kamar,jumlah,lama menginap, dan total harga kamar 
        self.textarea.insert(END,"\n==================================================")                        # Variasi bill
   
    def PriceRoomsType(self,event=""):                                              # Membuat fungsi PriceRoomsType dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboRoomType.get()=="Superior Double":                            # Membuat decision bila memilih kamar jenis 1 
            self.ComboRoomPrice.config(value=self.price_SuperiorDouble)             # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 1
            self.ComboRoomPrice.current(0)                                          # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Superior Twin":                     # Membuat decision bila memilih kamar jenis 2        
            self.ComboRoomPrice.config(value=self.price_SuperiorTwin)     # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 2
            self.ComboRoomPrice.current(0)                              # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                    # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                    # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Superior Triple":                           # Membuat decision bila memilih kamar jenis 3
            self.ComboRoomPrice.config(value=self.price_SuperiorTriple)           # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 3
            self.ComboRoomPrice.current(0)                                      # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                            # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                            # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Deluxe Room":                                   # Membuat decision bila memilih kamar jenis 4
            self.ComboRoomPrice.config(value=self.price_DeluxeRoom)                   # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 4
            self.ComboRoomPrice.current(0)                                               # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                     # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                     # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Suite Room":                                   # Membuat decision bila memilih kamar jenis 5
            self.ComboRoomPrice.config(value=self.price_DeluxeRoom)                   # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 4
            self.ComboRoomPrice.current(0)                                               # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                     # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                     # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan
        if self.ComboRoomType.get()=="Corner Suite":                                   # Membuat decision bila memilih kamar jenis 6
            self.ComboRoomPrice.config(value=self.price_DeluxeRoom)                   # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel harga kamar tipe 4
            self.ComboRoomPrice.current(0)                                               # Meng set harga kamar otomatis membaca index 0
            self.var_quantity.set(1)                                                     # Meng set quantity kamar menjadi 1 dan dapat diubah sesuai keinginan pemesan
            self.var_noofdays.set(1)                                                     # Meng set lama menginap menjadi 1 dan dapat diubah sesuai keinginan pemesan    
        
    def LateCheckOut_Add(self,event=""):                                    # Membuat fungsi LateCheckOut_Add dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu 
        if self.ComboEarlyCheckIn.get()=="09.00 WIB":                       # Membuat decision bila memilih waktu 09.00 WIB di early checkin
            self.ComboLateCheckOut.config(value=self.LateCheckOut)          # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel latecheckout
            self.ComboLateCheckOut.current(0)                               # Meng set late checkout otomatis membaca index 0                        
        if self.ComboEarlyCheckIn.get()=="13.00 WIB":                   # Membuat decision bila memilih waktu 13.00 WIB di early checkin
            self.ComboLateCheckOut.config(value=self.LateCheckOut)      # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel latecheckout
            self.ComboLateCheckOut.current(0)                           # Meng set late checkout otomatis membaca index 0
    
    def Meal_Add(self,event=""):                             # Membuat fungsi Meal dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu    
        if self.ComboLateCheckOut.get()=="15.00 WIB":           # Membuat decision bila memilih waktu 15.00 WIB di late checkout
            self.ComboMeal.config(value=self.Meallist)          # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel meallist
            self.ComboMeal.current(0)                           # Meng set meal otomatis membaca index 0
        if self.ComboLateCheckOut.get()=="18.00 WIB":               # Membuat decision bila memilih waktu 18.00 WIB di late checkout
            self.ComboMeal.config(value=self.Meallist)              # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel meallist
            self.ComboMeal.current(0)                               # Meng set meal otomatis membaca index 0

    def PaymentMethod_Add(self,event=""):                                   # Membuat fungsi PaymentMethod dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboMeal.get()=="Breakfast":                               # Membuat decision bila memilih waktu breakfast di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)    # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                              # Meng set paymentmethod otomatis membaca index 0
        if self.ComboMeal.get()=="Lunch":                                           # Membuat decision bila memilih waktu lunch di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)            # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                                      # Meng set paymentmethod otomatis membaca index 0
        if self.ComboMeal.get()=="Dinner":                                      # Membuat decision bila memilih waktu dinner di meal
            self.ComboPaymentMethod.config(value=self.PaymentMethodlist)        # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel combopaymentmethod
            self.ComboPaymentMethod.current(0)                                  # Meng set paymentmethod otomatis membaca index 0

    def OnlinePaymentMethod_Add(self,event=""):                                         # Membuat fungsi OnlinePaymentMethod dengan parameter self dan dengan data (event) dapat dimasukkan atau bernilai tertentu
        if self.ComboPaymentMethod.get()=="Non-Cash":                                   # Membuat decision bila memilih Non-Cash di Payment method
            self.ComboOnlinePaymentMethod.config(value=self.OnlinePaymentMethodlist)    # Maka akan mengkonfigurasi/mengambil nilai (value) dari variabel OnlinePaymentMethodlist
            self.ComboOnlinePaymentMethod.current(0)                                    # Meng set onlinepaymentmethod otomatis membaca index 0


if __name__ == "__main__":          # Saat interpreter Python membaca file, variabel __name__ ditetapkan sebagai __main__ jika modul sedang dijalankan, atau sebagai nama modul jika diimpor. if __name__ == '__main__': main() Ini memeriksa apakah __name__ atribut skrip Python adalah '__main__' . 
    main()                          # Dengan kata lain, jika program itu sendiri dijalankan, atributnya adalah __main__ , sehingga program akan dieksekusi (dalam hal ini fungsi main())
    