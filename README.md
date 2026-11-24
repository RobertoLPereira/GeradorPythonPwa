# GeradorPythonPwa
Cria Crud de aplicação PWA com Backend em Python 3.12

# Inicializar o ambiente
pythom -m venv .venv
.venv\Scripts\Activate.ps1

# Instalação de bibliotecas básicas
pip install pydantic-settings pymysql fastapi dotenv sqlmodel uvicorn pyinstaller httpx httpcore requests

# Criar o arquivos com as bibliotecas importadas
 pip freeze > requirements.txt.

# configurar o github Actions
mkdir -p .github/workflows
