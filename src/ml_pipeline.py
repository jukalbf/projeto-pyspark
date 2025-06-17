import pandas as pd
import glob
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Lê todos os arquivos CSV das partições
arquivos = glob.glob("data/processed/dataset.csv/part-*.csv")

# Concatena tudo em um único DataFrame Pandas
df = pd.concat([pd.read_csv(arquivo) for arquivo in arquivos], ignore_index=True)

df.head()

# Substituir nulos por 0 (tratamento simples para rodar o ML)
df.fillna(0, inplace=True)

# Features de entrada (só com os campos que você tem no momento)
X = df[['codigo_cl', 'circular']].astype(float)

# Alvo temporário: circular (apenas para fins de demonstração)
y = df['circular'].astype(float)


# Cria o modelo Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Treina o modelo
model.fit(X, y)


# Faz as predições
y_pred = model.predict(X)

# Calcula as métricas
mae = mean_absolute_error(y, y_pred)
rmse = mean_squared_error(y, y_pred, squared=False)

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")


# Garante que o diretório exista
os.makedirs("data/models", exist_ok=True)

# Salva o modelo
joblib.dump(model, "data/models/random_forest.pkl")

print("Modelo salvo em: data/models/random_forest.pkl")