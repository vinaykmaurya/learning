import pymysql
# DB connection
# db = pymysql.connect(   host="localhost",
#                         user= "root",
#                         password="root",
#                         database = "testDB",
#                         charset='utf8mb4'
#                     )
db = pymysql.connect(   host="fyers-testing-db.cluster-cvghve20lauv.ap-south-1.rds.amazonaws.com",
                        user= "fy_master_test",
                        password="HEIP8NyvaIfBoQqmHX7K",
                        database = "Persons",
                        charset='utf8mb4'
                    )
# # cursur object
cursor = db.cursor()


sql = """SELECT * FROM USER"""

try:
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
except:
    print("Error: Unable to fetch")

db.close()