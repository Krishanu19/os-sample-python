from flask import Flask,render_template
#import mysql.connector
import MySQLdb

application = Flask(__name__)

@application.route("/")
#@application.route('/', methods=['GET', 'POST'])
def hello():
    return "<h1>Hello World! From fertile Mind!</h1>"
    #return render_template('https://github.com/Krishanu19/os-sample-python.git/Template/index.html')

@application.route("/ab/")
def dbconnect():
    #mydb = mysql.connector.connect(
    #     host="mysql.gamification.svc.cluster.local",
    #     user="xxuser",
    #     passwd="welcome1",
    #     database=sampledb
    #    )
    conn=MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1')
    #return "DB Connected"
    mycursor = conn.cursor()
    sql = "select list_price from XXIBM_PRODUCT_PRICING where item_number=1001"
    mycursor.execute(sql)
    data=conn.fetchall()    

if __name__ == "__main__":
    application.run(debug=TRUE)
