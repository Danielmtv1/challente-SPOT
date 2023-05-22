import uvicorn
from fastapi import FastAPI

from api.routes import api_router
from db.migrations import run_alembic_autogenerate

run_alembic_autogenerate()

app = FastAPI(
        title="Challenge Spot",
        description="SPOT Challenge is an API that "
        "receives a JSON with three data points: "
        "the date, the image in Base64, and the camera ID. "
        "It decodes the Base64 image and stores it in Azure storage, "
        "then saves the URL in the database along with the date and camera ID",
        version="0.0.1"
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
