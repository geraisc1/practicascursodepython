#CREAR UNA BASE DE DATOS CON NUEVOS PRODUCTOS

import sqlite3

conexion = sqlite3.connect("database2.db")
cursor = conexion.cursor()
conexion.close