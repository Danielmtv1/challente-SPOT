import base64
import os
import uuid
from datetime import datetime, timedelta
from typing import List

from azure.storage.blob import BlobSasPermissions, generate_blob_sas
from fastapi import APIRouter

from core.config.azure_conection import blob_service_client, container_name
from core.services.azureconect import test_container
from db.conect_db import get_database_connection
from domain.schemas.message import Message

router = APIRouter()


@router.get("/")
def read_root():
    result = test_container()

    if result is None:
        testcontainer = {}
    else:
        testcontainer = {name: '' for name in result}

    return testcontainer


@router.post("/uploadimage")
async def recibir_mensaje(message: Message):

    date = message.date
    image_base64 = message.image_base64
    camera_id = message.camera_id

    image_data = base64.b64decode(image_base64)

    ruta_carpeta_static = "static"

    if not os.path.exists(ruta_carpeta_static):
        os.makedirs(ruta_carpeta_static)
    filename = str(uuid.uuid4())

    local_file_path = os.path.join(ruta_carpeta_static, filename)
    with open(local_file_path, "wb") as archivo:
        archivo.write(image_data)

    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=filename
    )
    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data)

    sas_token = generate_blob_sas(
        account_name=blob_service_client.account_name,
        container_name=container_name,
        blob_name=filename,
        account_key=blob_service_client.credential.account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(days=1),
    )
    image_url = f"{blob_client.url}?{sas_token}"

    image_base64 = image_url
    with get_database_connection() as connection:
        cursor = connection.cursor()
        query = (
            "INSERT INTO images (date, camera_id, image_base64) "
            "VALUES (%s, %s, %s)"
        )
        values = (date, camera_id, image_base64)
        cursor.execute(query, values)
        connection.commit()

    return {"url_image_azure": image_url}


@router.post("/upload_images")
async def recibir_mensaje_lote(messages: List[Message]):

    with get_database_connection() as connection:
        cursor = connection.cursor()
        query = (
            "INSERT INTO images (date, camera_id, image_base64) "
            "VALUES (%s, %s, %s) ON CONFLICT DO NOTHING"
        )
        unique_images = set()

        for message in messages:
            date = message.date
            camera_id = message.camera_id
            image_base64 = message.image_base64

            if image_base64 in unique_images:
                continue

            unique_images.add(image_base64)
            image_data = base64.b64decode(image_base64)

            ruta_carpeta_static = "static"

            if not os.path.exists(ruta_carpeta_static):
                os.makedirs(ruta_carpeta_static)
            filename = str(uuid.uuid4())

            local_file_path = os.path.join(ruta_carpeta_static, filename)
            with open(local_file_path, "wb") as archivo:
                archivo.write(image_data)

            blob_client = blob_service_client.get_blob_client(
                container=container_name, blob=filename
            )
            with open(local_file_path, "rb") as data:
                blob_client.upload_blob(data)

            sas_token = generate_blob_sas(
                account_name=blob_service_client.account_name,
                container_name=container_name,
                blob_name=filename,
                account_key=blob_service_client.credential.account_key,
                permission=BlobSasPermissions(read=True),
                expiry=datetime.utcnow() + timedelta(days=1),
            )
            image_url = f"{blob_client.url}?{sas_token}"

            image_base64 = image_url
            values = (date, camera_id, image_base64)
            cursor.execute(query, values)

        connection.commit()

    return {"message": "Images uploaded successfully in batch"}


@router.get("/images")
async def get_images():
    with get_database_connection() as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM images"
        cursor.execute(query)
        rows = cursor.fetchall()

    images = []
    for row in rows:
        image = {
            "id": row[0],
            "date": row[1],
            "camera_id": row[2],
            "image_base64": row[3],
        }
        images.append(image)

    return {"images": images}
