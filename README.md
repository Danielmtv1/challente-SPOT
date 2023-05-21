# Challenge SPOT
## "Handling JSON messages with Base64 images"

![N|Solid](https://blog.pronus.io/images/python/fastapi_logo.svg)

"SPOT Challenge is an API that receives a JSON with three data points: the date, the image in Base64, and the camera ID. It decodes the Base64 image and stores it in Azure storage, then saves the URL in the database along with the date and camera ID.".


## Features

- Receives a JSON containing three data points: the date, the Base64 image, and the camera ID.
- Decodes the Base64 image.
- Stores the decoded image in Azure storage.
- Saves the URL of the stored image in a database.
- Also saves the date and camera ID in the database alongside the image URL.

## Tech

Challenge SPOT uses a number of open source projects to work properly:

- [Alembic] - Database migration tool for SQLAlchemy.

- [FastAPI] - A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

- [Gunicorn] - A Python WSGI HTTP Server for UNIX.

- [Azure-storage-blob] - Microsoft Azure Storage Library for Python.

- [SQLAlchemy] - The Python SQL Toolkit and Object-Relational Mapper.

- [Uvicorn] - The lightning-fast ASGI server.

- [Psycopg2-binary] - The most popular PostgreSQL adapter for Python.

- [Pydantic] - Data parsing using Python type annotations.

- [Python]: A powerful programming language used for a wide range of applications.

- [Poetry]: A dependency management and packaging tool for Python projects.

## Installation

To install, you need to clone the repository. Once the repository has been cloned, make sure you have Docker installed on your system. With Docker installed, you can simply run the command 'make api' to start the process."

```sh
make api
```
## Development

## License

MIT

**Free Software**

[//]: # ()
[Alembic]:<https://alembic.sqlalchemy.org/en/latest/>
[FastAPI]:<https://fastapi.tiangolo.com/>
[Gunicorn]:<https://gunicorn.org/>
[Azure-storage-blob]:<https://azuresdkdocs.blob.core.windows.net/$web/javascript/azure-storage-blob/12.0.0-preview.5/index.html#:~:text=Azure%20Blob%20storage%20is%20Microsoft's,as%20text%20or%20binary%20data.>
[SQLAlchemy]:<https://www.sqlalchemy.org/>
[Uvicorn]:<https://www.uvicorn.org/>

[Psycopg2-binary]:<https://pypi.org/project/psycopg2-binary/>

[Pydantic]:<https://docs.pydantic.dev/latest/>
[Python]:<https://www.python.org/>
[Poetry]:<https://python-poetry.org/>
  