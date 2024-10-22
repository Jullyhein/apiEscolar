from flask import Flask, request, Blueprint, jsonify
from .model_aluno import AlunoNaoEncontrado, aluno_id, lista_alunos, excluir_alunos, adiciona_aluno, atualizar_alunos, excluir_alunos

aluno = Blueprint('alunos', __name__)


@aluno.route("/")
def home():
    return 'API Escolar está ativa !'


@aluno.route("/alunos", methods=['GET'])
def alunos():
    return jsonify(lista_alunos())

@aluno.route("/alunos/<int:id_aluno>", methods=["GET"])
def get_aluno(id_aluno):
    try:
        aluno = aluno_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return ({"erro": 'Aluno não encontrado'}), 404
    
@aluno.route("/alunos", methods=["POST"])
def create_aluno(id_aluno):
    data = request.json
    try:
        atualizar_alunos(id_aluno, data)
        return jsonify(aluno_id(id_aluno))
    except AlunoNaoEncontrado:
        return jsonify ({"erro": 'Aluno não encontrado'}), 404


@aluno.route("/deletar", methods=["POST", "DELETE"])
def delete_alunos(id_aluno):
    try:
        excluir_alunos(id_aluno)
        return '', 204
    except AlunoNaoEncontrado:
        return jsonify({"erro": 'Aluno não encontrado'}), 404