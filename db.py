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
    
    return json.dumps(data)

