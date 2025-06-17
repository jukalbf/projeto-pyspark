import pandas as pd
import numpy as np
import json
import glob
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# =========================================================
# ETAPA 1 - Carregar o dataset do SPTrans (gerado pelo PySpark)
# =========================================================

# Leitura dos arquivos de partição do Spark (SPTrans)
arquivos = glob.glob("data/processed/dataset.csv/part-*.csv")
df_sptrans = pd.concat([pd.read_csv(arq) for arq in arquivos], ignore_index=True)

# Substituindo nulos por 0
df_sptrans.fillna(0, inplace=True)

# =========================================================
# ETAPA 2 - Carregar o dataset do IBGE (arquivo JSON processado)
# =========================================================

# Carregando o JSON do IBGE já baixado
with open("data/raw/ibge_mobilidade.json", "r", encoding="utf-8") as f:
    ibge_raw = json.load(f)

# Normaliza o JSON
df_ibge = pd.json_normalize(ibge_raw)

# Atenção: dependendo da estrutura do seu JSON, você pode precisar ajustar essas colunas:
# Exemplo de renomeação para facilitar a integração:
df_ibge.rename(columns={
    'localidade.nome': 'municipio',
    'serie.2023': 'valor'
}, inplace=True)

# Como não temos o município na base SPTrans, vamos apenas adicionar média nacional simulada:
# (para que o código rode normalmente na integração acadêmica)
renda_media_simulada = 2500  # simulação
taxa_desemprego_simulada = 9  # simulação

df_sptrans['renda_media'] = renda_media_simulada
df_sptrans['taxa_desemprego'] = taxa_desemprego_simulada

# =========================================================
# ETAPA 3 - Adicionar variáveis complementares simuladas
# =========================================================

# Criamos as variáveis auxiliares necessárias
df_sptrans['horario_pico'] = np.random.randint(0, 2, len(df_sptrans))
df_sptrans['feriado'] = np.random.randint(0, 2, len(df_sptrans))
df_sptrans['chuva_mm'] = np.random.randint(0, 50, len(df_sptrans))
df_sptrans['eventos_na_cidade'] = np.random.randint(0, 4, len(df_sptrans))
df_sptrans['fluxo_passageiros'] = np.random.randint(200, 600, len(df_sptrans))

# =========================================================
# ETAPA 4 - Montar as features e target
# =========================================================

X = df_sptrans[['codigo_cl', 'circular', 'horario_pico', 'feriado', 'chuva_mm',
                 'eventos_na_cidade', 'renda_media', 'taxa_desemprego']]
y = df_sptrans['fluxo_passageiros']

# =========================================================
# ETAPA 5 - Treinar o modelo Random Forest
# =========================================================

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Avaliação do modelo
y_pred = model.predict(X)
mae = mean_absolute_error(y, y_pred)
rmse = mean_squared_error(y, y_pred, squared=False)
mape = (abs(y - y_pred) / y).mean() * 100

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")
print(f"MAPE: {mape}%")

# =========================================================
# ETAPA 6 - Salvar o modelo treinado
# =========================================================

os.makedirs("data/models", exist_ok=True)
joblib.dump(model, "data/models/random_forest.pkl")

print("Modelo salvo em: data/models/random_forest.pkl")