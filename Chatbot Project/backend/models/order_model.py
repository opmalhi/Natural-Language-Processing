from utils.db_helper import db
from mysql.connector import Error

class Order:
    def get_status(order_id: int):
        try:
            #creating a connection to te database
            conn = db.get_connection()

            #creating a cursor object
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT status FROM order_tracking WHERE order_id = %s", (order_id,))

            #fetching the result
            result = cursor.fetchone()

            return result['status'] if result else None
        finally:
            #closing the cursor and connection
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_next_order_id():
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT max(order_id) FROM orders")
            result = cursor.fetchone()[0]
            return 1 if result is None else result + 1
        finally:
            #closing the cursor and connection
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_total_order_price(order_id):
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT get_total_order_price(%s)", (order_id,))
            result = cursor.fetchone()[0]
            return result
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def insert_order_item(food_item, quantity, order_id):
        try:
            conn = db.get_connection()
            cursor = conn.cursor()

            # Call stored procedure
            cursor.callproc('insert_order_item', (food_item, quantity, order_id))
            
            # Commit transaction
            conn.commit()
            print("Order item inserted successfully!")
            
            return 1

        except Error as err:
            print(f"Error inserting order item: {err}")

            # Rollback changes
            if conn:
                conn.rollback()
            return -1

        except Exception as e:
            print(f"An error occurred: {e}")

            # Rollback changes
            if conn:
                conn.rollback()
            return -1
        
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def insert_order_tracking(order_id, status):
        try:
            conn = db.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)", (order_id, status))
            conn.commit()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()