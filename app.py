from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem-vindo à minha API de Python Pro!"})

@app.route('/saudar/<nome>')
def saudar(nome):
    return jsonify({"saudacao": f"Olá, {nome}! Projeto funcionando."})

if __name__ == '__main__':
    app.run(debug=True)