from flask import Blueprint, request, jsonify
from .professores_model import ProfessorNaoEncontrado, lista_professor, professor_id, adiciona_professor, atualiza_prof, deleta_prof

professor = Blueprint('professores', __name__)



@professor.route("/professores", methods=['GET'])
def professores():
    return jsonify(lista_professor())

@professor.route("/professores/<int:nProfessor>", methods=["GET"])
def get_professor(id_professor):
    try:
        professor = professor_id(id_professor)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({"erro": 'Professor não encontrado'}, 400)
    
@professor.route("/professores/", methods=["POST"])
def create_professor():
    data = request.json
    adiciona_professor(data)
    return jsonify(data), 201
    

@professor.route('/professores/<int:id_professor>', methods=['PUT'])
def update_professores(id_professor):
    data = request.json
    try:
        atualizar_professor(id_professor, data)
        return jsonify(professor_id(id_professor))
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


@professor.route("/professores/<int:id_professores>", methods=["DELETE"])
def delete_professores(id_professor):
    try:
        deleta_prof(id_professor)
        return '', 204
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404