from src.utilitarios import input_validado
from src.config import ConfigIni
from src.conexao import Conexao
from src.controle import Controle

# ------------------------------------------------------------------- PROGRAMA -------------------------------------------------------------------
class Main():
    conexao:Conexao  = None
    controle:Controle  = None

    #ENTRADA DA APLICAÇÃO
    def run_main(self):
        try:
            print(" ------------ Bem vindo ------------ ")
            self.initialize()
            self.run_pessoas()
        finally:
            if self.controle is not None:
                self.controle.fechar_conexao()

    # INICIALIZAÇÃO DA APLICAÇÃO
    def initialize(self):
        #Inicializando componentes
        self.conexao = Conexao()
        self.controle = Controle(self.conexao)

        #Configurar conexao
        if not ConfigIni.verificar_ini():
            estado_config_inicial = False
            while not estado_config_inicial:
                fb_dll = (input("Caminho da dll fbclient x64:\n")).strip()
                db_path = (input("caminho do banco: \n")).strip()
                db_user = (input("User: \n")).strip()
                db_pass = (input("Passworld: \n")).strip()

                estado_config_inicial,error = self.conexao.testar_conexao(fb_dll,db_path,db_user,db_pass)
                if not estado_config_inicial:
                    print(f"Falha ao acessar o banco, verifique as credênciais utilizadas! Error:\n {error}")
                else:
                    ConfigIni.gerar_ini(fb_dll,db_path,db_user,db_pass)

        #Iniciar conexao
        estado_conexao = False
        while not estado_conexao:
            estado_conexao,error = self.conexao.iniciar_conexao()
            if not estado_conexao:
                print(f"Ocorreu uma falha ao tentar se conectar com o banco. \n Error: {error} \n Oque deseja fazer?")
                print("[1] - Tentar novamente")
                print("[2] - Configurar conexao novamente")
                estado_input = False;
                while not estado_input:
                    opcao = input("\n")
                    if opcao not in ["1","2"]:
                        print("Opção inválida, selecione uma das opções informadas")
                    else:
                        estado_input = True;
                if opcao == "1":
                    continue
                elif opcao == "2":
                    ConfigIni.deletar_ini()
                    return self.initialize()

    #FLUXO PESSOAS
    def run_pessoas(self):
        # ***** Preset: *****
    
        #Verifica PF/PJ
        def receber_info_pessoa():
            tipo_pessoa = input("Qual o tipo da pessoa dos registros? (PF/PJ):\n").strip().upper()
            if tipo_pessoa not in ["PF","PJ"]:
                raise Exception("Valor inválido, digite PF ou PJ")
            elif tipo_pessoa == "PF":
                return "F"
            elif tipo_pessoa == "PJ":
                return "J"
    
        #Verificar se é cliente
        def receber_info_cliente():
            eh_cliente = input("Pessoas devem ser clientes? (S/N):\n").strip().upper()
            if eh_cliente not in ["S","N"]:
                raise Exception("Valor inválido, digite S ou N")
            elif eh_cliente == "S":
                return True
            elif eh_cliente == "N":
                return False
    
        #Verificar quantidade de contatos
        def receber_quantidade_contatos():
            try:
                quantidade_contatos =  int(input("Quantos contatos cada registro deve ter?\n"))
            except: 
                raise Exception("Digite um valor válido!")
            if quantidade_contatos < 0:
                raise ValueError("A quantidade não pode ser negativa.")
            
            return quantidade_contatos

            
        
        #Receber quantidade de registros
        def receber_numero_registros():
            quantidade_registros = int((input("Qual a quantidade de registros você deseja gerar?\n")))
            if quantidade_registros <= 0:
                raise ValueError("Informe uma quantidade maior que zero.")
            return quantidade_registros 
    
        #Verificar nova execução
        def receber_finalizacao():
            finalizacao = input("Deseja continuar? (S/N):\n").strip().upper()
            if finalizacao not in ["S","N"]:
                raise Exception("Valor inválido, digite S ou N")
            #Continuar programa
            elif finalizacao == "S":
                return True
            #Finalizar programa
            elif finalizacao == "N":
                return False
               
        
        # ***** Execucao: ******
        continuar = True;
        while continuar:
            #UI
            print("###### CONFIGURANDO A GERAÇÃO #####");
        
            #Verificar tipo pessoa
            tipo_pessoa = input_validado(receber_info_pessoa,'')
        
            #Verificar se é cliente
            info_cliente = False
            if tipo_pessoa == "F":
                info_cliente = input_validado(receber_info_cliente,'') 
        
            #Verificar quantidade de contatos por pessoa
            quantidade_contatos = input_validado(receber_quantidade_contatos,'')
                
            #Verificar quantidade registros
            quantidade_registros = input_validado(receber_numero_registros,'Informe um valor válido!') 

            print('Gerando registros.....');

            #Execucao:
            try:
                self.controle.gerar_pessoas(tipo_pessoa,info_cliente,quantidade_contatos,quantidade_registros)
                print('Registros gerados com sucesso!')
            except Exception as E:
                print(f"Falha na criação dos registros. Error:\n {E}")

            #Verificar repeticao do fluxo
            continuar = input_validado(receber_finalizacao,'')

# ------------------------------------------------------------------- CHAMDA -------------------------------------------------------------------
programa = Main()
#Entrada da aplicação
programa.run_main()







    

