from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(slots=True)
class Usuario():
   id: int
   nome_usuario: str
   login: str
   senha: str
   cargo: str
   created_at: datetime
   updated_at:  Optional[datetime] | None
   deleted_at: Optional[datetime] | None
   
@dataclass(slots=True)
class CreateUsuarioDTO:
    nome_usuario: str
    login: str
    senha: str
    cargo: str
    
@dataclass(slots=True)
class UsuarioPublic:
    nome_usuario: str
    login: str
    cargo: str

