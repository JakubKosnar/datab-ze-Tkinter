from tkinter import *
import psycopg2

root = Tk()
root.title("Škola a datáze")
root.geometry("300x280")
root.resizable(False,False)

# labels a entries
label_general = Label(root, text="Add data")
label_general.grid(row=0, column=1)

# name section
label_name = Label(root, text="Name: ")
label_name.grid(row=1, column=0)

entry_name = Entry(root)
entry_name.grid(row=1, column=1)

# age section
label_age = Label(root, text="Age: ")
label_age.grid(row=2, column=0)

entry_age = Entry(root)
entry_age.grid(row=2, column=1)

# address section
label_address = Label(root, text="Address: ")
label_address.grid(row=3, column = 0)

entry_address = Entry(root)
entry_address.grid(row=3, column=1)


root.mainloop()
