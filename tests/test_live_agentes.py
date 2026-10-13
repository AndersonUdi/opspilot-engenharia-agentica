"""Testes AO VIVO (chamam a OpenAI). Rodam só com ``pytest -m live`` e com chave.

No CI eles rodam no job ``agentic-eval`` (veja ``.github/workflows/agentic-ci.yml``),
que só existe quando o secret ``OPENAI_API_KEY`` está configurado no repositório.
"""

import pytest

from opspilot.config import tem_chave_openai

pytestmark = [
    pytest.mark.live,
    pytest.mark.skipif(not tem_chave_openai(), reason="OPENAI_API_KEY não configurada"),
]


def test_agente_react_responde_com_ferramentas():
    from opspilot.agente_react import criar_agente_react

    agente = criar_agente_react()
    estado = agente.invoke({"messages": [{"role": "user", "content": "Como estão as métricas do pagamentos-db?"}]})
    usou_ferramenta = any(m.type == "tool" for m in estado["messages"])
    assert usou_ferramenta, "O agente deveria ter consultado as métricas em vez de responder de cabeça"


def test_fsm_encontra_causa_raiz():
    from opspilot.grafo import construir_grafo

    estado = construir_grafo(aprovacao_humana=False).invoke(
        {"messages": [{"role": "user", "content": "Checkout com 503 e lento desde as 18h. Investigue."}]},
        config={"recursion_limit": 40},
    )
    assert estado["categoria"] == "incidente"
    assert (estado.get("diagnostico") or {}).get("servico_causa_raiz") == "pagamentos-db"
