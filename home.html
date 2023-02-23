from flask import Flask, render_template, request, redirect, url_for,flash

app = Flask(__name__)

from flask import Flask

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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

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
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image = request.files['image']

        flash('Artículo subido con éxito', 'success')
        return redirect(url_for('index'))

    return render_template('subir-articulo.html')

if __name__ == '__main__':
    app.run(debug=True , port=5000)
