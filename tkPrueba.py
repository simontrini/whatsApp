from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
#import sqlite3
#import crudSqlite
from crudSqlite import CrudSqlite
from modelo import Modelo
titulo = 'MAD'
#self.textactividades = StringVar()
#act = Modelo(bd, 'actividad', 'nombreActividad')
class Asistencia:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title(titulo)
        #meters = StringVar()
        self.note = ttk.Notebook(self.ventana)
        self.note.grid(column=0, row=0, sticky=(N, W, E, S))
        self.ventana.columnconfigure(0, weight=1) 
        self.ventana.rowconfigure(0, weight=1)        
        self.marcoAsistencia = ttk.Frame(self.note )
        #self.marco1 = ttk.Frame(self.note )
        self.note.add(self.marcoAsistencia, text='Asistencia')
        #----- 
        self.lblActividades = ttk.Labelframe(self.marcoAsistencia, text='Actividades')
        self.lblActividades.grid(column=0, row=0, sticky=(W, E))
        self.lblActividades.columnconfigure(0, weight=1) 
        self.lblActividades.rowconfigure(0, weight=1)        
        self.textactividades = StringVar()
        self.actividades = ttk.Combobox(self.lblActividades, textvariable=self.textactividades) 
        self.actividades.grid(column=0, row=2, sticky=(W, E))
        ttk.Button(self.lblActividades, text="Agregar", command=self.masActividad).grid(column=2, row=3, sticky=W)
        ttk.Button(self.lblActividades, text="Eliminar", command=self.eliminarActividad).grid(column=3, row=3, sticky=W)
        #----- 
        self.lblDescripcion = ttk.Labelframe(self.marcoAsistencia, text='Descripción')
        self.lblDescripcion.grid(column=0, row=1, sticky=(W, E))
        #self.lblDescripcion.columnconfigure(0, weight=1) 
        #self.lblDescripcion.rowconfigure(0, weight=1)        
        #-----
        #self.scrolledtext1=st.ScrolledText(self.marcoAsistencia, width=30, height=10)
        #self.scrolledtext1.grid(column=0,row=3, padx=10, pady=10)   
        
        #-----------asistencias
        self.lblAsistentes = ttk.Labelframe(self.marcoAsistencia, text='Asistencia')
        self.lblAsistentes.grid(column=0, row=2, sticky=(W, E))        
        self.treeAsistencias = ttk.Treeview(self.lblAsistentes, height=10, columns=['id','nombre','fecha','lugar'], show= 'headings')
        self.treeAsistencias.grid(row=0, column=0)
        self.treeAsistencias.heading("id",text="Id")
        self.treeAsistencias.heading("nombre",text="Nombre")
        self.treeAsistencias.heading("fecha",text="Fecha")
        self.treeAsistencias.heading("lugar",text="Lugar")
        #ttk.Button(self.lblAsistentes, text="Agregar" ).grid(column=3, row=2, sticky=W)
        #ttk.Button(self.lblAsistentes, text="Eliminar").grid(column=3, row=3, sticky=W)        
        #-----------asistencias
        #----- Informacion personas
        self.lblInformacion = ttk.Labelframe(self.marcoAsistencia, text='Informacion')
        self.lblInformacion.grid(column=0, row=3, sticky=(W, E))
        #ttk.Button(self.lblInformacion, text="Agregar" ).grid(column=3, row=0, sticky=W)
        #ttk.Button(self.lblInformacion, text="Eliminar").grid(column=3, row=1, sticky=W)        
        #self.lblInformacion.columnconfigure(0, weight=1) 
        #self.lblInformacion.rowconfigure(0, weight=1)        
        #----- Informacion personas 
        #----- Informacion personas botones
        self.lblBotones = ttk.Labelframe(self.marcoAsistencia)
        self.lblBotones.grid(column=0, row=4, sticky=(W, E))
        ttk.Button(self.lblBotones, text="Nuevo",command=self.formPersona ).grid(column=0, row=0, sticky=W)
        ttk.Button(self.lblBotones, text="Agregar",command=self.formAsistencia).grid(column=1, row=0, sticky=W)
        ttk.Button(self.lblBotones, text="Eliminar").grid(column=2, row=0, sticky=W)        
        self.lblBotones.columnconfigure(0, weight=1) 
        self.lblBotones.rowconfigure(0, weight=1)        
        #----- Informacion personas           
        
        
        #def item_selected(event):
            #for selected_item in tree.selection():
                #item = tree.item(selected_item)
                #record = item['values']
                ## show a message
                #showinfo(title='Information', message=','.join(record))        
        
        #self.note.add(self.marco1, text='two')
        #s = ttk.Separator(self.marco, orient=HORIZONTAL)
        # ***********modelos *********
        self.bd = CrudSqlite("dataMad")
        self.act = tkmodelo(self.bd, 'actividad', 'nombreActividad') 
        self.listarActividades()
        self.actividades.set('Seleccione Una Actividad1')
        #self.actividades.current(END)
        self.asi = tkmodelo(self.bd, 'asistencia', 'persona_id')
        self.per = tkmodelo(self.bd, 'personas', 'nombreCompleto')
        #self.act.form()
        #self.asi.form()
        #self.per.form()
        
        #----------------------
        
        self.actividades.bind("<<ComboboxSelected>>", self.listarAsistencia)
        self.treeAsistencias.bind('<<TreeviewSelect>>', self.informacionPersonas)
        
    def nuevaPersona(self):
        #print(self.ventana.children)
        id = self.per.crear((self.nombre.get(),self.cedula.get(),self.telefono.get(),self.correo.get(),self.organizacion.get()),self.nombre.get())
        actividad = self.act.buscar(self.act.clave, self.actividades.get())
        #actividad = self.act.buscar(self.act.clave, self.actividades.get())
        print('0',id)
        print('1',actividad)
        print('2',actividad[0][0])
        self.asi.crear((id,actividad[0][0],'asistente',NONE,0),id)
        #_root().destroy()
        self.listarAsistencia()
        return()        
        
    def formAsistencia(self):
        t = Toplevel(self.ventana)
        self.textAsistencia = StringVar()
        self.actividad = ttk.Combobox(
            t,
            state="readonly",
            textvariable=self.textAsistencia) 
        self.actividad.grid(column=0, row=2, sticky=(W, E)) 
        self.actividad['values'] = [self.actividades.get()]
        self.actividad.set(self.actividades.get()) 
        #----------------
        self.textPersona = StringVar()
        self.persona = ttk.Entry(
            t,
            #state="readonly",
            #command=self.buscarPersonas,
            textvariable=self.textPersona) 
        self.persona.grid(column=0, row=3, sticky=(W, E)) 
        self.persona.bind("<Key>", self.buscarPersonas)
        #----------------
        self.treePersona = ttk.Treeview(t, height=10, columns=['id','nombre','telefono','correo','organizacion'], show= 'headings')
        self.treePersona.grid(row=5, column=0)
        self.treePersona.heading("id",text="Id")
        self.treePersona.heading("nombre",text="Nombre")
        self.treePersona.heading("telefono",text="telefono")
        self.treePersona.heading("correo",text="correo")
        self.treePersona.heading("organizacion",text="organizacion")  
        self.treePersona.bind("<Double-Button-1>", self.agregarAsistente)
        #-----------------
        #print(self.actividad.get())
        #print(self.buscarPersonas())
        
    def agregarAsistente(self,eventObject):
        for selected_item in self.treePersona.selection():
            item = self.treePersona.item(selected_item)
            id_persona = item['values'][0]
            id_actividad = self.act.buscar(self.act.clave,self.textAsistencia.get())[0][0]#self.actividades.get()
            ## show a message
            print(id_persona,id_actividad)          
        #print('aistente',self.treePersona.selection_get(item))
        try:
            self.asi.crear((id_persona,id_actividad,'asistente','',0),'') 
        except:
            print('warnin')
        #messagebox.showinfo(message="Mensaje", title="Título")
        self.textPersona.set('')
        self.listarAsistencia2()
        self.listarAsistencia1()
        
        #pass  
        return
    
    
    def buscarPersonas(self,eventObject):
        print('buscamdo')
        self.listarAsistencia1()
        pass
        
    def formPersona(self):
        #self.per.nuevo(self.ventana)
        t = Toplevel(self.ventana)
        #-----------
        self.nombre = StringVar()
        actividad_entry = ttk.Entry(t, width=7, textvariable=self.nombre)
        actividad_entry.grid(column=3, row=1, sticky=(W, E))
        ttk.Label(t, text='Nombre').grid(column=2, row=1, sticky=(W, E)) 
        #-----------
        self.cedula = StringVar()
        fecha_entry = ttk.Entry(t, width=7, textvariable=self.cedula)
        fecha_entry.grid(column=3, row=2, sticky=(W, E))
        ttk.Label(t, text='Cedula').grid(column=2, row=2, sticky=(W, E))
        #-----------
        self.telefono = StringVar()
        lugar_entry = ttk.Entry(t, width=7, textvariable=self.telefono)
        lugar_entry.grid(column=3, row=3, sticky=(W, E))
        ttk.Label(t, text='Telefono').grid(column=2, row=3, sticky=(W, E)) 
        #-----------
        self.correo = StringVar()
        descripcion_entry = ttk.Entry(t, width=7, textvariable=self.correo)
        descripcion_entry.grid(column=3, row=4, sticky=(W, E))
        ttk.Label(t, text='Correo').grid(column=2, row=4, sticky=(W, E))
        #-----------
        self.organizacion = StringVar()
        lugar_entry = ttk.Entry(t, width=7, textvariable=self.organizacion)
        lugar_entry.grid(column=3, row=5, sticky=(W, E))
        ttk.Label(t, text='Organizacion').grid(column=2, row=5, sticky=(W, E)) 
        #-----------        
        ttk.Button(t, text="Agregar", command=self.nuevaPersona).grid(column=3, row=6, sticky=W)
                
            
    
    def masActividad(self):
        t = Toplevel(self.ventana)
        #-----------
        self.actividad = StringVar()
        actividad_entry = ttk.Entry(t, width=7, textvariable=self.actividad)
        actividad_entry.grid(column=3, row=1, sticky=(W, E))
        ttk.Label(t, text='Actividad').grid(column=2, row=1, sticky=(W, E)) 
        #-----------
        self.fecha = StringVar()
        fecha_entry = ttk.Entry(t, width=7, textvariable=self.fecha)
        fecha_entry.grid(column=3, row=2, sticky=(W, E))
        ttk.Label(t, text='Fecha').grid(column=2, row=2, sticky=(W, E))
        #-----------
        self.lugar = StringVar()
        lugar_entry = ttk.Entry(t, width=7, textvariable=self.lugar)
        lugar_entry.grid(column=3, row=3, sticky=(W, E))
        ttk.Label(t, text='Lugar').grid(column=2, row=3, sticky=(W, E)) 
        #-----------
        self.descripcion = StringVar()
        descripcion_entry = ttk.Entry(t, width=7, textvariable=self.descripcion)
        descripcion_entry.grid(column=3, row=4, sticky=(W, E))
        ttk.Label(t, text='Descripcion').grid(column=2, row=4, sticky=(W, E))
        ttk.Button(t, text="Agregar", command=self.agregarActividad).grid(column=3, row=6, sticky=W)
        
        
    def eliminarActividad(self):
        #print(self.act.buscar('nombreActividad',self.actividades.get())[0][0])
        print(self.act.eliminar(self.act.buscar('nombreActividad',self.actividades.get())[0][0]))
        #self.tree.delete("1.0", END)
        self.listarActividades()
        return()
    
    def agregarActividad(self):        
        id = self.act.crear((self.actividad.get(),self.fecha.get(),self.lugar.get(),self.descripcion.get()),self.actividad.get())
        self.listarActividades()
        return(id)
        
    def listarActividades(self):
        
        #self.scrolledtext1.delete("1.0", END) 
        
        
        cursor = self.act.listar()
        #print(cursor)
        #for documento in coleccion.find():
            #self.tree.insert('',0,text=documento["_id"],values=documento["nombre"])        
        act = []
        for fila in cursor:
            act.append(fila[1])
            #texto = " "+str(fila[1])+" "+fila[2]+" "+str(fila[3])+"\n\n"
            #self.tree.insert('',END,values=(fila[1],fila[2],fila[3]))
            #self.scrolledtext1.insert(END,texto )
        self.actividades['values'] = act  
        self.actividades.set(fila[1])
    
    def listarAsistencia1(self):
        for item in self.treePersona.get_children():
            self.treePersona.delete(item)        
        #actividad = self.act.buscar(self.act.clave, self.actividad.get())
       
        #actividad_id = actividad[0][0]
        #cursor = self.asi.buscar('actividad_id', actividad_id)
        cursor = self.per.buscarEntre(self.per.clave, self.textPersona.get())
        print(cursor,self.per.clave, self.textPersona.get())       
        #act = []
        for fila in cursor:
            #persona = self.per.buscar('id',fila[1])[0]
            self.treePersona.insert('',END,values=(fila[0],fila[1],fila[2],fila[3],fila[4]))  
    
    def listarAsistencia(self,eventObject ):
        self.listarAsistencia2()
        return
        
    def listarAsistencia2(self ):
        #def clear_all():
        #self.act.cform(self.marcoAsistencia)
        for item in self.treeAsistencias.get_children():
            self.treeAsistencias.delete(item)        
        actividad = self.act.buscar(self.act.clave, self.actividades.get())
        self.destruirHijos(self.lblDescripcion)
        self.act.cform(self.lblDescripcion,actividad[0])
        actividad_id = actividad[0][0]
        #print(actividad_id)
        #self.asi
        cursor = self.asi.buscar('actividad_id', actividad_id)
        print(cursor)
        #for documento in coleccion.find():
            #self.tree.insert('',0,text=documento["_id"],values=documento["nombre"])        
        act = []
        #self.treeAsistencias.delete(0)
        for fila in cursor:
            persona = self.per.buscar('id',fila[1])[0]
            self.treeAsistencias.insert('',END,values=(persona[0],persona[1],persona[2],persona[3]))
            #self.scrolledtext1.insert(END,texto )
        #self.actividades['values'] = act
        return
    
    def destruirHijos(self, padre):        
        for child in padre.winfo_children(): 
            print(child.destroy()   )
                

        
    def informacionPersonas(self,eventObject): 
        for selected_item in self.treeAsistencias.selection():
            item = self.treeAsistencias.item(selected_item)
            id = item['values'][0]
            ## show a message
            print(id)        
        datos = self.per.buscar('id', id)
        print(datos)
        self.destruirHijos(self.lblInformacion)
        self.per.cform(self.lblInformacion,datos[0])        
        
#class constructor():
    
    #def __init__(self,obj):
        #self.obj = obj
    #frm = {}   
    #def form(self, padre):
        #lf = ttk.Labelframe(padre, text='Label')
        #lf.grid(column=0, row=9, sticky=(W, E))
        #for campo in self.obj.get_campos():
            #ttk.Label(lf, text=campo).grid(column=0, row=0, sticky=(W, E))
            ##frm.append("""leble{0}""".format(campo)):ttk.Label(lf, text=campo).grid(column=0, row=0, sticky=(W, E))
            ##self.actividad = StringVar()
            ##actividad_entry = ttk.Entry(t, width=7, textvariable=self.actividad)
            ##actividad_entry.grid(column=3, row=1, sticky=(W, E))
            ##ttk.Label(t, text='Actividad').grid(column=2, row=1, sticky=(W, E))             
        ##lf = ttk.Labelframe(parent, text='Label')        
        #return(lf)    
    
    #pass

class tkmodelo(Modelo):
    #from . import constructor
    frm = {}   
    def cform(self, padre,datos):
        #lf = ttk.Labelframe(padre, text='Label')
        #print(lf.identify)
        #lf.grid(column=0, row=9, sticky=(W, E))
        for i, campo in enumerate(self.get_campos()):
            ttk.Label(padre, text=campo).grid(column=0, row=i, sticky=(W, E))
            ttk.Label(padre, text=datos[i+1]).grid(column=3, row=i, sticky=(W, E))
            #frm.append("""leble{0}""".format(campo)):ttk.Label(lf, text=campo).grid(column=0, row=0, sticky=(W, E))
            #self.actividad = StringVar()
            #actividad_entry = ttk.Entry(t, width=7, textvariable=self.actividad)
            #actividad_entry.grid(column=3, row=1, sticky=(W, E))
            #ttk.Label(t, text='Actividad').grid(column=2, row=1, sticky=(W, E))             
        #lf = ttk.Labelframe(parent, text='Label')        
        return() 
    
    def tkbuscar(self, dato):
        return(self.bd.listar("""SELECT * FROM {0} WHERE {1} = '{2}'""".format(self.tabla, self.clave, dato))[0])    
    
    def form(self, padre):
        print(self.get_campos())
        self.cform(self, padre)
        return
    
    #def nuevoObj(self,eventObject):
        #datos=[]
        #for i, campo in enumerate(self.get_campos()):
            #datos.append(self.variables[campo].get())
        #self.nuevo(datos,self.clave)
    
    #def nuevo(self, ventana):
        #padre = Toplevel(ventana)
        #self.variables = {}
        #for i, campo in enumerate(self.get_campos()):
            #ttk.Label(padre, text=campo).grid(column=0, row=i, sticky=(W, E))
            ##-----------
            #self.variables[campo] = StringVar()
            ##self.actividad = StringVar()
            #actividad_entry = ttk.Entry(padre, width=7, textvariable=self.variables[campo])
            #actividad_entry.grid(column=3, row=i, sticky=(W, E))
            ##ttk.Label(t, text='Actividad').grid(column=2, row=1, sticky=(W, E)) 
            ###-----------            
            ##ttk.Label(padre, text=datos[i+1]).grid(column=3, row=i, sticky=(W, E))
            
            ###-----------
            ##self.actividad = StringVar()
            ##actividad_entry = ttk.Entry(t, width=7, textvariable=self.actividad)
            ##actividad_entry.grid(column=3, row=1, sticky=(W, E))
            ##ttk.Label(t, text='Actividad').grid(column=2, row=1, sticky=(W, E)) 
            ###-----------
            ##self.fecha = StringVar()
            ##fecha_entry = ttk.Entry(t, width=7, textvariable=self.fecha)
            ##fecha_entry.grid(column=3, row=2, sticky=(W, E))
            ##ttk.Label(t, text='Fecha').grid(column=2, row=2, sticky=(W, E))
            ###-----------
            ##self.lugar = StringVar()
            ##lugar_entry = ttk.Entry(t, width=7, textvariable=self.lugar)
            ##lugar_entry.grid(column=3, row=3, sticky=(W, E))
            ##ttk.Label(t, text='Lugar').grid(column=2, row=3, sticky=(W, E)) 
            ###-----------
            ##self.descripcion = StringVar()
            ##descripcion_entry = ttk.Entry(t, width=7, textvariable=self.descripcion)
            ##descripcion_entry.grid(column=3, row=4, sticky=(W, E))
            ##ttk.Label(t, text='Descripcion').grid(column=2, row=4, sticky=(W, E))
        ##for i, campo in enumerate(self.get_campos()):
            ##print(variables[campo].get())
        #ttk.Button(padre, text="Agregar", command= self.nuevoObj).grid(column=3, row=6, sticky=W)            
if __name__=='__main__':
    ventana = Tk()
    app = Asistencia(ventana)
    ventana.mainloop()



#mainframe = ttk.Frame(root, padding="3 3 12 12")
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
##columnconfigure/rowconfigure le dicen a Tk que el marco debe expandirse para llenar cualquier espacio adicional 
##si se cambia el tamaño de la ventana
#root.columnconfigure(0, weight=1) 
#root.rowconfigure(0, weight=1)


##s = ttk.Separator(parent, orient=HORIZONTAL)
##Los marcos de etiquetas se crean usando la ttk.Labelframeclase:
##lf = ttk.Labelframe(parent, text='Label')
##Los cuadernos se crean usando la ttk.Notebookclase:
##n = ttk.Notebook(parent)
##f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
##f2 = ttk.Frame(n)   # second page
##n.add(f1, text='One')
##n.add(f2, text='Two')

#feet = StringVar()
#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#feet_entry.grid(column=2, row=1, sticky=(W, E))

#meters = StringVar()
#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#for child in mainframe.winfo_children(): 
    #child.grid_configure(padx=5, pady=5)

#feet_entry.focus()
#root.bind("<Return>", calculate)

#root.mainloop()
#get information on all options for this widget:
#button.configure()

#Para cada widget, imprimimos información básica, incluida su clase (botón, marco, etc.), ancho, alto y posición relativa a su 
#elemento principal.
#def print_hierarchy(w, depth=0):
    #print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    #for i in w.winfo_children():
        #print_hierarchy(i, depth+1)
#print_hierarchy(root)