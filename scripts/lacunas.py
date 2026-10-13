"""Lista as lacunas que ainda faltam preencher: ``make lacunas`` (ou ``make lacunas AULA=2``).

Procura por ``___`` nos arquivos do curso e mostra o código da lacuna, o arquivo
e a linha — clique no caminho no terminal do Codespace para ir direto até ela.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTAS = ["opspilot", "aulas", ".github/workflows"]
PADRAO_ID = re.compile(r"LACUNA \[(A\d-L\d+)\]")
BURACO = re.compile(r"(?<![`\w])___(?![`\w])")  # ___ solto (ignora ``___`` em docstrings)


def main() -> int:
    filtro_aula = sys.argv[1] if len(sys.argv) > 1 else ""
    abertas: list[tuple[str, str, int, str]] = []
    for pasta in PASTAS:
        for arquivo in sorted((RAIZ / pasta).rglob("*")):
            if arquivo.suffix not in {".py", ".yml", ".yaml"} or not arquivo.is_file():
                continue
            lacuna_atual = "?"
            for numero, texto in enumerate(arquivo.read_text(encoding="utf-8").splitlines(), start=1):
                achou = PADRAO_ID.search(texto)
                if achou:
                    lacuna_atual = achou.group(1)
                if BURACO.search(texto) and not texto.lstrip().startswith("#"):
                    abertas.append((lacuna_atual, str(arquivo.relative_to(RAIZ)), numero, texto.strip()))

    if filtro_aula:
        abertas = [a for a in abertas if a[0].startswith(f"A{filtro_aula}-")]

    if not abertas:
        print("🎉 Nenhuma lacuna aberta" + (f" na Aula {filtro_aula}." if filtro_aula else "."))
        return 0

    print(f"📝 {len(abertas)} linha(s) com lacuna aberta:\n")
    for lacuna, caminho, numero, texto in abertas:
        print(f"  [{lacuna}] {caminho}:{numero}\n      {texto}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
