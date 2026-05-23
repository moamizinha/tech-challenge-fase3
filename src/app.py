from assistant import gerar_resposta


if __name__ == "__main__":

    pergunta = input(
        "Digite a pergunta clínica: "
    )

    resposta = gerar_resposta(pergunta)

    print(resposta)