import mysqlcon as m

def partialMatch(plist,ptext):
    result=[]
    if ptext==None:
        return plist
    for element in plist:
        if element.find(ptext)!=-1:
            result.append(element)
    return result

class Table:
    'well, a table. '
    columns={}
    pKey=None
    
    def __init__(self, tableName,columns=None,pKey=None):
        self.tableName=tableName
        self.pKey=pKey
        self.columns=columns
        pass
    
    def setPkey(self,pKey):
        self.pKey=pKey
        pass
    
    def getPkey(self):
        return self.pKey
        pass
        
    def setColumns(self,columns):
        self.columns=columns
        
    def getTableName(self):
        return self.tableName
        
    def getColumns(self):
        return self.columns
        
    def getColumnNames(self):
        return [x for x in self.columns.keys()]
        
    
class DBSchema:
    'The inmemory index that stores a db schema'    
    tables=[]
    
    def __init__(self, tables=None):
        self.tables=tables
        pass
        
    def populate(self,data):
        
        'write the code to statically populate the tabe structure here '
        pass
        
    def getTables(self):
        return self.tables
        pass
        
    def addTable(self,table):
	if self.tables==None:
		self.tables=[]
        self.tables.append(table)
        pass
        
    def getTableOf(self,tableNames):
	listOfTables = []
        for x in self.tables:
	    for tableName in tableNames:
	        if tableName == x.getTableName():
		   listOfTables.append(x)
	return listOfTables 

    def getTableNames(self):
        
        return [x.getTableName() for x in self.tables]
        pass
        
    def getAllColumns(self):
        
        allCol = []
        
        for x in self.tables:
            allCol=allCol+x.getColumnNames()  
        return allCol
    
    def recPredicate(self,tables,partialText):   
        result=[]
        resultUnsorted=[]
        EquiCol={}
        NotEquiCol={}
        
	    #plen=len(partialText)
    	dict1 = {}
        
        table1=tables[0]   #join for two tables only
        table2=tables[1]
        
        i=0
        j=0
        
        for t1Col in table1.getColumns():
            for t2Col in table2.getColumns():
                if table1.getColumns()[t1Col]==table2.getColumns()[t2Col]:   #Form the Cartesion Product with same datatypes
                    if t2Col==t1Col:     #Rank the equal ones higher
                        EquiCol[j]=(t1Col,t2Col)
                        j+=1
                    else:
                        NotEquiCol[i]=(t1Col,t2Col)
                        i+=1
                    
                    
                    #for key in enumerate(i):   #Concatenate Equicol and NonEquiCol to form the final cartesion product
                    #    EquiCol[j+key]=NotEquiCol[key]
                    
                    cartProd=dict(EquiCol.items()+NotEquiCol.items())
        #print EquiCol
                
    	'''for x in tables:
    	    for y in x.getColumnNames():
                if(dict1.get(y) is not None):
                    dict1[y].append(x.getTableName())
                else:
                    dict1[y]=list(x.getTableName())'''
        #print EquiCol        
        for key in cartProd:
                resultUnsorted.append(table1.getTableName()+"."+cartProd[key][0]+"="+table2.getTableName()+"."+cartProd[key][1])
                
        #print resultUnsorted
                
        result=partialMatch(resultUnsorted,partialText)
            
    	return result
    
    def getGlobalColRec(self,partialText):
        
        allCol = []       
        convCol=[]
        
        for x in self.tables:
            allCol=allCol+x.getColumnNames()
            
        for thing in allCol:
            plen=len(partialText)
            if(partialText==thing[0:plen]):
                convCol.append(thing)             
        return convCol
    
    def getTablesWithColumn(self,columnName):

	allCol = []
	tablesWithColumnName = []

	for x in self.tables:
	    #allCol=allCol+x.getColumnNames()
	    for y in x.getColumnNames():
		if y == columnName:
		   tablesWithColumnName.append(x)
	return tablesWithColumnName

    def getColumnsOfTables(self,tablesWithSpecificColumnName):
	
    	col = []
	for x in tablesWithSpecificColumnName:
	    col.append(x.getColumnNames())
	return col
	
    def getTablesWithColumns(self,columnsInQuery):
	
	dict = {}
	listOfTables = []
	for y in columnsInQuery:
	    for x in self.tables:
		for z in x.getColumnNames():
		    if y == z:
		       listOfTables.append(x)
	    dict[y] = listOfTables
	    listOfTables = []
	return dict
       
tbs=m.getTableDef()
mySchema=DBSchema()

for key in tbs:
    'value is a list of dictionaries. Each element is of the format (key,value)=(columnname,datatype)'
    pkey=tbs[key]["magicNum999"]
    del tbs[key]["magicNum999"]
    tbl=Table(key,tbs[key],pkey)
    mySchema.addTable(tbl)
    

#for x in mySchema.getTables():
    #print(x.getPkey())

#print mySchema.recPredicate([mySchema.getTables()[0],mySchema.getTables()[1]],"s")
