#!/Users/vishnu/anaconda/bin/python
print 
import cgi
import json
from DBSchema import mySchema as databaseSchema
x=cgi.FieldStorage()
global completeList
completeList = {}
keywords=['select','update','delete','insert into','from']

if (x.getvalue('term'))[0:6] == "select" and len(x.getvalue('term'))>6:
	possibleColumns = databaseSchema.getGlobalColRec((x.getvalue('term'))[7:len(x.getvalue('term'))])
	for column in possibleColumns:
		keywords.append('select '+column)

context = x.getvalue('term')
partsOfQuery = context.split(" ")

if len(partsOfQuery) == 2:
	columnNames = partsOfQuery[1].split(",")
	if (partsOfQuery[0] == "select" and len(columnNames)>1):
		columnNames.pop()
		if (context[::-1]).index(',') > 0:
	        	possibleColumns = databaseSchema.getGlobalColRec(context[-(context[::-1]).index(','):])
			for column in possibleColumns:
				for i in columnNames:
					if i != column:
						keywords.append(context[0:len(context)-((context[::-1]).index(','))]+column)
		else:
                        possibleColumns = databaseSchema.getGlobalColRec('')
                        for column in possibleColumns:
                                for i in columnNames:
					if i != column:
						keywords.append(context[0:len(context)-((context[::-1]).index(','))]+column)
		
if (partsOfQuery[0] == "select" and len(partsOfQuery) == 3 and context[-1:] != "," and context[-2:-1] != ","):
	keywords.append(partsOfQuery[0]+' '+partsOfQuery[1]+' '+"from")

if len(partsOfQuery) == 4:
	if (partsOfQuery[0] == "select" and partsOfQuery[2] == "from"):
		columnNames = partsOfQuery[1].split(",")
		possibleTables = databaseSchema.getTablesWithColumns(columnNames)
		results = []
		results = databaseSchema.getTableNames()
		for key in possibleTables:
			xyz = []
			for table in possibleTables[key]:
				xyz.append(table.getTableName())
			results = (results and xyz)
		for result in results:
                        keywords.append(partsOfQuery[0]+' '+partsOfQuery[1]+' '+partsOfQuery[2]+' '+result)
		for key in possibleTables:
                       for table in possibleTables[key]:
                               keywords.append(partsOfQuery[0]+' '+partsOfQuery[1]+' '+partsOfQuery[2]+' '+table.getTableName())

if len(partsOfQuery) == 4:
	tableNames = partsOfQuery[3].split(",")
	if (partsOfQuery[0] == "select" and len(tableNames)>1):
		columnNames = partsOfQuery[1].split(",")
                possibleTables = databaseSchema.getTablesWithColumns(columnNames)
                tableNames.pop()
		for key in possibleTables:
                       for table in possibleTables[key]:
				for i in tableNames:
					if (i != table.getTableName()):
                               			keywords.append(context[0:len(context)-((context[::-1]).index(','))]+table.getTableName())

if len(partsOfQuery) == 5 and partsOfQuery[4] != "where" and context[-1:] != "," and context[-2:-1] != ",":
	keywords.append(partsOfQuery[0]+' '+partsOfQuery[1]+' '+partsOfQuery[2]+' '+partsOfQuery[3]+' '+"where")

if len(partsOfQuery) == 6:
	partialText = partsOfQuery[5]
	tablesList = (partsOfQuery[3]).split(",")
	for entry in databaseSchema.recPredicate(databaseSchema.getTableOf(tablesList),partialText):
		keywords.append(partsOfQuery[0]+' '+partsOfQuery[1]+' '+partsOfQuery[2]+' '+partsOfQuery[3]+' '+partsOfQuery[4]+' '+entry)

def populateList(keyWord):
    	completeList[keyWord] = {"id":keyWord,"label":keyWord,"value":keyWord}

for keyword in keywords:
    	populateList(keyword)

listWithContextTerm = []
partialLength = len(x.getvalue('term'))
for item in completeList:
	#print item[0:partialLength] + 'hehehehhe' + x.getvalue('term')
	if item[0:partialLength] == x.getvalue('term'):
		listWithContextTerm.append(completeList[item])
print json.dumps(listWithContextTerm)
