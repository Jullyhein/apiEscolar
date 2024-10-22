dados = { 
        "professores":[
                    {"nome":"Camila","id":25},
                    {"nome":"Jully","id":27}]}


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



def atualizar_professor(id_professor, novos_dados):
    professor = professor_id(id_professor)
    professor.update(novos_dados)



def excluir_professor(id_professor):
    professor = professor_id(id_professor)
    dados['professores'].remove(professor)