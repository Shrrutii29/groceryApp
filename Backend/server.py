from flask import Flask, request, jsonify
import products_dao
import unit_dao
import order_dao
import json
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods = ['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUnit', methods = ['GET'])
def get_unit():
    units = unit_dao.get_unit(connection)
    response = jsonify(units)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods = ['GET'])
def get_all_orders():
    orders = order_dao.get_all_orders(connection)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
@app.route('/insertProduct', methods = ['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    
    response = jsonify({
        'product_id' : product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods = ['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = order_dao.insert_order(connection, request_payload)
    
    response = jsonify({
        'order_id' : order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
if __name__ == "__main__":
    print("Starting python flask server for Grocery store Management System")
    
    app.run(port = 5000)