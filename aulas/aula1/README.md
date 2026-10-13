# Aula 1 · Fundamentos & LangChain

**Resultado:** ambiente padronizado e seu 1º agente ReAct rodando.

| Passo | Arquivo | Lacunas |
|---|---|---|
| 1. LLM puro vs. agente | `aulas/aula1/a1_01_llm_vs_agente.py` | A1-L1 |
| 2. Ferramentas | `opspilot/tools.py` | A1-L2, A1-L3 |
| 3. Prompt estruturado | `opspilot/prompts.py` | A1-L4 |
| 4. O agente | `opspilot/agente_react.py` | A1-L5, A1-L6 |

```bash
make check
python -m aulas.aula1.a1_01_llm_vs_agente
make test AULA=1        # deve ficar verde após A1-L2, L3, L4
make aula1              # o agente investigando o checkout lento
```

**Checkpoint:** você vê `🤖 → chama ferramenta consultar_metricas(...)` e uma resposta final com *Causa raiz* e *Evidências*.
