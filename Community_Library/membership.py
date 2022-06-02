from tkinter import *
import sqlite3
root = Tk()
root.title("Membership Table")
root.geometry("400x400")

con = sqlite3.connect("membership.db")
c = con.cursor()

c.execute("""CREATE TABLE client(
        fist_name text,
        last_name text,
        gender text,
        contact_number integer,
        address text
        )""")

con.commit()
con.close()
mainloop()