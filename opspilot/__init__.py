"""OpsPilot — Codebase de Referência do curso *Engenharia Agêntica: do Zero ao Deploy*.

O OpsPilot é um agente de **triagem de incidentes** para a loja fictícia
*MercadoNimbus*. Ele cresce uma camada por aula:

======  ===============================  ==========================================
Aula    Módulo                           O que entra
======  ===============================  ==========================================
1       ``tools.py``, ``prompts.py``,    Ferramentas, prompt estruturado e o
        ``agente_react.py``              primeiro agente ReAct (``create_agent``).
2       ``grafo.py``                     Máquina de estados (FSM) em LangGraph com
                                         rotas de erro, persistência e aprovação
                                         humana.
3       ``deep_agent.py``                Harness *Deep Agent*: planejamento,
                                         sistema de arquivos, sub-agentes e
                                         memória longa.
4       ``observabilidade.py``,          Tracing com Langfuse, avaliação
        ``avaliacao.py``                 automática e gate de CI.
======  ===============================  ==========================================

Convenção de lacunas: no branch ``main`` os trechos marcados ``LACUNA [Ax-Ly]``
contêm ``___`` para você completar. O gabarito vive no branch ``solucoes``.
"""

__version__ = "1.0.0"
