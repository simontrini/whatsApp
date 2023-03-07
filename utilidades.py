import csv
import sqlite3
conexion=sqlite3.connect("dataMad")
#cursor=conexion.execute("select * FROM main.personas")
#conexion.execute("""INSERT INTO "main"."personas" ("nombreCompleto", "cedula", "telefono", "correE", "organizacion") VALUES ('Roger Mérida', '8683800', '0414-2218626', 'rogermerida1209@gmail.com', 'Vanguardia Popular')""")

#for fila in cursor:
    #print(fila)
#conexion.commit()
#conexion.close()
with open('asamblea19Enero2023.csv', newline='') as File:  
    reader = csv.reader(File)
    viejos = 0
    nuevos = 0
    error = 0
    for row in reader:
        print(row)
        if row[1]:
            sqltext1 = """SELECT COUNT(*),* FROM "main"."personas" WHERE personas.cedula = {0}""".format(row[1])
            sqltext2 = """SELECT COUNT(*),* FROM "main"."personas" WHERE personas.telefono = {0}""".format(row[2])
            sqltext = """INSERT INTO "main"."personas" (
                "nombreCompleto", 
                "cedula", 
                "telefono", 
                "correE", 
                "organizacion"
                ) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(row[0],row[1],row[2],row[3],row[4])
            #print("error en {0}".format(sqltext)) 
            try:
                cursor = conexion.execute(sqltext1)
                #print('mmm',cursor.fetchall()[0][3])
                #exit
                if cursor.fetchall()[0][3]:
                    #print('si')
                    viejos += 1
                    cursor_ = []
                    for fila in cursor:
                        cursor_.append(fila)            
                        print(cursor_[0][2:])
                else:
                    cursor = conexion.execute(sqltext1)
                    #print('cc', cursor.fetchall())
                    if cursor.fetchall()[0][3]:
                        print('si tiene telefono')
                    nuevos += 1
                    print('pp',row)
                    conexion.execute(sqltext) 
                #continue
            
            except Exception as  e:
                error += 1
                print("error en {0} con {1}".format(row[1],e)) 
                #print("error en {0} con {1}".format(sqltext,e))
    print("En base de datos = {0} -- Nuevos = {1} -- Errores = {2}".format(viejos,nuevos,error))
conexion.commit()
conexion.close()

#para insertar por actividades
#INSERT INTO "main"."asistencia" (
            #"persona_id","actividad_id") SELECT personas.id,actividad.id FROM "main"."personas","main"."actividad" where personas.id > 102 and actividad.id = 4

#INSERT INTO "main"."asistencia" (
            #"persona_id","actividad_id") SELECT personas.id,actividad.id FROM "main"."personas","main"."actividad" where personas.id > 102 and actividad.id = 4

#toquen github
#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