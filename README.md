# Kanvas 📔
Kanvas é uma sistema de gerenciamento para plataformas de ensino, com o intuito de auxiliar e agilizar as tarefas mais comuns em um ambiente acadêmico.

Ao utilizar esta API, deve ser possível criar, ler e atualistudieszar informações sobre usuários, cursos, atividades e submissões.

## Como instalar e rodar? 🚀
Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte:
```
# Aqui é como devemos clonar o repositório
git clone git@github.com:w4nd0/kanvas.git
```
Depois que terminar de baixar, é necessário entrar na pasta, criar um ambiente virtual e entrar nele:
```
# Entrar na pasta
cd kanvas

# Criar um ambiente virtual
python3 -m venv venv

# Entrar no ambiente virtual
source venv/bin/activate
```

Então, para instalar as dependências, basta:

`pip install -r requirements.txt`

Depois de ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:

`./manage.py migrate`

Então, para rodar, basta digitar o seguinte, no terminal:

`./manage.py runserver`

E o sistema estará rodando em http://127.0.0.1:8000/

## Utilização 🖥️
Para utilizar este sistema, é necessário utilizar um API Client, como o [Insomnia](https://insomnia.rest/download)

### Rotas 🔄

**POST /api/accounts/**

Rota para criar uma conta, de acordo com a requisição:
- Estudante (is_superuser `false` e is_staff `false`)
- Facilitador (is_superuser `false` e is_staff `true`)
- Instrutor (is_superuser `true` e is_staff `true`)

Request:

```
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
```

`RESPONSE STATUS -> HTTP 201 (create)`

Response:

```
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
```

**POST /api/login/**

Rota para logar na aplicação, retorna o token para acessar as rotas autentificadas.

Request:

```
{
    "username": "student",
    "password": "1234"
}
```

`RESPONSE STATUS -> HTTP 200 (ok)`

Response:

```
{
    "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}   
```

**POST /api/courses/**  🔑(somente instrutor)

Rota para criar um curso.

Request:

```
{
    "name": "Node"
}
```

`RESPONSE STATUS -> HTTP 201 (create)`

Response:

```
{
    "id": 1,
    "name": "Node",
    "users": []
}   
```

**PUT /api/courses/\<int:course_id>/**  
🔑(somente instrutor)

Rota para atualizar um curso, a partir do seu id

Request:

```
{
    "name": "JavaScript"
}
```

`RESPONSE STATUS -> HTTP 200 (ok)`

Response:

```
{
    "id": 1,
    "name": "JavaScript",
    "users": []
}   
```

**PUT /api/courses/\<int:course_id>/registrations/**\
🔑(somente instrutor)

Rota para atualizar a lista de estudantes matriculados em um curso.\
*Somente estudantes são aceitos.

Request:

```
{
    "user_ids": [3, 4, 5]
}      
```

`RESPONSE STATUS -> HTTP 200 (ok)`

Response:

```
{
    "id": 1,
    "name": "Node",
    "users": [
        {
        "id": 3,
        "username": "student1"
        },
        {
        "id": 4,
        "username": "student2"
        },
        {
        "id": 5,
        "username": "student3"
        }
    ]
}   
```

**GET /api/courses/**  

Rota para listar todos os cursos com seus respectivos alunos.

`RESPONSE STATUS -> HTTP 200 (ok)`

Response:

```
[
    {
        "id": 1,
        "name": "Node",
        "users": [
            {
                "id": 3,
                "username": "student1"
            }
        ]
    },
    {
        "id": 2,
        "name": "Django",
        "users": []
    },
    {
        "id": 3,
        "name": "React",
        "users": []
    }
]
```

**GET /api/courses/\<int:course_id>/**  

Rota para listar um curso específico com seus respectivos alunos.

`RESPONSE STATUS -> HTTP 200 (ok)`

Response:

```
{
    "id": 1,
    "name": "Node",
    "users": [
        {
            "id": 3,
            "username": "student1"
        }
    ]
}
```

**DELETE /api/courses/\<int:course_id>/**\
🔑(somente instrutor)

Rota para deletar um curso.

`RESPONSE STATUS -> HTTP 204 (no content)`


**POST /api/activities/**\
 🔑(somente instrutor ou facilitador)

Rota para criar uma atividade.

Request:

```
{
    "title": "Kenzie Pet",
    "points": 10
}
```

`RESPONSE STATUS -> HTTP 201 (create)`

Response:

```
{
    "id": 1,
    "title": "Kenzie Pet",
    "points": 10,
    "submissions": []
} 
```

**GET /api/activities/**\
🔑(somente instrutor ou facilitador)

Rota para listar as atividades.

`RESPONSE STATUS -> HTTP 200 (ok)`

Response:

```
[
    {
        "id": 1,
        "title": "Kenzie Pet",
        "points": 10,
        "submissions": [
            {
                "id": 1,
                "grade": 10,
                "repo": "http://gitlab.com/kenzie_pet",
                "user_id": 3,
                "activity_id": 1
            }
        ]
    },
    {
        "id": 2,
        "title": "Kanvas",
        "points": 10,
        "submissions": [
            {
                "id": 2,
                "grade": 8,
                "repo": "http://gitlab.com/kanvas",
                "user_id": 4,
                "activity_id": 2
            }
        ]
    },
    ...
]
```

**PUT /api/activities/\<int:activity_id>/**\
🔑(somente instrutor ou facilitador)

Rota para atualizar uma atividade.\
*A atividade não pode ter submissões.

Request:

```
{
    "title": "Kapstone",
    "points": 100
}
```

`RESPONSE STATUS -> HTTP 200 (ok)`

Response:

```
{
    "id": 1,
    "title": "Kapstone",
    "points": 100,
    "submissions": []
} 
```

**POST /api/activities/\<int:activity_id>/submissions/**\
🔑(somente estudante)

Rota para um estudante enviar uma submissão para uma atividade.

Request:

```
{
    "repo": "http://gitlab.com/kenzie_pet"
}
```

`RESPONSE STATUS -> HTTP 201 (create)`

Response:

```
{
    "id": 7,
    "grade": null,
    "repo": "http://gitlab.com/kenzie_pet",
    "user_id": 3,
    "activity_id": 1
} 
```

**PUT /api/submissions/\<int:submission_id>/**\
🔑(somente instrutor ou facilitador)

Rota para lançar a nota para uma submissão de um estudante.

Request:

```
{
    "grade": 10
}
```

`RESPONSE STATUS -> HTTP 200 (ok)`

Response:

```
{
    "id": 3,
    "grade": 10,
    "repo": "http://gitlab.com/kenzie_pet",
    "user_id": 3,
    "activity_id": 1
}
```

**GET /api/submissions/**\
🔑(somente usuários autentificados)

Rota para listar as submissões.\
*Se o usuário for um estudante, retorna somente suas submissões.


`RESPONSE STATUS -> HTTP 200 (ok)`

Response:

```
// Header -> Authorization: Token <token-do-estudante>
[
    {
        "id": 1,
        "title": "Kenzie Pet",
        "points": 10,
        "submissions": [
            {
                "id": 1,
                "grade": 10,
                "repo": "http://gitlab.com/kenzie_pet",
                "user_id": 3,
                "activity_id": 1
            }
        ]
    },
    {
        "id": 2,
        "title": "Kanvas",
        "points": 10,
        "submissions": [
            {
                "id": 2,
                "grade": 8,
                "repo": "http://gitlab.com/kanvas",
                "user_id": 4,
                "activity_id": 2
            }
        ]
    },
    ...
]
```

```
// Header -> Authorization: Token <token-do-facilitador ou token-do-instrutor>
[
    {
        "id": 1,
        "grade": 10,
        "repo": "http://gitlab.com/kenzie_pet",
        "user_id": 3,
        "activity_id": 1
    },
    {
        "id": 2,
        "grade": 8,
        "repo": "http://gitlab.com/kanvas",
        "user_id": 4,
        "activity_id": 2
    },
    {
        "id": 3,
        "grade": 4,
        "repo": "http://gitlab.com/kmdb",
        "user_id": 5,
        "activity_id": 3
    },
    {
        "id": 4,
        "grade": null,
        "repo": "http://gitlab.com/kmdb2",
        "user_id": 5,
        "activity_id": 3
    }
]  
```

## Tecnologias utilizadas 📱
* Django
* Django Rest Framework
* SQLite

<hr>

**Licence**
MIT
