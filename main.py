import psycopg2

def create():
    connection = psycopg2.connect(
            dbname='student',
            user='postgres',
            password='admin',
            host='localhost',
            port='5432'
        )


    cur = connection.cursor()
    cur.execute('''CREATE TABLE teacher(
                ID SERIAL,
                NAME TEXT,
                AGE INT,
                ADDRESS TEXT
        )''')
    connection.commit()
    connection.close()

