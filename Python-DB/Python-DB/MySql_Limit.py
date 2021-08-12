import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "Madrika",
database = "Madrika"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 4")
myresult = mycursor.fetchall()


for x in myresult:
    print(x)
