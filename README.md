# Calorie Tracker Backend

Calorie Tracker Backend is a simple REST service which allows CRUD methods to operate on the data in our database.
It provides a set of APIs for:

- User management
- Product management
- Meal management
- Diary management

# Hutan Mihai-Alexandru -- Contact

- Personal email: hutanmihai29@gmail.com
- LinkedIn: https://www.linkedin.com/in/hutanmihai/
- Personal GitHub: https://github.com/hutanmihai

## Development

### Technology Stack

#### Runtime environment

- Docker (https://docs.docker.com/get-started/overview/)
- docker-compose for containers management and orchestration (https://docs.docker.com/compose/)
- Python 3.11

##### Additional information

- [Python 3.11 changelog](https://docs.python.org/3/whatsnew/3.11.html)
- [Docker vs Virtual Machine](https://geekflare.com/docker-vs-virtual-machine/)

#### Third-party dependency management and build tool

- Poetry - dependency management and packaging tool (https://python-poetry.org/)
- Poe - task runner for poetry (https://github.com/nat-n/poethepoet)

#### Web/API framework

- REST API (https://docs.microsoft.com/uk-ua/azure/architecture/best-practices/api-design)
- FastAPI as API framework (https://fastapi.tiangolo.com/)
- OpenAPI for API documentation (https://swagger.io/specification/). OpenAPI specification will be autogenerated by
  FastAPI (https://fastapi.tiangolo.com/features/)
- Result: Swagger for created (auto-generated) API is available and exposed

##### Additional information

- [HTTP Protocol Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

#### RDBMS

- Postgres 15
- SQLAlchemy ORM (https://www.sqlalchemy.org/)
- Alembic for schema and data migrations (https://alembic.sqlalchemy.org/en/latest/)

### Testing

- pytest test runner (https://docs.pytest.org/en/7.2.x/)

### Design Principles (by Uncle Bob)

- [Lesson 1](https://www.youtube.com/watch?v=7EmboKQH8lM&t=582s)
- [Lesson 2](https://www.youtube.com/watch?v=2a_ytyt9sf8&t=1s)
- [Lesson 3](https://www.youtube.com/watch?v=Qjywrq2gM8o)
- [Lesson 4](https://www.youtube.com/watch?v=58jGpV2Cg50&t=4881s)

### Development methodology

### Team, responsibility and roles

| Name           | Email                                | Responsibility | Scrum Role |
|----------------|--------------------------------------|----------------|------------|
| Hutan Mihai    | mihai-alexandru.hutan@s.unibuc.ro    | Tech Lead      | Dev        |
| Besliu Radu    | radu-stefan.besliu@s.unibuc.ro       | PM             | SM, PO     |
| Florea Madalin | madalin-alexandru.florea@s.unibuc.ro | Team Lead      | Dev        |

### How to start working on a feature

All new features must be developed in a separate branch. Use the following branch name
template: `[feature|bugfix]<ticket-id>-short-description-of-changes` e.g.: in case if I'm working on issue 34, and I'm
going to add `/users` endpoint in scope of this ticket, I'm going to create a branch called `feature-34-users-endpoint`.

### Local dev env

Pre-requisites:

- Python 3.11
- Docker
- docker-compose
- poetry

#### Build the app locally

```shell
poetry install
```

#### Run the app locally

```shell
poetry run uvicorn updateservice.app:app --host 0.0.0.0 --port 8080
```

Then open http://127.0.0.1:8080/docs in your browser

#### Run tests locally

In order to run the test you must enter the following command in the terminal. The arguments are optional and generate
coverage files of the type specified (html/xml).

```shell
poe test [--cov-report] <type>
```

If you are working on the project and run tests, before commit make sure you run the following command which deletes all
artifacts:

```shell
poe clean
```

#### Create DB migration

```shell
poe create_migration
```

#### Upgrade DB schema

```shell
poe upgrade_schema
```

#### Downgrade DB schema

```shell
poe downgrade_schema
```
