"""Diagnóstico do ambiente — rode no minuto 1 de cada aula: ``make check``.

Verifica Python, bibliotecas, chaves e (opcionalmente) faz UMA chamada mínima
ao modelo para provar que a chave funciona. Cada problema vem com a correção.
"""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

OK, AVISO, ERRO = "✅", "⚠️ ", "❌"
problemas = 0


def linha(simbolo: str, texto: str, dica: str = "") -> None:
    global problemas
    if simbolo == ERRO:
        problemas += 1
    print(f"{simbolo} {texto}")
    if dica:
        print(f"     ↳ {dica}")


def main() -> int:
    print("🩺 Diagnóstico do ambiente OpsPilot\n")

    versao = sys.version_info
    if versao >= (3, 11):
        linha(OK, f"Python {versao.major}.{versao.minor}")
    else:
        linha(ERRO, f"Python {versao.major}.{versao.minor} (precisa 3.11+)", "Use o Codespace do curso.")

    for modulo, pacote in [
        ("langchain", "langchain"),
        ("langchain_openai", "langchain-openai"),
        ("langgraph", "langgraph"),
        ("langgraph.checkpoint.sqlite", "langgraph-checkpoint-sqlite"),
        ("deepagents", "deepagents"),
        ("langfuse", "langfuse"),
    ]:
        try:
            mod = importlib.import_module(modulo)
            versao_mod = getattr(mod, "__version__", "")
            linha(OK, f"{pacote} {versao_mod}".strip())
        except ImportError:
            linha(ERRO, f"{pacote} não instalado", "Rode: pip install -r requirements.txt")

    from opspilot.config import MODELO, tem_chave_openai, tem_langfuse

    if tem_chave_openai():
        linha(OK, f"OPENAI_API_KEY configurada · modelo: {MODELO}")
    else:
        linha(
            ERRO,
            "OPENAI_API_KEY ausente ou inválida",
            "Cadastre em github.com → Settings → Codespaces → Secrets e REINICIE o Codespace "
            "(ou crie um .env a partir do .env.example).",
        )

    if tem_langfuse():
        linha(OK, f"Langfuse configurado ({os.getenv('LANGFUSE_BASE_URL', 'URL padrão')})")
    else:
        linha(AVISO, "Langfuse não configurado (só é necessário na Aula 4)")

    if tem_chave_openai() and "--sem-chamada" not in sys.argv:
        try:
            from opspilot.config import obter_llm

            resposta = obter_llm(max_retries=1, timeout=30).invoke("Responda apenas: pong")
            linha(OK, f"Chamada de teste ao modelo respondeu: {str(resposta.content)[:40]!r}")
        except Exception as erro:  # noqa: BLE001
            linha(ERRO, f"Chamada ao modelo falhou: {erro}", "Confira a chave, os créditos da conta e o nome do modelo.")

    print("\n" + ("🎉 Tudo certo!" if problemas == 0 else f"Encontrei {problemas} problema(s) acima."))
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
