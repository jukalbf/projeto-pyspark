import pandas as pd
import numpy as np
import json
import glob
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

arquivos = glob.glob("data/processed/dataset.csv/part-*.csv")
df_sptrans = pd.concat([pd.read_csv(arq) for arq in arquivos], ignore_index=True)

df_sptrans.fillna(0, inplace=True)

with open("data/raw/ibge_mobilidade.json", "r", encoding="utf-8") as f:
    ibge_raw = json.load(f)

df_ibge = pd.json_normalize(ibge_raw)

df_ibge.rename(columns={
    'localidade.nome': 'municipio',
    'serie.2023': 'valor'
}, inplace=True)

renda_media_simulada = 2500  # simulado
taxa_desemprego_simulada = 9  # simulado

df_sptrans['renda_media'] = renda_media_simulada
df_sptrans['taxa_desemprego'] = taxa_desemprego_simulada

df_sptrans['horario_pico'] = np.random.randint(0, 2, len(df_sptrans))
df_sptrans['feriado'] = np.random.randint(0, 2, len(df_sptrans))
df_sptrans['chuva_mm'] = np.random.randint(0, 50, len(df_sptrans))
df_sptrans['eventos_na_cidade'] = np.random.randint(0, 4, len(df_sptrans))
df_sptrans['fluxo_passageiros'] = np.random.randint(200, 600, len(df_sptrans))

X = df_sptrans[['codigo_cl', 'circular', 'horario_pico', 'feriado', 'chuva_mm',
                 'eventos_na_cidade', 'renda_media', 'taxa_desemprego']]
y = df_sptrans['fluxo_passageiros']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

y_pred = model.predict(X)
mae = mean_absolute_error(y, y_pred)
rmse = mean_squared_error(y, y_pred, squared=False)
mape = (abs(y - y_pred) / y).mean() * 100

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")
print(f"MAPE: {mape}%")

os.makedirs("data/models", exist_ok=True)
joblib.dump(model, "data/models/random_forest.pkl")

print("Modelo salvo em: data/models/random_forest.pkl")