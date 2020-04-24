#CREAR UNA BASE DE DATOS CON NUEVOS PRODUCTOS

import sqlite3

conexion = sqlite3.connect("database0.db")
cursor = conexion.cursor()

#cursor.execute("CREATE TABLE PRODUCTOS (id INTEGER,nombre TEXT,presio INTEGER)")
#lista1 = [(1,'impresora',300),(2,'raton',20),(3,'ordenador',600)]
#cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",lista1)
cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()

for productos in productos:
    print(productos)

#conexion.commit()
conexion.close()
