import json
from flask import Flask, jsonify 
from dados import Aluno, Professor, Turma
import dados



app = Flask(__name__)


caminho_json = r"C:\Users\jully\myproject\dados.py"


def carregar_dados():
    with open(caminho_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
    professor = Professor(**data['professor'])
    turma = Turma(**data['turma'], professor=professor)
    aluno = Aluno(**data['aluno'], turma=turma)
    return(aluno, turma, professor)

@app.route("/")
def home():
    return 'API Escolar está ativa !'


@app.route('/users', methods=['GET'])
def get_users():
    dados = carregar_dados()
    return jsonify(dados), 201

if __name__ == '__main__':
    app.run(debug=True)