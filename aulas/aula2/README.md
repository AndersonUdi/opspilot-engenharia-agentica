# Aula 2 · Orquestração (LangGraph)

**Resultado:** o agente vira uma Máquina de Estados com rota de erro, persistência e aprovação humana.

| Passo | Arquivo | Lacunas |
|---|---|---|
| 1. Estado e reducer | `opspilot/grafo.py` | A2-L1 |
| 2. Rotas (arestas condicionais) | `opspilot/grafo.py` | A2-L2, A2-L3, A2-L4 |
| 3. Humano no loop | `opspilot/grafo.py` | A2-L5 |
| 4. Persistência | `opspilot/grafo.py` | A2-L6 |

```bash
make test AULA=2                  # rotas testadas SEM gastar tokens
make aula2-grafo                  # desenha o grafo (Ctrl+Shift+V no workspace/grafo_aula2.md)
make aula2                        # responda "depois", feche o terminal e retome:
python -m aulas.aula2.a2_01_rodar_grafo --thread inc-2041 --retomar sim
```

**Checkpoint:** depois de retomar, existe um arquivo novo em `data/tickets/`.
