from tkinter import *
import psycopg2

root = Tk()
root.title("Škola a datáze")
root.geometry("300x280")
root.resizable(False,False)

# functions
def insert_data(name, age, address):
    connection = psycopg2.connect(
                dbname='student',
                user='postgres',
                password='admin',
                host='localhost',
                port='5432'
            )
    
    cur = connection.cursor()
    query = ('''INSERT INTO teacher(name, age, address) 
                VALUES (%s, %s, %s)''')
    cur.execute(query, (name, age, address))
    connection.commit()
    connection.close()


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

# button
button = Button(root, text="Add", command=lambda:insert_data(entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)


root.mainloop()
