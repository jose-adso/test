from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola, los ejercicios estan!'

@app.route('/index')
def hola_adso():
    return '¡Hola - los lunes son los dias mas fuertes !'

@app.route('/index2')
def hola_adso2():
    return '¡Hola - ADSO TARDE SE ESFUERZA POR APRENDER !'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000) 
