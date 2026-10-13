"""Utilitários pequenos usados em várias aulas (impressão bonita, extração de texto)."""

from __future__ import annotations

from typing import Any


def texto_de(mensagem: Any) -> str:
    """Extrai o texto de uma mensagem do LangChain, qualquer que seja o formato.

    Por que isso existe?
        Dependendo do modelo/API, ``AIMessage.content`` pode ser uma *string* ou
        uma *lista de blocos* (``[{"type": "text", "text": "..."}, ...]``). Este
        helper é o "parse" defensivo da anatomia do agente: o resto do código não
        precisa saber qual formato veio.
    """
    conteudo = getattr(mensagem, "content", mensagem)
    if isinstance(conteudo, str):
        return conteudo
    if isinstance(conteudo, list):
        partes = []
        for bloco in conteudo:
            if isinstance(bloco, str):
                partes.append(bloco)
            elif isinstance(bloco, dict) and bloco.get("type") == "text":
                partes.append(bloco.get("text", ""))
        return "".join(partes)
    return str(conteudo)


def imprimir_passo(mensagem: Any) -> None:
    """Imprime UM passo do ciclo ReAct de forma legível no terminal.

    Mostra se o modelo *pensou e chamou ferramenta* (Act), se a ferramenta
    *respondeu* (Observation) ou se o modelo deu a *resposta final*.
    """
    tipo = getattr(mensagem, "type", "?")
    chamadas = getattr(mensagem, "tool_calls", None) or []
    if tipo == "human":
        print(f"\n🧑 Usuário: {texto_de(mensagem)}")
    elif tipo == "ai" and chamadas:
        for chamada in chamadas:
            print(f"🤖 → chama ferramenta {chamada['name']}({chamada['args']})")
    elif tipo == "tool":
        texto = texto_de(mensagem)
        resumo = texto if len(texto) < 300 else texto[:300] + " …"
        print(f"🔧 ← {getattr(mensagem, 'name', 'ferramenta')}: {resumo}")
    elif tipo == "ai":
        print(f"\n✅ Resposta final:\n{texto_de(mensagem)}")
