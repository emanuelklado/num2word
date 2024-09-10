from flask import Flask, request, jsonify, render_template
from num2words import num2words

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/numero_por_extenso', methods=['GET'])
def numero_por_extenso():
    numero = request.args.get('numero', default=None, type=int)
    if numero is None:
        return jsonify({'erro': 'Número não fornecido'}), 400
    
    numero_extenso = num2words(numero, lang='pt_BR')
    return jsonify({'numero': numero, 'por_extenso': f'{numero_extenso} Reais'})

if __name__ == '__main__':
    app.run(debug=True)
