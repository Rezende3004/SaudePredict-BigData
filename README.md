# SaudePredict-BigData: Predição de Risco de Diabetes
> **Projeto Integrador IV-A - PUC Goiás**  
> **Parceria Extensionista:** Centro Médico Jamous

## Contexto do Projeto
Este projeto foi desenvolvido como parte da disciplina de Projeto Integrador IV-A da PUC Goiás. A solução visa auxiliar o **Centro Médico Jamous** na triagem automatizada de pacientes com risco de diabetes, utilizando tecnologias de Big Data e Inteligência Artificial para processar grandes volumes de dados clínicos.

## Arquitetura da Solução
A solução utiliza uma arquitetura híbrida com processamento distribuído local e armazenamento/visualização em nuvem (GCP).

![Arquitetura do Projeto](src/arquitetura_big_data_-_centro_medico_jamous.png)

### Camadas:
1.  **Ingestão:** Geração de dados sintéticos baseados em parâmetros clínicos reais.
2.  **Processamento:** Engine **Apache Spark** (PySpark) para limpeza (Imputer) e treinamento de modelo de Machine Learning (**Random Forest**).
3.  **Nuvem:** Armazenamento dos resultados no **Google Cloud Storage (GCS)**.
4.  **Visualização:** Dashboard interativo no **Looker Studio**.

## Tecnologias Utilizadas
*   **Linguagem:** Python 3.10+
*   **Big Data:** Apache Spark (PySpark 3.x)
*   **Machine Learning:** Spark MLlib (Random Forest Classifier)
*   **Cloud:** Google Cloud Platform (GCS)
*   **Documentação:** Diagrams as Code (Python library)
*   **Visualização:** Looker Studio

## Estrutura de Pastas
```text
SaudePredict-BigData/
├── data/
│   ├── processed/   # Predições finais geradas pelo Spark
│   └── raw/         # Dataset sintético inicial
├── docs/            # Documentação adicional do projeto
├── notebooks/       # Jupyter Notebooks de testes (se houver)
├── src/             # Código-fonte da solução
│   ├── arquitetura_projeto.py
│   ├── cloud_ingestion.py
│   ├── data_generator.py
│   ├── processing_ml.py
│   └── arquitetura_big_data_-_centro_medico_jamous.png
└── README.md