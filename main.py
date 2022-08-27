from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from routes import user_router, userGetElements, teste_router
import logging


logging.basicConfig(level=logging.INFO)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(userGetElements)
app.include_router(teste_router)

if __name__ == "__main__":
    logging.info("Connect start with uvicorn PORT:8000 : HOST:127.0.0.1.")
    uvicorn.run(app, host='127.0.0.1', port=8000)
