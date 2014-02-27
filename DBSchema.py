class Table:
    'well, a table. '
    column={}
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
        
    
class DBSchema:
    'The inmemory index that stores a db schema'
    
    list tables
    
    def _init_(self):
        pass
        
    def populate(self):
        pass
        
    def getTables(self):
        pass
        
    def getTableNames(self):
        pass
    
    
    

    