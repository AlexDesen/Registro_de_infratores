import sqlite3
from FUNC_SISTEM.fun import cadastro_infrator



conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
while opcao != 3:
    print("-------------------------------")
    print("Digite uma das opção")
    print('1 - para cadastrar.')
    print("2 - para consulta.")
    print("3 - para sair.")
    print("-------------------------------")
    print()
    opcao = int(input("Digite uma das opções: "))


    if opcao == 1:
        cadastro_infrator(cursor,conexao)
        
           
         
              
        
