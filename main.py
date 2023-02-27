import sqlite3
from FUNC_SISTEM.fun import cadastro_registro, pesquisa_cadastro, registro



conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()

pesquisa_cadastro(cursor)
opcao = None
while opcao != 4:
   
    print("-------------------------------")
    print("Digite uma das opção")
    print('1 - para realizar uma nova pesquisa')
    print('2 - para cadastrar e resgistro.')
    print('3 - para registro ')
    print("4 - para sair.")
    print("-------------------------------")
    print()
    opcao = int(input("Digite uma das opções: "))    


    if opcao == 1:
       pesquisa_cadastro(cursor)
    
    elif opcao == 2:
        cadastro_registro(cursor,conexao)
    
    elif opcao == 3:
        registro(cursor, conexao)

    elif opcao == 4:    
        print("O programa foi encerrado.") 
        break

    


               
      
