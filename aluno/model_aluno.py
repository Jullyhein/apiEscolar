from config import db
from datetime import datetime
from turma.turma_models import Turma

from config import db

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id', ondelete="SET NULL"), nullable=True)
    turma = db.relationship('Turma', backref='alunos')
    data_nascimento = db.Column(db.Date)
    nota_semestre_1 = db.Column(db.Integer)
    nota_semestre_2 = db.Column(db.Integer)
    media_final = db.Column(db.Integer)

    def __init__(self, nome, turma_id, data_nascimento, nota_semestre_1, nota_semestre_2):
        self.nome = nome
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_semestre_1 = nota_semestre_1
        self.nota_semestre_2 = nota_semestre_2
        self.media_final = self.calcula_media()

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "turma_id": self.turma.descricao if self.turma else "Sem Turma",
            "data_nascimento": self.data_nascimento.strftime('%Y-%m-%d') if self.data_nascimento else None,
            "nota_semestre_1": self.nota_semestre_1,
            "nota_semestre_2": self.nota_semestre_2,
            "media_final": self.media_final
        }
    
    def calcula_media(self):
        return (float(self.nota_semestre_1) + float(self.nota_semestre_2)) / 2



class AlunoNaoEncontrado(Exception):
    pass


def aluno_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno.to_dict()

def adicionar_aluno(aluno_data):
    
    novo_aluno = Aluno(
        nome=aluno_data['nome'],
        turma_id=aluno_data['turma_id'],
        data_nascimento=datetime.strptime(aluno_data['data_nascimento'], '%Y-%m-%d'),
        nota_semestre_1=aluno_data['nota_semestre_1'],
        nota_semestre_2=aluno_data['nota_semestre_2']
    )

    db.session.add(novo_aluno)
    db.session.commit()

    return novo_aluno



def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]



def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    aluno.nome = novos_dados["nome"]
    aluno.turma_id = novos_dados["turma_id"]
    aluno.data_nascimento = datetime.strptime(novos_dados["data_nascimento"], '%Y-%m-%d')
    aluno.nota_semestre_1 = novos_dados["nota_semestre_1"]
    aluno.nota_semestre_2 = novos_dados["nota_semestre_2"]
    aluno.media_final = novos_dados["media_final"]

    db.session.commit()


def deletar_aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()