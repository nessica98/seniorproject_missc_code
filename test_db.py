import csv
import psycopg2

import csv

conn = psycopg2.connect(
    host="localhost",
    database="test1",
    user="postgres",
    password="1234")

 # create a cursor
cur = conn.cursor()
        
	# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')

        # display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)
sql = """INSERT INTO public.fakegps("nodeName","LAT","LONG","UpdateDatetime") VALUES(%s,%s,%s,%s) ;"""

with open('result1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row[1])
        cur = conn.cursor()
        cur.execute(sql, (row[0],row[1],row[2],row[3]))
        conn.commit()

        