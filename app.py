import os 
from config import app
from professor.professores_routes import professor
from aluno.aluno_route import aluno

app.register_blueprint(professor)
app.register_blueprint(aluno)

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])