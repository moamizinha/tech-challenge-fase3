from langchain_ollama import OllamaLLM

from retrieval import buscar_protocolo


llm = OllamaLLM(
    model="qwen2.5:3b",
    temperature=0
)


def montar_prompt(pergunta, protocolo):

    contexto = protocolo.get("texto_para_rag")
    fonte = protocolo.get("fonte_simulada")
    risco = protocolo.get("nivel_risco_padrao")
    titulo = protocolo.get("titulo")
    id_protocolo = protocolo.get("id_protocolo")

    return f"""
Você é um assistente acadêmico de apoio à decisão clínica.

Seu objetivo é:
- organizar informações clínicas
- destacar sinais importantes
- indicar riscos presentes no protocolo
- identificar dados faltantes
- recomendar validação humana

IMPORTANTE:
- Não invente diagnósticos definitivos.
- Não prescreva medicamentos.
- Não invente histórico clínico inexistente.
- Não relacione sintomas sem evidência.
- Não substitua avaliação médica.

Você pode:
- reorganizar os dados informados
- destacar sinais de alerta presentes
- explicar riscos mencionados no protocolo
- sugerir avaliação profissional

PROTOCOLO RECUPERADO:
ID: {id_protocolo}
Título: {titulo}
Risco: {risco}
Fonte: {fonte}

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

Responda em português no formato:

1. Resumo do caso
2. Sinais de atenção encontrados
3. Dados importantes ainda não informados
4. Risco identificado pelo protocolo
5. Orientação segura
6. Fonte utilizada

Se o contexto for insuficiente, diga isso claramente.
"""


def gerar_resposta(pergunta):

    resultado = buscar_protocolo(pergunta)

    if resultado is None:
        return """
Nenhum protocolo relacionado foi encontrado. Necessário mais informações para uma avaliação mais adequada

Recomenda-se avaliação por profissional de saúde.
"""

    score, protocolo = resultado

    prompt = montar_prompt(
        pergunta,
        protocolo
    )

    resposta = llm.invoke(prompt)

    return f"""
=== PROTOCOLO RECUPERADO ===

Score: {score}
ID: {protocolo.get("id_protocolo")}
Título: {protocolo.get("titulo")}
Área: {protocolo.get("area_clinica")}
Risco: {protocolo.get("nivel_risco_padrao")}
Fonte: {protocolo.get("fonte_simulada")}

=== RESPOSTA ===

{resposta}
"""