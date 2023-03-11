import sys


from libs.bookinglibs import Booking
import mysql.connector

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database=' taximanagement')

    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn
book=Booking()




def insertBooking(book):
    sql = "INSERT INTO booking VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (book.getBid(),book.getInitial_address(),book.getFinal_address(),book.getPickup_date(),book.getPickup_time(),book.getBooking_status(),book.getCid(),book.getDid())
    result1 = False
    try:
        conn = connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result1=True

        print("Inserted!")
    except:
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        return result1


def deleteBooking(a):
    sql = " delete from booking where bid=%s "
    values = (a,)
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


def updateBooking(book):
    sql = "update booking set initial_address=%s,final_address=%s,pickup_date=%s,pickup_time=%s where bid=%s"
    values = (book.getInitial_address(),book.getFinal_address(),book.getPickup_date(),book.getPickup_time(),book.getBid())
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

def custtable(cid):
    sql = "SELECT bid, initial_address, final_address, pickup_date, pickup_time, booking_status FROM booking WHERE cid=%s "
    values = (cid,)
    cuspending = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        cuspending = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return cuspending

#select booking.bid, customer.name , booking.initial_address , booking.final_address ,booking.pickup_date ,booking.pickup_time , booking.booking_status from booking left join customer on booking.cid=customer.cid where booking.booking_status="pending";