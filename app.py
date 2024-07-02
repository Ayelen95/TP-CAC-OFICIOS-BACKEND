#importamos el modulo de flask para que funcione el proyecto
from flask import Flask, render_template, request, redirect, url_for, jsonify

#importamos el modulo os para acceder mas facil a los directorios
import os

# importamos para la base de datos
import database as db

#definimos la ruta absoluta del proyecto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#unimos las rutas de las carpetas src y templates a la ruta del proyecto de la línea anterior
template_dir = os.path.join(template_dir, 'src', 'templates')

#indicamos que se busque el archivo index.html (en carpeta templates) al lanzar la aplicación
app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
# @app.route('/') es un decorador que vincula una función con una URL específica del sitio web. En este caso, '/' representa la ruta raíz o homepage del sitio web.

# La función home() que sigue al decorador es la que se ejecutará cuando un usuario visite la página principal (homepage) del sitio. La declaración return render_template('index.html') dentro de esta función indica que Flask debe buscar y renderizar el archivo HTML llamado index.html, que generalmente contiene el contenido que se mostrará en la página principal del sitio web.

# IMPORTANTE: importar en la linea 2 del codigo el modulo render_template para lanzar la pagina index.html. Debe quedar asi:
# from flask import Flask, render_template


# cursor es un objeto que apunta a la base de datos y nos permitira interactuar con el. database es el nombre de la variable que se encuentra en el archivo database.py y que contiene toda la informacion de conexion a la base de datos.

#  cursor.execute("SELECT * FROM users") ejecuta la consulta sql a la base de datos

# el metodo fetchall toma todos los registros devueltos en la ejecucion de la consulta anterior y guarda el resultado en la variable miResultado.

# insertarObjectos = [] crea una lista vacia

# nombreDeColumnas = [columna[0] for columna in cursor.description]
# Los nombres de las columnas se obtienen de cursor.description y los guarda en la variable nombreDeColumnas.

# for unRegistro in miResultado:
#     insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
# Recorre cada registro del resultado de ejecutar la consulta y lo convierten en un diccionario. Esto se hace mediante el uso de zip() para emparejar los nombres de las columnas con los valores de cada registro. 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administracion')
def administracion():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM alumnos")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarAlumnos= [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarAlumnos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    cursor.execute("SELECT * FROM cursos")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarCursos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarCursos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    cursor.execute("SELECT * FROM provincias")
    miResultado = cursor.fetchall()
    insertarProvincias = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    
    for unRegistro in miResultado:
        insertarProvincias.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('administracion.html', alumnos=insertarAlumnos,cursos=insertarCursos,provincias=insertarProvincias)



@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM alumnos")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarAlumnos= [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarAlumnos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    cursor.execute("SELECT * FROM cursos")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarCursos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarCursos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    cursor.execute("SELECT * FROM provincias")
    miResultado = cursor.fetchall()
    insertarProvincias = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    
    for unRegistro in miResultado:
        insertarProvincias.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('index.html', alumnos=insertarAlumnos,cursos=insertarCursos,provincias=insertarProvincias)


@app.route('/alumno', methods=['POST'])
def agregar_alumno(): 
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    genero = request.form['genero']
    cod_provincia = request.form['provincia']
    cod_curso= request.form['curso']

        # Guardar los datos en la base de datos MySQL
        
        
    if nombre and apellido and dni and genero and cod_provincia and cod_curso:
        cursor = db.database.cursor()
        sql = "INSERT INTO alumnos (nombre, apellido, dni,genero,cod_provincia,cod_curso) VALUES (%s, %s, %s,%s,%s,%s)"
        data = (nombre, apellido, dni,genero,cod_provincia,cod_curso)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('administracion'))

@app.route('/registro', methods=['POST'])
def registrar_alumno(): 
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    genero = request.form['genero']
    cod_provincia = request.form['provincia']
    cod_curso= request.form['curso']

        # Guardar los datos en la base de datos MySQL
        
        
    if nombre and apellido and dni and genero and cod_provincia and cod_curso:
        cursor = db.database.cursor()
        sql = "INSERT INTO alumnos (nombre, apellido, dni,genero,cod_provincia,cod_curso) VALUES (%s, %s, %s,%s,%s,%s)"
        data = (nombre, apellido, dni,genero,cod_provincia,cod_curso)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('administracion'))

@app.route("/cursos/<string:turno>")
def obtener_cursos(turno):
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM cursos WHERE turno = %s", (turno,))
    miResultado = cursor.fetchall()
    
    # Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return jsonify(insertarObjectos)
 
@app.route('/eliminar_alumno/<string:id>')
def eliminar_alumno(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM alumnos WHERE id = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('administracion'))

@app.route('/eliminar_provincia/<string:id>')
def eliminar_provincia(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM provincias WHERE id = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('administracion'))


@app.route('/eliminar_curso/<string:id>')
def eliminar_curso(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM cursos WHERE id = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('administracion'))



@app.route('/editar_alumno/<string:id>', methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    genero = request.form['genero']
    cod_provincia = request.form['provincia']
    cod_curso= request.form['curso']
    
    if nombre and apellido and dni and genero and cod_provincia and cod_curso:
        cursor = db.database.cursor()
        sql = "UPDATE alumnos SET nombre = %s, apellido = %s, dni = %s, genero = %s,cod_provincia=%s,cod_curso=%s WHERE id = %s"
        data = (nombre,apellido,dni,genero,cod_provincia,cod_curso,id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('administracion'))

@app.route('/editar_provincia/<string:id>', methods=['POST'])
def edit_provincia(id):
    provincia = request.form['nombre']
    
    if provincia:
        cursor = db.database.cursor()
        sql = "UPDATE provincias SET provincia = %s WHERE id = %s"
        data = (provincia,id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('administracion'))

@app.route('/editar_curso/<string:id>', methods=['POST'])
def edit_curso(id):
    nombre = request.form['nombre']
    turno = request.form['turno']
    if nombre and turno:
        cursor = db.database.cursor()
        sql = "UPDATE cursos SET nombre = %s, turno = %s WHERE id = %s"
        data = (nombre,turno,id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('administracion'))

@app.route("/provincias")
def obtener_provincias():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM provincias")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('contacto.html', data=insertarObjectos)

@app.route('/curso', methods=['POST'])
def agregar_curso():
    codigo=request.form['codigo_curso']
    nombre = request.form['nombre_curso']
    turno= request.form['turno_curso']

        # Guardar los datos en la base de datos MySQL
        
        
    if codigo and nombre and turno:
        cursor = db.database.cursor()
        sql = "INSERT INTO cursos (id,nombre, turno) VALUES (%s, %s,%s)"
        data = (codigo,nombre,turno)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('administracion'))

@app.route('/provincia', methods=['POST'])
def agregar_provincia():
    
    nombre = request.form['nombre_provincia']
   

        # Guardar los datos en la base de datos MySQL
        
        
    if nombre :
        cursor = db.database.cursor()
        sql = "INSERT INTO provincias (provincia) VALUES (%s)"
        data = (nombre,)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('administracion'))

@app.route('/contacto')
def contacto():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM provincias")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('contacto.html', data=insertarObjectos)

#ejecucion directa de este archivo en modo de desarrollador en el puerto 4000 del localhost o servidor local creado por flask.
if __name__ == '__main__':
    app.run(debug=True, port=4000)
