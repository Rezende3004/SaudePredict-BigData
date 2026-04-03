from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import Looker 
from diagrams.onprem.analytics import Spark
from diagrams.programming.language import Python
from diagrams.onprem.client import User

# Configurações do Diagrama
graph_attr = {
    "fontsize": "20",
    "bgcolor": "white"
}

with Diagram("Arquitetura Big Data - Centro Médico Jamous", show=False, direction="LR", graph_attr=graph_attr):
    
    # Ator inicial
    pacientes = User("Dados de Pacientes")

    with Cluster("1. Ingestão e Geração"):
        gerador = Python("Gerador de Dados\n(Pandas / Synthetic)")

    with Cluster("2. Processamento Distribuído"):
        spark_job = Spark("Pipeline PySpark\n(Limpeza + Random Forest)")

    with Cluster("3. Nuvem (Google Cloud Platform)"):
        bucket = GCS("Bucket de Destino\n(Cloud Storage)")
        
    with Cluster("4. Visualização de Resultados"):
        dashboard = Looker("Looker Studio\n(Dashboard de Risco)")

    # Fluxo do Dado
    pacientes >> gerador >> Edge(label="CSV Raw") >> spark_job
    spark_job >> Edge(label="Parquet/CSV Processado") >> bucket
    bucket >> Edge(label="Conector Looker") >> dashboard