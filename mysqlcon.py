
from __future__ import print_function

import pymysql

val={}
allTables={}
def getTableDef():

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='northwind')

    cur = conn.cursor()
    cur.execute("SHOW TABLES")
    #print(cur.description)

    #print()
    tables=[]
    for row in cur:
        tables.append(row[0])

    val=dict()
    for x in tables:
        cur.execute("DESCRIBE " + x )
        for row in cur:
            val[row[0]]=row[1]
        allTables[x]=val
        val=dict()
        
    for x in tables:
        cur.execute("SHOW KEYS FROM "+str(x)+" WHERE Key_name = \'PRIMARY\'")
        for row in cur:
            for key in allTables:
                if row[0]==key:
                    allTables[row[0]]["magicNum999"]=row[4]

    cur.close()
    conn.close()

    return allTables


#getTableDef()
#print(str(getTableDef()))
