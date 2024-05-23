from flask import Flask, request, jsonify
from flask_cors import CORS
import lexer
import logging

app = Flask(__name__)
CORS(app)
app.secret_key = 'clavee22'
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['POST'])
def index():
    data = request.json
    codigo = data.get('textarea_content', '')

    tokens = lexer.analizar_texto(codigo)

    return jsonify({'tokens': tokens})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
