"""
Pipeline de Big Data - Processamento e IA
Contexto: Projeto Integrador IV-A (PUC GO) - Centro Médico Jamous
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import DoubleType
from pyspark.ml.feature import VectorAssembler, Imputer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import os

def iniciar_spark():
    return SparkSession.builder \
        .appName("SaudePredict-Jamous-BigData") \
        .getOrCreate()

# Função para extrair a probabilidade da classe '1' (Risco Alto)
# O modelo retorna um vetor [prob_0, prob_1], quero apenas o prob_1.
extrair_prob_risco = udf(lambda v: float(v[1]), DoubleType())

def executar_pipeline():
    spark = iniciar_spark()
    # Reduz o nível de log para focar nos resultados
    spark.sparkContext.setLogLevel("ERROR")

    print("\n Lendo dados sintéticos...")
    caminho_input = "data/raw/exames_sinteticos.csv"
    df = spark.read.csv(caminho_input, header=True, inferSchema=True)

    print("\n Tratando valores nulos...")
    imputer = Imputer(inputCols=["glicose_jejum"], outputCols=["glicose_jejum"]).setStrategy("median")
    df_limpo = imputer.fit(df).transform(df).dropna()

    print("\n Treinando a Inteligência Artificial...")
    assembler = VectorAssembler(
        inputCols=["idade", "imc", "pressao_sistolica", "glicose_jejum", "insulina"],
        outputCol="features"
    )
    df_vetorizado = assembler.transform(df_limpo)

    # Divisão Treino/Teste
    treino, teste = df_vetorizado.randomSplit([0.8, 0.2], seed=42)
    
    # Random Forest
    rf = RandomForestClassifier(labelCol="risco_diabetes", featuresCol="features", numTrees=30)
    modelo = rf.fit(treino)

    # Avaliação
    predicoes = modelo.transform(teste)
    evaluator = MulticlassClassificationEvaluator(labelCol="risco_diabetes", metricName="accuracy")
    acuracia = evaluator.evaluate(predicoes)
    
    print(f"\n PERFORMANCE DO MODELO: {acuracia * 100:.2f}%")

    print(" Formatando indicadores para o Dashboard...")
    df_final = predicoes.withColumn("probabilidade_risco", extrair_prob_risco(col("probability"))) \
                        .select(
                            col("paciente_id"),
                            col("idade"),
                            col("glicose_jejum"),
                            col("prediction").alias("diagnostico_ia"),
                            col("probabilidade_risco")
                        )

    output_path = "data/processed/predicoes_finais"
    print(f" Salvando resultados em: {output_path}")
    
    df_final.write.mode("overwrite").csv(output_path, header=True)
    
    print("\n Pipeline finalizado!")
    spark.stop()

if __name__ == "__main__":
    os.makedirs("data/processed", exist_ok=True)
    executar_pipeline()