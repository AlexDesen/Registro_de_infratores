import datetime

def cadastro_registro(cursor,conexao):
    print("--------------------------------")
    # INSERINDO CADASTRO DO INFRATOR  
    print("Área para cadastro do infrator.")
    infrator = input(" Nome do infrator: ")
    cpf = input("CPF do infrator: ")
    nome_pai = input("Nome do pai do infrantor: ")    
    nome_mae = input("Nome da mãe do infrator: ")           
    print("--------------------------------")        
    inserir = '''INSERT INTO cadastro_infrator (infrator, cpf, nome_pai, nome_mae) 
    VALUES(?,?,?,?)''';     
    valor = [infrator, cpf, nome_pai, nome_mae]
    comando = cursor.execute(inserir, valor)
         
    # INSERINDO REGISTRO   
    data_do_registro = datetime.date.today()
    id_cadastro_infrator = cursor.lastrowid
    valores = [id_cadastro_infrator, data_do_registro]
    inserir_registro = '''INSERT INTO registro(id_cadastro_infrator, data_do_registro )
     VALUES(?,?)'''
    cursor.execute(inserir_registro, valores)
    conexao.commit()    
    conexao.close()
    print("Cadastro e registro realizado com sucesso!")

