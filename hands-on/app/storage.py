from __future__ import annotations

from datetime import datetime

from app.models import StatusTarefa, Tarefa

tarefas: dict[int, Tarefa] = {}
proximo_id = 1


def criar_tarefa(titulo: str, descricao: str | None = None) -> Tarefa:
    global proximo_id

    agora = datetime.now()
    tarefa = Tarefa(
        id=proximo_id,
        titulo=titulo,
        descricao=descricao,
        status=StatusTarefa.PENDENTE,
        criada_em=agora,
        atualizada_em=agora,
    )
    tarefas[tarefa.id] = tarefa
    proximo_id += 1
    return tarefa


def listar_tarefas() -> list[Tarefa]:
    return sorted(tarefas.values(), key=lambda tarefa: tarefa.criada_em, reverse=True)


def obter_tarefa(tarefa_id: int) -> Tarefa | None:
    return tarefas.get(tarefa_id)


def atualizar_tarefa(tarefa_id: int, **campos: object) -> Tarefa | None:
    tarefa = obter_tarefa(tarefa_id)
    if tarefa is None:
        return None

    atualizacoes = {chave: valor for chave, valor in campos.items() if valor is not None}
    if not atualizacoes:
        return tarefa

    tarefa_atualizada = tarefa.model_copy(
        update={**atualizacoes, "atualizada_em": datetime.now()}
    )
    tarefas[tarefa_id] = tarefa_atualizada
    return tarefa_atualizada


def deletar_tarefa(tarefa_id: int) -> bool:
    return tarefas.pop(tarefa_id, None) is not None
