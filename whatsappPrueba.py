import time
import pywhatkit
import sqlite3
import crudSqlite
import smsKannel
from smsAirMore import SmsAirMore
#kannel = smsKannel.SmsKannel()
airMore = SmsAirMore()
personas = []
bd = crudSqlite.CrudSqlite("dataMad")
cursor = bd.listar("select nombreCompleto, telefono FROM main.personas JOIN main.asistencia on main.personas.id = main.asistencia.persona_id and main.asistencia.actividad_id = 22")
#print(cursor)
for fila in cursor:
        personas.append({"nombre":fila[0],"telefono":"+58 {0}".format(fila[1])})
        #print(fila)
#personas = [
            #{"nombre":"simon","telefono":"+58 0412-7239359"},
            ##{"nombre":"Kalioska Garrido","telefono":"+58 4265199557"},
            ##{"nombre":"cruz meryyy","telefono":"+584129027646"}
            #]
#mensajes = """Coordinadora De Trabajadores En Lucha De Los Altos Mirandinos
#Invita a {0}35.
#"""
mensajes = """{0} El profesor Simón Bolívar te invita a formar parte del grupo whatsapp 
De los Talleres de Formación Técnica. 
Unete https://chat.whatsapp.com/EDrC0asb86tLcfLw6KAFWp .

"""
cuenta = 0
for persona in personas:
        try:
                mensaje = mensajes.format(persona["nombre"])
                #print(mensaje)
                #*** WhatsApp
                #pywhatkit.sendwhatmsg_instantly(persona["telefono"],mensaje,tab_close=True)
                #sendwhats_image()
                #print('enviado {0}, {1},{2}, exitoso'.format(persona["nombre"],persona["telefono"],mensaje))
                #****
                #*** sms con kannel
                #kannel.enviar(persona["telefono"],mensaje)
                #****
                #*** sms con airmore
                airMore.enviar(persona["telefono"],mensaje)
                #****                
                
                cuenta += 1
                print(cuenta,persona["nombre"])
                time.sleep(1)
        except Exception as  e:
                print('error en {0}, {1}, Error :{2}'.format(persona["nombre"],persona["telefono"],e))
        
        #print(mensaje)    
        #consulta mad con twitter
        #select nombreCompleto, telefono, rrss.usuario
        #FROM main.personas 
        #JOIN main.asistencia on main.personas.id = main.asistencia.persona_id and main.asistencia.actividad_id = 6 
        #LEFT join rrss on personas.id = rrss.persona_id
        