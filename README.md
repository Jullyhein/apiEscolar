# Documentação da API Escolar

## Visão Geral

A API Escolar permite o gerenciamento de alunos, turmas e professores. Através de endpoints RESTful, é possível realizar operações de CRUD (Criar, Ler, Atualizar e Deletar) para cada uma dessas entidades.

### Base URL

http://127.0.0.1:8000


## Estrutura das Entidades

### Professor

- **id**(int): Identificador único do professor (gerado automaticamente).
- **nome**(str): Nome do professor.
- **idade**(id): Idade do professor.
- **materia**(str): Matéria que o professor leciona.
- **observacao**(str): Observações adicionais sobre o professor.

### Turma

- **id**(int): Identificador único da turma (gerado automaticamente).
- **nome**(str): Nome da turma.
- **professor_id**(int): Identificador do professor responsável pela turma.

### Aluno

- **id**(int): Identificador único do aluno (gerado automaticamente).
- **nome**(str): Nome do aluno.
- **idade**(int): Idade do aluno.
- **turma_id**(int): Identificador da turma à qual o aluno pertence.

## Endpoints

### 1. Professores

#### 1.1 Listar Professores

- **GET** `/professores`

Retorna uma lista de todos os professores.

#### 1.2 Criar Professor

- **POST** `/professores`
  
**Body** (JSON):
```json
{
  "nome": "Nome do Professor",
  "idade": 40,
  "materia": "Matemática",
  "observacao": "Observação sobre o professor."
}

```

#### 1.3 Atualizar Professor

- **PUT** `/professores/<id>`

**Body** (JSON):
```json
{
  "nome": "Novo Nome",
  "idade": 41,
  "materia": "Física",
  "observacao": "Nova observação."
}
```

#### 1.4 Deletar Professor

- **DELETE** `/professores/<id>`
  
Deleta um professor com o ID especificado.

### 2. Turmas

#### 2.1 Listar Turmas

- **GET** `/turmas`
  
Retorna uma lista de todas as turmas.

#### 2.2 Criar Turma

- **POST** `/turmas`
  
**Body** (JSON):
  ```json
  {
  "nome": "Turma A",
  "professor_id": 1
}
```

#### 2.3 Atualizar Turma

- **PUT** `/turmas/<id>`
  
**Body** (JSON):

```json
{
  "nome": "Turma B",
  "professor_id": 2
}
```

#### 2.4 Deletar Turma

- **DELETE** `/turmas/<id>`
Deleta uma turma com o ID especificado.

### 3. Alunos

#### 3.1 Listar Alunos

- **GET** `/alunos`
Retorna uma lista de todos os alunos.

### 3.2 Criar Aluno

- **POST** `/alunos`
- 
**Body** (JSON):

```json
{
  "nome": "Nome do Aluno",
  "idade": 12,
  "turma_id": 1
}
```

#### 3.3 Atualizar Aluno

- **PUT** `/alunos/<id>`

**Body** (JSON):

```json
{
  "nome": "Novo Nome",
  "idade": 13,
  "turma_id": 2
}
```

#### 3.4 Deletar Aluno

- **DELETE** `/alunos/<id>`
Deleta um aluno com o ID especificado.

**Respostas**
As respostas da API são retornadas no formato JSON. Em caso de sucesso, os dados solicitados serão retornados com um status HTTP 200. Em caso de erro, um status apropriado (como 400 ou 404) será retornado com uma mensagem de erro.

Exemplo de Resposta de Erro
```json
{
  "erro": "Aluno não encontrado."
}
```

**Conclusão**

Essa documentação fornece uma visão geral da API Escolar, suas entidades e como interagir com os endpoints disponíveis. Para mais detalhes sobre a implementação, sinta-se à vontade para consultar o código-fonte do projeto.
