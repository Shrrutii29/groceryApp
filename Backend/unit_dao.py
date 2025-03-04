def get_unit(connection):
    cursor = connection.cursor()
    query = ("select * from unit")
    
    cursor.execute(query)
    
    response = []
    for (unit_id, uname) in cursor:
        response.append(
            {
                'unit_id' : unit_id,
                'uname' : uname,
            }
        )
    return response

if __name__ == '__main__':
    from sql_connection import get_sql_connection
    
    connection = get_sql_connection()
    print(get_unit(connection))
    