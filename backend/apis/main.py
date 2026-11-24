import os
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlmodel import Session, select, text
import uvicorn

from backend.apis.database_unificado import get_session, inicializar_bancos, mysql_online

from backend.models.model import (agora_iso)
from backend.gerar_todos_model import gerador_router
from backend.gerador_crud_routes import gerador_crud_router

app = FastAPI(
    title="API Central do Gerador - Model e Crud Python com PWA",
    version="4.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False, # Importante: com allow_origins=["*"], allow_credentials deve ser False no padrão Fetch!
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    inicializar_bancos()

app.include_router(gerador_router)
app.include_router(gerador_crud_router)

caminho_frontend = os.path.join("frontend")
if os.path.exists(caminho_frontend):
    app.mount("/", StaticFiles(directory=caminho_frontend, html=True), name="frontend")
if __name__ == "__main__":
    # Inicia o servidor local na porta 8092
    uvicorn.run("backend.apis.main:app", host="0.0.0.0", port=8092, reload=True)
#python -m uvicorn backend.apis.main