from flask import Flask, request, jsonify
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/ping')
def ping():
    return jsonify({'status': 'ok',
                    'message': 'pong!'})

@app.route('/usuarios/<string:name>')
def usuario_by_name(name):
    return jsonify({'name': name})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({'id': id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

#GET
@app.route('/recurso', methods=['GET'])
def get_recursos():
    return jsonify({'status': 'ok',
                    'message': 'GET!',
                    'data': ["Lista de recursos"],
                    'data2': 'Lista de recursos 2'}) 

#POST
@app.route('/recurso', methods=['POST'])
def post_recursos():
    return jsonify({'data': 'Recurso creado con POST'}) 

if __name__ == '__main__':
    app.run(debug=True, port=5000)