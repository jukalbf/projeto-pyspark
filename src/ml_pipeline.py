
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os

df = pd.DataFrame({
    'horario_pico': [1, 0, 1, 0],
    'feriado': [0, 0, 1, 0],
    'chuva_mm': [5, 10, 0, 20],
    'eventos_na_cidade': [0, 1, 0, 2],
    'fluxo_passageiros': [100, 250, 150, 300]
})

X = df[['horario_pico', 'feriado', 'chuva_mm', 'eventos_na_cidade']]
y = df['fluxo_passageiros']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

y_pred = model.predict(X)
mae = mean_absolute_error(y, y_pred)
rmse = mean_squared_error(y, y_pred, squared=False)

print(f"MAE: {mae} | RMSE: {rmse}")

os.makedirs("data/models", exist_ok=True)
joblib.dump(model, "data/models/random_forest.pkl")
