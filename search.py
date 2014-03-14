#!/Users/vishnu/anaconda/bin/python
print 
import cgi
import json
x=cgi.FieldStorage()
global completeList

keywords=['select','update','delete','insert into','from']

completeList = {}
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

