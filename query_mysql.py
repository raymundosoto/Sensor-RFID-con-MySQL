# import mysql.connector

# print("Conectandose a base de datos")
# cnx= mysql.connector.connect(user ="raymundo_soto", password ="1234", host= "127.0.0.1", database = 'datosclima')
# query = ("SELECT id,nombre,tem FROM clima WHERE id=200;")
# res= cnx.cmd_query(query)

# print("Respuesta")
# print(res)
# cnx.close()



# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="raymundo_soto",
#   password="1234",
#   database="datosclima")

# mycursor = mydb.cursor()
# mycursor.execute("SELECT id,nombre,tem FROM clima WHERE id=200;")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x) 
# mydb.close()




import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="raymundo_soto",
  password="1234",
  database="datosclima")

mycursor = mydb.cursor()
mycursor.execute("SELECT id,nombre,tem FROM clima WHERE nombre='Raymundo, Ecatepec';")
myresult = mycursor.fetchall()
for x in myresult:
  print(x) 
mydb.close()
