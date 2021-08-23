import os
import unittest
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.app.example import router as example_router

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "*"
]

app = FastAPI(
    title='FARM BACKEND',
    docs_url='/'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(example_router, prefix="", tags=["example"])

app.mount("/static", StaticFiles(directory="static"), name="static")
