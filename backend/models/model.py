import uuid
from datetime import datetime, timezone, timedelta

def gerar_uuid() -> str:
    return str(uuid.uuid4())

def agora_iso() -> str:
    fuso_br = timezone(timedelta(hours=-3))
    return datetime.now(fuso_br).strftime('%Y-%m-%dT%H:%M:%S%z')[:-2] + ':00'

