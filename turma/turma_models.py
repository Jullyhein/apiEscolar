from flask import Flask
from config import db
from professor.professores_model import Professor

class Turma(db.Model):
    __tablename__= 'turma'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id', ondelete="SET NULL"), nullable=True)
    professor_id = db.relationship('Professor', backref='turmas')
    ativo = db.Column(db.Boolean, default=True)
    

    def __init__(self, descricao, professor, ativo):
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo


    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "professor": self.professor.nome if self.professor else "Sem Professor",
            "ativo": self.ativo
        }


class DadoNaoEncontrado(Exception):
    pass


def turma_id(id_turma):
    lista_turma = Turma.query.get(id_turma)
    if not lista_turma:
        raise DadoNaoEncontrado
    return Turma.to_dict()


def adicionar_turma(turma_data):
    professor_id = turma_data.get('professor')
    prof = Professor.query.get(professor_id)
    if not prof:
        raise ValueError(f'Professor com id {professor_id} não encontrado')
    # Cria a nova turma com a instância do professor associada
    nova_turma = Turma(
        descricao=turma_data['descricao'],
        professor=prof,
        ativo=turma_data["ativo"]  # Atribui a instância de Professor, não o ID
    )
    db.session.add(nova_turma)
    db.session.commit()


def lista_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]


def atualiza_tudo(id_turma, novos_dados):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise DadoNaoEncontrado
    turma.descricao = novos_dados["descricao"]
    turma.professor = novos_dados["professor"]
    turma.ativo = novos_dados["ativo"]
    db.session.commit()


def delete_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise DadoNaoEncontrado
    db.session.delete(turma)
    db.session.commit()
