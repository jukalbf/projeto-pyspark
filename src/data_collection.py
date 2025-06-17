import requests
import pandas as pd
import json
import os

os.makedirs("data/raw", exist_ok=True)

TOKEN = '6ff041a582cca5e890789498dd2e38ecf68fb2ad2ea830a0ada4002e2a405c80'

session = requests.Session()
login_url = f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={TOKEN}"
resp_login = session.post(login_url)

if resp_login.status_code == 200 and resp_login.text == "true":
    print("Autenticado com sucesso na API SPTrans")
else:
    print("Falha na autenticação SPTrans:", resp_login.text)

linhas_url = "http://api.olhovivo.sptrans.com.br/v2.1/Posicao"
resp_linhas = session.get(linhas_url)
linhas = resp_linhas.json()

with open("data/raw/sptrans_linhas.json", "w", encoding="utf-8") as f:
    json.dump(linhas, f, ensure_ascii=False, indent=4)

df_linhas = pd.DataFrame(linhas)
df_linhas.to_csv("data/raw/sptrans_linhas.csv", index=False)
print("Linhas SPTrans salvas com sucesso em CSV e JSON.")

url_ibge = "https://servicodados.ibge.gov.br/api/v3/agregados"
response = requests.get(url_ibge)
dados_ibge = response.json()

with open("data/raw/ibge_mobilidade.json", "w", encoding="utf-8") as f:
    json.dump(dados_ibge, f, ensure_ascii=False, indent=4)
print("IBGE Mobilidade salvo com sucesso.")
