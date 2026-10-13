# Runbook: Latência alta em API

**Serviços:** checkout-api, qualquer API HTTP · **Severidade típica:** SEV2 (SEV1 se taxa de erro > 5%)
**Palavras-chave:** latência, lentidão, p95, timeout, checkout lento

## Sintomas
- p95 acima de 3x o baseline por mais de 5 minutos.
- Clientes relatam "carregando infinito" no checkout.

## Diagnóstico (nesta ordem)
1. Compare `latencia_p95_ms` com `baseline_latencia_p95_ms` em `consultar_metricas`.
2. Se a CPU da API estiver **baixa** (< 60%), o gargalo provavelmente é uma **dependência**. Verifique cada serviço listado em `dependencias`.
3. Procure nos logs da API por `timeout`, `pool` ou `upstream`.
4. Correlacione o início do problema com o horário do `ultimo_deploy` da API **e das dependências**.

## Mitigação
- Se uma dependência for a causa, siga o runbook dela.
- Se o último deploy da própria API coincidir com o início, faça rollback.
- Nunca escale pods da API às cegas: se o gargalo é o banco, mais pods = mais pressão no pool.
