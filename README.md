# mentalhealth-backend

## Usefull links

- https://www.docker.com/
- https://fastapi.tiangolo.com/
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/

## Running app locally

### With docker

#### First run

Create .env file with following content

```
DATABASE_CONNECTOR = mysql+pymysql
DATABASE_USER = user
DATABASE_PASSWORD = password
DATABASE_ADDRESS = db
DATABASE_DB = mentalhealth
DATABASE_URL = mysql+pymysql://user:password@db:3306/mentalhealth
SUPERUSER_EMAIL = admin@mentalhealth.pl
SUPERUSER_PASSWORD = Password
```

```console
docker-compose build # this command create web and database containers
docker-compose up # this command runs our app
```

Then in separate console run this commands

```console
docker-compose run web alembic upgrade head # this command execute all migrations on connected database
docker-compose run web python app/initial_data.py # this command create initial super user with email and password set in .env
```

#### Regular running app

```console
docker-compose up # this command runs our app
```

### With windows

Will be added if needed

## Creating migrations

!!Execute migration only on local database
Create file with table structure in models folder
Remember to import created model to

- app/models/**init**.py
- app/db/base.py

run this commands

```console
docker-compose run web alembic revision --autogenerate -m "migration message" # This command will create migration file in alembic/versions
docker-compose run web alembic upgrade head # this command will make changes from migration on database
```

Check if migration file was created correctly
Check if your local database was correctly updated

## Creating new endpoints

<pre>
Start from creating new schemas
    app/schemas/{resource_name}.py(You can take a look on user schema and create simmilar with correct fields)
Create new crud class
    app/crud/crud_{model_name}.py(You can take a look on crud_user.py to get familliar how this file should look like)
Create new endpoint
    app/api/api_v1/endpoints/{resource_name}.py (you can take a look on users.py to get familliar how routers and endpoints are created)
Register endoint
    app/api/api_v1/api.py (Here you need to register created router)
</pre>

## Running linters

```console
pip install black isort flake8 bandit
black app # this command lint code
isort app # this command sort imports in correct way
flake8 app # this command check if app didn't have any pep8 violation
bandit app # this command check code complexity
```

## Project structure

<pre>
.
├── alembic (alembic is responsible for for creating database migrations, most likely there will be no need for any changes)
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── XXX_first_migration.py (This in automatically create migration file)
├── alembic.ini (File with alembic configuration)
├── app (This is base project file which contain code)
│   ├── api (This folder contains all api endpoints separated by version)
│   │   ├── api_v1 (Api endoints version one)
│   │   │   ├── api.py (There we register all routers)
│   │   │   ├── endpoints (Here we store all routers separated by category)
│   │   │   │   ├── __init__.py
│   │   │   │   ├── login.py (Here is router responsible for authentication)
│   │   │   │   └── users.py (Here is router responsible for managing users)
│   │   │   └── __init__.py
│   │   ├── deps.py (There we create authorization rules)
│   │   └── __init__.py
│   ├── backend_pre_start.py
│   ├── core (There we store important files)
│   │   ├── config.py (Here is application config)
│   │   ├── __init__.py
│   │   └── security.py (Here are security function: verify_password, get_password_hash, create_access_token)
│   ├── crud (Here are Create Retrieve Update Delete functions)
│   │   ├── base.py (Here is base class for CRUD operations)
│   │   ├── crud_user.py (Here is class with CRUD operations for user)
│   │   └── __init__.py
│   ├── db (This folder contains things responsible for connection with db)
│   │   ├── base_class.py (Contains base class, most likely there will be no need for any changes)
│   │   ├── base.py (Here all models needs to be imported)
│   │   ├── init_db.py (Create first super user)
│   │   ├── __init__.py
│   │   └── session.py (Creates session with database)
│   ├── initial_data.py (Nothing important)
│   ├── __init__.py
│   ├── main.py (Fastapi main file)
│   ├── models (Here we define all database models from which migrations are created)
│   │   ├── __init__.py
│   │   └── user.py (Here is defined user model(more filds will be added in future like: role, discord_id))
│   ├── schemas (Here we store all schemas used for communication between frontend and backend)
│   │   ├── __init__.py
│   │   ├── msg.py (Class with message schema)
│   │   ├── token.py (Schemas used for authentication)
│   │   └── user.py (Schemas used for user creation, update, delete)
│   ├── tests (Here are code testst)
│   │   ├── api (Tests for api endpoint)
│   │   │   ├── api_v1 (tests for api version 1)
│   │   │   │   ├── __init__.py
│   │   │   │   ├── test_login.py (Login tests)
│   │   │   │   └── test_users.py (User tests)
│   │   │   └── __init__.py
│   │   ├── conftest.py
│   │   ├── crud (Crud tests)
│   │   │   ├── __init__.py
│   │   │   └── test_user.py (User crud tests)
│   │   ├── __init__.py
│   │   └── utils (utilities)
│   │       ├── __init__.py
│   │       ├── user.py (user utilities)
│   │       └── utils.py (general utilities)
│   └── tests_pre_start.py
├── docker-compose.yml (Docker-compose file(More informations soon))
├── Dockerfile (Docker file(More informations soon))
├── pyproject.toml (poetry equivalent of requirements.txt)
└── README.md (You are here)
</pre>
