from sql_connection import get_sql_connection
from datetime import datetime

def insert_order(connection, order):
    cursor = connection.cursor()
    query = ("insert into orders(customer_name, total, datetime) values (%s, %s, %s)")
    order_data = (order['customer_name'], order['total'], datetime.now())
    
    cursor.execute(query, order_data)
    order_id = cursor.lastrowid
    
    query2 = ("insert into order_details(order_id, product_id, quantity, total_price) values (%s, %s, %s, %s)")
    data2 = []
    for i in order['order_details']:
        data2.append([
            order_id,
            int(i['product_id']),
            float(i['quantity']),
            float(i['total_price'])
        ])
    
    cursor.executemany(query2, data2)
    connection.commit()
    return order_id

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("select * from orders")
    
    cursor.execute(query)
    
    response = []
    for (order_id, customer_name, total, datetime) in cursor:
        response.append(
            {
                'order_id' : order_id,
                'customer_name' : customer_name,
                'total' : total,
                'datetime' : datetime
            }
        )
    return response
    
if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_orders(connection))
