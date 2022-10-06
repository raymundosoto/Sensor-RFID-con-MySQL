import mysql.connector


print("Conectandose a base de datos")
cnx= mysql.connector.connect(user ="raymundo_soto", password ="1234", host= "127.0.0.1", database = 'codigoIoT')
print("conexion_realizada")
print(cnx)
print("Cerrar conexión")

cnx.close()
print("Conexion_cerrada")