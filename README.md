
# Sistema Inteligente de Previsão de Demanda no Transporte Público

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo a implementação prática de um sistema inteligente capaz de prever a demanda de passageiros no transporte público, utilizando dados reais de órgãos públicos brasileiros, processamento em Big Data (PySpark), integração de APIs (SPTrans e IBGE), Machine Learning (Random Forest), e visualização interativa via Dashboard (Dash).

O projeto simula a aplicação de técnicas de Big Data para otimização de rotas e eficiência no transporte público, com potencial aplicação em órgãos de mobilidade urbana.

---

## 👨‍💻 Equipe

- João Lucas
- Matheus Eduardo
- Raphael Marinho
- Douglas Kauan
- Icaro Bonfiglio
- Pedro Lucas
- Gabriel De Paula

---

## 🛠 Tecnologias Utilizadas

- Python 3.10
- PySpark → Processamento dos dados de SPTrans
- Pandas & Numpy → Manipulação e transformação de dados
- APIs Públicas → SPTrans & IBGE
- Scikit-learn (RandomForestRegressor) → Treinamento e predição de fluxo de passageiros
- Dash (Plotly) → Desenvolvimento do Dashboard interativo
- Joblib → Persistência do modelo treinado

---

## 🗄 Estrutura de Diretórios

```text
projeto_pyspark/
├── data/
│   ├── raw/                # Dados brutos (SPTrans, IBGE)
│   ├── processed/          # Dados processados pelo PySpark
│   └── models/             # Modelos treinados (.pkl)
│
├── src/
│   ├── data_collection.py  # Scripts de coleta de dados (APIs)
│   ├── data_processing.py  # Processamento e transformação com PySpark
│   └── ml_pipeline.py      # Treinamento e salvamento do modelo
│
├── dashboard/
│   └── dashboard.py        # Código do Dashboard interativo
│
├── requirements.txt        # Dependências necessárias
└── README.md               # Documentação do projeto
```

## 🔗 Fontes de Dados Utilizadas

### SPTrans (São Paulo Transporte)
- API: http://api.olhovivo.sptrans.com.br/v2.1
- Utilização: Dados de linhas de ônibus, códigos de linha, tipos de trajeto (circular ou não).

### IBGE (Instituto Brasileiro de Geografia e Estatística)
- API: https://servicodados.ibge.gov.br/api/v3/agregados
- Utilização: Renda média, taxa de desemprego, dados socioeconômicos para enriquecer o modelo.

---

## 🔎 Pipeline Completo

1️⃣ Coleta de dados públicos (SPTrans + IBGE)  
2️⃣ Processamento dos dados brutos com PySpark  
3️⃣ Integração das fontes e criação de variáveis complementares (chuva, feriado, eventos, horário de pico)  
4️⃣ Treinamento do modelo de Machine Learning (Random Forest Regressor)  
5️⃣ Salvamento do modelo treinado com Joblib  
6️⃣ Construção de Dashboard interativo com Dash (Python)  
7️⃣ Simulação de cenários urbanos e previsão de demanda de passageiros

---

## 📊 Variáveis Utilizadas no Modelo

| Variável | Origem | Descrição |
| -------- | ------ | --------- |
| codigo_cl | SPTrans | Código da linha |
| circular | SPTrans | Linha circular (1=Sim, 0=Não) |
| horario_pico | Simulado | Se é horário de pico |
| feriado | Simulado | Se é feriado |
| chuva_mm | Simulado | Volume de chuva |
| eventos_na_cidade | Simulado | Quantidade de grandes eventos na cidade |
| renda_media | IBGE | Renda média da população |
| taxa_desemprego | IBGE | Taxa de desemprego local |
| fluxo_passageiros | Simulado | Quantidade de passageiros (variável alvo) |

---

## 📈 Avaliação do Modelo

O modelo Random Forest foi avaliado utilizando:

| Métrica  | Interpretação Rápida                          | Quando usar?                                     |
| -------- | --------------------------------------------- | ------------------------------------------------ |
| **MAE**  | Erro médio absoluto em unidades               | Boa no geral                                     |
| **RMSE** | Erro médio com penalização para grandes erros | Quando grandes erros são críticos                |
| **MAPE** | Erro percentual médio                         | Útil para comparar modelos em escalas diferentes |

Mede a média dos erros absolutos entre os valores previstos e os reais.

É uma métrica direta: quanto menor, melhor.

Exemplo de resultado de avaliação (com dados simulados):
MAE: 36.72
RMSE: 45.81
MAPE: 8.12%


## 💻 Dashboard Interativo
O Dashboard foi desenvolvido com a biblioteca Dash (Plotly). Ele permite:

Entrada manual de variáveis como código da linha, circularidade, chuva, feriado, etc.

Visualização imediata da previsão de demanda de passageiros

Interface responsiva e intuitiva para simulação de cenários




## Previsão: Unidade de Medida
A previsão gerada representa a quantidade estimada de passageiros por viagem de ônibus, com base nas variáveis fornecidas.
 Como os dados são simulados, a unidade de tempo pode ser adaptada (por hora, por dia, por faixa horária) em versões futuras, dependendo da granularidade dos dados reais disponíveis.




 ## Possíveis Melhorias Futuras
-Utilizar dados reais com granularidade por horário (via SPTrans)

-Adicionar mapas interativos (geolocalização das linhas)

-Treinamento com dados históricos reais de fluxo

-Integração com eventos meteorológicos e culturais em tempo real


---

## 💻 Executando o Projeto

### Instalar as dependências:

```bash
pip install -r requirements.txt
```

### Rodar o pipeline de ML:

```bash
python src/ml_pipeline.py
```

### Iniciar o Dashboard:

```bash
python dashboard/dashboard.py
```

✅ Projeto desenvolvido para disciplina de Big Data - Análise Preditiva com Integração de APIs Públicas e Machine Learning.
