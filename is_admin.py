import pymysql

import pymysql
"""
Fetch data from admin table
print all admin email and name
"""
# DB connection
db = pymysql.connect(   host="fyers-trading-db-cluster.cluster-ro-cvghve20lauv.ap-south-1.rds.amazonaws.com",
                        user= "fy_dbmaster_1329",
                        password="fyersDbAdmin1329",
                        database = "fyers_api",
                        charset='utf8mb4'
                    )

cursor = db.cursor()

# sql query for fetch decrpyted data
getAllUserSql = """SELECT AES_DECRYPT(EmailId,'fyAuth91537'),AES_DECRYPT(Name,'fyAuth91537') FROM `admin` WHERE Active = 1;"""

# execute
cursor.execute(getAllUserSql)

# fetch all
sqlFetchAll = cursor.fetchall()

# printing data
print(sqlFetchAll)

# dbCLose
db.close()