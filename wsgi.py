from flask import Flask,render_template
from flask_mysqldb import MySQL
#import mysql.connector
import MySQLdb

application = Flask(__name__)

@application.route("/")
#@application.route('/', methods=['GET', 'POST'])
def hello():
	return "<h1>Hello World! From fertile Mind!</h1>"
    #return render_template('index.html')

@application.route("/db/")
def dbconnect():
    #mydb = mysql.connector.connect(
    #     host="mysql.gamification.svc.cluster.local",
    #     user="xxuser",
    #     passwd="welcome1",
    #     database=sampledb
    #    )
    conn=MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1') 
    sql = "select * from XXIBM_PRODUCT_PRICING where item_number=1001"
	cursor = conn.cursor()
	cursor.execute(sql)
	records = cursor.fetchall()
	print("Total number of rows: ", cursor.rowcount)
	for row in records:
        print("PriceID = ", row[0], )
        print("Item Number = ", row[1])
        print("List Price  = ", row[2])
		print("Discount  = ", row[3])
		print("InStock  = ", row[4])
        print("Price Effective Date  = ", row[5], "\n")
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
		
#return render_template('index.html')
		
if __name__ == "__main__":
    application.run(debug=TRUE)
