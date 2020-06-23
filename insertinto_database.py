
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jedidiah",
  passwd="",
  database="myfirstdatabase"
)


 # create a cursor first to secure connection then one can then insert 
mycursor = mydb.cursor()


sql = "INSERT INTO RegisterAccount (firstname,lastname,username,email,password)VALUES (%s, %s , %s,%s,%s)"

val=('Rodney','Kwao','jedidiah','rodneytetteh@gmail.com','footb001')

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

