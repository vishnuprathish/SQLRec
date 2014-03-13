import mysqlcon as m



class Table:
    'well, a table. '
    columns={}
    pKey=None
    
    def _init_(self, tableName,columns=None,pKey=None):
        self.tableName=tableName
        self.pKey=pKey
        self.columns=columns
        pass
    
    def setPkey(self,pKey):
        self.pKey=pKey
        pass
        
    def setColumns(self,columns):
        self.columns=columns
        
    def getTableName(self):
        return self.tableName
        
    def getColumnNames(self):
        return [x for x in columns.keys()]
        
    
class DBSchema:
    'The inmemory index that stores a db schema'    
    tables=[]
    
    def _init_(self, tables):
        self.tables=tables
        pass
        
    def populate(self,data):
        
        'write the code to statically populate the tabe structure here '
        pass
        
    def getTables(self):
        return self.tables
        pass
        
    def addTable(self,table):
        tables.append(table)
        pass
        
    def getTableNames(self):
        
        return [x.getTableName() for x in tables]
        pass
    
    

tbs=m.getTableDef()
mySchema=DBSchema()


for (key,value) in tbs:
    'value is a list of dictionaries. Each element is of he format (key,value)=(columnname,datatype)'
    tbl=Table(key,value)
    mySchema.addT
    

print tbs


    