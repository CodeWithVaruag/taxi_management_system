import mysql.connector
import sys

from libs.driverlibs import Diver
from libs.bookinglibs import Booking


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database=' taximanagement')

    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn
def insertDriver(dri):
    sql = "INSERT INTO driver VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"
    values = (dri.getDid(), dri.getName(), dri.getEmail(), dri.getContact(), dri.getAddress(),dri.getLisence_no(),dri.getCar_no(), dri.getPassword(),dri.getDriver_status())
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

def custtable(cid):
    sql = " select booking.bid,customer.name,booking.initial_address,booking.final_address,booking.pickup_date,booking.pickuptime,booking.booking_status,driver.drivername where booking.booking_status='pending'"
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


def available_driver():
    sql = "SELECT did,name from driver where driver_status='active'"
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

def driver_table(driver):
    sql = "select booking.bid ,booking.cid ,customer.name,booking.initial_address,booking.final_address,booking.pickup_time,booking.pickup_date,booking.booking_status from booking left join customer on booking.cid=customer.cid where booking.did=%s "
    values = (driver,)
    cuspending1 = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        cuspending1 = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return cuspending1


def Check_driver(z):
    sql="SELECT * FROM driver WHERE email=%s AND password=%s"
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


def changedriverstatus(book):
    sql = "update booking set booking_status='booked' where bid=%s"
    values = (book,)
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


def changedriverstatus1(did):
    sql = "update driver set driver_status='inactive' where did=%s"
    result1 = False
    values=(did,)
    try:
        conn = connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        result1=True

        print("Inserted!")
    except:
        print("Error", sys.exc_info())
    finally:
        del sql
        return result1
