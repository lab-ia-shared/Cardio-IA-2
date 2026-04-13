# 💓 CardioIA - Fase 2: Diagnóstico Automatizado (IA no Estetoscópio Digital)

## 📋 Descrição do Projeto

O **CardioIA** é um projeto acadêmico focado na convergência entre tecnologia e saúde cardiovascular. Nesta **Fase 2**, evoluímos da coleta de dados (Fase 1) para o desenvolvimento de módulos inteligentes. O objetivo é simular a automatização do diagnóstico utilizando IA, atuando como o "estetoscópio digital do século XXI".

Desenvolvemos duas soluções principais:
1. Um sistema de **Processamento de Linguagem Natural (NLP) baseado em regras** para extração de sintomas.
2. Um **Classificador de Machine Learning** para triagem hospitalar automática (Alto vs. Baixo Risco).

## 👨‍⚕️ Integrantes do Grupo
- <a href="https://www.linkedin.com/in/nicolas--araujo/">Nicolas Antonio Silva Araujo</a> 
- <a href="https://www.linkedin.com/in/vitoria-bagatin-31ba88266/">Vitória Pereira Bagatin</a> 

## 🎬 Vídeo Demonstrativo
Confira a demonstração completa do código, testes ao vivo e explicação sobre os vieses do modelo:
> **[CLIQUE AQUI PARA ASSISTIR AO VÍDEO NO YOUTUBE] (INSERIR LINK AQUI)**

---

## 📂 Estrutura de Arquivos

A organização do repositório separa os dados (textos e bases) da lógica de programação (scripts Python):

```text
Cardio-IA-2/
│
├── docs/
│   ├── mapa_conhecimento.csv      # Ontologia relacionando sintomas a doenças
│   ├── sintomas_pacientes.txt     # Relatos simulados de pacientes (10+ frases)
│   └── triagem_risco.csv          # Dataset rotulado (Alto/Baixo risco) com 55 frases
│
├── classificador_risco.py         # Script de Machine Learning (Triagem)
├── extracao_diagnostico.py        # Script de NLP (Diagnóstico via regras)
└── README.md                      # Documentação principal
````

---

## ⚙️ Arquitetura e Fluxo de Dados (Como os arquivos se conectam)

Para garantir a modularidade do sistema, cada script Python consome bases de dados específicas da pasta `/docs`:

### 🩺 Parte 1: Extração de Sintomas (NLP Baseado em Regras)
**Script Responsável:** `extracao_diagnostico.py`

Este script simula o mapeamento lógico que um médico faz ao ouvir um paciente. Ele utiliza a biblioteca Pandas para consumir os seguintes arquivos:
* **Entrada 1 (`sintomas_pacientes.txt`):** Contém frases complexas relatando sintomas, tempo de início e impacto na rotina. O script lê cada linha como um "paciente" diferente.
* **Entrada 2 (`mapa_conhecimento.csv`):** Funciona como a "Ontologia" (Cérebro) do sistema. O script cruza as palavras do relato do paciente com as colunas `sintoma_1` e `sintoma_2` deste arquivo para sugerir a `doenca_associada`.

### 🧠 Parte 2: Classificador de Triagem (Machine Learning)
**Script Responsável:** `classificador_risco.py`

Este script utiliza a biblioteca `scikit-learn` para aplicar Inteligência Artificial real na triagem clínica.
* **Entrada (`triagem_risco.csv`):** Fornece o histórico de treinamento para a IA. O script lê a coluna `frase` e a coluna `situacao` (rótulo).
* **Processamento:** Transforma o texto em matrizes numéricas utilizando o método **TF-IDF** com `ngram_range=(1,2)`.
* **Decisão:** Treina um modelo **Decision Tree (Árvore de Decisão)** separando 80% dos dados para treino e 20% para teste. O script também permite testes em tempo real via terminal.

---

## 📊 Avaliação do Modelo e Análise de Distorções

O modelo de Árvore de Decisão atingiu uma acurácia média de **72.73%**. Durante os testes de validação, observamos e documentamos distorções intrínsecas ao Processamento de Linguagem Natural que afetam sistemas de saúde do mundo real:

1. **Sensibilidade Lexical e Ortográfica:** O modelo demonstrou distorções ao classificar palavras com e sem acento de forma diferente (ex: o termo "abdômen" com acento estava atrelado a baixo risco no treino, mas ao testar "abdomen" sem acento, o modelo errou a classificação por não reconhecer a palavra). Isso evidencia a necessidade de pipelines de pré-processamento (remoção de acentos e *stemming*).
2. **O Viés da Palavra "Dor":** Inicialmente, o modelo associava a palavra "dor" quase exclusivamente a "alto risco". Para corrigir isso, inserimos *n-grams (1,2)* e balanceamos a base com casos de dor de baixo risco (ex: dor no dedo, dor nas costas). O modelo corrigiu o viés, mas tornou-se dependente de contextos mais longos para classificar emergências com precisão.

---

## 🛡️ Governança e Ética em IA

Este projeto reafirma os pilares da Governança de Dados estabelecidos na Fase 1:

* **Qualidade e Volume de Dados:** Reconhecemos o fenômeno de *underfitting* durante os primeiros testes devido à escassez de dados. O dataset foi expandido iterativamente para 55 registros visando melhorar a capacidade de generalização da árvore de decisão.
* **Dados Sintéticos:** O uso de dados simulados é uma ferramenta valiosa para prova de conceito (PoC), porém possui limitações em representar a variabilidade linguística regional e gírias de pacientes reais do SUS.
* **Finalidade e Privacidade:** Os dados e modelos são utilizados estritamente para fins acadêmicos. O CardioIA não substitui a avaliação médica humana, atuando exclusivamente como um sistema de suporte à decisão (DSS) e priorização de filas.

