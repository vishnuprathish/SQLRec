
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

    for x in tables:
        cur.execute("DESCRIBE " + x )
        for row in cur:
            val[row[0]]=row[1]
        allTables[x]=val

    cur.close()
    conn.close()

    return allTables


print(str(getTableDef()))
