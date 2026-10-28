from firebird.driver import connect , driver_config
from Queries import gerar_query_pessoas,gerar_query_pj,gerar_query_pf,gerar_query_cliente,gerar_query_comp_cliente,gerar_query_contatos
from utilitarios import input_validado
from config import gerar_ini,verificar_ini,carregar_ini

#Conexão ao banco
def gerar_conexao():
    config_ini = carregar_ini()
        
    #Configuração driver FB
    driver_config.fb_client_library.value = config_ini["dll"]
    #Conectar
    conexao = connect(
        database=config_ini["banco"], 
        user=config_ini["usuario"],
        password=config_ini["senha"],
        charset="UTF8",
    )

    cursor = conexao.cursor()
    print("Conexão estabelecida com sucesso!")

    return conexao,cursor

#Geração dos registros
def gerar_registros_pk(cursor,query,quantidade):
    for i in range(quantidade):
        valores,sql = query()
        cursor.execute(sql,valores)

        #Buscar id
        resultado = cursor.fetchone()
        id_pessoa = resultado[0]
        
    return id_pessoa

def gerar_registros_pk_parametrizado(cursor,query,quantidade,parametro):
    for i in range(quantidade):
        valores,sql = query(parametro)
        cursor.execute(sql,valores)

        #Buscar id
        resultado = cursor.fetchone()
        id_pessoa = resultado[0]            
    return id_pessoa



def gerar_registros_fk(cursor,fk,query,quantidade):
    for i in range(quantidade):
        valores,sql = query(fk)
        cursor.execute(sql,valores)







# ------------------------------------------------------------------- PROGRAMA -------------------------------------------------------------------
#Execucao do programa
def main(): 
    # ***** Preset: *****

    #Receber configuração
    def receber_configuracao():
        if not verificar_ini():
            fb_dll = (input("Caminho da dll fbclient x64:\n"))
            db_path = (input("caminho do banco: \n"))
            db_user = (input("User: \n"))
            db_pass = (input("Passworld: \n"))
            
            gerar_ini(fb_dll,db_path,db_user,db_pass) 


    #Verifica PF/PJ
    def receber_info_pessoa():
        tipo_pessoa = input("Qual o tipo da pessoa dos registros? (PF/PJ):\n")
        if tipo_pessoa not in ["pf","PF","Pf","pF","pj","PJ","pJ","Pj"]:
            raise Exception("Valor inválido, digite PF ou PJ")
        elif tipo_pessoa in ["pf","PF","Pf","pF"]:
            return "F"
        elif tipo_pessoa in ["pj","PJ","pJ","Pj"]:
            return "J"

    #Verificar se é cliente
    def receber_info_cliente():
        eh_cliente = input("Pessoas devem ser clientes? (S/N):\n")
        if eh_cliente not in ["S","N","s","n"]:
            raise Exception("Valor inválido, digite S ou N")
        elif eh_cliente in ["S","s"]:
            return True
        elif eh_cliente in ["N","n"]:
            return False

    #Verificar quantidade de contatos
    def receber_quantidade_contatos():
        try:
            quantidade_contatos =  int(input("Quantos contatos cada registro deve ter?\n"))
    
            return quantidade_contatos
        except: 
            raise Exception("Digite um valor válido!")
    
    #Receber quantidade de registros
    def receber_numero_registros():
        return int((input("Qual a quantidade de registros você deseja gerar?\n")))

    #Verificar nova execução
    def receber_finalizacao():
        finalizacao = input("Inserir mais regitros? (S/N):")
        if finalizacao not in ["S","N","s","n"]:
            raise Exception("Valor inválido, digite S ou N")
        #Continuar programa
        elif finalizacao in ["S","s"]:
            return False
        #Finalizar programa
        elif finalizacao in ["N","n"]:
            return True
       

    # ***** Execucao: ***** -> Melhor tratamento da conexão e passagem da configuração!

    print(" ------------ Bem vindo ------------ ");

    
    #Conectar ao BD
    input_validado(lambda: receber_configuracao(),'')
    conexao,cursor =  gerar_conexao()

    #UI
    print("Configure a geração:");

    #Verificar tipo pessoa
    tipo_pessoa = input_validado(lambda: receber_info_pessoa(),'')

    #Verificar se é cliente
    info_cliente = False
    if tipo_pessoa == "F":
        info_cliente = input_validado(lambda: receber_info_cliente(),'') 

    #Verificar quantidade de contatos por pessoa
    quantidade_contatos = input_validado(lambda: receber_quantidade_contatos(),'')
        
    #Verificar quantidade registros
    quantidade_registros = input_validado(lambda: receber_numero_registros(),'Informe um valor válido!') 

    try:
        try:
            #Controle de execução
            parar_programa = False
            while not parar_programa:

                #Geração de registros
                for I in range(quantidade_registros):
                    #Geração do registro PK

                    #Pessoa
                    id_pessoa = gerar_registros_pk_parametrizado(cursor,gerar_query_pessoas,1,tipo_pessoa)
                    
                    #PF/PJ
                    if tipo_pessoa == "F": 
                        gerar_registros_fk(cursor,id_pessoa,gerar_query_pf,1)
                    elif tipo_pessoa == "J": 
                        gerar_registros_fk(cursor,id_pessoa,gerar_query_pj,1)
                    
                    if info_cliente:
                        gerar_registros_fk(cursor,id_pessoa,gerar_query_cliente,1)
                        gerar_registros_fk(cursor,id_pessoa,gerar_query_comp_cliente,1)

                    gerar_registros_fk(cursor,id_pessoa,gerar_query_contatos,quantidade_contatos)

                #Persistir dados
                conexao.commit()
                print("Registros gerados!")

                #Verificar nova execucao
                parar_programa = input_validado(lambda: receber_finalizacao(),'')

        except Exception as E:
            print(f"Falha na criação dos registros. Error:\n {E}")
            conexao.rollback()
    
    finally:
        #Finalização
        cursor.close()
        conexao.close()

# ------------------------------------------------------------------- CHAMDA -------------------------------------------------------------------

main()


    

