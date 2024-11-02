from flask import Flask, request, Blueprint, jsonify, render_template, redirect, url_for
from .model_aluno import AlunoNaoEncontrado, aluno_id, listar_alunos, atualizar_aluno, deletar_aluno_por_id, adicionar_aluno

aluno = Blueprint('alunos', __name__)


@aluno.route("/")
def home():
    return render_template("home.html")


@aluno.route("/alunos/listar_alunos", methods=['GET'])
def listar_alunos_view():
    alunos_data = listar_alunos()
    return render_template('listar_alunos.html', alunos_data=alunos_data)


@aluno.route("/alunos/<int:id_aluno>", methods=["GET"])
def get_aluno(id_aluno):
    try:
        aluno = aluno_id(id_aluno)
        return render_template('aluno_id.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return ({"erro": 'Aluno não encontrado'}), 404
    

@aluno.route("/alunos/adicionar", methods=["GET"])
def mostrar_formulario_aluno():
    return render_template('criar_aluno.html')
    

@aluno.route("/alunos/criar", methods=["POST"])
def create_aluno():
    # Captura os dados do formulário
    data = {
        "nome": request.form['nome'],
        "turma_id": request.form["turma_id"],
        "data_nascimento": request.form["data_nascimento"],
        "nota_semestre_1": request.form["nota_semestre_1"],
        "nota_semestre_2": request.form["nota_semestre_2"]
    }
    
    try:
        # Função para adicionar o novo aluno ao banco de dados
        novo_aluno = adicionar_aluno(data)
        return redirect(url_for('alunos.listar_alunos_view'))
    except AlunoNaoEncontrado:
        return jsonify({"erro": 'Erro ao adicionar aluno'}), 404
    

@aluno.route("/alunos/editar/<int:id_aluno>", methods=["PUT", "POST"])
def update_aluno(id_aluno):
    print("Dados recebidos no formulário:", request.form)
    try:
        aluno = aluno_id(id_aluno)
        nome = request.form['nome']
        aluno['nome'] = nome
        data_nascimento = request.form['data_nascimento']
        aluno['data_nascimento'] = data_nascimento
        turma_id = request.form['turma_id']
        aluno['turma_id'] = turma_id
        nota_semestre_1 = request.form['nota_semestre_1']  # Supondo que ainda esteja recebendo 'nota_1st' do form
        aluno['nota_semestre_1'] = nota_semestre_1
        nota_semestre_2 = request.form['nota_semestre_2']  # Supondo que ainda esteja recebendo 'nota_2st' do form
        aluno['nota_semestre_2'] = nota_semestre_2
        
        atualizar_aluno(id_aluno, aluno)
        return redirect(url_for('alunos.listar_alunos_view', aluno=aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    

@aluno.route('/alunos/editar/<int:id_aluno>', methods=['GET'])
def editar_aluno_page(id_aluno):
    try:
        aluno = aluno_id(id_aluno)
        return render_template('update_aluno.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404


@aluno.route("/deletar/deletar/<int:id_aluno>", methods=["POST"])
def delete_alunos(id_aluno):
    if request.method == "POST":
        # Verifique se o método oculto é DELETE
        if request.form.get('_method') == 'DELETE':
            try:
                deletar_aluno_por_id(id_aluno)
                return redirect(url_for('alunos.listar_alunos_view'))
            except AlunoNaoEncontrado:
                return jsonify({"erro": 'Aluno não encontrado'}), 404
    return jsonify({"erro": "Método não permitido"}), 405
