from fastapi import APIRouter
from core.services.azureconect import test_container

router = APIRouter()


@router.get("/")
def read_root():
    result = test_container()

    if result is None:
        testcontainer = {}
    else:
        testcontainer = {name: '' for name in result}

    return testcontainer
