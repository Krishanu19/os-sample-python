from flask import Flask, render_template, request
import MySQLdb

application = Flask(__name__, template_folder='templates')

@application.route('/')
def index():
  return render_template('index.html')



@application.route('/data', methods=['GET', 'POST'])
def data():
            if request.method == "POST":
            details = request.form
            fromDisc = details['fromDisc']
            toDisc = details['toDisc']
            conn = MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1',db='sampledb')
            cursor = conn.cursor()
            cursor.execute("select PP.List_Price,PS.Description,PP.Discount,PS.SKUAtt_Value1 "Size Available" from XXIBM_PRODUCT_PRICING PP inner join XXIBM_PRODUCT_SKU PS on PP.Item_Number=PS.Item_number where PP.Discount between %s and %s")
            data = cursor.fetchall()
            print("Total number of rows in Laptop is: ", cursor.rowcount)
            print("\nPrinting record")
            for row in data:
               print("list_price = ", row[0])
               print("Description = ", row[1])
               print("Discount = ", row[0])
               print("SKUAtt_Value1 = ", row[0])
            return render_template('product.html', data=data)

if __name__ == '__main__':
    application.run()