from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class StatusTarefa(str, Enum):
    PENDENTE = "pendente"
    CONCLUIDA = "concluida"


class TarefaCreate(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=100)
    descricao: str | None = Field(default=None, max_length=500)


class TarefaUpdate(BaseModel):
    titulo: str | None = Field(default=None, min_length=1, max_length=100)
    descricao: str | None = Field(default=None, max_length=500)
    status: StatusTarefa | None = None


class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str | None = None
    status: StatusTarefa
    criada_em: datetime
    atualizada_em: datetime
