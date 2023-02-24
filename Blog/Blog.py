from flask import Flask, render_template, request, redirect, url_for,flash,session
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)

app.secret_key = 'miclavesecreta'

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '170504Md*'
app.config['MYSQL_DB'] = 'economiaentusmanos_users'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Definir algunas publicaciones de muestra
publicaciones = [
    
    {
        'titulo': 'Cómo ahorrar dinero en tiempos difíciles',
        'autor': 'Gustavo Salazar',
        'fecha': '1 de enero de 2023',
        'contenido': 'En estos tiempos difíciles, ahorrar dinero es más importante que nunca. Aquí hay algunos consejos útiles para empezar...'
    },
    {
        'titulo': 'Cómo invertir en el mercado de valores',
        'autor': 'Gustavo Salazar',
        'fecha': ' de febrero de 2023',
        'contenido': 'Invertir en el mercado de valores puede parecer intimidante al principio, pero con un poco de investigación y paciencia, cualquiera puede hacerlo. Aquí hay algunos consejos para empezar...'
    },
    {
        'titulo': 'Cómo Invertir 100$',
        'autor': 'Gustavo Salazar',
        'fecha': '18 de febrero de 2023',
        'contenido': 'Lo mas importante al tener un capital reducido es enteder bien el mercado al que estas entrando y tener bien claro las deficiencias que hay en el mismo ya que ese sera nuestro edge para sacar futuras recompensas'

    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Recuperar la información del formulario
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        # Crear un cursor y ejecutar la consulta para recuperar la información del usuario
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM usuarios WHERE correo = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()

        # Verificar la contraseña
        if user and bcrypt.checkpw(password, user['contrasena'].encode('utf-8')):
            # Iniciar la sesión del usuario
            session['loggedin'] = True
            session['id'] = user['id']
            session['name'] = user['nombre']
            session['email'] = user['correo']

            # Redirigir al usuario a la página de inicio
            return redirect(url_for('index'))
        else:
            # Mostrar un mensaje de error si las credenciales son incorrectas
            flash('Credenciales incorrectas.')

    return render_template('login.html')

# Página de registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Recuperar la información del formulario
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        # Encriptar la contraseña
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # Crear un cursor y ejecutar la consulta de inserción en la base de datos
        cursor = mysql.connection.cursor()
        query = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, hashed_password))
        mysql.connection.commit()

        # Cerrar el cursor y mostrar un mensaje de éxito
        cursor.close()
        flash('¡Registro exitoso!')

        # Redirigir al usuario a la página de inicio de sesión
        return redirect(url_for('login'))

    return render_template('registro.html')

# Cerrar la sesión del usuario
@app.route('/logout')
def logout():
    # Eliminar todas las variables de sesión
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('name', None)
    session.pop('email', None)

    # Redirigir al usuario a la página de inicio
    return render_template('/home.html')


# Definir la ruta para la página principal
@app.route('/index')
def index():
    return render_template('index.html', publicaciones=publicaciones)

# Definir la ruta para las publicaciones individuales
@app.route('/publicacion/<int:id>')
def publicacion(id):
    publicacion = publicaciones[id]
    return render_template('publicacion.html', publicacion=publicacion)

@app.route('/admin/upload_article', methods=['GET', 'POST'])
def upload_article():
    # Verificar si el usuario está logueado
    if 'loggedin' in session:
        if request.method == 'POST':
            titulo = request.form['titulo']
            contenido = request.form['contenido']
            imagen = request.files['imagen']
            fecha_publicacion = request.form['fecha_publicacion']

           # Guardar la imagen en el servidor
            imagen.save('static/img/' + imagen.filename)

            # Crear un cursor y ejecutar la consulta para insertar el artículo en la base de datos
            cursor = mysql.connection.cursor()
            query = "INSERT INTO articulos (titulo, contenido, imagen, autor) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (titulo, contenido, imagen.filename, session['nombre']))
            mysql.connection.commit

            flash('Artículo subido con éxito', 'success')
            return redirect(url_for('/admin/upload_article'))


    return render_template('subir-articulo.html')

if __name__ == '__main__':
    app.run(debug=True , port=5000)
