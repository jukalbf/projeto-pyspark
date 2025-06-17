import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import joblib
import numpy as np
import pandas as pd
import os

# Caminho do modelo salvo
modelo_path = "data/models/random_forest.pkl"

# Verifica se o modelo existe
if not os.path.exists(modelo_path):
    raise FileNotFoundError(f"Arquivo de modelo não encontrado em: {modelo_path}")

# Carrega o modelo treinado
model = joblib.load(modelo_path)

# Inicializa o app Dash
app = dash.Dash(__name__)
app.title = "Previsor de Evasão - Transporte Público"

# Layout da interface
app.layout = html.Div([
    html.H1("Sistema Preditivo de Demanda de Transporte", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Código da Linha (codigo_cl):"),
        dcc.Input(id='input_codigo_cl', type='number', value=0),

        html.Label("É Circular? (1=Sim, 0=Não):"),
        dcc.Input(id='input_circular', type='number', min=0, max=1, step=1, value=0),

        html.Br(),
        html.Button('Prever Demanda', id='btn_prever', n_clicks=0),
    ], style={'width': '50%', 'margin': 'auto', 'padding': '20px'}),

    html.H2(id='output_previsao', style={'textAlign': 'center', 'marginTop': 30})
])

# Função de predição
@app.callback(
    Output('output_previsao', 'children'),
    Input('btn_prever', 'n_clicks'),
    Input('input_codigo_cl', 'value'),
    Input('input_circular', 'value')
)
def prever_demanda(n_clicks, codigo_cl, circular):
    if n_clicks > 0:
        entrada = pd.DataFrame([{
            'codigo_cl': codigo_cl,
            'circular': circular
        }])
        predicao = model.predict(entrada)[0]
        return f"Previsão de fluxo (ajustado): {predicao:.0f}"
    return ""

# Roda o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
