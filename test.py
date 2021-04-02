import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="seal",
    database="seal"
    )

my_cursor = db.cursor()

#my_cursor.execute("CREATE TABLE Teams (name VARCHAR(50), year_founded int UNSIGNED, teamID int PRIMARY KEY AUTO_INCREMENT)")

my_cursor.execute("DESCRIBE Teams")

for x in my_cursor:
    print(x)

