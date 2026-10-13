# Runbook: Pool de conexões do banco esgotado

**Serviços:** pagamentos-db e qualquer PostgreSQL com pool · **Severidade típica:** SEV1 quando afeta checkout
**Palavras-chave:** pool, conexões, connection pool exhausted, espera por conexão, PoolTimeout

## Sintomas
- `conexoes_ativas` == `conexoes_max_pool` de forma sustentada.
- `espera_por_conexao_p95_ms` alto, mas **CPU do banco baixa** (o banco está ocioso esperando clientes que não conseguem conectar).
- Nos logs das APIs: `PoolTimeout`, `could not acquire connection`.

## Diagnóstico
1. Compare `conexoes_max_pool` com `baseline_conexoes_max_pool`. Redução recente = forte suspeita.
2. Verifique `ultimo_deploy` do banco/config: mudanças de variável de ambiente são a causa nº 1.
3. Confirme no log do banco a linha de inicialização com o tamanho do pool.

## Mitigação
1. Reverter a configuração do pool para o último valor estável (rollback de config).
2. Reiniciar os pods consumidores **em lotes** para liberar conexões presas.
3. Acompanhar `espera_por_conexao_p95_ms` voltar ao normal (< 50 ms).

## Prevenção
- Validar no CI que `DB_POOL_SIZE` não reduz mais que 20% sem aprovação.
