from flask import Flask, render_template
import pymysql

app = Flask(__name__, template_folder='templates')


class Database:
    def __init__(self):
        host = "mysql.gamification.svc.cluster.local"
        user = "xxuser"
        password = "welcome1"
        db = "sampledb"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_prd(self):
        self.cur.execute("select list_price, item_number from XXIBM_PRODUCT_PRICING LIMIT 10")
        result = self.cur.fetchall()

        return result

@app.route('/')
def prd():

    def db_query():
        db = Database()
        prd = db.list_prd()

        return prd

    res = db_query()

    return render_template('product.html', result=res, content_type='application/json')