import pyodbc

# debemos usar un interprete de 64bits
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\db\BD_Artardor_3.accdb;')

cursor = conn.cursor()

print("TABLA")
cursor.execute("select * from Participacions")
for row in cursor.fetchall():
    print(row)

# borramos todos los registros de la tabla Participacions
cursor.execute("delete from Participacions")
conn.commit()

print("TABLA")
cursor.execute("select * from Participacions")
for row in cursor.fetchall():
    print(row)

cursor.execute("select * from Artistes")
for row in cursor.fetchall():

    id_artista = 0
    print(id_artista)
    try:
        int(id_artista)
    except ValueError:
        continue

    nom_artista = row[0]
    print(nom_artista)
    exp = ("select * from Participants where NOM_ARTISTA = '" + nom_artista + "'")
    cursor.execute(exp)

    for row in cursor.fetchall():
        print(row)
        anys_participacio = str.split(row[4], ";")
        modalitats = str.split(row[5], ";")

        len_anys_participacio = len(anys_participacio)
        len_modalitats = len(modalitats)

        if len_modalitats == 0: continue
        if len_anys_participacio == 0: continue

        print('****************************************************')
        print(len_anys_participacio, len_modalitats)
        if len_anys_participacio == len_modalitats:
            for any_participacio,modalitat in zip(anys_participacio,modalitats):
                print(any_participacio, modalitat)
                try:
                    int(any_participacio)
                except ValueError:
                    continue

                cursor.execute('''INSERT INTO Participacions (nom_artista,any,modalitat) VALUES (?,?,?)''', (nom_artista, int(any_participacio), modalitat))
                # exp = "INSERT INTO Participacions (id_artista, any_participacio, modalitat) VALUES ('" + str(id_artista) + "','" + str(any_participacio) + "', '" + modalitat + "'"

        if (len_anys_participacio > 1) & (len_modalitats == 1):
            for any_participacio in anys_participacio:
                print(any_participacio, modalitats[0])

                try:
                    int(any_participacio)
                except ValueError:
                    continue

                cursor.execute('''INSERT INTO Participacions (nom_artista,any,modalitat) VALUES (?,?,?)''', (nom_artista, int(any_participacio), modalitats[0]))
                # exp = "INSERT INTO Participacions (id_artista, any_participacio, modalitat) VALUES ('" + str(id_artista) + "','" + str(any_participacio) + "', '" + modalitats[0] + "'"

        if (len_anys_participacio == 1) & (len_modalitats > 1):
            for modalitat in modalitats:
                print(anys_participacio[0], modalitat)

                try:
                    int(anys_participacio[0])
                except ValueError:
                    continue

                cursor.execute('''INSERT INTO Participacions (nom_artista,any,modalitat) VALUES (?,?,?)''', (nom_artista, int(anys_participacio[0]), modalitat))
                # exp = "INSERT INTO Participacions (id_artista, any_participacio, modalitat) VALUES ('" + str(id_artista) + "','" + str(anys_participacio[0]) + "', '" + modalitat + "'"

        if (len_anys_participacio > 1) & (len_modalitats > 1) & (len_anys_participacio != len_modalitats):
            # imposible asignar
            print('imposible asignar')
            print(anys_participacio, modalitats)
            pass

        conn.commit()
