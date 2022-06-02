from tkinter import *
import sqlite3
root = Tk()
root.title("Return_Material Table")
root.geometry("400x400")

con = sqlite3.connect("return_material.db")
c = con.cursor()

c.execute("""CREATE TABLE return(
        first_name text,
        last_name text,
        name_of_material text,
        month text,
        date integer,
        year integer
        )""")

con.commit()
con.close()
mainloop()