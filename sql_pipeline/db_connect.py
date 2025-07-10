#select first_name, last_name, gender from people where first_name like 'B%';
import psycopg2

# Establish the connection
conn = psycopg2.connect(
    dbname="stemma_db_copy", 
    user="postgres", 
    password="andrewroot", 
    host="localhost"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM people;")
print(cursor.fetchall())

cursor.close()
conn.close()