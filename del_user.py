
import pymysql

# DB connection
db = pymysql.connect(   host="localhost",
                        user= "root",
                        password="root",
                        database = "testDB",
                        charset='utf8mb4'
                    )

# cursur object
cursor = db.cursor()

# DELETE record
sql = """ DELETE FROM USER WHERE NAME = 'VKM' """

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()