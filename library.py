from tkinter import*
from tkinter import ttk

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1280x720+0+0")


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1280,height=300)

        #DataFrameLeft
        DataFrameLeft=LabelFrame(frame,text="Library Member Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=700,height=265)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",8,"bold"),width=37,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtPRN_No.grid(row=1,column=1)

        lblID_No=Label(DataFrameLeft,bg="powder blue",text="ID No",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblID_No.grid(row=2,column=0,sticky=W)
        txtID_No=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtID_No.grid(row=2,column=1)

        lblN=Label(DataFrameLeft,bg="powder blue",text="Name",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblN.grid(row=3,column=0,sticky=W)
        txtN=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtN.grid(row=3,column=1)

        lblA=Label(DataFrameLeft,bg="powder blue",text="Address",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblA.grid(row=4,column=0,sticky=W)
        txtA=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtA.grid(row=4,column=1)

        lblPC=Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblPC.grid(row=5,column=0,sticky=W)
        txtPC=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtPC.grid(row=5,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblMobile.grid(row=6,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtMobile.grid(row=6,column=1)

        lblBID=Label(DataFrameLeft,bg="powder blue",text="Book ID",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblBID.grid(row=7,column=0,sticky=W)
        txtBID=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtBID.grid(row=7,column=1)

        lblBT=Label(DataFrameLeft,bg="powder blue",text="Book Title",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblBT.grid(row=0,column=2,sticky=W)
        txtBT=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtBT.grid(row=0,column=3)

        lblAN=Label(DataFrameLeft,bg="powder blue",text="Author Name",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblAN.grid(row=1,column=2,sticky=W)
        txtAN=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtAN.grid(row=1,column=3)

        lblDB=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblDB.grid(row=2,column=2,sticky=W)
        txtDB=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtDB.grid(row=2,column=3)

        lblDD=Label(DataFrameLeft,bg="powder blue",text="Date Due",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblDD.grid(row=3,column=2,sticky=W)
        txtDD=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtDD.grid(row=3,column=3)

        lblDOB=Label(DataFrameLeft,bg="powder blue",text="Days On Book",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblDOB.grid(row=4,column=2,sticky=W)
        txtDOB=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtDOB.grid(row=4,column=3)

        lblLRF=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblLRF.grid(row=5,column=2,sticky=W)
        txtLRF=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtLRF.grid(row=5,column=3)

        lblDOD=Label(DataFrameLeft,bg="powder blue",text="Date Over Due",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblDOD.grid(row=6,column=2,sticky=W)
        txtDOD=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
        txtDOD.grid(row=6,column=3)

        lblAP=Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("times new roman",8,"bold"),padx=2,pady=6)
        lblAP.grid(row=7,column=2,sticky=W)
        txtAP=Entry(DataFrameLeft,font=("times new roman",8,"bold"),width=40)
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
                 "Nineteen Eighty-Four","The Grapes of Wrath","1984",]
        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=11)
        listBox.grid(row=0,column=0,padx=4,)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        #Buttons Frame
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=430,width=1280,height=70)

        btnAddData=Button(Framebutton,text="Add Data",font=("times new roman",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button (Framebutton, text="Show Data", font=("times new roman", 12, "bold"), width=21, bg="blue",fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData=Button (Framebutton, text="Update", font=("times new roman", 12, "bold"), width=21, bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData=Button (Framebutton, text="Delete", font=("times new roman", 12, "bold"), width=21, bg="blue", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData=Button (Framebutton, text="Reset", font=("times new roman", 12, "bold"),width=21, bg="blue",fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData=Button (Framebutton, text="Exit", font=("times new roman", 12, "bold"), width=21, bg="blue",fg="white")
        btnAddData.grid(row=0, column=5)

        #Information Frame
        Framedetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framedetails.place(x=0,y=500,width=1280,height=157)

        Table_frame=Frame(Framedetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1220,height=130)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","name","address","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"))
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



if __name__ == "__main__":
    root=Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()