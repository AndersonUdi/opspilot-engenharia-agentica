# Runbook: Certificado TLS expirando

**Serviços:** auth-gateway e qualquer endpoint público · **Severidade típica:** SEV3 (vira SEV1 no dia da expiração)
**Palavras-chave:** certificado, TLS, SSL, expiração, https

## Sintomas
- `certificado_tls_expira_em_dias` < 14.

## Ação
1. Abrir ticket SEV3 para o time de plataforma com o prazo.
2. Confirmar se a renovação automática (cert-manager) está ativa.
3. Isto **não** causa latência: não confunda com incidentes de performance.
