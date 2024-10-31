from flask import Blueprint, request, jsonify
from professor.professores_model import Professor
from turma.turma_models import lista_turmas, adicionar_turma, delete_turma
from config import db

turma_blueprint = Blueprint('turma', __name__) 


@turma_blueprint.route('/turma/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    print('lista turmas')
    return jsonify(lista_turmas(id_turma))

@turma_blueprint.route("/turma", methods=["POST"])
def create_turma():
   dados = request.get_json()
   nome = dados.get('nome')
   professor_id = dados.get('professor_id')

   if not nome or not professor_id:
        return jsonify({'erro': 'Nome da turma e professor_id são obrigatórios'}), 400

   professor = Professor.query.get(professor_id)
   if not professor:
        return jsonify({'erro': 'Professor não encontrado'}), 404

   adicionar_turma(nome=nome, professor_id=professor_id)
    
   return jsonify({'mensagem': 'Turma criada com sucesso!'}), 201
   

@turma_blueprint.route("/turma/<int:id_turma>", methods=["DELETE"])
def delete_turma(id_turma):
    delete_turma(id_turma)
    return "turma deletada" 