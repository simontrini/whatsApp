import csv
import sqlite3
conexion=sqlite3.connect("dataMad")
#cursor=conexion.execute("select * FROM main.personas")
#conexion.execute("""INSERT INTO "main"."personas" ("nombreCompleto", "cedula", "telefono", "correE", "organizacion") VALUES ('Roger Mérida', '8683800', '0414-2218626', 'rogermerida1209@gmail.com', 'Vanguardia Popular')""")

#for fila in cursor:
    #print(fila)
#conexion.commit()
#conexion.close()
with open('Marchadel16.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
        sqltext = """INSERT INTO "main"."personas" (
            "nombreCompleto", 
            "cedula", 
            "telefono", 
            "correE", 
            "organizacion"
            ) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(row[0],row[1],row[2],row[3],row[4])
        #print("error en {0}".format(sqltext)) 
        try:
            conexion.execute(sqltext) 
            #continue
        except Exception as  e:
            print("error en {0} con {1}".format(row[1],e)) 
            #print("error en {0} con {1}".format(sqltext,e))
conexion.commit()
conexion.close()

#para insertar por actividades
#INSERT INTO "main"."asistencia" (
            #"persona_id","actividad_id") SELECT personas.id,actividad.id FROM "main"."personas","main"."actividad" where personas.id > 102 and actividad.id = 4
