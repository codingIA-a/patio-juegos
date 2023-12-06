from flask import Flask, render_template #importamos librerias: flask
#y desde flask importamos render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Página de inicio'

@app.route('/play/<int:numero>/<string:color>')
def play_room(numero, color):
    number = numero
    color_caja = color
    return render_template('patio_de_juegos.html', number=number, color_caja=color_caja)


if __name__ == '__main__':
    app.run(debug=True, port=9000)
