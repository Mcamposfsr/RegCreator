
from src.config import ConfigIni
from firebird.driver import connect , driver_config

class Conexao:
    def __init__(self):
        self.conexao = None 

    #Leitura do arquivo de configuração para conexão
    def iniciar_conexao(self):
        config_ini = ConfigIni.carregar_ini()
            
        #Configuração driver FB
        driver_config.fb_client_library.value = config_ini["dll"]
        try:
            #Conectar
            self.conexao = connect(
                database=config_ini["banco"], 
                user=config_ini["usuario"],
                password=config_ini["senha"],
                charset="UTF8",
            )
            return True, None
        except Exception as E:
            return False,E


    #Finalizar conexao
    def finalizar_conexao(self):
        if self.conexao is not None:
            self.conexao.close()
            self.conexao = None

    #Teste de conexao
    def testar_conexao(self,dll_path,db_path,db_user,db_pass):
        #Configuração driver FB
        driver_config.fb_client_library.value = dll_path
        #Conectar
        try:
            conexao_teste = None
            try:
                conexao_teste = connect(
                    database=db_path, 
                    user=db_user,
                    password=db_pass,
                    charset="UTF8",
                )
        
                conexao_teste.close()
                
                return True, ""
            except Exception as E:
                return False, str(E)
        finally:
            if conexao_teste is not None:
                conexao_teste.close()

    #Executar em transacao
    def em_transacao(self,procedure):
        try:
            procedure()
            self.conexao.commit()
        except Exception as E:
            self.conexao.rollback()
            raise E
            
    #Executar query
    def executar_query(self,sql,valores):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(sql,valores)

            #Buscar id
            resultado = cursor.fetchone()
            if resultado is None:
                return ""
            else:
                id = resultado[0]
                return id
        finally:
            cursor.close()

    #Executar query
    def executar_query_consulta(self,sql,valores=()):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(sql,valores)

            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()

    
        
        
        

