# src/data_generator.py
import pandas as pd
import numpy as np
import os

def gerar_dados_exames(num_registros=5000):
    """Gera um dataset sintético de exames clínicos para predição de diabetes."""
    np.random.seed(42)
    
    dados = {
        'paciente_id': range(1, num_registros + 1),
        'idade': np.random.randint(18, 90, num_registros),
        'imc': np.round(np.random.normal(28, 6, num_registros), 1), # Índice de Massa Corporal
        'pressao_sistolica': np.random.randint(90, 180, num_registros),
        'glicose_jejum': np.random.randint(70, 200, num_registros),
        'insulina': np.random.randint(15, 200, num_registros),
    }
    
    df = pd.DataFrame(dados)
    
    # Lógica simples para gerar o "Outcome" (1 = Risco Alto, 0 = Risco Baixo)
    # Na vida real, o modelo vai descobrir isso. Aqui estamos forçando um padrão.
    df['risco_diabetes'] = np.where(
        (df['glicose_jejum'] > 125) & (df['imc'] > 30), 1, 0
    )
    
    # Introduzindo alguns valores nulos (sujeira) para o PySpark limpar depois
    df.loc[np.random.choice(df.index, 50), 'glicose_jejum'] = np.nan
    
    caminho_saida = 'data/raw/exames_sinteticos.csv'
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    df.to_csv(caminho_saida, index=False)
    print(f"Dataset gerado com sucesso em: {caminho_saida}")

if __name__ == "__main__":
    gerar_dados_exames()