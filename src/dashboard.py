import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import joblib
import numpy as np
import pandas as pd
import os

# Carregando o modelo treinado
modelo_path = "data/models/random_forest.pkl"

if not os.path.exists(modelo_path):
    raise FileNotFoundError(f"Modelo não encontrado: {modelo_path}")

model = joblib.load(modelo_path)

# Inicializando o app
app = dash.Dash(__name__)
app.title = "Previsor de Demanda de Transporte Público"

# Layout com estilo
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'fontFamily': 'Arial'}, children=[
    
    html.H1("Sistema Inteligente de Transporte Público", 
            style={'textAlign': 'center', 'color': '#333333', 'marginBottom': '30px'}),
    
    html.Div([
        html.Label("Código da Linha (codigo_cl):"),
        dcc.Input(id='input_codigo_cl', type='number', value=1000, style={'width': '100%'}),
        html.Br(), html.Br(),

        html.Label("Circular? (1=Sim, 0=Não):"),
        dcc.Input(id='input_circular', type='number', min=0, max=1, value=0, style={'width': '100%'}),
        html.Br(), html.Br(),

        html.Label("Horário de Pico (1=Sim, 0=Não):"),
        dcc.Input(id='input_pico', type='number', min=0, max=1, value=1, style={'width': '100%'}),
        html.Br(), html.Br(),

        html.Label("Feriado? (1=Sim, 0=Não):"),
        dcc.Input(id='input_feriado', type='number', min=0, max=1, value=0, style={'width': '100%'}),
        html.Br(), html.Br(),

        html.Label("Chuva (mm):"),
        dcc.Input(id='input_chuva', type='number', value=10, style={'width': '100%'}),
        html.Br(), html.Br(),

        html.Label("Eventos na Cidade:"),
        dcc.Input(id='input_eventos', type='number', value=1, style={'width': '100%'}),
        html.Br(), html.Br(),

        html.Label("Renda Média (IBGE):"),
        dcc.Input(id='input_renda', type='number', value=2500, style={'width': '100%'}),
        html.Br(), html.Br(),

        html.Label("Taxa de Desemprego (%):"),
        dcc.Input(id='input_desemprego', type='number', value=9, style={'width': '100%'}),
        html.Br(), html.Br(),

        html.Button('Prever Demanda', id='btn_prever', n_clicks=0, 
                    style={'backgroundColor': '#007ACC', 'color': 'white', 'padding': '10px 20px',
                           'fontWeight': 'bold', 'border': 'none', 'borderRadius': '5px'})
    ], 
    style={'width': '400px', 'margin': 'auto', 'backgroundColor': '#ffffff', 
           'padding': '30px', 'borderRadius': '10px', 'boxShadow': '0px 0px 10px 0px rgba(0,0,0,0.1)'}),
    
    html.Div(id='output_previsao', 
             style={'textAlign': 'center', 'fontSize': '28px', 'marginTop': '40px', 'color': '#007ACC', 'fontWeight': 'bold'})
])

# Função de predição
@app.callback(
    Output('output_previsao', 'children'),
    [
        Input('btn_prever', 'n_clicks'),
        Input('input_codigo_cl', 'value'),
        Input('input_circular', 'value'),
        Input('input_pico', 'value'),
        Input('input_feriado', 'value'),
        Input('input_chuva', 'value'),
        Input('input_eventos', 'value'),
        Input('input_renda', 'value'),
        Input('input_desemprego', 'value')
    ]
)
def prever_demanda(n_clicks, codigo_cl, circular, pico, feriado, chuva, eventos, renda, desemprego):
    if n_clicks > 0:
        entrada = pd.DataFrame([{
            'codigo_cl': codigo_cl,
            'circular': circular,
            'horario_pico': pico,
            'feriado': feriado,
            'chuva_mm': chuva,
            'eventos_na_cidade': eventos,
            'renda_media': renda,
            'taxa_desemprego': desemprego
        }])
        predicao = model.predict(entrada)[0]
        return f"Previsão de fluxo de passageiros: {predicao:.0f} passageiros"
    return ""

# Rodando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
