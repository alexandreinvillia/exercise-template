from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE_URL = "http://127.0.0.1:8000"
TIMEOUT_SECONDS = 10
PROJECT_DIR = Path(__file__).parent


def formatar_resposta(titulo: str, status_code: int, payload: object) -> None:
    print(f"\n## {titulo}")
    print(f"status: {status_code}")
    print(json.dumps(payload, indent=2, ensure_ascii=False, default=str))


def chamar_api(metodo: str, rota: str, payload: dict[str, object] | None = None) -> tuple[int, object]:
    body = None
    headers = {}
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = Request(f"{BASE_URL}{rota}", data=body, method=metodo, headers=headers)
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            content = response.read().decode("utf-8")
            return response.status, json.loads(content) if content else {}
    except HTTPError as error:
        content = error.read().decode("utf-8")
        return error.code, json.loads(content) if content else {}


def api_disponivel() -> bool:
    try:
        status_code, _ = chamar_api("GET", "/health")
        return status_code == 200
    except URLError:
        return False


def iniciar_servidor() -> subprocess.Popen[str] | None:
    if api_disponivel():
        print("Usando servidor já em execução em http://127.0.0.1:8000")
        return None

    print("Iniciando servidor local para a demonstração...")
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8000",
        ],
        cwd=PROJECT_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )

    deadline = time.time() + TIMEOUT_SECONDS
    while time.time() < deadline:
        if api_disponivel():
            return process
        time.sleep(0.25)

    process.terminate()
    process.wait(timeout=5)
    raise RuntimeError("Não foi possível iniciar a API no tempo esperado.")


def encerrar_servidor(process: subprocess.Popen[str] | None) -> None:
    if process is None:
        return

    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()


def executar_fluxo() -> None:
    formatar_resposta("Healthcheck", *chamar_api("GET", "/health"))
    formatar_resposta(
        "Criar tarefa 1",
        *chamar_api("POST", "/tarefas", {"titulo": "Preparar demo SDD"}),
    )
    formatar_resposta(
        "Criar tarefa 2",
        *chamar_api(
            "POST",
            "/tarefas",
            {"titulo": "Executar com o cliente", "descricao": "Mostrar fluxo completo"},
        ),
    )
    formatar_resposta("Listar tarefas", *chamar_api("GET", "/tarefas"))
    formatar_resposta("Detalhar tarefa 1", *chamar_api("GET", "/tarefas/1"))
    formatar_resposta(
        "Atualizar tarefa 1",
        *chamar_api("PUT", "/tarefas/1", {"status": "concluida"}),
    )
    formatar_resposta("Deletar tarefa 2", *chamar_api("DELETE", "/tarefas/2"))
    formatar_resposta("Confirmar deleção", *chamar_api("GET", "/tarefas/2"))


def main() -> None:
    process = iniciar_servidor()
    try:
        executar_fluxo()
    finally:
        encerrar_servidor(process)


if __name__ == "__main__":
    main()