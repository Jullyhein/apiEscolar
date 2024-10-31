import os 
from config import app, db
from professor.professores_routes import professor
from aluno.aluno_route import aluno
from turma.turma_route import turma_blueprint

app.register_blueprint(professor)
app.register_blueprint(aluno)
app.register_blueprint(turma_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])