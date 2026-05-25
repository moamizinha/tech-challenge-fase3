# Tech Challenge - Fase 3  
# Assistente Médico Acadêmico com LLM, RAG, LangChain e LangGraph

Projeto acadêmico desenvolvido para o **Tech Challenge - Fase 3**, com o objetivo de criar um assistente virtual médico capaz de apoiar profissionais de saúde na consulta a protocolos internos, organização de informações clínicas, geração de respostas contextualizadas e validação de segurança.

A solução utiliza uma **LLM local executada com Ollama**, integrada ao **LangChain**, com recuperação contextual por **RAG - Retrieval-Augmented Generation** e fluxo demonstrável com **LangGraph**. O projeto também contempla dados médicos sintéticos, preparação para fine-tuning, validação de segurança, rastreabilidade, logging e explainability das respostas.

> **Aviso importante:** este projeto possui finalidade exclusivamente acadêmica e demonstrativa. O assistente não substitui médicos, enfermeiros ou qualquer profissional de saúde habilitado.

---

## 1. Contexto do desafio

Após a automação de análises de exames e textos clínicos, o desafio propõe a criação de um assistente virtual médico treinado ou customizado com dados próprios de um hospital. Esse assistente deve ser capaz de auxiliar profissionais de saúde na consulta a protocolos internos, dúvidas clínicas, procedimentos e informações estruturadas de pacientes.

Além disso, o desafio solicita a organização de fluxos de decisão automatizados e seguros, nos quais o sistema possa receber informações clínicas, consultar bases estruturadas, sugerir caminhos de atendimento, emitir alertas e apresentar respostas rastreáveis com apoio do LangChain e LangGraph.

---

## 2. Objetivo do projeto

O objetivo principal do projeto é desenvolver um **assistente médico acadêmico baseado em LLM**, capaz de:

- responder perguntas clínicas com apoio de protocolos hospitalares fictícios;
- recuperar informações relevantes antes da geração da resposta;
- contextualizar a resposta da LLM com dados estruturados simulados;
- demonstrar um pipeline de preparação para fine-tuning;
- utilizar LangChain para integração entre LLM, prompt e recuperação contextual;
- utilizar LangGraph para organizar o fluxo de atendimento;
- aplicar limites de segurança para evitar sugestões impróprias;
- indicar a fonte/protocolo utilizado na resposta;
- registrar logs para rastreamento e auditoria;
- demonstrar explainability nas respostas geradas.

---

## 3. Problema abordado

Hospitais e equipes médicas lidam diariamente com grande volume de informações clínicas, protocolos internos, prontuários, modelos de laudos, receitas, procedimentos e dúvidas recorrentes. A busca manual por essas informações pode tornar o atendimento mais lento e dificultar a padronização das condutas.

Além disso, respostas clínicas geradas por IA podem apresentar riscos se não houver limites claros, validação humana, rastreabilidade e controle de segurança. Um assistente médico precisa evitar diagnóstico definitivo, prescrição direta, liberação indevida de pacientes e respostas sem fonte.

Dessa forma, o problema central deste projeto é:

**Como construir um assistente virtual médico baseado em LLM, capaz de consultar dados internos simulados, recuperar protocolos hospitalares e gerar respostas contextualizadas de forma segura, rastreável e validada?**

---

## 4. Tecnologias utilizadas

- Python
- Ollama
- Qwen 2.5 3B
- LangChain
- LangGraph
- RAG - Retrieval-Augmented Generation
- JSON
- JSONL
- CSV
- Prompt engineering clínico
- Guardrails de segurança
- Logging para auditoria

---

## 5. Visão geral da solução

A solução foi organizada em camadas:

1. **Camada de dados sintéticos**  
   Contém protocolos hospitalares fictícios, perguntas e respostas médicas, prontuários sintéticos, modelos documentais e condutas clínicas.

2. **Camada de preparação para fine-tuning**  
   Organiza a base médica em formato conversacional, com mensagens nos papéis `system`, `user` e `assistant`.

3. **Camada de recuperação contextual - RAG**  
   Busca o protocolo hospitalar mais aderente à pergunta clínica.

4. **Camada de geração com LLM**  
   Utiliza o modelo Qwen 2.5 3B via Ollama, integrado ao LangChain.

5. **Camada de fluxo com LangGraph**  
   Organiza as etapas de entrada, verificação, consulta, geração, validação e resposta final.

6. **Camada de segurança e auditoria**  
   Aplica validação da resposta, indicação de fonte, logging e rastreabilidade.

Fluxo geral:

```text
Entrada do paciente ou profissional
↓
Verificação dos dados
↓
Consulta aos protocolos hospitalares fictícios
↓
Recuperação contextual via RAG
↓
Construção do prompt clínico especializado
↓
Geração de resposta com LLM local
↓
Validação de segurança
↓
Resposta final com fonte
↓
Registro de auditoria