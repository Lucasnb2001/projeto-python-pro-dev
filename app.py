from flask import Flask, jsonify, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"projeto": "Análise de Sentimento Python Pro", "status": "online"})

@app.route('/analisar', methods=['POST'])
def analisar_sentimento():
    # Pega o texto enviado no corpo da requisição (JSON)
    dados = request.get_json()
    texto = dados.get('texto', '')

    if not texto:
        return jsonify({"erro": "Nenhum texto fornecido"}), 400

    # Realiza a análise (TextBlob funciona melhor em inglês por padrão)
    analise = TextBlob(texto)
    polaridade = analise.sentiment.polarity

    if polaridade > 0:
        sentimento = "Positivo"
    elif polaridade < 0:
        sentimento = "Negativo"
    else:
        sentimento = "Neutro"

    return jsonify({
        "texto": texto,
        "sentimento": sentimento,
        "polaridade": polaridade
    })

if __name__ == '__main__':
    app.run(debug=True)