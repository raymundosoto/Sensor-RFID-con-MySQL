# Bibliotecas
import mysql.connector

# Conexión a my ql
cnx = mysql.connector.connect(user='raymundo_soto', password='1234', host='127.0.0.1', database='RFID')

# Cursor (creación)
cursor = cnx.cursor()

query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Raymundo Soto','Prueba de inserción',88843565);"

# Ejecuciòn cursor
cursor.execute (query_insert)

# Reallzar operación en la  base de datos
cnx.commit()
print ("Query realizado correctamente")

# Cerrar
print("Cerrando base de datos")
cursor.close()
cnx.close()