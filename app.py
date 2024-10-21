from flask import Flask, request 
import model_aluno_professor as model




app = Flask(__name__)


@app.route("/")
def home():
    return 'API Escolar está ativa !'


@app.route("/alunos", methods=['GET'])
def alunos():
    print("Lista de todos os alunos")
    return model.lista_alunos()

@app.route("/alunos/<int:nAluno>", methods=["GET"])
def alunoPorId(nAluno):
    try:
        return model.aluno_id(nAluno)
    except model.AlunoNaoEncontrado:
        return ({"erro": 'Aluno não encontrado'}, 400)
    
@app.route("/alunos", methods=["POST"])
def criar_aluno():
    dict = request.json
    dict['id'] = int(dict['id'])
    model.adiciona_aluno(dict)
    return model.lista_alunos()


@app.route("/deletar", methods=["POST", "DELETE"])
def deletar_alunos():
    model.apagar_alunos()
    return "Deletado"


@app.route("/professores", methods=['GET'])
def professores():
    print("Lista de todos os professores")
    return model.lista_professor()

@app.route("/professores/<int:nProfessor>", methods=["GET"])
def ProfessorPorId(nProfessor):
    try:
        return model.professor_id(nProfessor)
    except model.ProfessorNaoEncontrado:
        return ({"erro": 'Professor não encontrado'}, 400)
    
@app.route("/professores", methods=["POST"])
def criar_professor():
    dict = request.json
    dict['id'] = int(dict['id'])
    model.adiciona_professor(dict)
    return model.lista_professor()


@app.route("/apagar", methods=["POST", "DELETE"])
def deletar_professores():
    model.apagar_professores()
    return "Professores deletados"

if __name__ == '__main__':
    app.run(debug=True)