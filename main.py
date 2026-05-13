#Preparando ambiente
import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#Criando tabelas
cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              titular TEXT NOT NULL,
              saldo FLOAT NOT NULL,
              cpf TEXT NOT NULL UNIQUE
              )""")

#Inserindo dados
# cursor.execute("""INSERT INTO contas_bancarias 
#                (titular, saldo, cpf) 
#                VALUES ('Gabriela', 100.000, '123.456.789-13')""")



#Obtendo com dados
# cursor.execute("""SELECT titular, saldo FROM contas_bancarias
#                   WHERE saldo < 0
#                """)

#Deletando dados
# cursor.execute("""DELETE FROM contas_bancarias
#                   WHERE id = 1
#                """)

#Atualizando valores
# cursor.execute("""UPDATE contas_bancarias 
#                SET saldo = 100000000.00
#                WHERE id = 4 
#                """)



#Consultando dados
contas = cursor.fetchall()

for conta in contas:
    titular, saldo = conta
    print(f"""
              Titular: {titular}
              Saldo: {saldo}
              """)
    print("\n")
    
#Salvando alterações
conexao.commit()