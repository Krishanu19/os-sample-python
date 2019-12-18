from flask import Flask, render_template
import MySQLdb

application = Flask(__name__, template_folder='templates')

@application.route('/')
#def index():
#    return render_template('index.html')

#@application.route("/db/")


def index():
            conn = MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1',db='sampledb')
            cursor = conn.cursor()
            cursor.execute("select list_price, item_number from XXIBM_PRODUCT_PRICING LIMIT 10")
            data = cursor.fetchall()
            return render_template('product.html', data=data)

if __name__ == '__main__':
    application.run()