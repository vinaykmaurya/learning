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

# Update record
sql = """ UPDATE USER SET AGE = 25 WHERE NAME = 'VKM' """

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
