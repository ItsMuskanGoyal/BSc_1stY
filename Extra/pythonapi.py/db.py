import mysql.connector 


db = mysql.connector.connect(
    host = "brfytvylwdzhculozfq5-mysql.services.clever-cloud.com",
    user = "uh06snweshud7gzj",
    password = "24c1orUcFmlEOgctcpFH",
    database = "brfytvylwdzhculozfq5",
    port = "3306"
)
print (db)


mycursor= db.cursor()

mycursor.execute("Show table")



# result = mycursor.fetchall()

# for i in result









