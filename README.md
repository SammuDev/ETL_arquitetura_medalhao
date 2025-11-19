**`ETL Arquitetura Medalhão`**

## Extração (Bronze Layer):

• Extraí dados de API

• Realizei a leitura de diferentes fontes de arquivos como JSON e CSV

## Transformação (Silver Layer):

• Utilizei o conceito de classes com funções dedicadas para manipulação dos dados

• Realizei a Normalização e o Tratamento de Dados (limpeza, padronização, etc..)

• Transformei e salvei os dados limpos e estruturados no formato .parquet (excelente para performance)

## Carga e Análise (Gold Layer):

• Containerização: Iniciei a configuração com docker-compose para criar um container Docker

• Conectamos o projeto a um banco de dados PostgreSQL para ler os arquivos .parquet e materializar os dados em tabelas estruturadas

• Análise: Criei um arquivo .sql com queries (como JOINs) para análises e relatórios de negócio

• Para finalizar, criei um notebook .ipynb para fins de visualização do DataFrame e visualização dos dados em formato de tabela com Matplotlib

## Stacks do projeto

⇛ Python (para o pipeline ETL)

⇛ Docker / Docker Compose (Containerização)

⇛ PostgreSQL (Banco de Dados)

⇛ SQL (Consultas e Análises)

⇛ Jupyter Notebook / Matplotlib (Visualização)

## Skills

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)

[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](#)

[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=fff)](#)

[![Jupyter](https://img.shields.io/badge/Jupyter-ffffff?logo=Jupyter)](#)
