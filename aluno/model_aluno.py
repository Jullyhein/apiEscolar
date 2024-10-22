dados = {"alunos":[
                   {"nome":"lucas","id":15},
                   {"nome":"cicero","id":29},
                  ]}


class AlunoNaoEncontrado(Exception):
    pass

def aluno_id(id_aluno):
    lista_alunos = dados['alunos']
    for i in lista_alunos:
        if i['id'] == id_aluno:
            return i
    raise AlunoNaoEncontrado

def adiciona_aluno(dict):
    dados['alunos'].append(dict)


def lista_alunos():
    return dados["alunos"]


def atualizar_alunos(id_aluno, novos_dados):
    aluno = aluno_id(id_aluno)
    aluno.update(novos_dados)

def excluir_alunos(id_aluno):
    aluno = aluno_id(id_aluno)
    dados['alunos'].remove(aluno)