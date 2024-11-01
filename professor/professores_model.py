from config import db

class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(90))
    observacao = db.Column(db.String(30))

    def __init__(self, nome, idade, materia, observacao):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacao = observacao

    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia,
            "observacao": self.observacao,
        }

class ProfessorNaoEncontrado(Exception):
    pass


def professor_id(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado
    return professor


def professor_existe(id_professor):
    try:
        professor_id(id_professor)
        return True
    except ProfessorNaoEncontrado:
        return False



def adiciona_professor(prof_dados):

    required_keys = ["nome", "idade", "materia", "observacao"]

    # Verifica se todas as chaves estão presentes
    for key in required_keys:
        if key not in prof_dados:
            raise ValueError(f'Chave {key} está faltando nos dados do professor.')

    novo_prof = Professor(
        nome = prof_dados["nome"],
        materia = prof_dados["materia"],
        idade = prof_dados["idade"],
        observacao = prof_dados["observacao"],
    )
    db.session.add(novo_prof)
    db.session.commit()


def lista_professor():
    professores = Professor.query.all()
    return[professor.to_dict() for professor in professores]



def deleta_prof(id_prof):
    professor = Professor.query.get(id_prof)
    if not professor:
        raise ProfessorNaoEncontrado
    db.session.delete(professor)
    db.session.commit()



def atualiza_prof(id_professor, professor):
    db.session.query(Professor).filter(Professor.id == id_professor).update({
        'nome': professor.nome,
        'materia': professor.materia,
        'idade': professor.idade,
        'observacao': professor.observacao
         })
    db.session.commit()


