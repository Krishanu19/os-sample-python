from flask import Flask, render_template, request
import MySQLdb

application = Flask(__name__, template_folder='templates')

@application.route('/')
def index():
  return render_template('index.html')



@application.route('/data', methods=['GET', 'POST'])
def data():
            conn = MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1',db='sampledb')
            cursor = conn.cursor()
            if request.method == "POST":
             details = request.form
             fromDisc = details['fromDisc']
             toDisc = details['toDisc']
             query = "select PP.list_price,PS.description,PP.discount,PS.catalogue_category from XXIBM_PRODUCT_PRICING PP inner join XXIBM_PRODUCT_SKU PS on PP.item_number=PS.item_number where PP.discount between %s and %s"
             cursor.execute(query, (fromDisc, toDisc))
             data = cursor.fetchall()
             print("Total number of rows in Laptop is: ", cursor.rowcount)
             print("\nPrinting record")
             for row in data:
               print("list_price = ", row[0])
               print("description = ", row[1])
               print("discount = ", row[2])
               print("catalogue_category = ", row[3])
             return render_template('product.html', data=data)

if __name__ == '__main__':
    application.run()