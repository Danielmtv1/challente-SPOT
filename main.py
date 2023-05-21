from db.migrations import run_alembic_autogenerate
import uvicorn
from fastapi import FastAPI

from api.routes import api_router

app = FastAPI()
run_alembic_autogenerate()
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
