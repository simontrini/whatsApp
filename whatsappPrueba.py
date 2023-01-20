import pywhatkit
import sqlite3
import crudSqlite
personas = []
bd = crudSqlite.CrudSqlite("dataMad")
cursor = bd.listar("select nombreCompleto, telefono FROM main.personas JOIN main.asistencia on main.personas.id = main.asistencia.persona_id and main.asistencia.actividad_id = 4")
#print(cursor)
for fila in cursor:
        personas.append({"nombre":fila[0],"telefono":"+58 {0}".format(fila[1])})
        #print(fila)
#personas = [{"nombre":"simon","telefono":"+58 0412-7239359"},
            ##{"nombre":"mariosaka","telefono":"+58 4269709360"}
            #]
mensajes = """Coordinadora De Trabajadores En Lucha De Los Altos Mirandinos.
Convoca a {0}, a una asamblea en la sede del colegio de profesores a las 2:00 pm.
punto a tratar:
a) Situación nacional y en los Altos Mirandinos. 
b) Organización de Comités de conflicto, derechos y deberes.
c) Próximas actividades.

Dirección:
Calle Medina Angarita, frente al colegio Manuel Díaz Rodríguez, diagonal a la Fundación del Niño, La Estrella Los Teques Edo Miranda

Recibes este mensaje debido a que asististe a la marcha del lunes 16 de enero del 2023 en 
Los Teques .
Si no eres tú ignora este mensaje.
"""

cuenta = 0
for persona in personas:
        try:
                mensaje = mensajes.format(persona["nombre"])
                
                pywhatkit.sendwhatmsg_instantly(persona["telefono"],mensaje,tab_close=True)
                #sendwhats_image()
                #print('enviado {0}, {1},{2}, exitoso'.format(persona["nombre"],persona["telefono"],mensaje))
                cuenta += 1
                print(cuenta,persona["nombre"])
        except Exception as  e:
                print('error en {0}, {1}, Error :{2}'.format(persona["nombre"],persona["telefono"],e))
        
        #print(mensaje)     

        