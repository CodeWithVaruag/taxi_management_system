import sys
import mysql.connector

from libs.customerlibs import Customer
# from connection import connect

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database=' taximanagement')

    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn
def insertCustomer(ins):
    sql = "INSERT INTO customer VALUES (%s,%s, %s, %s, %s, %s, %s)"
    values = (ins.getCid(),ins.getName(),ins.getEmail(),ins.getContact(),ins.getAddress(),ins.getPassword(),ins.getPayment())
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

def getAll():
    pass


def Check_cus(z):
    sql="SELECT * FROM customer WHERE email=%s AND password=%s"
    values=(z.getEmail(),z.getPassword())
    record1=None
    try:
        conn= connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        record1 = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("error",sys.exc_info())
    finally:
        del values,sql
        return record1









def delete(cid):
    conn =None
    sql = "delete * from copies where cid=%s"
    cid=cid.getCID()
    try:
       conn=connect()
       cursor=conn.cursor()
       cursor.execute(sql,cid)
       conn.commit()
       cursor.close()
       conn.close()
    except:
        pass
    finally:
        pass