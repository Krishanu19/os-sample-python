from flask import Flask, render_template

application = Flask(__name__, template_folder='templates')

#@application.route('/')
#def index():
#    return render_template('index.html')

#@application.route("/db/")

class Database:
    def __init__(self):
            host = "mysql.gamification.svc.cluster.loca"
            user = "xxuser"
            password = "welcome1"
            db = "XXIBM_PRODUCT_PRICING"
            self.con = MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1')
            self.cur = self.con.cursor()
        def list_product(self):
            self.cur.execute("select list_price from XXIBM_PRODUCT_PRICING where item_number=1001")
            result = self.cur.fetchall()
            return result
@app.route('/')
    def product():
        def db_query():
            db = Database()
            prod = db.list_product()
            return prod
        res = db_query()
        return render_template('product.html', result=res, content_type='application/json')

if __name__ == '__main__':
    application.run()