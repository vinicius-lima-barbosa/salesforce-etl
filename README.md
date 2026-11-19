# SalesFlow ETL

Pipeline de dados desenvolvida em Python para extrair dados comerciais de uma API, validar e transformar os dados e carregá-los em um banco de dados PostgreSQL.

O projeto utiliza dados da DummyJSON e tem como objetivo demonstrar um fluxo simples de engenharia de dados (ETL).

# Fluxo

1. **Extração:** coleta dos dados de carrinhos e produtos por meio da API DummyJSON.
2. **Validação:** verifica se os dados recebidos possuem a estrutura e os campos esperados.
3. **Transformação:** organiza e transforma os dados em DataFrames utilizando Pandas.
4. **Carga:** armazena os dados no PostgreSQL, atualizando registros existentes quando necessário.
5. **Análise:** disponibiliza consultas SQL para analisar vendas, produtos e clientes.

## Tecnologias

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Docker
- Pytest

## Execução

Configure o ambiente python com:

```bash
make setup
```

Com o ambiente configurado e o banco de dados em execução, execute:

```bash
make run
```

## Testes

Execute os testes automatizados com:

```bash
make test
```

## Análises SQL

O projeto possui consultas SQL para:

- Resumo geral das vendas.
- Desempenho por produto.
- Desempenho por cliente.

As consultas estão disponíveis em `sql/analytics/`.

## Logs

As execuções da pipeline são registradas no terminal e no arquivo `logs/pipeline.log`.

## Status

Em desenvolvimento.
