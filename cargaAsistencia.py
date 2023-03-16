import csv
from crudSqlite import CrudSqlite
from modelo import Modelo

class CargarAsistencia():
    def __init__(self, bd, actividad, archivo):
        self.bd = bd
        self.actividad = actividad
        self.archivo = archivo
        self.act = Modelo(self.bd, 'actividad', 'nombreActividad')
        self.asi = Modelo(self.bd, 'asistencia', 'persona_id')
        self.per = Modelo(self.bd, 'personas', 'nombreCompleto')        
        self.agregarActividad()
        self.cargaData()
        
    def agregarActividad(self):        
        id = self.act.crear(self.actividad,self.actividad[0])
        print(id)
        return(id)  
    
    def cargaData(self):  
        with open(self.archivo, newline='') as File:  
            reader = csv.reader(File)
            #viejos = 0
            #nuevos = 0
            error = 0
            asistencia = 0
            procesados = 0
            for row in reader:
                #if True:
                try:
                    #print(asistencia,'nueva persona',tuple(row))
                    procesados += 1
                    id_persona = self.nuevaPersona(tuple(row))
                    self.asistencia(id_persona)
                    asistencia += 1
                except Exception as eror:
                    error += 1
                    print(type(eror))    
                    print(eror.args)     
                    print(eror) 
            print('procesados',procesados)
            print('asistencia',asistencia)
            print('errores',error)
            
                
    
    def nuevaPersona(self, data):
        #print(self.ventana.children)
        id = self.per.crear(data,data[0])
        return(id)   
    
    def asistencia(self, id_persona):
        id_actividad = self.act.buscar(self.act.clave, self.actividad[0])[0][0]
        #print(id_persona,id_actividad,'asistente','',0)
        self.asi.crear((id_persona,id_actividad,'asistente','',0),'') 
        return()
    
if __name__=='__main__':
    bd = CrudSqlite("dataMad")
    #act = ['nombreActividad','fecha','lugar','descripcion']
    actividad = ('Taller de Formación Técnica 1','2023-03-01 14:00:00','Oficina','1er Taller de formación técnica con adolescentes de la comunidad el mána ')
    archivo = 'tallerFormacionTecnica1.csv'
    cA = CargarAsistencia(bd, actividad, archivo)
    #act = Modelo(bd, 'actividad', 'nombreActividad')
    print('cargando actividad')
#import csv
#import sqlite3
#conexion=sqlite3.connect("dataMad")
##cursor=conexion.execute("select * FROM main.personas")
##conexion.execute("""INSERT INTO "main"."personas" ("nombreCompleto", "cedula", "telefono", "correE", "organizacion") VALUES ('Roger Mérida', '8683800', '0414-2218626', 'rogermerida1209@gmail.com', 'Vanguardia Popular')""")

##for fila in cursor:
    ##print(fila)
##conexion.commit()
##conexion.close()
#with open('asamblea19Enero2023.csv', newline='') as File:  
    #reader = csv.reader(File)
    #viejos = 0
    #nuevos = 0
    #error = 0
    #for row in reader:
        #print(row)
        #if row[1]:
            #sqltext1 = """SELECT COUNT(*),* FROM "main"."personas" WHERE personas.cedula = {0}""".format(row[1])
            #sqltext2 = """SELECT COUNT(*),* FROM "main"."personas" WHERE personas.telefono = {0}""".format(row[2])
            #sqltext = """INSERT INTO "main"."personas" (
                #"nombreCompleto", 
                #"cedula", 
                #"telefono", 
                #"correE", 
                #"organizacion"
                #) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(row[0],row[1],row[2],row[3],row[4])
            ##print("error en {0}".format(sqltext)) 
            #try:
                #cursor = conexion.execute(sqltext1)
                ##print('mmm',cursor.fetchall()[0][3])
                ##exit
                #if cursor.fetchall()[0][3]:
                    ##print('si')
                    #viejos += 1
                    #cursor_ = []
                    #for fila in cursor:
                        #cursor_.append(fila)            
                        #print(cursor_[0][2:])
                #else:
                    #cursor = conexion.execute(sqltext1)
                    ##print('cc', cursor.fetchall())
                    #if cursor.fetchall()[0][3]:
                        #print('si tiene telefono')
                    #nuevos += 1
                    #print('pp',row)
                    #conexion.execute(sqltext) 
                ##continue
            
            #except Exception as  e:
                #error += 1
                #print("error en {0} con {1}".format(row[1],e)) 
                ##print("error en {0} con {1}".format(sqltext,e))
    #print("En base de datos = {0} -- Nuevos = {1} -- Errores = {2}".format(viejos,nuevos,error))
#conexion.commit()
#conexion.close()

##para insertar por actividades
##INSERT INTO "main"."asistencia" (
            ##"persona_id","actividad_id") SELECT personas.id,actividad.id FROM "main"."personas","main"."actividad" where personas.id > 102 and actividad.id = 4

##INSERT INTO "main"."asistencia" (
            ##"persona_id","actividad_id") SELECT personas.id,actividad.id FROM "main"."personas","main"."actividad" where personas.id > 102 and actividad.id = 4

##toquen github
##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