# Aprendendo SQL PYTHON

**O que são tabelas?**

## Tabelas são como se fossem listas, elas são usadas para armazenar dados, elas são criadas com o comando CREATE TABLE e elas são compostas por colunas e linhas, as colunas são as propriedades dos objetos e as linhas são os objetos em si.

_Relacionais_

# Aqui a gente trabalha com tabelas que tem relacionamentos entre elas, como por exemplo, uma tabela de clientes e uma tabela de pedidos, onde cada pedido tem um cliente associado a ele. Tabelas que são uma estrutura de dados que a gente cria e precisa respeitar na hora de inserir dados.

_Não Relacionais_

# Aqui a gente trabalha com tabelas que não tem relacionamentos entre elas, como por exemplo, uma tabela de produtos e uma tabela de clientes, onde cada produto pode ser comprado por qualquer cliente. Bancos não relacionais, não exigem essa estrutura de dados, e são muito mais livre para inserir os dados no formato que a gente quiser.

---

**Banco De Dados**

_criando tabelas_

```sql

CREATE TABLE contas_bancarias (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  titular TEXT NOT NULL,
  saldo FLOAT NOT NULL,
  cpf TEXT NOT NULL UNIQUE
)

```

_inserindo dados_

```sql

INSERT INTO pessoas(nome, idade, email) VALUES('Jeff', 1000.50, '123.456.789-10');

```

_Obtendo com dados_

```sql

SELECT titular, saldo FROM contas_bancarias
WHERE saldo < 0

```

vai mostrar tipo o nome e o saldo das pessoas que tem saldo negativo

_Atualizando dados_

```sql


UPDATE contas_bancarias
SET saldo = 2000
WHERE cpf = '123.456.789-10'

```

vai atualizar o saldo da pessoa que tem o cpf 123.456.789-10

_Deletando dados_

```sql

DELETE FROM contas_bancarias
WHERE id = 1

```

vai deletar a pessoa que tem o id 1

_Conectando com o banco de dados_

```python

import sqlite3 # vai importar o modulo sqlite3

conexao = sqlite3.connect('banco.db') # vai criar um banco de dados

cursor = conexao.cursor() # vai criar um cursor para fazer as consultas

contas = cursor.fetchall() # vai trazer todos os dados do banco de dados

```

_Fechando a conexão com o banco de dados_

```python

conexao.close() # vai fechar a conexão com o banco de dados

```
