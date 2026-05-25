def validar_resposta_segura(resposta: str, entrada_usuario: str = "") -> dict:
    """
    Valida a entrada do usuário e a resposta gerada pela LLM.

    O objetivo é bloquear:
    - pedidos de prescrição direta;
    - pedidos de diagnóstico definitivo;
    - pedidos para liberar paciente;
    - respostas que contenham orientação clínica insegura.
    """

    texto_resposta = resposta.lower()
    texto_entrada = entrada_usuario.lower()

    termos_bloqueados_resposta = [
        "tome ",
        "use ",
        "prescrevo",
        "prescrever",
        "receita",
        "diagnóstico é",
        "você tem",
        "está liberado",
        "pode ir para casa",
        "não precisa procurar médico",
        "não precisa de avaliação",
    ]

    termos_bloqueados_entrada = [
        "prescreva",
        "qual remédio",
        "que remédio",
        "qual medicamento",
        "diga o diagnóstico",
        "dê o diagnóstico",
        "diagnóstico definitivo",
        "diga que é",
        "libere o paciente",
        "liberar paciente",
        "pode ir para casa",
        "não precisa procurar médico",
        "não precisa de avaliação",
        "sem validação médica",
        "sem avaliação médica",
    ]

    ocorrencias_resposta = []
    ocorrencias_entrada = []

    for termo in termos_bloqueados_resposta:
        if termo in texto_resposta:
            ocorrencias_resposta.append(termo)

    for termo in termos_bloqueados_entrada:
        if termo in texto_entrada:
            ocorrencias_entrada.append(termo)

    if ocorrencias_entrada:
        return {
            "segura": False,
            "motivo": (
                "A entrada do usuário contém solicitação imprópria, como prescrição, "
                "diagnóstico definitivo ou liberação sem validação profissional."
            ),
            "ocorrencias": ocorrencias_entrada,
            "origem": "entrada_usuario",
        }

    if ocorrencias_resposta:
        return {
            "segura": False,
            "motivo": (
                "A resposta contém termos que podem indicar prescrição, diagnóstico "
                "definitivo ou liberação indevida."
            ),
            "ocorrencias": ocorrencias_resposta,
            "origem": "resposta_llm",
        }

    return {
        "segura": True,
        "motivo": "Entrada e resposta aprovadas pelas regras básicas de segurança.",
        "ocorrencias": [],
        "origem": "entrada_e_resposta",
    }