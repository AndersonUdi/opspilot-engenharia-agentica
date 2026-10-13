"""Aula 2 · Exercício 2 — Desenhe o grafo (não precisa de chave de API).

Gera o diagrama Mermaid da FSM em ``workspace/grafo_aula2.md``. Abra o arquivo
no Codespace e use "Open Preview" (Ctrl+Shift+V) para ver o desenho.

Como rodar::

    python -m aulas.aula2.a2_02_desenhar_grafo
"""

from __future__ import annotations

from langgraph.checkpoint.memory import InMemorySaver

from opspilot.config import DIR_WORKSPACE
from opspilot.grafo import construir_grafo


def main() -> None:
    grafo = construir_grafo(aprovacao_humana=True, checkpointer=InMemorySaver())
    mermaid = grafo.get_graph().draw_mermaid()
    destino = DIR_WORKSPACE / "grafo_aula2.md"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(f"# FSM do OpsPilot (Aula 2)\n\n```mermaid\n{mermaid}\n```\n", encoding="utf-8")
    print(mermaid)
    print(f"\n✅ Diagrama salvo em {destino.relative_to(DIR_WORKSPACE.parent)} — abra com Ctrl+Shift+V.")


if __name__ == "__main__":
    main()
