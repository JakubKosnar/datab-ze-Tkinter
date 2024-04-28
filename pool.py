import psycopg2
from psycopg2 import pool


# inicializace poolu
db_pool = pool.SimpleConnectionPool(1, 10,
                                    dbname='student',
                                    user='postgres',
                                    password='admin',
                                    host='localhost',
                                    port='5432')


def create_table():
    with db_pool.getconn() as conn:
        with conn.cursor() as cur:
            cur.execute('''CREATE TABLE test(
                ID SERIAL,
                NAME TEXT,
                AGE INT,
                ADDRESS TEXT
            )''')
            conn.commit()
        db_pool.putconn(conn)

def insert_data():

    teacher_name = input("Jmeno učitele: ")
    teacher_age = input("věk učitele: ")
    teacher_adress = input("adresa učitele: ")


    with db_pool.getconn() as conn:
        with conn.cursor() as cur:
            query = ('''INSERT INTO test(name, age, address) VALUES (%s, %s, %s)''')
            cur.execute(query, (teacher_name, teacher_age, teacher_adress))
            conn.commit()
        db_pool.putconn(conn)

insert_data()

# def insert_data():
#     connection = psycopg2.connect(
#                 dbname='student',
#                 user='postgres',
#                 password='admin',
#                 host='localhost',
#                 port='5432'
#             )
    
#     teacher_name = input("Jmeno učitele: ")
#     teacher_age = input("věk učitele: ")
#     teacher_adress = input("adresa učitele: ")

#     cur = connection.cursor()
#     query = ('''INSERT INTO teacher(name, age, address) 
#                 VALUES (%s, %s, %s)''')
#     cur.execute(query, (teacher_name, teacher_age, teacher_adress))
#     connection.commit()
#     connection.close()
    
# insert_data()