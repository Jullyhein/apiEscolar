import pytest
import sys
sys.path.insert(0, "C:/Users/jully/apiEscolar/apiEscolar")
from app import app, db
from turma.turma_models import Turma
from professor.professores_model import Professor

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_create_turma(client):
    with app.app_context():
        # Certifica-se de que um professor existe
        professor = Professor(nome="Professor Teste", idade=40, materia="Matemática", observacao="Experiente")
        db.session.add(professor)
        db.session.commit()

        dados = {"descricao": "Matemática", "professor_id": professor.id, "ativo": True}
        response = client.post('/turma', json=dados)
        assert response.status_code == 201
        assert response.json["mensagem"] == "Turma criada com sucesso!"


def test_update_turma(client):
    with app.app_context():
        # Criação de um professor
        professor = Professor(nome="Professor Teste", idade=40, materia="Matemática", observacao="Experiente")
        db.session.add(professor)
        db.session.commit()

        # Criação de uma turma
        turma = Turma(descricao="Ciências", professor=professor, ativo=True)
        db.session.add(turma)
        db.session.commit()

        # Dados para atualização, incluindo o ID da turma
        novos_dados = {
            "turma_id": turma.id,  # Adiciona o ID da turma aqui
            "descricao": "Ciências Atualizado",
            "professor_id": professor.id,
            "ativo": False
        }

        # Fazendo a requisição PUT para atualizar a turma
        response = client.put('/turma', json=novos_dados)
        
        # Verificando o status e a mensagem de resposta
        assert response.status_code == 200
        assert response.json["mensagem"] == "Turma atualizada com sucesso!"



def test_delete_turma(client):
    with app.app_context():
        # Cria um professor e uma turma de teste
        professor = Professor(nome="Professor Teste", idade=40, materia="Matemática", observacao="Experiente")
        db.session.add(professor)
        db.session.commit()

        turma = Turma(descricao="História", professor=professor, ativo=True)
        db.session.add(turma)
        db.session.commit()

        response = client.delete(f'/turma/{turma.id}')
        assert response.status_code == 200
        assert response.json["mensagem"] == "Turma deletada"
