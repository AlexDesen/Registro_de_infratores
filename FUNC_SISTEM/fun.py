def cadastro_infrator(cursor,conexao):
     
    print("--------------------------------")  
    print("Área para cadastro do infrator.")
    infrator = input(" Nome do infrator: ")
    cpf = input("CPF do infrator: ")
    nome_pai = input("Nome do pai do infrantor: ")    
    nome_mae = input("Nome da mãe do infrator: ")           
    print("--------------------------------")        
    inserir = '''INSERT INTO cadastro_infrator (infrator, cpf, nome_pai, nome_mae) 
    VALUES(?,?,?,?)''';     
    valor = [infrator, cpf, nome_pai, nome_mae]
    cursor.execute(inserir, valor)
    conexao.commit()
    conexao.close()
    print("Cadastro realizado com sucesso!")