from typing import Any
from datetime import datetime

def to_camel_case(string: str) -> str:
    """Converte snake_case para camelCase."""
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def now_utc() -> datetime:
    """Retorna o datetime atual em UTC."""
    return datetime.utcnow()


