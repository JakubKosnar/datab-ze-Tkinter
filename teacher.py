from tkinter import *
import psycopg2
from psycopg2 import pool

root = Tk()
root.title("Škola a datáze")
root.geometry("330x320")
root.resizable(False,False)

db_pool = pool.SimpleConnectionPool(1, 10, 
                                    dbname='student',
                                    user='postgres',
                                    password='admin',
                                    host='localhost',
                                    port='5432')

# functions
def insert_data(name, age, address):
    if name and age and address: 
        entry_name.delete(0, END)
        entry_age.delete(0, END)
        entry_address.delete(0, END)

        with db_pool.getconn() as conn:
            with conn.cursor() as cur:
                query = ('''INSERT INTO teacher(name, age, address) 
                            VALUES (%s, %s, %s)''')
                cur.execute(query, (name, age, address))
                conn.commit()
            db_pool.putconn(conn)
        show_db()
    else:
        listbox.delete(0,END)
        listbox.insert(0, "zadejte všechny položky")

 
def search_id(id):
    with db_pool.getconn() as conn:
            with conn.cursor() as cur:
                query = ('''SELECT * FROM teacher WHERE id = (%s) ''')
                cur.execute(query, (id,))
                searched_teacher = cur.fetchone()
                display_search(searched_teacher)
                conn.commit()
            db_pool.putconn(conn)

    
def display_search(data):
    listbox.delete(0,END)
    if data:
        listbox.insert(0,("id:",data[0]), ("name:",data[1]), ("age:",data[2]), ("address:",data[3]))
    else:
        listbox.insert(0,"ID nenalezeno")

def down_db():
    with db_pool.getconn() as conn:
            with conn.cursor() as cur:
                query = ('''SELECT * FROM teacher''')
                cur.execute(query)
                all_teacher = cur.fetchall()
                conn.commit()
            db_pool.putconn(conn)
    return all_teacher


def error_id():
     listbox.delete(0,END)
     listbox.insert(0,"zadejte ID")

def show_db():
    listbox.delete(0,END)
    all_teacher = down_db()
    for teacher in all_teacher:
            listbox.insert(END,teacher)

def delete_from_db(listbox):
    selected_indices = listbox.curselection()
    to_delete = str(listbox.get(selected_indices)[0])
    
    with db_pool.getconn() as conn:
        with conn.cursor() as cur:
            query = ('''DELETE FROM teacher WHERE id = %s''')
            cur.execute(query, (to_delete,))
            conn.commit()
        db_pool.putconn(conn)
    show_db()

    
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
button = Button(root, text="Add", command=lambda:insert_data(entry_name.get().strip(), entry_age.get().strip(), entry_address.get().strip()))
button.grid(row=4, column=1)

## search section
# general label
label_search = Label(root, text=" Search data")
label_search.grid(row=5, column=1)

label_id = Label(root, text="Search by id: ")
label_id.grid(row=6, column=0)

entry_id=Entry(root)
entry_id.grid(row=6, column=1)

button_search = Button(root, text="search", command=lambda:search_id(entry_id.get()) if entry_id.get().strip() else error_id())
button_search.grid(row=6, column=3)

# vložení listboxu
listbox = Listbox(root, width=20, height=7)
listbox.grid(row=7, column=1)

# vytvoření scrollbar widgetu
scrollbar = Scrollbar(root)
# umístění scrollbar v okně
scrollbar.grid(row=7, column=2, sticky="nsw")
# připojení Scrollbar k listboxu
# scrollbar reaguje na posouvání v listboxu
listbox.config(yscrollcommand=scrollbar.set)
# listbox reaguje na posouvání scrollbarem
scrollbar.config(command=listbox.yview)

# tlačítko na zobrazení celé databáze
button_showall = Button(root, text="show database", command=show_db, height=2, width=7, wraplength=60)
button_showall.grid(row=7, column=3, sticky="e")

# tlačítko na smazání položky z databáze
button_delete = Button(root, text="delete from db", command=lambda:delete_from_db(listbox))
button_delete.grid(row=8, column=1)

show_db()

root.mainloop()
