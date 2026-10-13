"""Testes OFFLINE do prompt estruturado (Aula 1)."""

from opspilot.prompts import montar_prompt_sistema


def test_prompt_estruturado_tem_todas_as_secoes():
    prompt = montar_prompt_sistema()
    for secao in ("## PAPEL", "## OBJETIVO", "## FERRAMENTAS", "## PROCESSO", "## FORMATO", "## RESTRIÇÕES"):
        assert secao in prompt
    assert "___" not in prompt, "Ainda há lacuna aberta no prompt (Aula 1, A1-L4)"
