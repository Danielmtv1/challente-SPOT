from contextlib import contextmanager
import psycopg2


@contextmanager
def get_database_connection():
    connection = psycopg2.connect(
        "postgresql://postgres:postgres@postgres:5432/postgres")
    try:
        yield connection
    finally:
        connection.close()
