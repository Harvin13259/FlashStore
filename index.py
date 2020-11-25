from flask import Flask, render_template  #inicializamos flask

app = Flask(__name__) #Objeto llamado app donde apartir de este objeto inicializamos un servidor (Hasta la linea 10)

@app.route('/')  #Ruta inicial, se puede acceder con localhost:5000
def home():
    return render_template('inicio_sesion.html')

@app.route('/registro')  #Ruta about
def registro():
    return render_template('registro.html')

@app.route('/flash_store')  #Ruta about
def flash():
    return render_template('flash_store.html')


if __name__== '__main__':
    app.run(debug=True)
