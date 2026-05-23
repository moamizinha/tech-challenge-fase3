import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DATASET = (
    BASE_DIR
    / "data"
    / "dataset_medico_qa_sintetico.jsonl"
)

OUTPUT_DATASET = (
    BASE_DIR
    / "data"
    / "dataset_finetuning_formatado.jsonl"
)


def carregar_dataset():

    registros = []

    with open(
        INPUT_DATASET,
        "r",
        encoding="utf-8"
    ) as file:

        for linha in file:
            registros.append(
                json.loads(linha)
            )

    return registros


def converter_para_formato_treinamento(registro):

    pergunta = registro.get(
        "pergunta",
        ""
    )

    resposta = registro.get(
        "resposta",
        ""
    )

    categoria = registro.get(
        "categoria",
        "geral"
    )

    return {
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é um assistente acadêmico "
                    "especializado em apoio clínico."
                )
            },
            {
                "role": "user",
                "content": pergunta
            },
            {
                "role": "assistant",
                "content": resposta
            }
        ],
        "metadata": {
            "categoria": categoria
        }
    }


def gerar_dataset_formatado():

    dataset_original = carregar_dataset()

    dataset_convertido = []

    for registro in dataset_original:

        convertido = (
            converter_para_formato_treinamento(
                registro
            )
        )

        dataset_convertido.append(
            convertido
        )

    with open(
        OUTPUT_DATASET,
        "w",
        encoding="utf-8"
    ) as file:

        for item in dataset_convertido:

            file.write(
                json.dumps(
                    item,
                    ensure_ascii=False
                )
            )

            file.write("\n")

    print(
        f"Dataset formatado gerado em:"
    )

    print(OUTPUT_DATASET)

    print()

    print(
        f"Total de registros:"
    )

    print(len(dataset_convertido))


if __name__ == "__main__":

    gerar_dataset_formatado()