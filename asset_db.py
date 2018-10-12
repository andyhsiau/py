# coding:utf-8
import pyodbc
import json



def get_CI_from_DB(hostname):

    cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=TWTPESQLDB1; DATABASE=FAS; UID=FAS; PWD=DeltAFAS')
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM PCNameIPMacView WHERE WORKSTATIONNAME LIKE N\'"+hostname+"%\'")
    rows = cursor.fetchall()
    for row in rows:

        data = { 'WORKSTATIONNAME' :row[0], 'LOGGEDUSER' : row[1], 'MODEL' : row[2], 'SERVICETAG' : 
                row[3], 'OSNAME' :row[4], 'VERSION' :row[5], 'IPADDRESS' :row[6], 'MACADDRESS' :
                row[7], 'ASSETTAG' :row[8], 'SERIALNO' :row[9], 'LASTAGENTSCANTIME' :row[10] }



        row = cursor.fetchone()
    try:
        return data
    except:
        return {"_result":"No Data"}
    

def get_CI_from_DB_user(username) :

    cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=TWTPESQLDB1; DATABASE=FAS; UID=FAS; PWD=DeltAFAS')
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM PCNameIPMacView WHERE LOGGEDUSER LIKE  N\'"+username+"%\'")
    rows = cursor.fetchall()
    data=[]
    for row in rows:

        data.append({ 'WORKSTATIONNAME' :row[0], 'LOGGEDUSER' : row[1], 'MODEL' : row[2], 'SERVICETAG' : 
                row[3], 'OSNAME' :row[4], 'VERSION' :row[5], 'IPADDRESS' :row[6], 'MACADDRESS' :
                row[7], 'ASSETTAG' :row[8], 'SERIALNO' :row[9], 'LASTAGENTSCANTIME' :row[10] })



        row = cursor.fetchone()

    if data == [] :
        data = {"_result":"No Data"}

    try:
        return data
    except:
        return {"_result":"No Data"}







