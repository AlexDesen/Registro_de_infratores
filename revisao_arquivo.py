import sqlite3
import datetime

conect = sqlite3.connect('db.sqliteData')
# INDENTIFICANDO CLIENTE E DATA
data = datetime.date.today()
cliente_id = int(input('DIGITE O ID DO CLIENTE: '))
valores = [data,cliente_id]
sql = '''INSERT INTO pedido (data, cliente_id) VALUES (?,?);'''
cursor = conect.cursor()
cursor.execute(sql, valores)
conect.commit()
print('DADOS INSERIDOS COM SUCESSO!')
# TABELA DE PEDIDO
tabela_pedido = '''SELECT * FROM pedido'''
execute = cursor.execute(tabela_pedido)
for imprime in execute:
    print('ID;',imprime[0],'DATA;', imprime[1], 'CLIENTE_ID:', imprime[2])
print('ID do pedido:',cursor.lastrowid) 
#INSERINDO PEDIDOS
quantidade_itens = int(input('DIGITE A QUNTIDADE DE ITENS: '))
for i in range(quantidade_itens):
    pedido_id = cursor.lastrowid
    produto = input('DIGITE O NOME DO PRODUTO: ')
    valor = int(input('DIGITE O VALOR DO PRODUTO: '))
    quantidade = int(input('DIGITE A QUANTIDADE DO PRODUTO: '))
    valores = [pedido_id, produto, valor, quantidade ]
    sql = '''INSERT INTO itens_pedido (pedido_id, produto, valor, quantidade) VALUES (?,?,?,?);'''
    cursor.execute(sql,valores)
sql = '''SELECT * FROM itens_pedido;''' 
execute = cursor.execute(sql) 
for i in execute: 
    print('ID:',i[0],'PEDIDO_ID:',i[1],'PRODUTO:',i[2],'VALOR:',i[3],'QUANTIDADE:',i[4])
conect.commit()    
conect.close()
print('INDENTIFICAMOS O CLIENTE E DATA DO PEDIDO')