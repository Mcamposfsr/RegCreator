from src.models.pessoa import ModelPessoas
from src.models.dependencias_pessoas import ModelDummyPessoas
from src.conexao import Conexao

class Controle:
    def __init__(self,conexao: Conexao):
        self.conexao = conexao
        self.model_pessoas = ModelPessoas(self.conexao)
        self.model_dummy_pessoas = ModelDummyPessoas(self.conexao)

    def verificar_dependencias_pessoas(self):
        # ESTADOS
        if not self.model_dummy_pessoas.select_estados():
            self.model_dummy_pessoas.insert_estados()

        # CIDADES
        if not self.model_dummy_pessoas.select_cidades():
            self.model_dummy_pessoas.insert_cidades()

        # EMPRESA - PARA BANCOS NOVOS
        if not self.model_dummy_pessoas.select_empresa():
            self.model_dummy_pessoas.insert_empresa()


        # ROTAS
        if not self.model_dummy_pessoas.select_rotas():
            self.model_dummy_pessoas.insert_rotas()

        # SITUACOES
        if not self.model_dummy_pessoas.select_situacoes():
            self.model_dummy_pessoas.insert_situacoes()

        # CONVENIOS
        if not self.model_dummy_pessoas.select_convenios():
            self.model_dummy_pessoas.insert_convenios()

        # BOLETOS
        if not self.model_dummy_pessoas.select_boletos():
            self.model_dummy_pessoas.insert_boletos()

        
    def gerar_pessoas(self,tipo_pessoa,eh_cliente,quantidade_contatos,quantidade_registros):

        #Execucao da geração de registros
        def gerar_registros():

            #Verificar dependências
            self.verificar_dependencias_pessoas()

            for I in range(quantidade_registros):
            #Geração do registro PK
                #Pessoa
                id_pessoa = self.model_pessoas.insert_pes(tipo_pessoa)
                
                #PF/PJ
                if tipo_pessoa == "F": 
                    self.model_pessoas.insert_pf(id_pessoa)
                elif tipo_pessoa == "J": 
                    self.model_pessoas.insert_pj(id_pessoa)

                #Cliente
                if eh_cliente:
                    self.model_pessoas.insert_cliente(id_pessoa)
                    self.model_pessoas.insert_comp_cliente(id_pessoa)

                #Contatos
                for J in range(quantidade_contatos):
                    self.model_pessoas.insert_contatos(id_pessoa)

        self.conexao.em_transacao(gerar_registros)


    def fechar_conexao(self):
        self.conexao.finalizar_conexao()
