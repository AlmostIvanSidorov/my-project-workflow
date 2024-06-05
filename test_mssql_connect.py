from os import getenv
import pymssql


server = ""
user = ""
password = ""

conn = pymssql.connect(server, user, password, database="dbtest")
cursor = conn.cursor()

cursor.execute('select count(*) from pjrep.msp_epmassignmentbaseline;')
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

conn.close()