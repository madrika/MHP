import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password = "Madrika")

# Creat Database 
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Arjang")
