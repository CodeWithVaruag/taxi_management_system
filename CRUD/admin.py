import sys
import mysql.connector


from libs.adminlibs import Admin
def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database=' taximanagement')

    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn


def manage_customer_table():
    sql = "select booking.bid, customer.name , booking.initial_address , booking.final_address ,booking.pickup_date ,booking.pickup_time , booking.booking_status from booking left join customer on booking.cid=customer.cid where booking.booking_status='pending'"
    cuspending = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        cuspending = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return cuspending




def assign_booking(bk):
    sql = "update booking set did=%s where bid=%s "
    values = (bk.getDid(),bk.getBid())
    result1 = False
    try:
        conn = connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result1=True

        # print("Inserted!")
    except:
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        return result1

def Check_admin(z):
    sql="SELECT * FROM admin WHERE email=%s AND password=%s"
    values=(z.getEmail(),z.getPassword())
    record2=None
    try:
        conn= connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        record2 = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("error",sys.exc_info())
    finally:
        del values,sql
        return record2



