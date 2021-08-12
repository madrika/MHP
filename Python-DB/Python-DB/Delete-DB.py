import mysql.connector
mydb = mysql.connector.connect(host="localhost",
user="root",
password = "Madrika",
database = "Madrika"
)

mycursor = mydb.cursor()
sql = " DROP DATABASE arjang "
mycursor.execute(sql)
