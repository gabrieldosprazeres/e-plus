# E-Plus

## Documentação

#

### Objetivo

E-Plus, API criada para gerenciar estudantes.
Conta com registro do estudante, atualização do aluno cadastrado, deleção do cadastro e obtenção de todos os alunos cadastrados.

#

## Link da API hospedada no Heroku

- [E-Plus](https://e-plus-school.herokuapp.com/api).

#

## Instalação

- Primeiro faça o fork deste [repositório](https://github.com/gabrieldosprazeres/e-plus).

- Em seguida faça um git clone para a sua maquina

- Crie um ambiente [virtual em python](https://docs.python.org/pt-br/3/tutorial/venv.html)

```
$ python -m venv venv --upgrade-deps
```

- Entre no ambiente virtual

```
$ source venv/bin/activate
```

- Instale as dependencias necessárias utilizando o `requirements.txt`

```
$ pip install -r requirements.txt
```

- Configure suas variáveis seguindo o `.env.example`

  - Não esqueça de criar o seu banco de dados e adicionar no .env
  - Banco de dados utilizado: PostgreSQL com ORM SQLAlchemy

- Crie as tabelas no banco de dados através do comando

```
$ flask db upgrade
```

- Inicie a aplicação local através do comando

```
$ flask run
```

- A aplicação inicializará na rota http://127.0.0.1:5000/. Você deverá ver algo semelhante ao snippet logo abaixo no seu terminal:

```
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 112-925-941
```

#

## Documentação das rotas e retornos

Você pode acessar a documentação das rotas clicando em [Doc API](https://documenter.getpostman.com/view/18794559/UVXerHjv)

#

## Projeto desenvolvido por:

- [Gabriel dos Prazeres](https://www.linkedin.com/in/gabrieldosprazeres/)
