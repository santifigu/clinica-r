#Importamos bibliotecas
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

#Desarrollo de la interfaz gráfica
ventana = tk.Tk()
ventana.title('Clínica Rosalía')
ventana.geometry("930x355+225+150")#930 355
ventana.resizable(width=False, height=False)
ventana.configure(background="lightblue")

#Gestion de pacientes
id = tk.StringVar()
nombre = tk.StringVar()
apellido = tk.StringVar()
dni = tk.StringVar()
edad = tk.StringVar()
obra_social = tk.StringVar()

#Conexión a BBDD
def conexionBBDD():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE pacientes(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) NOT NULL,
        APELLIDO VARCHAR(50) NOT NULL,
        EDAD INTEGER NOT NULL,
        OBRA_SOCIAL VARCHAR(50) NOT NULL,
        DNI INTEGER NOT NULL
        ) 
        """)
        messagebox.showinfo(title='Conexión', message='Base de Datos creada exitosamente.')
        conn.commit()
    except:
        messagebox.showinfo(title='Conexión', message='Conexión exitosa.') #si esta funcion es para crear una base de datos dejamos el título ahí, si no ponemos 'pass' y listo si ya está creada

#Eliminar la base de datos
def eliminarBBDD():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    try:
        valor = messagebox.askyesno(title='Base de Datos', message='¿Desea borrar la Base de Datos?')
        if valor:
            cursor.execute("""
            DROP TABLE pacientes
            """)
            messagebox.showinfo(title='Información', message='La Base de Datos ha sido eliminada.')
            conn.commit()
        else:
            pass
    except:
        messagebox.showerror(title='Error', message='No existe una Base de Datos.')
    limpiarcampos()
    mostrar()

#Salir de la aplicación
def salir():
    conn = sqlite3.connect('base_pacientes')
    valor = messagebox.askquestion(title='Salir', message='¿Deseas salir y guardar los cambios?')
    if valor == 'yes':
        conn.commit()
        ventana.destroy()
    else:
        pass

#Limpiar campos
def limpiarcampos():
    id.set('')
    nombre.set('')
    apellido.set('')
    dni.set('')
    edad.set('')
    obra_social.set('')

#Info de la app
def info():
    acerca = messagebox.showinfo(title='Información de la aplicación', message= """
    Aplicación Clínica
    Versión 1.0 
    """)

#Insertar valores
def registrar(event):#creamos una funcion llamada registrar la cual va a contener la funcion crear, la misma que se utiliza para registrar a los usuarios
    crear()
ventana.bind('<Return>', registrar)#y acá hacemos que apretando el enter llame a la función registrar creando o registrando los valores dentro de la tabla

def crear():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    try:
        if obra_social.get() == 'ips' or obra_social.get() == 'Ips':
            datos = nombre.get().title(), apellido.get().title(), edad.get(), obra_social.get().upper(), dni.get()
        else: 
            datos = nombre.get().title(), apellido.get().title(), edad.get(), obra_social.get().title(), dni.get()
        cursor.execute("INSERT INTO pacientes VALUES(NULL, ?, ?, ?, ?, ?)", (datos))
        conn.commit()
    except:
        messagebox.showwarning(title='Error', message='Hubo un error en la Base de Datos')
        pass
    limpiarcampos()
    mostrar()

def mostrar():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        cursor.execute("SELECT * FROM pacientes")
        for row in cursor:
            tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
    except:
        pass

def mostrarfiltro0_3():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    edad_min = 1
    edad_max = 3
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        cursor.execute("SELECT * FROM pacientes WHERE Edad >= ? AND Edad <= ? ORDER BY edad DESC", (edad_min, edad_max))
        for row in cursor:
            tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
    except:
        messagebox.showerror(title='Error', message='Hubo un error al mostrar los registros filtrados.')
    conn.close()

def mostrarfiltro4_6():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    edad_min = 4
    edad_max = 6
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        cursor.execute("SELECT * FROM pacientes WHERE Edad >= ? AND Edad <= ? ORDER BY edad DESC", (edad_min, edad_max))
        for row in cursor:
            tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
    except:
        messagebox.showerror(title='Error', message='Hubo un error al mostrar los registros filtrados.')
    conn.close()

def mostrarfiltro7_9():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    edad_min = 7
    edad_max = 9
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        cursor.execute("SELECT * FROM pacientes WHERE Edad >= ? AND Edad <= ? ORDER BY edad DESC", (edad_min, edad_max))
        for row in cursor:
            tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
    except:
        messagebox.showerror(title='Error', message='Hubo un error al mostrar los registros filtrados.')
    conn.close()
    
def mostrarfiltro10_12():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    edad_min = 10
    edad_max = 12
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        cursor.execute("SELECT * FROM pacientes WHERE Edad >= ? AND Edad <= ? ORDER BY edad DESC", (edad_min, edad_max))
        for row in cursor:
            tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
    except:
        messagebox.showerror(title='Error', message='Hubo un error al mostrar los registros filtrados.')
    conn.close()

################################################### Tabla ###############################################################
tree = ttk.Treeview(height=10, columns=('#0', '#1', '#2', '#3','#4'))#heigth=le damos altura, columns=cantidad de columnas con numeral
tree.place(x=0, y=130)
tree.column('#0', width=100) #especificamos la columna y le damos una anchura de 100
tree.heading('#0', text='ID', anchor=tk.CENTER)#especificando de nuevo la columna, le ponemos en el parametro 'text' el nombre y con 'anchor' le decimos que la palabra quede centrada
tree.heading('#1', text='Nombre', anchor=tk.CENTER)
tree.heading('#2', text='Apellido', anchor=tk.CENTER)
tree.column('#3', width=100)
tree.heading('#3', text='Edad', anchor=tk.CENTER)
tree.heading('#4', text='Obra Social', anchor=tk.CENTER)
tree.column('#5', width=130)
tree.heading('#5', text='DNI', anchor=tk.CENTER)

#Actualizar- Sirve para cuando queremos actulizar los datos de alguien
def actualizar():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    try:
        if obra_social.get() == 'ips' or obra_social.get() == 'Ips':
            datos = nombre.get().title(), apellido.get().title(), edad.get(), obra_social.get().upper(), dni.get()
        else: 
            datos = nombre.get().title(), apellido.get().title(), edad.get(), obra_social.get().title(), dni.get()
        cursor.execute("UPDATE pacientes SET NOMBRE=?, APELLIDO=?, EDAD=?, OBRA_SOCIAL=?, DNI=? WHERE ID="+ id.get(), (datos))
        conn.commit()
    except:
        messagebox.showwarning(title='Error', message='Ocurrió un error al actualizar el registro')
        pass
    limpiarcampos()
    mostrar()

#Clickear
def seleccionar(event):
    item = tree.identify('item', event.x, event.y)
    id.set(tree.item(item, 'text'))
    nombre.set(tree.item(item, 'values')[0])
    apellido.set(tree.item(item, 'values')[1])
    edad.set(tree.item(item, 'values')[2])
    obra_social.set(tree.item(item, 'values')[3])
    dni.set(tree.item(item, 'values')[4])

tree.bind('<Double-1>', seleccionar)

#Borrar
#borramos un paciente o empleado
def borrar():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    try:
        if messagebox.askyesno(message='¿Deseas eliminar el registro?', title='Advertencia'):
            cursor.execute("DELETE FROM pacientes WHERE ID=" + id.get())
            conn.commit()
            messagebox.showinfo(title='Información', message='El paciente ha sido eliminado.')
        else:
            pass
    except:
        messagebox.showerror(title='Error', message='Ocurrió un error al borrar el registro')
        pass
    limpiarcampos()
    mostrar()

#Filtrar
#filtramos pacientes
#0-3
def filtrar0_3():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    edad_min = 1
    edad_max = 3
    try:
        edad0_3 = cursor.execute("SELECT * FROM pacientes WHERE Edad >= ? AND Edad <= ? ORDER BY Edad ASC", (edad_min, edad_max))       
        resultado = cursor.fetchall()
    except:
        messagebox.showerror(title='Error', message='Hubo un error')
        pass
    limpiarcampos()
    mostrarfiltro0_3()

#4-6
def filtrar4_6():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    edad_min = 4
    edad_max = 6
    try:
        edad4_6 = cursor.execute("SELECT * FROM pacientes WHERE edad >= ? AND edad <= ? ORDER BY edad ASC", (edad_min, edad_max))
        resultado = cursor.fetchall()
    except:
        messagebox.showerror(title='Error', message='Hubo un error')
        pass
    limpiarcampos()
    mostrarfiltro4_6()

#7-9
def filtrar7_9():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    edad_min = 7
    edad_max = 9
    try:
        edad7_9 = cursor.execute("SELECT * FROM pacientes WHERE Edad >= ? AND Edad <= ? ORDER BY Edad ASC", (edad_min, edad_max))
        resultado = cursor.fetchall()
    except:
        messagebox.showerror(title='Error', message='Hubo un error')
        pass
    limpiarcampos()
    mostrarfiltro7_9()

#10-12
def filtrar10_12():
    conn = sqlite3.connect('base_pacientes')
    cursor = conn.cursor()
    edad_min = 10
    edad_max = 12
    try:
        edad10_12 = cursor.execute("SELECT * FROM pacientes WHERE Edad >= ? AND Edad <= ? ORDER BY Edad ASC", (edad_min, edad_max))
        resultado = cursor.fetchall()
    except:
        messagebox.showerror(title='Error', message='Hubo un error')
        pass
    limpiarcampos()
    mostrarfiltro10_12()


########################################################### Interfaz Gráfica #############################################################################    

#Barra de menú
#Inicio
menubar = tk.Menu(ventana) #creamos una barra de menu u opciones en realidad, en la parte de arriba
menubasedat = tk.Menu(menubar, tearoff=0) #creamos la estructura del menu para el inicio
menubasedat.add_command(label='Crear/Conectar a la Base de Datos', command=conexionBBDD) #creamos o nos conectamos a la base de datos
menubasedat.add_command(label='Eliminar Base de Datos', command=eliminarBBDD) #eliminar toda tabla, es decir, todo el registro
menubasedat.add_command(label='Salir', command=salir) #salir de la app
menubar.add_cascade(label='Inicio', menu=menubasedat) #vinculamos a la barra de menus

#Ayuda
menuayuda = tk.Menu(menubar, tearoff=0) #creacion del menu ayuda 
menuayuda.add_command(label='Info', command=info) #info de la app
menubar.add_cascade(label='Info', menu=menuayuda)#enlazamos las opciones de arriba con el menu

#Filtro - hacer su función
menufiltro = tk.Menu(menubar, tearoff=0)
menufiltro.add_command(label='0-3', command=filtrar0_3)
menufiltro.add_command(label='4-6', command=filtrar4_6)
menufiltro.add_command(label='7-9', command=filtrar7_9)
menufiltro.add_command(label='10-12', command=filtrar10_12)
menubar.add_cascade(label='Filtro', menu=menufiltro)

ventana.config(menu=menubar) #agregamos las barras a la pantalla así aparecen

#Caja
e1 = tk.Entry(ventana, textvariable=id) #primero le indicamos donde o en que ventana va a estar y luego con qué la vamos a enlazar

#Entrada-Nombre
l2 = tk.Label(ventana, text='Nombre', bg='lightblue')
l2.place(x=50, y=10)   
e2 = tk.Entry(ventana, textvariable=nombre, width=50)
e2.place(x=130,y=10)

#Entrada-Apellido
l3 = tk.Label(ventana, text='Apellido', bg='lightblue')
l3.place(x=50, y=40)   
e3 = tk.Entry(ventana, textvariable=apellido, width=50)
e3.place(x=130,y=40)

#Entrada-Edad
l4 = tk.Label(ventana, text='Edad', bg='lightblue')
l4.place(x=50, y=70)   
e4 = tk.Entry(ventana, textvariable=edad, width=2)
e4.place(x=130,y=70)

#Entrada-Obra Social
l5 = tk.Label(ventana, text='Obra Social', bg='lightblue')
l5.place(x=50, y=100)   
e5 = tk.Entry(ventana, textvariable=obra_social)
e5.place(x=130,y=100)

#Entrada-Obra Social
l6 = tk.Label(ventana, text='DNI', bg='lightblue')
l6.place(x=260, y=70)   
e6 = tk.Entry(ventana, textvariable=dni)
e6.place(x=310,y=70)


########################### Botones #####################################

botregistrar = tk.Button(ventana, text='Registrar', command=crear)
botregistrar.place(x=800, y=5)

botactualizar = tk.Button(ventana, text='Actualizar', command=actualizar)
botactualizar.place(x=800, y=35)

botmostrar = tk.Button(ventana, text='Ver Lista Pacientes', command=mostrar)
botmostrar.place(x=780, y=65)

boteliminar = tk.Button(ventana, text='Eliminar', bg='red', fg='white' ,command=borrar)
boteliminar.place(x=800, y=95)

ventana.config(menu=menubar)
ventana.mainloop()

