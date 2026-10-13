"""Testes OFFLINE do avaliador (Aula 4)."""

from opspilot.avaliacao import Caso, avaliar_regras, carregar_casos


def test_dataset_carrega_e_tem_todas_as_categorias():
    casos = carregar_casos()
    assert len(casos) >= 5
    assert {c.categoria_esperada for c in casos} == {"incidente", "duvida", "fora_escopo"}


def test_avaliar_regras_resposta_perfeita():
    caso = Caso(id="x", pergunta="?", categoria_esperada="incidente", servico_causa_esperado="pagamentos-db",
                termos_causa=["pool"], termos_proibidos=["certificado expirou"])
    estado = {"categoria": "incidente", "diagnostico": {"servico_causa_raiz": "pagamentos-db"}}
    notas = avaliar_regras(caso, "O pool de conexões foi reduzido.", estado)
    assert notas == {"categoria_correta": 1.0, "sem_termos_proibidos": 1.0, "cita_termos_causa": 1.0, "servico_correto": 1.0}


def test_avaliar_regras_pega_erros():
    caso = Caso(id="x", pergunta="?", categoria_esperada="incidente", servico_causa_esperado="pagamentos-db",
                termos_causa=["pool"], termos_proibidos=["certificado expirou"])
    estado = {"categoria": "duvida", "diagnostico": {"servico_causa_raiz": "checkout-api"}}
    notas = avaliar_regras(caso, "O certificado expirou.", estado)
    assert all(v == 0.0 for v in notas.values())
