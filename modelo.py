#import sqlite3
from crudSqlite import CrudSqlite
#tabla = 'actividad'
class Modelo():
    def __init__(self, bd, tabla, clave):
        self.bd = bd
        self.tabla = tabla
        self.clave = clave
        self.modelo = self.bd.listar("""SELECT name, type FROM pragma_table_info('{0}')""".format(self.tabla))
        self.get_campos()
        
    def get_campos(self):
        self.campos = []
        for fila in self.modelo:
            if fila[0] == 'id':
                continue
            self.campos.append(fila[0]  )     
        return(self.campos)
    
    def listar(self):
        return(self.bd.listar("""SELECT * FROM '{0}'""".format(self.tabla)))
    
    def buscar(self, campo, dato):
        return(self.bd.listar("""SELECT * FROM {0} WHERE {1} = '{2}'""".format(self.tabla, campo, dato)))
    
    def crear(self, datos, clave):
        cursor = self.buscar(self.clave,clave)
        if cursor:
            return(cursor[0][0])
        sql = """INSERT INTO {0}({1}) VALUES {2}""".format(self.tabla, ','.join(self.campos),datos)
        self.bd.agregar(sql)
        cursor = self.buscar(self.clave,clave)
        return(cursor[0][0])
    
    def eliminar(self, id):
        sql = """DELETE FROM {0} WHERE id IN ({1})""".format(self.tabla, id)
        return(self.bd.agregar(sql)) 
    
    def actualizar(self, id):
        print('sss')    
if __name__=='__main__':
    bd = CrudSqlite("dataMad")
    act = Modelo(bd, 'actividad', 'nombreActividad')
    print('hola',act.buscar('id', 7))