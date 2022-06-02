from tkinter import *
import sqlite3
root = Tk()
root.title("Add_Material Table")
root.geometry("400x400")

con = sqlite3.connect("add_material.db")
c = con.cursor()

c.execute("""CREATE TABLE material(
        type_of_material text,
        name_of_material text,
        author text,
        month text,
        date integer,
        year integer
        )""")

con.commit()
con.close()
mainloop()