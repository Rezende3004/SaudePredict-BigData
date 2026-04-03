"""
Pipeline de Big Data - Ingestão para Nuvem (Google Cloud)
Contexto: Projeto Integrador IV-A (PUC GO) - Centro Médico Jamous
"""

import os
import glob
from google.cloud import storage

#CONFIGURAÇÕES DO GOOGLE CLOUD
ID_PROJETO = "project-4839468d-68a4-4847-949"
NOME_BUCKET = "jamous-dados-predicao-joao" 

def autenticar_gcs():
    """Autentica via ADC informando o ID do Projeto explicitamente."""
    print(f"Autenticando no projeto: {ID_PROJETO}")
    # Passando o project aqui, garantindo que o SDK não se perca
    return storage.Client(project=ID_PROJETO)

def encontrar_arquivo_predicoes():
    """Localiza o arquivo CSV gerado pelo Spark na pasta processed."""
    diretorio_processado = "data/processed/predicoes_finais"
    padrao_procura = os.path.join(diretorio_processado, "part-*.csv")
    arquivos_encontrados = glob.glob(padrao_procura)
    
    if not arquivos_encontrados:
        raise FileNotFoundError("Nenhum arquivo de predições 'part-*.csv' encontrado.")
    
    print(f"Arquivo encontrado: {arquivos_encontrados[0]}")
    return arquivos_encontrados[0]

def executar_upload():
    print("\n INICIANDO FASE DE NUVEM: INGESTÃO E ARMAZENAMENTO")
    try:
        # 1. Conexão
        gcs_client = autenticar_gcs()
        
        # 2. Localização do CSV
        arquivo_local = encontrar_arquivo_predicoes()
        
        # 3. Definição do destino (pi4a = Projeto Integrador 4A)
        nome_destino_nuvem = "pi4a/predicoes_saude_jamous.csv"
        
        # 4. Upload
        print(f" Subindo para gs://{NOME_BUCKET}/{nome_destino_nuvem}...")
        bucket = gcs_client.bucket(NOME_BUCKET)
        blob = bucket.blob(nome_destino_nuvem)
        blob.upload_from_filename(arquivo_local)
        
        print("\n Upload Concluído!")
        print("Dados disponíveis para o Looker Studio no Google Cloud Storage.")
        
    except Exception as e:
        print(f" Falha no pipeline de nuvem: {e}")

if __name__ == "__main__":
    executar_upload()