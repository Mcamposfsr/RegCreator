from firebird.driver import connect , driver_config
from Generator import gerar_registro_pessoas
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
def gerar_registros(quantidade_registros: int,cursor,conexao):
    try:
        #Geração dos registros
        for I in range(quantidade_registros):
            valores,sql = gerar_registro_pessoas()
            cursor.execute(sql,valores)

        #Persistência
        conexao.commit()
        #Finalização
        cursor.close()
        conexao.close()

        print("Registros gerados!")
    except Exception as E:
            print(f"Erro ao executar script: {E}")


# ------------------------------------------------------------------- PROGRAMA -------------------------------------------------------------------
#Execucao do programa
def main(): 
    # ***** Preset: *****
    
    #Receber quantidade de registros
    def receber_numero_registros():
        return int((input("Qual a quantidade de registros você deseja gerar?\n")))

    #Receber configuração
    def receber_configuracao():
        if not verificar_ini():
            fb_dll = (input("Caminho da dll fbclient x64:\n"))
            db_path = (input("caminho do banco: \n"))
            db_user = (input("User: \n"))
            db_pass = (input("Passworld: \n"))
            
            gerar_ini(fb_dll,db_path,db_user,db_pass) 

    # ***** Execucao: *****

    print("Bem vindo - Configure a geração:");
    
    #Conectar ao BD
    input_validado(lambda: receber_configuracao(),'')
    conexao,cursor =  gerar_conexao()

    #Geração de registros
    quantidade_registros = input_validado(lambda: receber_numero_registros(),'Informe um valor válido!')
    gerar_registros(quantidade_registros,cursor,conexao)

     
# ------------------------------------------------------------------- CHAMDA -------------------------------------------------------------------

main()


    

