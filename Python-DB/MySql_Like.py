import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "Madrika",
database = "Madrika"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE  address LIKE '%way%' "
mycursor.execute(sql)
myresult = mycursor.fetchall()


for x in myresult:
    print(x)
