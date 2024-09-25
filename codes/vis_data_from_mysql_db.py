# Connecting to mysql database
# online database using mariadb, so import mariadb instead of mysql.connector
# import mysql.connector
import mariadb,os
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()
db_host = os.getenv("DB_HOST")
db_port = int(os.getenv("DB_PORT"))
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

mydb = mariadb.connect(host=db_host,
                               port=db_port,
                               user=db_user,
                               password=db_password,
                               database=db_name)
mycursor = mydb.cursor()

# Fetching Data From mysql to my python program
mycursor.execute("select year, name from nobel_winners")
result = mycursor.fetchall

Names = []
Marks = []

for i in mycursor:
    Names.append(i[0])
    Marks.append(i[1])

print("Name of Students = ", Names)
print("Marks of Students = ", Marks)

# Visualizing Data using Matplotlib
plt.bar(Names, Marks)
# plt.ylim(5, 40)
plt.xlabel("Name of Students")
plt.ylabel("Marks of Students")
plt.title("Student's Information")
plt.show()
