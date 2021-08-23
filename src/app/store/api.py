from fastapi import APIRouter, HTTPException, Body, UploadFile, File
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import numpy as np
from .controller import example_controller

router = APIRouter()

db = {'sup': 'nm'}

class KeyJSON(BaseModel):
    key: str

class KeyValueJSON(KeyJSON):
    value: str

@router.get('/hello')
async def basic():
    return { 'message': '!hello from the backend!' }

@router.get('/get', response_model = KeyValueJSON)
async def get_key(key: str):
    if key not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return { 'key': key, 'value': db[key] }



@router.post('/set', response_model = KeyValueJSON)
async def set_key(body: KeyValueJSON):
    key, value = body.key, body.value
    db[key] = value
    return { 'key': key, 'value': db[key] }


@router.post('/delete', response_model = KeyJSON)
async def delete_key(body: KeyJSON):
    key = body.key
    del db[key]
    return { 'key': key }
