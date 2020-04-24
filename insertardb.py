
#AHORA VAMOS A INSERTAR UNA FILA ES DECIR UN REGISTRO EN NUESTRA TABLA DE LA DATABASE

import sqlite3

conexion = sqlite3.connect("database1.db")
cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES('Gerardo','Cruz','Briseño',20)")
conexion.commit()
conexion.close()