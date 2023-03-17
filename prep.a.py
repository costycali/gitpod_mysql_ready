import mysql.connector
mydb= mysql.connector.connect( 

  host="localhost",
  user="root",
  password="",
  database="Animali"
  


)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Mammiferi (id VARCHAR (255), nome_proprio VARCHAR (255), razza VARCHAR (255), peso INT,eta INT)")


