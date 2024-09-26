

class Professor():
    def __init__(self, id:int, nome:str, idade:int, materia:str, observacoes:str ):
        self.id=id
        self.nome=nome
        self.idade=idade
        self.materia=materia
        self.observacoes=observacoes

    '''A linha que você mencionou define o método especial __repr__ dentro da classe Professor. 
    Este método é utilizado para fornecer uma representação textual oficial e detalhada 
    de um objeto da classe, que é útil principalmente para fins de depuração e desenvolvimento.'''

    def __repr__(self):
        return f"Professor(id={self.id}, nome='{self.nome}', idade={self.idade}, matéria='{self.materia}')"


class Turma():
    def __init__(self, id:int, descricao:str, professor:Professor, ativo:bool=True) -> None:
        self.id=id
        self.descricao=descricao
        self.professor=professor
        self.ativo=ativo


    def __repr__(self):
        return f"Turma(id={self.id}, descricao='{self.descricao}', professor={self.professor.nome}, ativo={self.ativo})"
    



class Aluno():
    def __init__(self, id:int, nome:str, idade:int, turma:Turma, data_nascimento:str, nota_primeiro_semestre:float, nota_segundo_semestre:float):
        self.id=id
        self.nome=nome
        self.idade=idade
        self.turma=turma
        self.data_nascimento=data_nascimento
        self.nota_primeiro_semestre=nota_primeiro_semestre
        self.nota_segundo_semestre=nota_segundo_semestre
        self.media_final = self.calcular_media()

    def __repr__(self):
        return (f"Aluno(id={self.id}, nome='{self.nome}', idade={self.idade}, turma={self.turma.descricao}")
              

    def calcular_media(self):
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2
    
    def __repr__(self):
        return (f"Aluno (id={self.id}, nome'{self.nome}', idade={self.idade}, turma={self.turma.descricao}, "
                f"media_final={self.media_final:.2f})")


#professor1 = Professor(id=1, nome="Maria Silva", idade=40, materia="Matemática", observacoes="Especialista em álgebra")
#turma1 = Turma(id=1, descricao="Turma 5A", professor=professor1, ativo=True)
#aluno1 = Aluno(id=1, nome="João Santos", idade=16, turma=turma1, data_nascimento="2008-05-10", 
 #              nota_primeiro_semestre=8.5, nota_segundo_semestre=7.0)

#print(professor1)
#print(turma1)
#print(aluno1)