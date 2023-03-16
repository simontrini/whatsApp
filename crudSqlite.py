import sqlite3        
class CrudSqlite():
    
    def __init__(self, bd):
        self.bd = bd
        #self.conexion=sqlite3.connect(self.bd)
        
    def connect(self):
        self.conexion=sqlite3.connect(self.bd)
        return
    
    def executar(self, sql):
        self.conexion=sqlite3.connect(self.bd)
        #print(sql)
        cursor = self.conexion.execute(sql)
        cursor_ = []
        for fila in cursor:
            cursor_.append(fila)
            #print(fila)
        self.close()
        return cursor_        
        #return    
    
    def listar(self, sql):
        self.connect()
        cursor = self.conexion.execute(sql)
        cursor_ = []
        for fila in cursor:
            cursor_.append(fila)
            #print(fila)
        self.close()
        return cursor_
    
    def agregar(self, sql):
        #try:
        self.connect()
        #sql = """INSERT INTO "main"."personas" 
        #("nombreCompleto", "cedula", "telefono", "correE", "organizacion") 
        #VALUES ('yorobot', '1932222', '0412-2xxx', 'yorobot@gmail.com', 'Colegio de Profesores. Edo Miranda'); """
        cursor = self.conexion.execute(sql)
        #print(cursor.lastrowid) #lastrowid rowcount
        self.conexion.commit() 
        self.conexion.close()     
        #except Exception as eror:
            #print(type(eror))    
            #print(eror.args)     
            #print(eror)
            
        
    def close(self):
        self.conexion.close()
        return
    
#bd = CrudSqlite("dataMad")
#bd.agregar("hol")