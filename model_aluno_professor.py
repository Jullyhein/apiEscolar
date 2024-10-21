dados = {"alunos":[
                   {"nome":"lucas","id":15},
                   {"nome":"cicero","id":29},
                  ], 
        "professores":[
                    {"nome":"Camila","id":25},
                    {"nome":"Jully","id":27}]}


class AlunoNaoEncontrado(Exception):
    pass

def aluno_id(id_aluno):
    lista_alunos = dados['alunos']
    for i in lista_alunos:
        if i['id'] == id_aluno:
            return i
    raise AlunoNaoEncontrado

def aluno_existe(id_aluno):
    try:
        aluno_id(id_aluno)
        return True
    except AlunoNaoEncontrado:
        return False

def adiciona_aluno(dict):
    dados['alunos'].append(dict)


def lista_alunos():
    return dados["alunos"]


def apagar_alunos():
    dados['alunos'] = []


class ProfessorNaoEncontrado(Exception):
    pass

def professor_id(id_professor):
    lista_professor = dados['professores']
    for i in lista_professor:
        if i['id'] == id_professor:
            return i
    raise ProfessorNaoEncontrado

def professor_existe(id_professor):
    try:
        professor_id(id_professor)
        return True
    except ProfessorNaoEncontrado:
        return False

def adiciona_professor(dict):
    dados['professores'].append(dict)


def lista_professor():
    return dados["professores"]


def apagar_professor():
    dados['professores'] = []