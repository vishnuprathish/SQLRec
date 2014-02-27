class Table:
    'well, a table. '
    columns={}
    pKey=None
    
    def _init_(self, tableName,pKey=None,columns=None):
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
    list tables
    
    def _init_(self, tables):
        self.tables=tables
        pass
        
    def populate(self,data):
        
        'write the code to statically populate the tabe structure here '
        pass
        
    def getTables(self):
        return self.tables
        pass
        
    def getTableNames(self):
        
        return [x.getTableName() for x in tables]
        pass
    
    
    

    