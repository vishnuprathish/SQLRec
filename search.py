#!/Users/vishnu/anaconda/bin/python
print 
import cgi
import json
from DBSchema import mySchema as databaseSchema
x=cgi.FieldStorage()
global completeList
completeList = {}

keywords=['select','update','delete','insert into','from']

if (x.getvalue('term'))[0:6] == "select":
	possibleColumns = databaseSchema.getGlobalColRec((x.getvalue('term'))[7:len(x.getvalue('term'))])
	for column in possibleColumns:
		keywords.append('select '+column)

if ((x.getvalue('term'))[0:6] == "select" and (x.getvalue('term'))[-1:] == ","):
	temp = (((x.getvalue('term')).split(' '))[1])[:-1]
	possibleColumns = databaseSchema.getColumnsOfTables((databaseSchema.getTablesWithColumn(temp)))
	for column in possibleColumns:
		for i in column:
			keywords.append(x.getvalue('term')+i)
def populateList(keyWord):
    	completeList[keyWord] = {"id":keyWord,"label":keyWord,"value":keyWord}
for keyword in keywords:
    	populateList(keyword)

listWithContextTerm = []
partialLength = len(x.getvalue('term'))
for item in completeList:
	if item[0:partialLength] == x.getvalue('term'):
		listWithContextTerm.append(completeList[item])
print json.dumps(listWithContextTerm)
