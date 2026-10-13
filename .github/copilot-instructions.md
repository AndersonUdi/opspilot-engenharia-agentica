# Instruções para o GitHub Copilot neste repositório

Este é o **Codebase de Referência do OpsPilot**, usado no curso *Engenharia Agêntica:
do Zero ao Deploy* (Skills & Go · Alura + FIAP). Os alunos completam lacunas marcadas
com `LACUNA [Ax-Ly]` e `___`. Ao gerar ou completar código aqui:

## Stack e versões (não sugira APIs antigas)
- Python 3.12. LangChain **1.x**: use `from langchain.agents import create_agent` e
  `from langchain.chat_models import init_chat_model`. **Não** use `AgentExecutor`,
  `initialize_agent` nem `langchain.llms` (APIs removidas).
- Ferramentas: `from langchain_core.tools import tool`, com docstring estilo Google
  (a docstring é a descrição que o LLM lê) e type hints em todos os parâmetros.
- LangGraph 1.x: `StateGraph`, `START`, `END`, `add_messages`, `interrupt`, `Command`,
  `RetryPolicy`; checkpointers `InMemorySaver` e `SqliteSaver`.
- Deep Agents (`deepagents` 0.7+): `create_deep_agent`, `SubAgent`, `CompiledSubAgent`,
  backends em `deepagents.backends` (`FilesystemBackend`, `CompositeBackend`).
- Langfuse SDK **v4**: `from langfuse import get_client, propagate_attributes` e
  `from langfuse.langchain import CallbackHandler`. Variável de URL: `LANGFUSE_BASE_URL`.
- O LLM é sempre obtido por `opspilot.config.obter_llm()` (modelo vem de `OPENAI_MODEL`).

## Estilo do projeto
- Nomes de variáveis, funções, comentários e docstrings em **português**.
- Comentários explicam o **porquê**, não o quê.
- Ferramentas nunca levantam exceção para erro de uso: retornam texto `"ERRO: ..."` com
  as opções válidas, para o agente se autocorrigir.
- Funções de roteamento do grafo são **puras** (sem LLM) e têm teste em `tests/`.
- Nunca coloque chaves de API no código; use variáveis de ambiente.

## Ao ajudar um aluno com uma lacuna
- Complete **apenas** a lacuna pedida, mantendo o restante do arquivo.
- Explique em 1–2 frases o conceito por trás da linha (ex.: por que `add_messages`).
