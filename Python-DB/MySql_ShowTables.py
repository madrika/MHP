import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "Madrika",
database = "Madrika"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
