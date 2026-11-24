import os
from datetime import datetime
from decimal import Decimal
import sys
from typing import List, Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlmodel import Session, select, text
import uvicorn
import threading
import webbrowser

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

# Identifica se está rodando como .exe (PyInstaller) ou código Python normal
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.abspath(".")

caminho_frontend = os.path.join(base_dir, "frontend")

if os.path.exists(caminho_frontend):
    app.mount("/", StaticFiles(directory=caminho_frontend, html=True), name="frontend")

def abrir_navegador():
    webbrowser.open("http://localhost:8092")

if __name__ == "__main__":
    # Aguarda 1.5 segundo para o servidor subir antes de abrir a aba
    threading.Timer(1.5, abrir_navegador).start()
    uvicorn.run(app, host="0.0.0.0", port=8092, reload=False)
