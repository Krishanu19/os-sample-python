from flask import Flask, render_template, request
import MySQLdb

application = Flask(__name__, template_folder='templates')

@application.route('/')
def index():
  return render_template('welcome.html')

# @application.route('/data', methods=['GET', 'POST'])
# def data():
            # conn = MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1',db='sampledb')
            # cursor = conn.cursor()
            # if request.method == "POST":
             # details = request.form
             # fromdisc = details['fromdisc']
             # todisc = details['todisc']
             # query = "SELECT PP.list_price,PS.description,PP.discount,PS.catalogue_category from XXIBM_PRODUCT_PRICING PP INNER JOIN XXIBM_PRODUCT_SKU PS ON PP.item_number=PS.item_number where  PP.discount BETWEEN %s AND %s"
             # cursor.execute(query, (fromdisc, todisc))
             # data = cursor.fetchall()
             # print("Total number of rows: ", cursor.rowcount)
             # print("\nPrinting record")
             # for row in data:
               # print("list_price = ", row[0])
               # print("description = ", row[1])
               # print("discount = ", row[2])
               # print("catalogue_category = ", row[3])
             # return render_template('product.html', data=data)

@application.route('/apparels', methods=["GET", "POST"])
def apparels():
            conn = MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1',db='sampledb')
            cursor = conn.cursor()
            if request.method == "GET":
              details = request.form
              query = "select distinct class_name from sampledb.XXIBM_PRODUCT_CATALOGUE WHERE FAMILY_NAME='Clothing'"
              cursor.execute(query)
              clsData = cursor.fetchall()
              print("Total number of rows: ", cursor.rowcount)
              print("\nPrinting record")
              for row in clsdata:
                print("Available Class = ", row[0])
              return render_template('apparels.html', apparels=clsData)

if __name__ == '__main__':
    application.run()