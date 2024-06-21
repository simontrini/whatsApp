import time
import pywhatkit
import sqlite3
import crudSqlite
import smsKannel
from smsAirMore import SmsAirMore
### cvs
import csv


#kannel = smsKannel.SmsKannel()
airMore = SmsAirMore()
personas = []
## cvs
with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for fila in reader:
                print(fila)
                personas.append({"nombre":fila[0],"telefono":"+58{0}".format(fila[1])})
## cvs
## base datos
#bd = crudSqlite.CrudSqlite("dataMad")
#cursor = bd.listar("select nombreCompleto, telefono FROM main.personas JOIN main.asistencia on main.personas.id = main.asistencia.persona_id and main.asistencia.actividad_id = 22")
##print(cursor)
#for fila in cursor:
        #personas.append({"nombre":fila[0],"telefono":"+58 {0}".format(fila[1])})
        ##print(fila)
## base datos
print("iniciando")

#personas = [
            #{"nombre":"cru","telefono":"+58 0412-9027646"},
            ##{"nombre":"Kalioska Garrido","telefono":"+58 4265199557"},
            ##{"nombre":"cruz meryyy","telefono":"+584129027646"}
            #]

#mensajes = """Coordinadora De Trabajadores En Lucha De Los Altos Mirandinos
#Invita a {0}35.
#"""
#mensajes = """hola {0} miembro del equipo Cambio en Paz Guaicaipuro. Probando envió de SMS masivos personalizados.
#Por favor reenvía este mensaje al grupo de WhatsApp Equipo Promotor Guaicaipuro para cotejar como te llego.las limitantes de este medio son que usa el numero personal, la cantidad de SMS que tenga el plan o el saldo de la persona, usa un teléfono android.

#"""
mensajes = """0000 hola {0} miembro del equipo Cambio en Paz Guaicaipuro. Probando envió de SMS masivos personalizados.
.las limitantes de este medio son que usa el numero personal, la cantidad de SMS que tenga el plan o el saldo de la persona, usa un teléfono android.

"""
cuenta = 0
for persona in personas:
        try:
                mensaje = mensajes.format(persona["nombre"])
                #print(mensaje)
                print(persona["telefono"])
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
                time.sleep(5)
        except Exception as  e:
                print('error en {0}, {1}, Error :{2}'.format(persona["nombre"],persona["telefono"],e))
        
        #print(mensaje)    
        #consulta mad con twitter
        #select nombreCompleto, telefono, rrss.usuario
        #FROM main.personas 
        #JOIN main.asistencia on main.personas.id = main.asistencia.persona_id and main.asistencia.actividad_id = 6 
        #LEFT join rrss on personas.id = rrss.persona_id