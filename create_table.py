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

# creat table query
sql = """CREATE TABLE USER(
    NAME CHAR(20) NOT NULL,
    AGE INT,
    GENDER CHAR(1) )"""


cursor.execute(sql)

db.close()



