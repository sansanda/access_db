import pyodbc

#debemos usar un interprete de 64bits
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\db\BD_Artardor.accdb;')

cursor = conn.cursor()
cursor.execute("select * from Artistes")

for row in cursor.fetchall():
    print(row)
