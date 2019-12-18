from flask import Flask, render_template
#import mysql.connector
import MySQLdb

application = Flask(__name__)

class Database:
        def __init__(self):
            host = "mysql.gamification.svc.cluster.local"
            user = "xxuser"
            password = "welcome1"
            db = "XXIBM_PRODUCT_PRICING"
            self.con = MySQLdb.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.con.cursor()
        def list_price(self):
            self.cur.execute("select list_price from XXIBM_PRODUCT_PRICING LIMIT 50")
            result = self.cur.fetchall()
            return result
@application.route('/')
def product():
        def db_query():
            db = Database()
            listprice = db.list_price()
            return listprice
        res = db_query()
        return render_template('product.html', result=res, content_type='application/json')
