#!/usr/bin/env bash
# Roda UMA vez quando o Codespace é criado.
# Instala as dependências, o pacote opspilot em modo editável e valida o ambiente.
set -euo pipefail

echo "📦 Instalando dependências da turma..."
python -m pip install --upgrade pip --quiet
python -m pip install -r requirements.txt --quiet
python -m pip install -e . --quiet   # torna `import opspilot` disponível em qualquer pasta

echo "🩺 Verificando o ambiente..."
python scripts/check_env.py || true   # não falha a criação: o aluno pode cadastrar a chave depois

echo ""
echo "✅ Pronto! Próximo passo: abra o Guia do Aluno e siga a Aula 1."
echo "   Comandos úteis:  make check   make lacunas   make test"
