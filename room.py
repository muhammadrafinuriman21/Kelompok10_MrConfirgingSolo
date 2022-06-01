from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime 
from datetime import datetime
#   import mysql.connector
from tkinter import messagebox

class Roomboking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # =========== variable =====================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        # ==========title============================
        lbl_title=Label(self.root,text="ROOMBOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)


        # ==========logo=============================
        img2=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\logobaru.png")
        img2=img2.resize((120,60),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # =================LabelFrame====================
        LabelFrameleft= LabelFrame(self.root,bd=2,relief=RIDGE,text="Roomboking Details",font= ("times new roman",12,"bold"),padx=2)
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

        # =======================labels and entry=================
        # custcontact
        lbl_cust_contact=Label(LabelFrameleft,text="Customer Contact",font= ("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(LabelFrameleft,textvariable=self.var_contact,font= ("arial",13,"bold"),width=17)
        enty_contact.grid(row=0,column=1,sticky=W)

        # ==========Featch data buttom========================================
        #btnFeatchData=Button(LabelFrameleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        #btnFeatchData.place(x=314,y=0)

        #Check_in Date
        check_in_date=Label(LabelFrameleft,font=("arial",12,"bold"),text="Check in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(LabelFrameleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #Check_out Date
        lbl_Check_out_date=Label(LabelFrameleft,font=("arial",12,"bold"),text="Check Out Date:",padx=2,pady=6)
        lbl_Check_out_date.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(LabelFrameleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)

        # Room Type
        label_RoomType=Label(LabelFrameleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # Available room
        lblRoomAvailable=Label(LabelFrameleft,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(LabelFrameleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)

        # meal
        lblMeal=Label(LabelFrameleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(LabelFrameleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)

        # No Of Days
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="No Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        # Paid Tax
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)

        # Sub Total
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)

        # Total Cost
        lblIdNumber=Label(LabelFrameleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(LabelFrameleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        # ==========Bill Button=============================
        btnBill=Button(LabelFrameleft,text="Bill",font= ("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10, column=0,padx=1,sticky=W)

        # ===================btns============================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd=Button(btn_frame,text="Add",font= ("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0, column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font= ("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0, column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font= ("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0, column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font= ("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0, column=3,padx=1)

        #=========== Rightside Image ===================

        img3=Image.open(r"C:\TimProject_Kelompok10\Kelompok10_MrConfirgingSolo\images\bed.jpg")
        img3=img3.resize((520,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)

        
        # ==================tabel frame==================

        Tabel_Frame= LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font= ("times new roman",12,"bold"),padx=2)
        Tabel_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Tabel_Frame,font= ("arial",12,"bold"),text="Search By : ",bg="white",fg="red")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search=ttk.Combobox(Tabel_Frame,font= ("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room ")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        txtSearch=ttk.Entry(Tabel_Frame,font= ("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Tabel_Frame,text="Search",font= ("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0, column=3,padx=1)

        btnShowAll=Button(Tabel_Frame,text="Show All",font= ("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0, column=4,padx=1)

        # ======================= Show Data Tabel =======================

          #  menit 32    eps 4





if __name__ == "__main__":
    root=Tk()
    obj=Roomboking(root)
    root.mainloop()
