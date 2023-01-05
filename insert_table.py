import pymysql

# Connection

def MySQLconnection():
    db = pymysql.connect(   host="fyers-testing-db.cluster-cvghve20lauv.ap-south-1.rds.amazonaws.com",
                            user= "fy_master_test",
                            password="HEIP8NyvaIfBoQqmHX7K",
                            database = "fyers_trading_bridge.Persons",
                            charset='utf8mb4'
                        )

    return db
    

db = MySQLconnection()
cursor = db.cursor()
# Insert record
sql = """INSERT INTO USER(
    NAME , AGE , GENDER) VALUES ('hello',53,'M')"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()




