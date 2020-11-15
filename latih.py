import mysql.connector
con = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="Ari001PY"

)

cursor = con.cursor()
word = input("masukin data kategori :")
query = cursor.execute("select * from dictionary where kategori= '%s' " % word)
result = cursor.fetchall()
# print(result)
if not []:
    for hasil in result:
        print(hasil[0])
    else:
        print("hasil kosongdd")
