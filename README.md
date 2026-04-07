# SaudePredict-BigData: Predicao de Risco de Diabetes

Projeto Integrador IV-A - PUC Goias
Parceria Extensionista: Centro Medico Jamous

## Contexto do Projeto
Este projeto foi desenvolvido como parte da disciplina de Projeto Integrador IV-A da PUC Goias. A solucao visa auxiliar o Centro Medico Jamous na triagem automatizada de pacientes com risco de diabetes, utilizando tecnologias de Big Data e Inteligencia Artificial para processar grandes volumes de dados clinicos.

O carater extensionista do projeto foca na aplicacao de tecnologias de ponta para resolver problemas reais de saude publica, otimizando o tempo de atendimento e a precisao da triagem inicial.

## Arquitetura da Solucao
A solucao utiliza uma arquitetura hibrida com processamento distribuido local e armazenamento/visualizacao em nuvem (Google Cloud Platform). A documentacao da arquitetura foi gerada via codigo (Diagrams as Code).

### Camadas:
1. Ingestao: Geracao de dados sinteticos baseados em parametros clinicos reais.
2. Processamento: Engine Apache Spark (PySpark) para limpeza (Imputer) e engenharia de atributos (Feature Engineering).
3. Machine Learning: Treinamento de modelo preditivo utilizando Spark MLlib.
4. Nuvem: Persistencia e versionamento de dados no Google Cloud Storage (GCS).
5. Visualizacao: Dashboard de Business Intelligence no Looker Studio.

## Tecnologias Utilizadas
* Linguagem: Python 3.10+
* Big Data: Apache Spark (PySpark 3.x)
* Machine Learning: Spark MLlib (Random Forest Classifier)
* Cloud: Google Cloud Platform (GCS)
* Documentacao: Diagrams as Code (Python library)
* Visualizacao: Looker Studio
* Controle de Versao: Git e GitHub

## Como Executar

### Pre-requisitos
* Python 3.10 ou superior
* Java 8+ (necessario para execucao do Spark)
* gcloud CLI configurado e autenticado

### Instalacao
1. Clone o repositorio:
git clone https://github.com/Rezende3004/SaudePredict-BigData.git
cd SaudePredict-BigData

2. Instale as dependencias necessarias:
pip install -r requirements.txt

3. Autentique no Google Cloud (caso utilize o modulo de nuvem):
gcloud auth application-default login

### Execucao do Pipeline
Execute os scripts na ordem abaixo para garantir o fluxo correto dos dados:

1. Geracao de Dados:
python src/data_generator.py

2. Processamento e Treinamento de IA:
python src/processing_ml.py

3. Ingestao para Nuvem:
python src/cloud_ingestion.py

## Performance do Modelo
O algoritmo Random Forest Classifier alcancou uma performance de 98.64% de acuracia no conjunto de testes. A escolha do modelo se justifica pela sua robustez em lidar com variaveis clinicas nao-lineares e resistencia ao overfitting.

## Estrutura de Pastas
SaudePredict-BigData/
├── data/
│   ├── processed/    # Predicoes finais e dados tratados
│   └── raw/          # Datasets brutos (CSV)
├── docs/             # Relatorio tecnico e documentacao adicional
├── src/              # Codigo-fonte do projeto
│   ├── arquitetura_projeto.py
│   ├── cloud_ingestion.py
│   ├── data_generator.py
│   └── processing_ml.py
├── .gitignore        # Configuracao para evitar envio de metadados do Spark
├── README.md
└── requirements.txt
