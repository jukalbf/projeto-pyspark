
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.DataFrame({
    'data': ['2024-01-01','2024-01-02','2024-01-03','2024-01-04'],
    'fluxo_passageiros': [100, 150, 130, 160]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Monitor de Transporte Público"),
    dcc.Graph(
        figure={
            'data': [
                {'x': df['data'], 'y': df['fluxo_passageiros'], 'type': 'line', 'name': 'Fluxo'}
            ],
            'layout': {
                'title': 'Demanda de Passageiros'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
