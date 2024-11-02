from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .professores_model import Professor, ProfessorNaoEncontrado, lista_professor, professor_id, adiciona_professor, atualiza_prof, deleta_prof
from turma.turma_models import DadoNaoEncontrado, Turma
from config import db


professor = Blueprint('professores', __name__)



@professor.route("/professores", methods=['GET'])
def lista_professores():
    professores = lista_professor()
    return render_template("professores.html", professores=professores)



@professor.route("/professores/<int:id_professor>", methods=["GET"])
def get_professor_por_id(id_professor):
    try:
        professor = professor_id(id_professor)  # Presumindo que professor_id busque pelo ID
        return render_template("prof_id.html", professor=professor)  # Nome do template ajustado
    except DadoNaoEncontrado:  # Exceção mais genérica
        return jsonify({"erro": 'Professor não encontrado'}), 404
    


@professor.route('/professores/<int:id_professor>', methods=['GET'])
def get_professorPorId(id_prof):
    try:
        professor = professor_id(id_prof)
        return render_template("prof_id.html", professor=professor)
    except DadoNaoEncontrado:
        return jsonify({"erro": 'Professor nao encontrado'}), 404


## ROTA ACESSAR O FORMULARIO DE CRIAÇÃO DE UM NOVOS PROFESSORES 
@professor.route('/professores/adicionar', methods=['GET'])
def adicionar_professor_page():
    turmas = Turma.query.all()  # Busca todas as turmas
    return render_template('criarProfessor.html', turmas=turmas)
    

## ROTA QUE CRIA UM NOVO PROFESSOR  
@professor.route("/professores/", methods=["POST"])
def create_professor():
    nome = request.form['nome']
    idade = request.form['idade']
    materia = request.form['materia']
    observacao = request.form['observacao']
    turmas_ids = request.form.getlist('turmas')  # Captura as turmas selecionadas

    # Cria uma instância do novo professor
    novo_professor = Professor(nome=nome, idade=idade, materia=materia, observacao=observacao)

    # Adiciona o novo professor ao banco de dados
    db.session.add(novo_professor)
    db.session.commit()

    # Associa as turmas selecionadas ao novo professor
    for turma_id in turmas_ids:
        turma = Turma.query.get(turma_id)  # Busca a turma pelo ID
        if turma:
            turma.professor_id = novo_professor.id  # Associa a turma ao professor

    db.session.commit()

    return redirect(url_for('professores.lista_professores'))



## ROTA PARA O FORMULARIO PARA EDITAR UM NOVO PROFESSOR
@professor.route('/professores/editar/<int:id_professor>', methods=['GET'])
def editar_professor_page(id_professor):
    try:
        professor = professor_id(id_professor)
        return render_template('professores_update.html', professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404
    

## ROTA QUE EDITA UM ALUNO
@professor.route('/professores/<int:id_professor>', methods=['POST', 'PUT'])
def update_professores(id_professor):
    print("Dados recebidos no formulário:", request.form)
    try:
        professores = lista_professor()
        prof = professor_id(id_professor)  # Supondo que isso retorna um objeto Professor
        nome = request.form["nome"]
        materia = request.form["materia"]
        idade = request.form["idade"]
        observacao = request.form["observacao"]
        
        # Atualiza os atributos do objeto Professor
        prof.nome = nome
        prof.materia = materia
        prof.idade = idade
        prof.observacao = observacao
        
        # Atualiza o professor no banco de dados
        atualiza_prof(id_professor, prof)
        
        return render_template('professores.html', professores=professores)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


## ROTA QUE DELETA UM PROFESSOR
@professor.route("/professores/delete/<int:id_professor>", methods=["POST", "DELETE"])
def delete_professores(id_professor):
    if request.method == "POST":
        # Verifique se o método oculto é DELETE
        if request.form.get('_method') == 'DELETE':
            try:
                deleta_prof(id_professor)
                return redirect(url_for("professores.lista_professores"))
            except DadoNaoEncontrado:
                return jsonify({"erro": 'Professor não encontrado'}), 404
    return jsonify({"erro": "Método não permitido"}), 405
