import uvicorn
from fastapi import FastAPI

from api.routes import api_router
from core.services.azureconect import test_container
from db.migrations import run_alembic_autogenerate

run_alembic_autogenerate()

app = FastAPI()

app.include_router(api_router)


test_container()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
