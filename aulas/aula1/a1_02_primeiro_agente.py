"""Aula 1 · Exercício 2 — Rodando o primeiro agente ReAct e vendo cada passo.

Usamos ``stream_mode="values"``: a cada passo do loop recebemos o estado
completo e imprimimos só a mensagem nova. Assim você VÊ o ciclo
Raciocinar → Agir (ferramenta) → Observar → ... → Responder.

Como rodar::

    python -m aulas.aula1.a1_02_primeiro_agente
    python -m aulas.aula1.a1_02_primeiro_agente "A fila de e-mails está enorme, o que faço?"
"""

from __future__ import annotations

import sys

from opspilot.agente_react import criar_agente_react
from opspilot.config import LIMITE_RECURSAO
from opspilot.util import imprimir_passo

PERGUNTA_PADRAO = "O checkout está lento e dando erro 503 desde as 18h. Investigue."


def main() -> None:
    pergunta = " ".join(sys.argv[1:]) or PERGUNTA_PADRAO
    agente = criar_agente_react()

    vistas = 0  # quantas mensagens já imprimimos
    for estado in agente.stream(
        {"messages": [{"role": "user", "content": pergunta}]},
        config={"recursion_limit": LIMITE_RECURSAO},
        stream_mode="values",
    ):
        mensagens = estado["messages"]
        for mensagem in mensagens[vistas:]:
            imprimir_passo(mensagem)
        vistas = len(mensagens)

    print(f"\n📊 Total de mensagens no estado: {vistas}")


if __name__ == "__main__":
    main()
