# Runbook: Fila de mensagens atrasada

**Serviços:** notificacoes-worker · **Severidade típica:** SEV3 (SEV2 se > 1h de atraso)
**Palavras-chave:** fila, backlog, mensagens pendentes, e-mail atrasado, consumidores

## Sintomas
- `mensagens_pendentes` crescendo acima de 5x o baseline.
- Clientes recebem e-mail de confirmação com atraso.

## Diagnóstico
1. A fila pode crescer por **efeito colateral**: se a API que publica está lenta e fazendo retries, há mensagens duplicadas. Verifique a saúde da API produtora antes de mexer no worker.
2. Verifique `taxa_erro_pct` do worker: se baixa, o worker está saudável, só sobrecarregado.

## Mitigação
- Escalar consumidores temporariamente (até 12).
- Se for efeito colateral, resolver a causa na API produtora primeiro.
