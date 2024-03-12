from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1280x720+0+0")

        #variable
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.address_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1280,height=300)

        #DataFrameLeft
        DataFrameLeft=LabelFrame(frame,text="Library Member Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=700,height=265)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",8,"bold"),width=37,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman",8,"bold"),width=40)
        txtPRN_No.grid(row=1,column=1)

        lblID_No=Label(DataFrameLeft,bg="powder blue",text="ID No",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblID_No.grid(row=2,column=0,sticky=W)
        txtID_No=Entry(DataFrameLeft,textvariable=self.id_var,font=("times new roman",8,"bold"),width=40)
        txtID_No.grid(row=2,column=1)

        lblN=Label(DataFrameLeft,bg="powder blue",text="Name",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblN.grid(row=3,column=0,sticky=W)
        txtN=Entry(DataFrameLeft,textvariable=self.name_var,font=("times new roman",8,"bold"),width=40)
        txtN.grid(row=3,column=1)

        lblA=Label(DataFrameLeft,bg="powder blue",text="Address",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblA.grid(row=4,column=0,sticky=W)
        txtA=Entry(DataFrameLeft,textvariable=self.address_var,font=("times new roman",8,"bold"),width=40)
        txtA.grid(row=4,column=1)

        lblPC=Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblPC.grid(row=5,column=0,sticky=W)
        txtPC=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("times new roman",8,"bold"),width=40)
        txtPC.grid(row=5,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblMobile.grid(row=6,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman",8,"bold"),width=40)
        txtMobile.grid(row=6,column=1)

        lblBID=Label(DataFrameLeft,bg="powder blue",text="Book ID",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblBID.grid(row=7,column=0,sticky=W)
        txtBID=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("times new roman",8,"bold"),width=40)
        txtBID.grid(row=7,column=1)

        lblBT=Label(DataFrameLeft,bg="powder blue",text="Book Title",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblBT.grid(row=0,column=2,sticky=W)
        txtBT=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("times new roman",8,"bold"),width=40)
        txtBT.grid(row=0,column=3)

        lblAN=Label(DataFrameLeft,bg="powder blue",text="Author Name",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblAN.grid(row=1,column=2,sticky=W)
        txtAN=Entry(DataFrameLeft,textvariable=self.author_var,font=("times new roman",8,"bold"),width=40)
        txtAN.grid(row=1,column=3)

        lblDB=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblDB.grid(row=2,column=2,sticky=W)
        txtDB=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("times new roman",8,"bold"),width=40)
        txtDB.grid(row=2,column=3)

        lblDD=Label(DataFrameLeft,bg="powder blue",text="Date Due",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblDD.grid(row=3,column=2,sticky=W)
        txtDD=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("times new roman",8,"bold"),width=40)
        txtDD.grid(row=3,column=3)

        lblDOB=Label(DataFrameLeft,bg="powder blue",text="Days On Book",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblDOB.grid(row=4,column=2,sticky=W)
        txtDOB=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("times new roman",8,"bold"),width=40)
        txtDOB.grid(row=4,column=3)

        lblLRF=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblLRF.grid(row=5,column=2,sticky=W)
        txtLRF=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("times new roman",8,"bold"),width=40)
        txtLRF.grid(row=5,column=3)

        lblDOD=Label(DataFrameLeft,bg="powder blue",text="Date Over Due",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblDOD.grid(row=6,column=2,sticky=W)
        txtDOD=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("times new roman",8,"bold"),width=40)
        txtDOD.grid(row=6,column=3)

        lblAP=Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblAP.grid(row=7,column=2,sticky=W)
        txtAP=Entry(DataFrameLeft,textvariable=self.finalprice_var,font=("times new roman",8,"bold"),width=40)
        txtAP.grid(row=7,column=3)

        #DataFrameRight

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=710,y=5,width=507,height=265)

        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=11,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=["To Kill a Mockingbird","Pride and Prejudice","The Diary of a Young Girl","1984","The Great Gatsby",
                 "Harry Potter and the Philosopher's Stone","The Catcher in the Rye","Little Women","Animal Farm",
                 "Harry Potter and the Chamber of Secrets","Harry Potter and the Prisoner of Azkaban",
                 "Harry Potter and the Goblet of Fire","Harry Potter and the Order of the Phoenix",
                 "Harry Potter and the Half-Blood Prince","Harry Potter and the Deathly Hallows","The Hobbit","The Little Prince"
                 ,"The Da Vinci Code","The Hitchhiker's Guide to the Galaxy","Wuthering Heights","Jane Eyre","A Tale of Two Cities"
                 ,"Great Expectations","The Adventures of Huckleberry Finn","The Adventures of Tom Sawyer","The Chronicles of Narnia"
                 ,"Winnie-the-Pooh","Alice's Adventures in Wonderland","The Lion, the Witch and the Wardrobe","Catch-22",
                 "Nineteen Eighty-Four","The Grapes of Wrath"]

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="To Kill a Mockingbird"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Realistic")
                self.author_var.set("Harper Lee")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")

            elif (x=="Pride and Prejudice"):
                self.bookid_var.set("BKID5460")
                self.booktitle_var.set("Satire")
                self.author_var.set("Jane Austen")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.400")

            elif x == "The Diary of a Young Girl":
                self.bookid_var.set("BKID6363")
                self.booktitle_var.set("Biography")
                self.author_var.set("Anne Frank")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.500")

            elif x == "1984":
                self.bookid_var.set("BKID5458")
                self.booktitle_var.set("Dystopian Fiction")
                self.author_var.set("George Orwell")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(30)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.300")

            elif x == "The Great Gatsby":
                self.bookid_var.set("BKID1000")
                self.booktitle_var.set("Novel")
                self.author_var.set("F. Scott Fitzgerald")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(14)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.150")

            elif x == "Harry Potter and the Philosopher's Stone":
                self.bookid_var.set("BKID7181")
                self.booktitle_var.set("Fantasy")
                self.author_var.set("J.K. Rowling")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")

            elif x == "The Catcher in the Rye":
                self.bookid_var.set("BKID7180")
                self.booktitle_var.set("Novel")
                self.author_var.set("J.D. Salinger")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(14)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.250")

            elif x == "Little Women":
                self.bookid_var.set("BKID7182")
                self.booktitle_var.set("Novel")
                self.author_var.set("Louisa May Alcott")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")

            elif x == "Animal Farm":
                self.bookid_var.set("BKID9090")
                self.booktitle_var.set("Political Satire")
                self.author_var.set("George Orwell")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(14)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.350")

            elif x == "Harry Potter and the Chamber of Secrets":
                self.bookid_var.set("BKID9091")
                self.booktitle_var.set("Fantasy")
                self.author_var.set("J.K. Rowling")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.450")

            elif x == "Harry Potter and the Prisoner of Azkaban":
                self.bookid_var.set("BKID9093")
                self.booktitle_var.set("Fantasy")
                self.author_var.set("J.K. Rowling")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.300")

            elif x == "Harry Potter and the Goblet of Fire":
                self.bookid_var.set("BKID1013")
                self.booktitle_var.set("Fantasy")
                self.author_var.set("J.K. Rowling")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.700")

            elif x == "Harry Potter and the Order of the Phoenix":
                self.bookid_var.set("BKID1014")
                self.booktitle_var.set("Fantasy")
                self.author_var.set("J.K. Rowling")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.350")

            elif x == "Harry Potter and the Half-Blood Prince":
                self.bookid_var.set("BKID1015")
                self.booktitle_var.set("Fantasy")
                self.author_var.set("J.K. Rowling")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.500")

            elif x == "Harry Potter and the Deathly Hallows":
                self.bookid_var.set("BKID1016")
                self.booktitle_var.set("Fantasy")
                self.author_var.set("J.K. Rowling")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.360")

            elif x == "The Hobbit":
                self.bookid_var.set("BKID1017")
                self.booktitle_var.set("Fantasy")
                self.author_var.set("J.R.R. Tolkien")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.320")

            elif x == "The Little Prince":
                self.bookid_var.set("BKID1018")
                self.booktitle_var.set("Children's Literature")
                self.author_var.set("Antoine de Saint-Exupéry")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(14)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.450")

            elif x == "The Da Vinci Code":
                self.bookid_var.set("BKID2021")
                self.booktitle_var.set("Mystery")
                self.author_var.set("Dan Brown")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.550")

            elif x == "The Hitchhiker's Guide to the Galaxy":
                self.bookid_var.set("BKID2020")
                self.booktitle_var.set("Science Fiction")
                self.author_var.set("Douglas Adams")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.350")

            elif x == "Wuthering Heights":
                self.bookid_var.set("BKID2022")
                self.booktitle_var.set("Gothic Fiction")
                self.author_var.set("Emily Brontë")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.650")

            elif x == "Jane Eyre":
                self.bookid_var.set("BKID2023")
                self.booktitle_var.set("Gothic Fiction")
                self.author_var.set("Charlotte Brontë")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.600")

            elif x == "A Tale of Two Cities":
                self.bookid_var.set("BKID2024")
                self.booktitle_var.set("Historical Fiction")
                self.author_var.set("Charles Dickens")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.670")

            elif x == "Great Expectations":
                self.bookid_var.set("BKID2025")
                self.booktitle_var.set("Novel")
                self.author_var.set("Charles Dickens")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.760")

            elif x == "The Adventures of Huckleberry Finn":
                self.bookid_var.set("BKID2026")
                self.booktitle_var.set("Adventure Novel")
                self.author_var.set("Mark Twain")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.520")

            elif x == "The Adventures of Tom Sawyer":
                self.bookid_var.set("BKID2027")
                self.booktitle_var.set("Adventure Novel")
                self.author_var.set("Mark Twain")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.480")

            elif x == "The Chronicles of Narnia":
                self.bookid_var.set("BKID2028")
                self.booktitle_var.set("Fantasy Fiction")
                self.author_var.set("C.S. Lewis")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(14)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.720")

            elif x == "Winnie-the-Pooh":
                self.bookid_var.set("BKID2029")
                self.booktitle_var.set("Children's Fiction")
                self.author_var.set("A.A. Milne")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(7)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.350")

            elif x == "Alice's Adventures in Wonderland":
                self.bookid_var.set("BKID2030")
                self.booktitle_var.set("Fantasy Fiction")
                self.author_var.set("Lewis Carroll")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(14)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.490")

            elif x == "The Lion, the Witch and the Wardrobe":
                self.bookid_var.set("BKID2031")
                self.booktitle_var.set("Fantasy Fiction")
                self.author_var.set("C.S. Lewis")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(14)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.650")

            elif x == "Catch-22":
                self.bookid_var.set("BKID2032")
                self.booktitle_var.set("Satire")
                self.author_var.set("Joseph Heller")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.810")

            elif x == "Nineteen Eighty-Four":
                self.bookid_var.set("BKID2033")
                self.booktitle_var.set("Dystopian Fiction")
                self.author_var.set("George Orwell")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.780")

            elif x == "The Grapes of Wrath":
                self.bookid_var.set("BKID2034")
                self.booktitle_var.set("Historical Fiction")
                self.author_var.set("John Steinbeck")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=21)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.690")

        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=11)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4,)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        #Buttons Frame
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=430,width=1280,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("times new roman",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button (Framebutton,command=self.showData, text="Show Data", font=("times new roman", 12, "bold"), width=21, bg="blue",fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData=Button (Framebutton,command=self.update, text="Update", font=("times new roman", 12, "bold"), width=21, bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData=Button (Framebutton,command=self.delete, text="Delete", font=("times new roman", 12, "bold"), width=21, bg="blue", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData=Button (Framebutton,command=self.reset, text="Reset", font=("times new roman", 12, "bold"),width=21, bg="blue",fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData=Button (Framebutton,command=self.iExit, text="Exit", font=("times new roman", 12, "bold"), width=21, bg="blue",fg="white")
        btnAddData.grid(row=0, column=5)

        #Information Frame
        Framedetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framedetails.place(x=0,y=500,width=1280,height=157)

        Table_frame=Frame(Framedetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1220,height=130)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","name","address","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno", text="Reference No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("name", text="Name")
        self.library_table.heading("address", text="Address")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Auther")
        self.library_table.heading("dateborrowed", text="Date Of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("name", width=100)
        self.library_table.column("address", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column ("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column ("dateborrowed", width=100)
        self.library_table.column ("datedue", width=100)
        self.library_table.column ("days", width=100)
        self.library_table.column ("latereturnfine", width=100)
        self.library_table.column ("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
            my_cursor = conn.cursor()

            # Print values of variables
            print("Member Type:", self.member_var.get())
            print("PRN No:", self.prn_var.get())
            # Add print statements for other variables

            my_cursor.execute("INSERT INTO library VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.member_var.get(),
                self.prn_var.get(),
                self.id_var.get(),
                self.name_var.get(),
                self.address_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook_var.get(),
                self.latereturnfine_var.get(),
                self.dateoverdue_var.get(),
                self.finalprice_var.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Member has been inserted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE LIBRARY SET Member=%s, ID=%s, Name=%s, Address=%s, PostID=%s, Mobile=%s, BookID=%s, Booktitle=%s, Author=%s, Dateborrowed=%s, Datedue=%s, Daysonbook=%s, Latereturnfine=%s, Dateoverdue=%s, Finalprice=%s WHERE PRN_NO=%s",(
            self.member_var.get(),
            self.id_var.get(),
            self.name_var.get(),
            self.address_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            self.prn_var.get()
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member has been updated")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.name_var.set(row[3])
        self.address_var.set(row[4]),
        self.postcode_var.set(row[5]),
        self.mobile_var.set(row[6]),
        self.bookid_var.set(row[7]),
        self.booktitle_var.set(row[8]),
        self.author_var.set(row[9]),
        self.dateborrowed_var.set(row[10]),
        self.datedue_var.set(row[11]),
        self.daysonbook_var.set(row[12]),
        self.latereturnfine_var.set(row[13]),
        self.dateoverdue_var.set(row [14]),
        self.finalprice_var.set(row[15])

    def showData(self):
        self.txtBox.insert(END, "Member Type\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No: \t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No: \t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END, "Name:\t\t"+ self.name_var.get() + "\n")
        self.txtBox.insert(END, "Address: \t\t"+ self.address_var.get() + "\n")
        self.txtBox.insert(END, "Post Code: \t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No: \t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Auther:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END, "DateBorrowed: \t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "DateDue: \t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook: \t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "LateRateFine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverDue: \t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "FinallPrice:\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set(""),
        self.id_var.set(""),
        self.name_var.set(""),
        self.address_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
            my_cursor = conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","Member has been deleted")

if __name__ == "__main__":
    root=Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
