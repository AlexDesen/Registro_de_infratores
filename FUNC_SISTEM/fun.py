import datetime
import sqlite3

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()

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
    # INSERINDO DESCRIÇÃO REGISTRO 
    id_registro = cursor.lastrowid
    data_infracao = input("Digite data de infração: ")
    descricao_infracao = input("Descreva o ocorrido: ")
    vitimas = input("Declare as vítimas involvidas: ")
    valores = [id_registro, data_infracao, descricao_infracao,vitimas]
    inserir_decricao_ocorrido = '''INSERT INTO
     descricao_ocorrido(id_registro, data_infracao, descricao_infracao, vitimas) 
     VALUES(?,?,?,?)'''
    cursor.execute(inserir_decricao_ocorrido, valores)
    conexao.commit()    
    conexao.close()
    print("Cadastro e registros realizados com sucesso!")




def pesquisa_cadastro(cursor):
    # CHECAGEM DE CADASTRO
    print("-------------------------------") 
    print('CADASTRO:')
    print()
    cpf =input("Informe o cpf para pesquisa: ")
    sql = '''SELECT * FROM cadastro_infrator WHERE cpf = ?; '''
    valores = [cpf]
    a = cursor.execute(sql, valores)
    resultado = 0 
    for i in a:
      resultado = i[0]
      id_cadastro_infrator = i[0]
    if resultado > 0:
      print("Este cpf existe em nosso cadastro.")
      print('Confira os dados abaixo:')     
      print('Infrator:',i[1],'CPF:',i[2],'Nome da mãe:',i[3], 'Nome do pai:',i[4])
      print()
      print("-------------------------------") 
    # Imprimindo registro
      print('RESGISTRO(os):')
      
      valor = [id_cadastro_infrator]
      sql = '''SELECT * FROM registro WHERE id_cadastro_infrator = ?; '''    
      registro = cursor.execute(sql, valor)
      for i in registro:
        print(i[2])
        id_cadastro_infrator = i[1]
        print()  
      print("-------------------------------")   
      # Imprimindo a istânica selecionada da tabela descricao_ocorrido
      print('DESCRIÇÃO DO REGISTRO:')
      print()
      valor_descricao = [id_cadastro_infrator]
      sql_descricao = '''SELECT d.data_infracao, d.descricao_infracao, d.vitimas
       FROM registro as r, descricao_ocorrido as d WHERE d.id_registro = r.id
        AND r.id_cadastro_infrator = ?;'''
      descricao_cadastro = cursor.execute(sql_descricao, valor_descricao)
      for i in descricao_cadastro:
        print('Ocorrência em',i[0],'Delito:',i[1],'Vitima(s):',i[2])

    else:
       print("Não existe registro para o portador deste cpf:",cpf)


def registro(cursor, conexao):
  # adquirindo id da tabela cadastro
  cpf = input("Digite o cpf do infrator: ") 
  sql ='''SELECT *FROM cadastro_infrator WHERE cpf = ?'''  
  valor = [cpf]
  execute = cursor.execute(sql, valor)
  registro = 0
  for i in  execute:
    registro = i[0]
    id_cadastro_infrator = i[0]
  if registro == 0:
     print("CPF não incontrado,terá que realizar o casdastro.")
  else:
    
    data = datetime.date.today()
    valores = [id_cadastro_infrator, data]
    registro = '''INSERT INTO registro(id_cadastro_infrator, data_do_registro )
      VALUES(?,?)'''  
    cursor.execute(registro, valores)
 # INSERINDO DESCRIÇÃO REGISTRO
    print('-------------------------')
    print('CRIANDO REGISTRO:') 
    print()
    id_registro = cursor.lastrowid
    data_infracao = input("Digite a data de infração: ")
    descricao_infracao = input("Descreva o ocorrido: ")
    vitimas = input("Declare a(as) vítima(as) involvida(as): ")
    valores = [id_registro, data_infracao, descricao_infracao,vitimas]
    inserir_decricao_ocorrido = '''INSERT INTO
    descricao_ocorrido(id_registro, data_infracao, descricao_infracao, vitimas) 
    VALUES(?,?,?,?)'''
    cursor.execute(inserir_decricao_ocorrido, valores)
    conexao.commit()    
    conexao.close()
    print("Cadastro e registros realizados com sucesso!")
  
  

