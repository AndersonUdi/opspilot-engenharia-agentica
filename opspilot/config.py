"""Configuração central do OpsPilot.

Por que um módulo só para isso?
    Em projetos com agentes, **modelo, chaves e caminhos** mudam o tempo todo
    (troca de modelo para reduzir custo, ambiente de CI sem chave, etc.).
    Centralizar aqui evita "números mágicos" espalhados e deixa claro, em um
    lugar só, o que precisa existir para o sistema rodar.

Variáveis de ambiente lidas (veja ``.env.example``):
    OPENAI_API_KEY        Obrigatória para chamar o LLM.
    OPENAI_MODEL          Modelo no formato ``provedor:nome`` (padrão abaixo).
    OPENAI_JUDGE_MODEL    Modelo usado como "juiz" na avaliação (Aula 4).
    LANGFUSE_*            Opcionais; só a Aula 4 usa.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# --------------------------------------------------------------------------- #
# Caminhos do projeto
# --------------------------------------------------------------------------- #
#: Raiz do repositório (a pasta que contém ``opspilot/``).
RAIZ = Path(__file__).resolve().parent.parent

#: Base de conhecimento "da empresa": runbooks, métricas, logs e incidentes.
DIR_DADOS = RAIZ / "data"
DIR_RUNBOOKS = DIR_DADOS / "runbooks"
DIR_LOGS = DIR_DADOS / "logs"
DIR_TICKETS = DIR_DADOS / "tickets"
ARQ_METRICAS = DIR_DADOS / "metricas.json"

#: Área de trabalho do Deep Agent (Aula 3). Tudo que o agente escreve fica aqui.
DIR_WORKSPACE = RAIZ / "workspace"

#: Banco SQLite usado como checkpointer na Aula 2 (persistência entre execuções).
ARQ_CHECKPOINTS = RAIZ / ".checkpoints.sqlite"

# Carrega o .env (no Codespace, os *secrets* já chegam como variáveis de ambiente;
# o .env é só um plano B para quem roda localmente). ``override=False`` garante
# que um secret do Codespace nunca seja sobrescrito por um .env esquecido.
load_dotenv(RAIZ / ".env", override=False)

# --------------------------------------------------------------------------- #
# Modelos
# --------------------------------------------------------------------------- #
#: Modelo padrão dos agentes. Formato ``provedor:modelo`` entendido por
#: ``init_chat_model``, ``create_agent`` e ``create_deep_agent``.
#: Um modelo "mini" é suficiente para tool calling e mantém o custo da turma baixo.
#: Confira os modelos disponíveis em https://platform.openai.com/docs/models
MODELO = os.getenv("OPENAI_MODEL", "openai:gpt-5.4-mini")

#: Modelo usado como juiz (LLM-as-a-judge) na Aula 4. Pode ser o mesmo.
MODELO_JUIZ = os.getenv("OPENAI_JUDGE_MODEL", MODELO)

#: Temperatura baixa = respostas mais reprodutíveis, essencial para avaliar agentes.
TEMPERATURA = float(os.getenv("OPENAI_TEMPERATURE", "0"))

#: Limite de passos de raciocínio/ação. Protege contra loops infinitos (e contra a fatura).
LIMITE_RECURSAO = int(os.getenv("OPSPILOT_RECURSION_LIMIT", "40"))


def tem_chave_openai() -> bool:
    """Retorna ``True`` se existe uma ``OPENAI_API_KEY`` com cara de válida."""
    chave = os.getenv("OPENAI_API_KEY", "")
    return chave.startswith("sk-") and len(chave) > 20


def tem_langfuse() -> bool:
    """Retorna ``True`` se as duas chaves do Langfuse estão configuradas."""
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY")) and bool(os.getenv("LANGFUSE_SECRET_KEY"))


def obter_llm(modelo: str | None = None, **kwargs):
    """Cria o *chat model* usado em todo o curso.

    Usamos ``init_chat_model`` (e não ``ChatOpenAI`` direto) porque ele aceita a
    string ``"openai:gpt-..."``: trocar de provedor vira uma mudança de
    configuração, não de código.

    Args:
        modelo: Sobrescreve ``OPENAI_MODEL`` (ex.: ``"openai:gpt-5.4-nano"``).
        **kwargs: Repassados ao modelo (ex.: ``timeout=30``).

    Returns:
        Um ``BaseChatModel`` pronto para ``.invoke()``, ``.bind_tools()`` e
        ``.with_structured_output()``.
    """
    from langchain.chat_models import init_chat_model  # import tardio: acelera `pytest`

    kwargs.setdefault("temperature", TEMPERATURA)
    kwargs.setdefault("max_retries", 3)  # retry com backoff para erros 429/5xx da API
    return init_chat_model(modelo or MODELO, **kwargs)
