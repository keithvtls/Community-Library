from tkinter import *
from tkinter import messagebox
# from PIL import ImageTk, Image
import sqlite3

lobby = Tk()
lobby.title("Community Library Management System")
lobby.geometry("900x500+300+150")
lobby.configure(background="light blue")
lobby.resizable(0, 0)

            #----------------------------login window-----------------------------

class maincode:

    def code(self):
        main_frame = Frame(lobby, height=500, width=900, bg='white')
        main_frame.place(x=0, y=0)

        self.main_canvas = Canvas(main_frame, height=500, width=900, bg='light blue')
        self.main_canvas.place(x=0, y=0)

        self.main_photo = PhotoImage(file="MainWindow.png")
        self.main_canvas.create_image(70, 45, image=self.main_photo, anchor=NW)

        self.fm1 = Frame(self.main_canvas, height=260, width=300, bg='white', bd=3, relief='ridge')
        self.fm1.place(x=300, y=170)

        self.frame1 = Frame(self.main_canvas, height=65, width=400, bg='white', bd=3, relief='ridge')
        self.frame1.place(x=255, y=75)

        self.library_label = Label(main_frame, text="Community Library", bg="white", font=("times new roman", 30, "bold", "underline"))
        self.library_label.place(x=280, y=80)

        self.head_label = Label(main_frame, text="Log-In", bg="white", font=("consolas", 20, "bold"))
        self.head_label.place(relx=0.47, rely=0.4)

        self.position_label = Label(main_frame, text="Position", bg="white", font=("consolas", 10, "bold"))
        self.position_label.place(relx=0.37, rely=0.5)

        self.password_label = Label(main_frame, text="Password", bg="white", font=("consolas", 10, "bold"))
        self.password_label.place(relx=0.37, rely=0.6)

        self.login_btn = Button(main_frame, text='login', fg='white', bg='red', width=100, font=('Arial', 11, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.login_btn.bind("<Button-1>", self.dashboard)
        self.login_btn.place(x=25, y=160, relx=0.33, rely=0.37)
        self.logo1 = PhotoImage(file='user.png')
        self.login_btn.config(image=self.logo1, compound=LEFT)
        self.small_logo1 = self.logo1.subsample(1, 1)
        self.login_btn.config(image=self.small_logo1)

        self.clear_btn = Button(main_frame, text='Clear', fg='white', bg='blue', width=100, font=('Arial', 11, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2',
                           command=lobby.destroy)
        self.clear_btn.place(x=155, y=160, relx=0.35, rely=0.37)
        self.logo2 = PhotoImage(file='cart.png')
        self.clear_btn.config(image=self.logo2, compound=LEFT)
        self.small_logo2 = self.logo2.subsample(1, 1)
        self.clear_btn.config(image=self.small_logo2)

        self.position_box = Entry(main_frame, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.position_box.place(relx=0.47, rely=0.5)
        self.pass_box = Entry(main_frame, width=22, show='*', font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.pass_box.bind("<Return>", self.dashboard)
        self.pass_box.place(relx=0.47, rely=0.6)

                # -----------------dashboard window-----------------

    def dashboard(self,event):
        self.under_fm = Frame(lobby, height=500, width=900, bg='#fff')
        self.under_fm.place(x=0, y=0)
        self.fm2 = Frame(lobby, bg='#22224b', height=80, width=900)
        self.fm2.place(x=0, y=0)

        self.canvas1 = Canvas(self.under_fm, bg='black', width=400, height=300)
        self.canvas1.place(x=475, y=145)
        self.photo2 = PhotoImage(file="dashboard.png")
        self.canvas1.create_image(0, 0, image=self.photo2, anchor=NW)

        self.dashboard_lbl = Label(lobby, text='DASHBOARD', fg='White', bg='#22224b', font=('Arial', 30, 'bold'))
        self.dashboard_lbl.place(x=325, y=17)

                # -----------------add book button-----------------

        self.add_book_btn = Button(self.under_fm, text='Add Books', fg='black', bg='light blue', font=('Arial', 12, 'bold'), width=170,
                          height=0, bd=7, relief='flat', cursor='hand2', command=self.add_book)
        self.add_book_btn.place(x=60, y=125, relwidth=0.4, relheight=0.09)
        self.logo3 = PhotoImage(file='bt1.png')
        self.add_book_btn.config(image=self.logo3, compound=LEFT)
        self.small_logo3 = self.logo3.subsample(1, 1)
        self.add_book_btn.config(image=self.small_logo3)

                # -----------------add client button-----------------

        self.add_client_btn = Button(self.under_fm, text='Add Client', fg='black', bg='light blue',
                                     font=('Arial', 12, 'bold'),
                                     width=170, height=0, bd=7, relief='flat', cursor='hand2', command=self.add_client)
        self.add_client_btn.place(x=60, y=185, relwidth=0.4, relheight=0.09)
        self.logo4 = PhotoImage(file='bt2.png')
        self.add_client_btn.config(image=self.logo4, compound=LEFT)
        self.small_logo4 = self.logo4.subsample(1, 1)
        self.add_client_btn.config(image=self.small_logo4)

                 # -----------------Borrow book button-----------------

        self.borrow_book_btn = Button(self.under_fm, text='Borrow Books', fg='black', bg='light blue',
                                  font=('Arial', 12, 'bold'),
                                  width=170, height=0, bd=7, relief='flat', cursor='hand2', command=self.borrow_book)
        self.borrow_book_btn.place(x=60, y=245, relwidth=0.4, relheight=0.09)
        self.logo5 = PhotoImage(file='bt3.png')
        self.borrow_book_btn.config(image=self.logo5, compound=LEFT)
        self.small_logo5 = self.logo5.subsample(1, 1)
        self.borrow_book_btn.config(image=self.small_logo5)

                 # -----------------Return button-----------------

        self.return_book_btn = Button(self.under_fm, text='Return Books', fg='black', bg='light blue',
                                  font=('Arial', 12, 'bold'),
                                  width=170, height=0, bd=7, relief='flat', cursor='hand2', command=self.return_book)
        self.return_book_btn.place(x=60, y=305, relwidth=0.4, relheight=0.09)
        self.logo6 = PhotoImage(file='bt4.png')
        self.return_book_btn.config(image=self.logo6, compound=LEFT)
        self.small_logo6 = self.logo6.subsample(1, 1)
        self.return_book_btn.config(image=self.small_logo6)

                # -----------------library history button-----------------

        self.history_btn = Button(self.under_fm, text="Library's History", fg='black', bg='light blue', font=('Arial', 12, 'bold'),
                          width=170, height=0, bd=7, relief='flat', cursor='hand2', command=self.lib_history)
        self.history_btn.place(x=60, y=365, relwidth=0.4, relheight=0.09)
        self.logo8 = PhotoImage(file='bt5.png')
        self.history_btn.config(image=self.logo8, compound=LEFT)
        self.small_logo8 = self.logo8.subsample(1, 1)
        self.history_btn.config(image=self.small_logo8)

                # -----------------logout button-----------------

        self.logout_btn = Button(self.under_fm, text='Log-Out', fg='#fff', bg='red', font=('Arial', 12, 'bold'),
                          width=170, height=0, bd=7, relief='flat', cursor='hand2', command=self.code)
        self.logout_btn.place(x=60, y=430, relwidth=0.4, relheight=0.09)
        self.logo9 = PhotoImage(file='bt6.png')
        self.logout_btn.config(image=self.logo9, compound=LEFT)
        self.small_logo9 = self.logo9.subsample(1, 1)
        self.logout_btn.config(image=self.small_logo9)

                 # ------------------ADD BOOK------------------

    def add_book(self):
        self.under_fm1 = Frame(lobby, height=500, width=900, bg='#fff')
        self.under_fm1.place(x=0, y=0)
        self.fm3 = Frame(lobby, bg='#22224b', height=80, width=900)
        self.fm3.place(x=0, y=0)

        self.add_book_header = Label(lobby, text='ADD BOOK', fg='White', bg='#22224b', font=('Arial', 30, 'bold'))
        self.add_book_header.place(x=350, y=17)

        self.type_material = Label(lobby, text='Type of Material', fg='black', bg='white', font=('Arial', 12))
        self.type_material.place(x=80, y=180)

        self.name_material = Label(lobby, text='Name of Material', fg='black', bg='white', font=('Arial', 12))
        self.name_material.place(x=80, y=230)

        self.author = Label(lobby, text="Author's Name", fg='black', bg='white', font=('Arial', 12))
        self.author.place(x=80, y=280)

        self.date_published = Label(lobby, text='Date Published:', fg='black', bg='white', font=('Arial', 12))
        self.date_published.place(x=80, y=330)

        self.month = Label(lobby, text='Month', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.month.place(x=245, y=330)
        self.day = Label(lobby, text='Day', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.day.place(x=330, y=330)
        self.year = Label(lobby, text='Year', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.year.place(x=410, y=330)

        self.type_material_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.type_material_box.place(relx=0.25, rely=0.36, relwidth=0.5)

        self.name_material_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.name_material_box.place(relx=0.25, rely=0.46, relwidth=0.5)

        self.author_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.author_box.place(relx=0.25, rely=0.56, relwidth=0.5)

        self.month_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.month_box.place(relx=0.25, rely=0.72, relwidth=0.1)
        self.day_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.day_box.place(relx=0.36, rely=0.72, relwidth=0.05)
        self.year_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.year_box.place(relx=0.42, rely=0.72, relwidth=0.1)

        self.submit_btn = Button(self.under_fm1, text="Submit",
                                 fg='white', bg='red', width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2', command=self.add_book_submit_btn)
        self.submit_btn.place(x=10, y=220, relx=0.33, rely=0.37)

        self.show_book_btn = Button(self.under_fm1, text="Show Books",
                                 fg='black', bg='#33cccc', width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.show_book_btn.bind("<Button-1>", self.show_books)
        self.show_book_btn.place(relx=0.15, rely=0.17, relwidth=0.12, relheight=0.1)

        self.back_btn = Button(self.under_fm1, text="Back", fg='black', bg='light blue', width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.back_btn.bind("<Button-1>", self.dashboard)
        self.back_btn.place(relx=0.01, rely=0.17, relwidth=0.1, relheight=0.1)

    def show_books(self, event):
        self.under_fm1 = Frame(lobby, height=500, width=900, bg='#fff')
        self.under_fm1.place(x=0, y=0)
        self.fm3 = Frame(lobby, bg='#22224b', height=80, width=900)
        self.fm3.place(x=0, y=0)

        self.add_book_header = Label(lobby, text='LIBRARY BOOKS', fg='White', bg='#22224b',
                                        font=('Arial', 30, 'bold'))
        self.add_book_header.place(x=290, y=17)

        self.type_of_material = Label(lobby, text='Type of Material', fg='black', bg='white',
                                        font=('Arial', 15, 'bold'))
        self.type_of_material.place(x=20, y=140)

        self.name_of_material = Label(lobby, text='Name of Material', fg='black', bg='white',
                                        font=('Arial', 15, 'bold'))
        self.name_of_material.place(x=250, y=140)

        self.author_name = Label(lobby, text="Author's Name", fg='black', bg='white', font=('Arial', 15, 'bold'))
        self.author_name.place(x=490, y=140)

        self.date_published = Label(lobby, text='Date Published', fg='black', bg='white',
                                    font=('Arial', 15, 'bold'))
        self.date_published.place(x=730, y=140)

        self.back_btn = Button(self.under_fm1, text="Back to DashBoard", fg='black', bg='light blue', width=30,
                               font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.back_btn.bind("<Button-1>", self.dashboard)
        self.back_btn.place(relx=0.01, rely=0.17, relwidth=0.17, relheight=0.1)

            # --------------------DATA BASE SHOW BOOKS------------------#

        con = sqlite3.connect("add_material.db")
        c = con.cursor()

        c.execute("SELECT *, oid FROM material")
        library_books = c.fetchall()
        lib_book_type_material = " "
        lib_book_name_material = " "
        lib_book_author = " "
        lib_book_date_published = " "

        for record in library_books:
            lib_book_type_material += str(record[6]) + ") " + str(record[0]) + "\n\n"
        self.type_of_material = Label(lobby, text=lib_book_type_material, fg='black', bg="white",
                                        font=('Arial', 12))
        self.type_of_material.place(x=32, y=180)

        for record in library_books:
            lib_book_name_material += str(record[1]) + "\n\n"
        self.name_of_material = Label(lobby, text=lib_book_name_material, fg='black', bg="white",
                                        font=('Arial', 12))
        self.name_of_material.place(x=250, y=180)

        for record in library_books:
            lib_book_author += str(record[2]) + "\n\n"
        self.author = Label(lobby, text=lib_book_author, fg='black', bg="white", font=('Arial', 12))
        self.author.place(x=510, y=180)

        for record in library_books:
            lib_book_date_published += str(record[3]) + " " + str(record[4]) + ", " + str(record[5]) + "\n\n"
        self.date_of_published = Label(lobby, text=lib_book_date_published, fg='black', bg="white",
                                        font=('Arial', 12))
        self.date_of_published.place(x=750, y=180)

        con.commit()
        con.close()

                # ---------------DataBase ADD BOOK-------------------#

    def add_book_submit_btn(self):
        con = sqlite3.connect("add_material.db")
        c = con.cursor()

        c.execute("INSERT INTO material VALUES(:type_of_material,:name_of_material,:author,:month,:date,:year)",
                  {
                      "type_of_material": self.type_material_box.get(),
                      "name_of_material": self.name_material_box.get(),
                      "author": self.author_box.get(),
                      "month": self.month_box.get(),
                      "date": self.day_box.get(),
                      "year": self.year_box.get()
                  })
        con.commit()
        con.close()

        self.type_material_box.delete(0, END)
        self.name_material_box.delete(0, END)
        self.author_box.delete(0, END)
        self.month_box.delete(0, END)
        self.day_box.delete(0, END)
        self.year_box.delete(0, END)

        messagebox.showinfo("Update", "New material has been added in the library")

    # --------------------ADD CLIENT------------------#

    def add_client(self):
        self.under_fm1 = Frame(lobby, height=500, width=900, bg='#fff')
        self.under_fm1.place(x=0, y=0)
        self.fm3 = Frame(lobby, bg='#22224b', height=80, width=900)
        self.fm3.place(x=0, y=0)

        self.add_client_header = Label(lobby, text='ADD CLIENT', fg='White', bg='#22224b', font=('Arial', 30, 'bold'))
        self.add_client_header.place(x=350, y=17)

        self.f_name = Label(lobby, text='First Name', fg='black', bg='white', font=('Arial', 12))
        self.f_name.place(x=80, y=180)

        self.l_name = Label(lobby, text='Last Name', fg='black', bg='white', font=('Arial', 12))
        self.l_name.place(x=80, y=230)

        self.gender = Label(lobby, text="Gender", fg='black', bg='white', font=('Arial', 12))
        self.gender.place(x=80, y=280)

        self.contact_num = Label(lobby, text="Contact Number", fg='black', bg='white', font=('Arial', 12))
        self.contact_num.place(x=80, y=330)

        self.address = Label(lobby, text="Address", fg='black', bg='white', font=('Arial', 12))
        self.address.place(x=80, y=380)

        self.f_name_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.f_name_box.place(relx=0.25, rely=0.36, relwidth=0.5)

        self.l_name_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.l_name_box.place(relx=0.25, rely=0.46, relwidth=0.5)

        self.gender_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.gender_box.place(relx=0.25, rely=0.56, relwidth=0.5)

        self.contact_number_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.contact_number_box.place(relx=0.25, rely=0.66, relwidth=0.5)

        self.address_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.address_box.place(relx=0.25, rely=0.76, relwidth=0.5)

        self.submit_btn = Button(self.under_fm1, text="Submit", command=self.add_client_submit_btn,
                                 fg='white', bg='red', width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.submit_btn.place(x=10, y=240, relx=0.33, rely=0.37)

        self.back_btn = Button(self.under_fm1, text="Back", fg='black', bg='light blue', width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.back_btn.bind("<Button-1>", self.dashboard)
        self.back_btn.place(relx=0.01, rely=0.17, relwidth=0.1, relheight=0.1)

        # ---------------DataBase ADD CLIENT-------------------#

    def add_client_submit_btn(self):
        con = sqlite3.connect("membership.db")
        c = con.cursor()

        c.execute("INSERT INTO client VALUES(:first_name,:last_name,:gender,:contact_number,:address)",
                  {
                      "first_name": self.f_name_box.get(),
                      "last_name": self.l_name_box.get(),
                      "gender": self.gender_box.get(),
                      "contact_number": self.contact_number_box.get(),
                      "address": self.address_box.get()
                  })
        con.commit()
        con.close()

        self.f_name_box.delete(0, END)
        self.l_name_box.delete(0, END)
        self.gender_box.delete(0, END)
        self.contact_number_box.delete(0, END)
        self.address_box.delete(0, END)

        messagebox.showinfo("Update", "Successfully added new client")

            #--------------------BORROW BOOK------------------#

    def borrow_book(self):
        self.under_fm1 = Frame(lobby, height=500, width=900, bg='#fff')
        self.under_fm1.place(x=0, y=0)
        self.fm3 = Frame(lobby, bg='#22224b', height=80, width=900)
        self.fm3.place(x=0, y=0)

        self.add_client_header = Label(lobby, text='BORROW BOOKS', fg='White', bg='#22224b', font=('Arial', 30, 'bold'))
        self.add_client_header.place(x=290, y=17)

        self.f_name = Label(lobby, text='First Name', fg='black', bg='white', font=('Arial', 12))
        self.f_name.place(x=80, y=160)

        self.l_name = Label(lobby, text='Last Name', fg='black', bg='white', font=('Arial', 12))
        self.l_name.place(x=80, y=205)

        self.contact_number = Label(lobby, text="Contact Number", fg='black', bg='white', font=('Arial', 12))
        self.contact_number.place(x=80, y=250)

        self.name_material = Label(lobby, text="Name of Material", fg='black', bg='white', font=('Arial', 12))
        self.name_material.place(x=80, y=300)

        self.month = Label(lobby, text='Month', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.month.place(x=245, y=330)
        self.day = Label(lobby, text='Day', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.day.place(x=330, y=330)
        self.year = Label(lobby, text='Year', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.year.place(x=410, y=330)

        self.date_borrowed = Label(lobby, text="Date Borrowed", fg='black', bg='white', font=('Arial', 12))
        self.date_borrowed.place(x=80, y=360)

        self.expected_return_date = Label(lobby, text="Date of Return", fg='black', bg='white', font=('Arial', 12))
        self.expected_return_date.place(x=80, y=400)

        self.note = Label(lobby, text="Note: The book should be returned within a month", fg='red', bg='white',
                          font=('Arial', 12, 'italic', 'bold'))
        self.note.place(x=80, y=460)

        self.f_name_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.f_name_box.place(relx=0.25, rely=0.33, relwidth=0.5)

        self.l_name_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.l_name_box.place(relx=0.25, rely=0.41, relwidth=0.5)

        self.contact_number_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.contact_number_box.place(relx=0.25, rely=0.50, relwidth=0.5)

        self.name_material_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.name_material_box.place(relx=0.25, rely=0.60, relwidth=0.5)

        self.month_borrow_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.month_borrow_box.place(relx=0.25, rely=0.72, relwidth=0.1)
        self.day_borrow_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.day_borrow_box.place(relx=0.36, rely=0.72, relwidth=0.05)
        self.year_borrow_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.year_borrow_box.place(relx=0.42, rely=0.72, relwidth=0.1)

        self.month_return_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.month_return_box.place(relx=0.25, rely=0.80, relwidth=0.1)
        self.day_return_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.day_return_box.place(relx=0.36, rely=0.80, relwidth=0.05)
        self.year_return_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.year_return_box.place(relx=0.42, rely=0.80, relwidth=0.1)

        self.submit_btn = Button(self.under_fm1, text="Submit", command=self.borrow_book_submit_btn, fg='white', bg='red',
                            width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.submit_btn.place(relx=0.35, rely=0.87, relwidth=0.25, relheight=0.05)

        self.back_btn = Button(self.under_fm1, text="Back", fg='black', bg='light blue', width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.back_btn.bind("<Button-1>", self.dashboard)
        self.back_btn.place(relx=0.01, rely=0.17, relwidth=0.1, relheight=0.1)

    def borrow_book_submit_btn(self):
        receipt = Tk()
        receipt.title("Receipt")
        receipt.geometry("400x400")
        receipt.configure(background="light blue")
        receipt.resizable(0, 0)

        self.under_fm1 = Frame(receipt, height=400, width=400, bg='#fff')
        self.under_fm1.place(x=0, y=0)
        self.fm3 = Frame(receipt, bg='#22224b', height=80, width=400)
        self.fm3.place(x=0, y=0)

        self.add_client_header = Label(receipt, text='RECEIPT', fg='White', bg='#22224b',
                                        font=('Arial', 30, 'bold'))
        self.add_client_header.place(x=120, y=17)

        self.f_name = Label(receipt, text='First Name: ' + '\t' + self.f_name_box.get(), fg='black', bg='white',
                                font=('Arial', 12))
        self.f_name.place(x=40, y=120)

        self.l_name = Label(receipt, text='Last Name: ' + '\t' + self.l_name_box.get(), fg='black', bg='white',
                                font=('Arial', 12))
        self.l_name.place(x=40, y=170)

        self.contact_number = Label(receipt, text="Contact Number: " + '\t' + self.contact_number_box.get(),
                                    fg='black', bg='white', font=('Arial', 12))
        self.contact_number.place(x=40, y=220)

        self.name_material = Label(receipt, text="Name of Material: " + '\t' + self.name_material_box.get(),
                                    fg='black', bg='white', font=('Arial', 12))
        self.name_material.place(x=40, y=270)

        self.month = Label(receipt, text='Month', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.month.place(x=185, y=300)
        self.day = Label(receipt, text='Day', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.day.place(x=255, y=300)
        self.year = Label(receipt, text='Year', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.year.place(x=330, y=300)

        self.date_borrowed = Label(receipt,
                                    text="Date Borrowed: " + '\t' + self.month_borrow_box.get() + '\t' + self.day_borrow_box.get()
                                        + '\t' + self.year_borrow_box.get(), fg='black', bg='white',
                                    font=('Arial', 12))
        self.date_borrowed.place(x=40, y=320)

        self.expected_return_date = Label(receipt,
                                            text="Date Return: " + '\t' + self.month_return_box.get() + '\t' + self.day_return_box.get()
                                                + '\t' + self.year_return_box.get(), fg='black', bg='white',
                                            font=('Arial', 12))
        self.expected_return_date.place(x=40, y=355)

        self.back_btn = Button(self.under_fm1, text="Close", command=receipt.destroy, bg="red", fg="white",
                               activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.back_btn.place(relx=0.01, rely=0.22, relwidth=0.15, relheight=0.05)

        con = sqlite3.connect("borrow_material.db")
        c = con.cursor()

        c.execute("INSERT INTO borrow VALUES(:first_name,:last_name,:contact_number,:name_of_material,\
                                                :month_borrow,:date_borrow,:year_borrow,\
                                                :month_return,:date_return,:year_return)",
                    {
                        "first_name": self.f_name_box.get(),
                        "last_name": self.l_name_box.get(),
                        "contact_number": self.contact_number_box.get(),
                        "name_of_material": self.name_material_box.get(),
                        "month_borrow": self.month_borrow_box.get(),
                        "date_borrow": self.day_borrow_box.get(),
                        "year_borrow": self.year_borrow_box.get(),
                        "month_return": self.month_return_box.get(),
                        "date_return": self.day_return_box.get(),
                        "year_return": self.year_return_box.get()
                    })
        con.commit()
        con.close()

        self.f_name_box.delete(0, END)
        self.l_name_box.delete(0, END)
        self.contact_number_box.delete(0, END)
        self.name_material_box.delete(0, END)
        self.month_borrow_box.delete(0, END)
        self.day_borrow_box.delete(0, END)
        self.year_borrow_box.delete(0, END)
        self.month_return_box.delete(0, END)
        self.day_return_box.delete(0, END)
        self.year_return_box.delete(0, END)

        #--------------------RETURN BOOK------------------#

    def return_book(self):
        self.under_fm1 = Frame(lobby, height=500, width=900, bg='#fff')
        self.under_fm1.place(x=0, y=0)
        self.fm3 = Frame(lobby, bg='#22224b', height=80, width=900)
        self.fm3.place(x=0, y=0)

        self.add_client_header = Label(lobby, text='RETURN BOOKS', fg='White', bg='#22224b', font=('Arial', 30, 'bold'))
        self.add_client_header.place(x=290, y=17)

        self.f_name = Label(lobby, text='First Name', fg='black', bg='white', font=('Arial', 12))
        self.f_name.place(x=80, y=180)

        self.l_name = Label(lobby, text='Last Name', fg='black', bg='white', font=('Arial', 12))
        self.l_name.place(x=80, y=230)

        self.name_of_material = Label(lobby, text="Name of Material", fg='black', bg='white', font=('Arial', 12))
        self.name_of_material.place(x=80, y=280)

        self.returned_date = Label(lobby, text="Returned Date", fg='black', bg='white', font=('Arial', 12))
        self.returned_date.place(x=80, y=330)

        self.month = Label(lobby, text='Month', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.month.place(x=245, y=305)
        self.day = Label(lobby, text='Day', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.day.place(x=330, y=305)
        self.year = Label(lobby, text='Year', fg='black', bg='white', font=('Arial', 10, 'bold'))
        self.year.place(x=410, y=305)

        self.f_name_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.f_name_box.place(relx=0.25, rely=0.36, relwidth=0.5)

        self.l_name_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.l_name_box.place(relx=0.25, rely=0.46, relwidth=0.5)

        self.name_of_material_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.name_of_material_box.place(relx=0.25, rely=0.56, relwidth=0.5)

        self.month_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.month_box.place(relx=0.25, rely=0.66, relwidth=0.1)
        self.day_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.day_box.place(relx=0.36, rely=0.66, relwidth=0.05)
        self.year_box = Entry(lobby, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.year_box.place(relx=0.42, rely=0.66, relwidth=0.1)

        self.submit_btn = Button(self.under_fm1, text="Submit", command=self.return_book_submit_btn, fg='white', bg='red',
                            width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.submit_btn.place(x=10, y=240, relx=0.33, rely=0.37)

        self.back_btn = Button(self.under_fm1, text="Back", fg='black', bg='light blue', width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.back_btn.bind("<Button-1>", self.dashboard)
        self.back_btn.place(relx=0.01, rely=0.17, relwidth=0.1, relheight=0.1)

        # ---------------DataBase ADD CLIENT-------------------#

    def return_book_submit_btn(self):
        con = sqlite3.connect("return_material.db")
        c = con.cursor()

        c.execute("INSERT INTO return VALUES(:first_name,:last_name,:name_of_material,:month,:date,:year)",
                    {
                        "first_name": self.f_name_box.get(),
                        "last_name": self.l_name_box.get(),
                        "name_of_material": self.name_of_material_box.get(),
                        "month": self.month_box.get(),
                        "date": self.day_box.get(),
                        "year": self.year_box.get()
                    })
        con.commit()
        con.close()

        self.f_name_box.delete(0, END)
        self.l_name_box.delete(0, END)
        self.name_of_material_box.delete(0, END)
        self.month_box.delete(0, END)
        self.day_box.delete(0, END)
        self.year_box.delete(0, END)

        messagebox.showinfo("Update", "Successfully Return Book")

        #--------------------HISTORY ------------------#

    def lib_history(self):
        self.under_fm1 = Frame(lobby, height=500, width=900, bg='#fff')
        self.under_fm1.place(x=0, y=0)
        self.fm3 = Frame(lobby, bg='#22224b', height=80, width=900)
        self.fm3.place(x=0, y=0)

        self.add_client_header = Label(lobby, text="LIBRARY'S HISTORY", fg='White', bg='#22224b', font=('Arial', 30, 'bold'))
        self.add_client_header.place(x=250, y=17)

        self.name_of_client = Label(lobby, text='Name of Client', fg='black', bg='white', font=('Arial', 15, 'bold'))
        self.name_of_client.place(x=20, y=140)

        self.name_of_material = Label(lobby, text='Name of Material', fg='black', bg='white',
                                      font=('Arial', 15, 'bold'))
        self.name_of_material.place(x=250, y=140)

        self.borrow_date = Label(lobby, text='Date of Borrow', fg='black', bg='white', font=('Arial', 15, 'bold'))
        self.borrow_date.place(x=490, y=140)

        self.expected_return_date = Label(lobby, text='Date of Return', fg='black', bg='white',
                                          font=('Arial', 15, 'bold'))
        self.expected_return_date.place(x=730, y=140)

        self.back_btn = Button(self.under_fm1, text="Back", fg='black', bg='light blue', width=30, font=('Arial', 12, 'bold'),
                           activebackground='white', bd=3, relief='flat', cursor='hand2')
        self.back_btn.bind("<Button-1>", self.dashboard)
        self.back_btn.place(relx=0.01, rely=0.17, relwidth=0.1, relheight=0.1)

        # --------------------DATA BASE LIBRARY'S HISTORY------------------#
        con = sqlite3.connect("borrow_material.db")
        c = con.cursor()

        c.execute("SELECT *, oid FROM borrow")
        library_history = c.fetchall()
        lib_history_name_client = " "
        lib_history_name_material = " "
        lib_history_borrow = " "
        lib_history_expected_return = " "

        for record in library_history:
            lib_history_name_client += str(record[10]) + ") " + str(record[0]) + " " + str(record[1]) + "\n\n"
        self.name_of_client = Label(lobby, text=lib_history_name_client, fg='black', bg="white", font=('Arial', 12))
        self.name_of_client.place(x=10, y=180)

        for record in library_history:
            lib_history_name_material += str(record[3]) + "\n\n"
        self.name_of_material = Label(lobby, text=lib_history_name_material, fg='black', bg="white", font=('Arial', 12))
        self.name_of_material.place(x=300, y=180)

        for record in library_history:
            lib_history_borrow += str(record[4]) + " " + str(record[5]) + ", " + str(record[6]) + "\n\n"
        self.name_of_client = Label(lobby, text=lib_history_borrow, fg='black', bg="white", font=('Arial', 12))
        self.name_of_client.place(x=490, y=180)

        for record in library_history:
            lib_history_expected_return += str(record[7]) + " " + str(record[8]) + ", " + str(record[9]) + "\n\n"
        self.name_of_client = Label(lobby, text=lib_history_expected_return, fg='black', bg="white", font=('Arial', 12))
        self.name_of_client.place(x=740, y=180)

        con.commit()
        con.close()

community_library = maincode()
community_library.code()

lobby.mainloop()

