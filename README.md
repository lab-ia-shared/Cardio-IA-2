# 💓 CardioIA - A Nova Era da Cardiologia Inteligente

## 📋 Descrição do Projeto

O **CardioIA** é um projeto acadêmico inovador focado na convergência entre tecnologia de ponta e saúde cardiovascular. O objetivo é desenvolver uma plataforma digital que simule um ecossistema cardiológico moderno, integrando dados clínicos, modelos de Machine Learning, Visão Computacional e IoT para triagem e diagnósticos precoces.

Nesta **Fase 1 – Batimentos de Dados**, assumimos o papel de cientistas de dados hospitalares para levantar, organizar e estruturar a base de dados fundamental (numérica, textual e visual) que alimentará os futuros módulos inteligentes do sistema, sempre com foco na Governança de Dados e ética em IA.

## 👨‍⚕️ Integrantes do Grupo
- <a href="https://www.linkedin.com/in/nicolas--araujo/">Nicolas Antonio Silva Araujo</a> 
- <a href="https://www.linkedin.com/in/vitoria-bagatin-31ba88266/">Vitória Pereira Bagatin</a> 

## 📂 Estrutura de Arquivos

A organização do repositório segue a estrutura necessária para a gestão de ativos de dados:

```text
Cardio-IA/
│
├── docs/
│   ├── prontuario_hipertensao_1.txt    # Artigo textual 1 (NLP)
│   └── prontuario_hipertensao_2.txt    # Artigo textual 2 (NLP)
│   └── prontuario_hipertensao_3.txt    # Artigo textual 3 (NLP)
│
└── README.md                     # Documentação principal e justificativas
````

---

## 🔢 1. Dados Numéricos (IoT e Predição)
Utilizamos dados clínicos para identificar fatores de risco que antecedem eventos cardiovasculares, especialmente relacionados à hipertensão arterial.

* **Dataset:** Cardiovascular Disease Dataset  
* **Fonte:** https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset  
* **Link para os Dados:** [Google Drive: dados_numericos](https://drive.google.com/drive/folders/1CCQaHMffA81alzsbKZdoWiH_j-bZ7pTd?usp=sharing)

* **Origem:** Dataset público contendo aproximadamente **70.000 registros clínicos de pacientes**.

### Variáveis Relevantes
* **Pressão Sistólica/Diastólica (ap_hi / ap_lo):** essencial para classificação da hipertensão.
* **Colesterol:** marcador biológico associado ao risco cardiovascular.
* **Glicose:** indicador importante para doenças metabólicas relacionadas ao sistema cardiovascular.
* **Idade e Sexo:** variáveis demográficas relevantes na avaliação de risco.
* **Peso e Altura:** utilizados para cálculo de IMC.
* **Tabagismo, Consumo de Álcool e Atividade Física:** fatores comportamentais que influenciam diretamente no risco cardiovascular.

* **Justificativa para IA:** Estes dados permitem o treinamento de modelos de classificação binária para prever a presença de doenças cardiovasculares com base em biometria e exames laboratoriais.

---

## 📑 2. Dados Textuais (NLP)
Simulação de prontuários médicos para estruturação de dados não estruturados.

* **Arquivos:** Disponíveis na pasta `/docs` deste repositório.
* **Fontes:** Dados simulados baseados em diretrizes médicas sobre hipertensão arterial.
* **Link para os Dados:** [Google Drive: dados_textuais](https://drive.google.com/drive/folders/19qosASiNQtAEJ_rmdV79cak1ijW_uYCS?usp=sharing)

### Fontes Científicas Utilizadas
- http://www.scielo.br/j/abc/a/BXT7Vk4B9VKQnJFsJhgJ4Hn/?lang=pt  
- https://bvsms.saude.gov.br/bvs/publicacoes/linha_cuidado_adulto_hipertens%C3%A3o_arterial.pdf  
- https://www.scielo.br/j/abc/a/f6qfTvNPNTWSXnTYVQszRLs/?format=pdf&lang=pt  
- https://docs.bvsalud.org/biblioref/2018/03/881441/rbh-v21n1_3-12.pdf  
- https://www.scielo.br/j/csc/a/S3rGV7YyJgStLFgcBQxjkfK/?format=pdf&lang=pt  
- https://docs.bvsalud.org/biblioref/2018/03/881411/rbh-v21n2_75-82.pdf  

### Análises de NLP
* **Extração de Entidades Nomeadas (NER):** identificação automática de sintomas, pressão arterial e fatores de risco.
* **Classificação Clínica:** identificação de pacientes com suspeita de hipertensão.
* **Extração de Sintomas:** reconhecimento de termos como cefaleia, tontura e palpitações.
* **Estruturação de Prontuários:** conversão de registros clínicos em dados estruturados.

* **Justificativa para IA:** O processamento de linguagem natural permite transformar relatos clínicos em dados estruturados, auxiliando na triagem hospitalar.

---

## 👁️ 3. Dados Visuais (Visão Computacional)
Análise de exames de imagem para detecção de anomalias estruturais e dimensionais do coração.

* **Dataset:** [Cardiomegaly Disease Prediction (NIH Chest X-ray Subset)](https://www.kaggle.com/datasets/rahimanshu/cardiomegaly-disease-prediction-using-cnn)
* **Link para as Imagens:** [Google Drive: dados_visuais](https://drive.google.com/drive/folders/1Kszx-A_djPO3Qvl16BZtZl7vBnXPAhFB?usp=sharing)
* **Fonte Original:** NIH Clinical Center via Kaggle
* **Tipo de Exame:** Raio-X de Tórax (Chest X-ray)
* **Especificações Técnicas:** Imagens pré-processadas com CLAHE e redimensionadas para $128 \times 128$ pixels

### Aplicações de Visão Computacional:
* **Cálculo do Índice Cardio-Torácico (CTR):** Treinamento de algoritmos para medir automaticamente o diâmetro cardíaco e o diâmetro torácico, utilizando a fórmula $CTR = \frac{MRD + MLD}{ID}$.
* **Detecção de Cardiomegalia:** Identificação automatizada de casos onde o CTR excede 0.5, indicando o limite superior da normalidade.
* **Segmentação e Medição:** Uso de redes neurais convolucionais (CNNs) para delinear as bordas do coração e do tórax com precisão milimétrica.

**Justificativa para IA:** O diagnóstico da cardiomegalia por Raio-X é um dos indicadores mais críticos de insuficiência cardíaca. O uso de Visão Computacional padroniza as medições geométricas, eliminando a subjetividade humana e permitindo uma triagem em larga escala com alta precisão diagnóstica.

---

## 🛡️ Governança e Ética (Pensamento Crítico sobre Vieses)

Este projeto foi estruturado sob os pilares da Governança de Dados e Ética em IA, reconhecendo que a qualidade do diagnóstico automatizado depende da integridade da base de dados utilizada.

### Análise de Vieses e Limitações:
* **Viés de Gênero e Idade:** Identificamos que datasets históricos de doenças cardiovasculares podem apresentar sub-representação de mulheres ou grupos etários específicos, o que pode levar a modelos de IA menos precisos para esses perfis. O Grupo 56 compromete-se a monitorar a distribuição demográfica dos dados para mitigar diagnósticos tendenciosos.
* **Dados Sintéticos vs. Reais:** Reconhecemos que o uso de dados simulados (Parte 2 - NLP) é uma ferramenta valiosa para o desenvolvimento inicial, mas possui limitações em representar a complexidade e a variabilidade linguística de prontuários reais de diferentes regiões.
* **Qualidade Visual:** O dataset de Raio-X foi processado tecnicamente (CLAHE), porém, entendemos que variações na qualidade técnica do equipamento de imagem (ruído, contraste) podem atuar como um viés tecnológico, afetando a acurácia do cálculo do CTR pela Visão Computacional.

### Compromisso Ético:
* **Finalidade:** Os dados são utilizados estritamente para fins acadêmicos no contexto do projeto CardioIA.
* **Transparência:** Todas as fontes originais (Kaggle, NIH, SciELO) foram devidamente citadas, respeitando a proveniência da informação.
* **Privacidade:** Não foram utilizados dados sensíveis que permitam a identificação individual de pacientes reais, seguindo as boas práticas de proteção de dados.
---
