import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "protocolos_hospitalares_ficticios.json"


def carregar_protocolos():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def calcular_score(pergunta, protocolo):
    pergunta_normalizada = pergunta.lower()
    score = 0

    palavras_chave = protocolo.get(
        "palavras_chave_para_recuperacao",
        []
    )

    for palavra in palavras_chave:
        palavra_normalizada = palavra.lower()

        if palavra_normalizada in pergunta_normalizada:

            quantidade_palavras = len(
                palavra_normalizada.split()
            )

            if quantidade_palavras >= 2:
                score += 10
            else:
                score += 2

    titulo = protocolo.get("titulo", "").lower()
    area = protocolo.get("area_clinica", "").lower()
    texto_rag = protocolo.get("texto_para_rag", "").lower()

    for termo in pergunta_normalizada.split():

        termo = termo.strip(
            ".,;:!?()[]{}"
        )

        if len(termo) <= 3:
            continue

        if termo in titulo:
            score += 3

        if termo in area:
            score += 1

        if termo in texto_rag:
            score += 1

    return score


def buscar_protocolo(pergunta):
    protocolos = carregar_protocolos()
    protocolos_pontuados = []

    for protocolo in protocolos:
        score = calcular_score(pergunta, protocolo)

        if score > 0:
            protocolos_pontuados.append((score, protocolo))

    protocolos_pontuados.sort(
        key=lambda item: item[0],
        reverse=True
    )

    if not protocolos_pontuados:
        return None

    melhor_score = protocolos_pontuados[0][0]

    if melhor_score < 8:
        return None

    return protocolos_pontuados[0]