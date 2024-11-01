from flask import Blueprint, request, jsonify
from professor.professores_model import Professor
from turma.turma_models import Turma, lista_turmas, adicionar_turma, delete_turma
from config import db

turma_blueprint = Blueprint('turma', __name__) 


@turma_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = lista_turmas()  # Assumindo que essa função retorna uma lista de turmas
    turmas_json = [turma.to_dict() for turma in turmas]
    return jsonify(turmas_json)


@turma_blueprint.route("/turma", methods=["POST", "PUT"])
def manage_turma():
    dados = request.get_json()
    descricao = dados.get('descricao')
    professor_id = dados.get('professor_id')
    
    if not descricao or not professor_id:
        return jsonify({'erro': 'Nome da turma e professor_id são obrigatórios'}), 400

    # Verificando se o professor existe
    professor = db.session.get(Professor, professor_id)
    if not professor:
        return jsonify({'erro': 'Professor não encontrado'}), 404

    if request.method == "POST":
        # Lógica para criação de uma nova turma
        adicionar_turma({
            'descricao': descricao,
            'professor': professor_id,
            'ativo': dados.get('ativo', True)  # Define 'ativo' como True por padrão
        })
        return jsonify({'mensagem': 'Turma criada com sucesso!'}), 201
    
    elif request.method == "PUT":
        # Lógica para atualizar uma turma existente
        turma_id = dados.get('turma_id')
        turma = db.session.get(Turma, turma_id)
        
        if not turma:
            return jsonify({'erro': 'Turma não encontrada'}), 404
        
        turma.descricao = descricao
        turma.professor_id = professor_id
        turma.ativo = dados.get('ativo', turma.ativo)  # Mantém o valor atual de 'ativo' se não for passado
        db.session.commit()
        
        return jsonify({'mensagem': 'Turma atualizada com sucesso!'}), 200



@turma_blueprint.route("/turma/<int:id_turma>", methods=["DELETE"])
def delete_turma(id_turma):
    # Substitua `delete_turma(id_turma)` pela lógica de exclusão correta
    turma = db.session.get(Turma, id_turma)
    if turma:
        db.session.delete(turma)
        db.session.commit()
        return jsonify({'mensagem': 'Turma deletada'}), 200
    return jsonify({'erro': 'Turma não encontrada'}), 404
