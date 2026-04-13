from __future__ import annotations

from fastapi import FastAPI, HTTPException, status

from app.models import Tarefa, TarefaCreate, TarefaUpdate
from app.storage import (
    atualizar_tarefa,
    criar_tarefa,
    deletar_tarefa,
    listar_tarefas,
    obter_tarefa,
)

app = FastAPI(title="API de Tarefas", version="1.0.0")


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tarefas", response_model=Tarefa, status_code=status.HTTP_201_CREATED)
def criar_tarefa_endpoint(payload: TarefaCreate) -> Tarefa:
    return criar_tarefa(payload.titulo, payload.descricao)


@app.get("/tarefas", response_model=list[Tarefa])
def listar_tarefas_endpoint() -> list[Tarefa]:
    return listar_tarefas()


@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
def obter_tarefa_endpoint(tarefa_id: int) -> Tarefa:
    tarefa = obter_tarefa(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa_endpoint(tarefa_id: int, payload: TarefaUpdate) -> Tarefa:
    tarefa_atualizada = atualizar_tarefa(tarefa_id, **payload.model_dump(exclude_unset=True))
    if tarefa_atualizada is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa_atualizada


@app.delete("/tarefas/{tarefa_id}", status_code=status.HTTP_200_OK)
def deletar_tarefa_endpoint(tarefa_id: int) -> dict[str, str]:
    removida = deletar_tarefa(tarefa_id)
    if not removida:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"mensagem": "Tarefa deletada com sucesso"}