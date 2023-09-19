from flask import Flask, request, jsonify

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)