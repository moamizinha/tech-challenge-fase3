# Assistente Médico Acadêmico com LLM + RAG

Projeto acadêmico desenvolvido para demonstração de:
- LLM local com Ollama
- Integração com LangChain
- Recuperação contextual (RAG)
- Pipeline de adaptação/fine-tuning simulado
- Prompt engineering clínico
- Guardrails de segurança

## Tecnologias

- Python
- Ollama
- Qwen 2.5 3B
- LangChain

## Estrutura

```text
src/
├── app.py
├── assistant.py
├── retrieval.py
└── fine_tuning_simulado.py
```

## Execução

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar aplicação:

```bash
python src/app.py
```

Executar pipeline de adaptação:

```bash
python src/fine_tuning_simulado.py
```

## Arquitetura

```text
Usuário
↓
RAG
↓
Protocolo contextual
↓
Prompt especializado
↓
LLM local (Qwen)
↓
Resposta clínica controlada
```

## Observações

O projeto utiliza:
- especialização contextual via RAG
- prompt engineering
- pipeline de preparação para fine-tuning

Não foi realizado treinamento completo dos pesos do modelo.