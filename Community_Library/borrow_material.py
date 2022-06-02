from tkinter import *
import sqlite3
root = Tk()
root.title("Borrow_Material Table")
root.geometry("400x400")

con = sqlite3.connect("borrow_material.db")
c = con.cursor()

c.execute("""CREATE TABLE borrow(
        first_name text,
        last_name text,
        contact_num integer,
        name_of_material text,
        month_borrow text,
        date_borrow integer,
        year_borrow integer,
        month_return text,
        date_return integer,
        year_return integer
        )""")

con.commit()
con.close()
mainloop()