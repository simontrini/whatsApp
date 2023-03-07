import csv
import sqlite3
conexion=sqlite3.connect("dataMad")
with open('asamblea19Enero2023.csv', newline='') as File:  
    reader = csv.reader(File)
    viejos = 0
    nuevos = 0
    error = 0
    for row in reader:
        print(row)
        if row[1]:
            sqltext = """INSERT INTO "main"."asistencia" (
            "persona_id","actividad_id") SELECT personas.id,actividad.id FROM "main"."personas","main"."actividad" where personas.cedula = {0} and actividad.id = 5
""".format(row[1])
            try:
                cursor = conexion.execute(sqltext)
                print('mmm',cursor.fetchall()[0][3])
                nuevos += 1            
            except Exception as  e:
                error += 1
                print("error en {0} con {1}".format(row[1],e)) 
    print("En base de datos = {0} -- Nuevos = {1} -- Errores = {2}".format(viejos,nuevos,error))
conexion.commit()
conexion.close()

