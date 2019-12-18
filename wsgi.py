from flask import Flask, render_template

application = Flask(__name__, template_folder='templates')

@application.route('/')
def index():
    return render_template('index.html')

@application.route("/db/")
def dbconnect():
    #mydb = mysql.connector.connect(
    #     host="mysql.gamification.svc.cluster.local",
    #     user="xxuser",
    #     passwd="welcome1",
    #     database=sampledb
    #    )
    conn=MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1')    
    mycursor = conn.cursor()
    mycursor.execute("select list_price from XXIBM_PRODUCT_PRICING where item_number=1001")
    rv = mycursor.fetchall()
    return str(rv)
    #return "DB Connected"
    #mycursor.execute(sql)
    #data=conn.fetchall()    
    return render_template('product.html', result=res, content_type='application/json')

if __name__ == '__main__':
    application.run()