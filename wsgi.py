from flask import Flask
import mysql.connector

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! From fertile Mind!"

def dbconnect():
    mydb = mysql.connector.connect(
         host="mysql.gamification.svc.cluster.local",
         user="xxuser",
         passwd="welcome1",
         database=sampledb
        )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255) , mobile int)")
    sql = "INSERT INTO customers (name, address , mobile) VALUES (%s, %s, %d)"
    val = ("John", "Highway 21" , '12345')
    mycursor.execute(sql, val)
    mydb.commit()
    return "record inserted ->" mycursor.rowcount

if __name__ == "__main__":
    application.run()
