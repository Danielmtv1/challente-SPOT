import subprocess
import time
import psycopg2


def wait_for_postgres():
    while True:
        try:
            psycopg2.connect("postgresql://postgres:postgres@postgres"
                             ":5432/postgres"
                             )
            break
        except psycopg2.OperationalError:
            print("Waiting for PostgreSQL...")
            time.sleep(1)


def run_alembic_autogenerate():
    wait_for_postgres()

    subprocess.run(
        ["alembic", "-c", "alembic.ini", "revision",
         "--autogenerate", "-m", ""])
    subprocess.run(["alembic", "-c", "alembic.ini", "upgrade", "head"])
