
# Projeto BigData - Transporte Público Inteligente

Este projeto utiliza dados do SPTrans, IBGE e outros para prever demanda e otimizar rotas usando PySpark e Machine Learning.

## Estrutura

- data/raw: dados brutos
- data/processed: dados tratados
- data/models: modelos treinados
- src/: código principal (coleta, processamento, ML e dashboard)
- notebooks/: notebooks de análise
- reports/: relatório final

## Execução

1. Coletar dados (src/data_collection.py)
2. Processar dados (src/data_processing.py)
3. Treinar ML (src/ml_pipeline.py)
4. Rodar dashboard (src/dashboard.py)
