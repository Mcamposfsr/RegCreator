from src.utilitarios import para_ascii,normalizar_doc
import random
from faker import Faker
from datetime import date
from ..conexao import Conexao

faker = Faker("pt_BR")

class ModelPessoas:
    def __init__(self,conexao):
        self.conexao:Conexao = conexao

    #PESSOAS 
    def insert_pes(self,tipo_pessoa):

        #SQL TABELAS
        sql = """
        INSERT INTO PESSOAS (
            PES_PESSOA,
            PES_NOME,
            PES_ENDERECO,
            PES_ENDERECO_NO,
            PES_BAIRRO,
            CID_CODIGO,
            PAIS_CODIGO,
            PES_CEP,
            PES_HOME_PAGE,
            PES_CPF_CNPJ,
            PES_EH_CLIENTE,
            PES_EH_FORNECEDOR,
            PES_EH_REPRESENTANTE,
            PES_EH_TRANSPORTADORA,
            ROT_CODIGO
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        RETURNING PES_CODIGO
        """
        valores = (
        tipo_pessoa,# PF/PJ
        para_ascii(faker.name())[:60],# Nome
         para_ascii(faker.city())[:60],# Endereco
        random.randint(1, 100),# Numero
        para_ascii(faker.neighborhood())[:60],# Bairro
        1, # Cod cidade
        1, # Cod pais
        "44900-000",#Cep
        "Teste.com.br",# Home Page
        faker.cpf(),# CPF
        "N",# Cliente
        "N",# Fornecedor
        "S",# Representante
        "N",# Transportadora
        1 #Codigo rota
        )

        return self.conexao.executar_query(sql,valores)


    # PESSOA JURÍDICA
    def insert_pj(self, fk_pessoas):

        sql = """
        INSERT INTO COMPLEMENTO_PES_J (
            PES_CODIGO,
            PES_FANTASIA,
            PES_FUNDACAO,
            PES_CNPJ,
            PES_IE,
            PES_IM,
            PES_SIMPLES,
            PES_APELIDO_PJ,
            PES_ENTE_GOV,
            PES_IRRF,
            PES_CONTR_ICMS,
            PES_CONTR_SUBS,
            PES_TAG,
            PES_IE_FF,
            PES_REGIME
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        # GERANDO VALORES
        fantasia = para_ascii(faker.company())[:25]
        fundacao = faker.date_between(start_date="-50y", end_date="today")

        valores = (
            fk_pessoas,  # FK da tabela PESSOAS
            fantasia,  # Nome fantasia
            fundacao,  # Data de fundação
            faker.cnpj(),  # CNPJ
            "12345678901234",  # Inscrição estadual
            "12345678901234",  # Inscrição municipal
            faker.random_element(["S", "N"]),  # Simples
            fantasia,  # Apelido PJ
            1,  # Ente governamental
            faker.random_element(["S", "N"]),  # IRRF
            faker.random_element(["S", "N"]),  # Contribuinte ICMS
            faker.random_element(["S", "N"]),  # Contribuinte substituto
            1,  # TAG
            "12345678901234",  # Inscrição estadual fora do estado
            1  # Regime
        )
        self.conexao.executar_query(sql,valores)

    # PESSOA FÍSICA
    def insert_pf(self, fk_pessoas):

        sql = """
        INSERT INTO COMPLEMENTO_PES_F (
            PES_CODIGO,
            PES_APELIDO,
            PES_CPF,
            PES_RG
        )
        VALUES (?, ?, ?, ?)
        """

        valores = (
            fk_pessoas,  # FK da tabela PESSOAS
            para_ascii(faker.user_name()[:25]),# Apelido
            faker.cpf(),# CPF
            faker.rg()# RG
        )

        self.conexao.executar_query(sql,valores)

    # CLIENTE
    def insert_cliente(self, fk_pessoas):

        sql = """
        INSERT INTO PESSOA_CLIENTE_F (
            PES_CODIGO,
            PES_PAI,
            PES_MAE,
            PES_SSP,
            PES_ESTADO_CIVIL,
            PES_CONJUGE,
            PES_USA_IE
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        # GERANDO VALORES
        estado_civil =  faker.random_element(["SOL", "CAS", "SEP", "DIV", "VIU"])
        valores = (
            fk_pessoas,  # FK da tabela PESSOAS
            para_ascii(faker.name())[:35],  # Nome do pai
            para_ascii(faker.name())[:35],  # Nome da mãe
            "BA",  # SSP/UF
            estado_civil,  # Estado civil
            para_ascii(faker.name()) if estado_civil == "CAS" else "",  # Cônjuge
            faker.random_element(["S", "N"])  # Usa inscrição estadual
        )

        self.conexao.executar_query(sql,valores)


    # COMPLEMENTO CLIENTE
    def insert_comp_cliente(self, fk_pessoas):

        sql = """
        INSERT INTO COMPLEMENTO_PES_CLIENTE (
            PES_CODIGO,
            EMP_CODIGO,
            SIT_CODIGO,
            CNV_CODIGO,
            FID_CODIGO,
            PES_LIMITE_CREDITO,
            PES_DATA_CADASTRO,
            PES_OBSERVACOES,
            BOL_CODIGO,
            PES_TOLERANCIA_ATRASO,
            PES_PALAVRA_CHAVE,
            PES_CNPJ_AUT_XML
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        # GERANDO VALORES
        limite_credito = faker.pydecimal(
            left_digits=11,
            right_digits=2,
            positive=True
        )

        valores = (
            fk_pessoas,                 # FK da tabela PESSOAS
            1,                          # Empresa
            1,                          # Situação
            1,                          # Convênio
            1,                          # Fidelidade
            limite_credito,             # Limite de crédito
            date.today(),              # Data de cadastro
            "Cadastro gerado para teste",  # Observações
            1,                          # Boleto
            random.randint(1, 30),              # Tolerância de atraso
            "teste",                    # Palavra-chave
            ""                          # CNPJ para autorização XML
        )

        self.conexao.executar_query(sql,valores)


    # CONTATO
    def insert_contatos(self, fk_pessoas):

        sql = """
        INSERT INTO PESSOA_CONTATO (
            PES_CODIGO,
            CTC_NOME,
            CTC_NUMERO,
            CTC_MENSAGEIRO,
            CTC_EMAIL,
            CTC_PREF_XML
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """

        # GERANDO VALORES
        nome = para_ascii(faker.name())[:35]
        telefone = faker.cellphone_number().replace(" ", "").replace("-", "")
        email = nome.lower().replace(" ", ".") + "@example.com"

        valores = (
            fk_pessoas,  # FK da tabela PESSOAS
            nome,  # Nome do contato
            telefone,  # Número de telefone
            faker.random_element(["S", "N"]),  # Mensageiro
            email,  # E-mail
            faker.random_element(["S", "N"]),  # Preferência XML
        )

        self.conexao.executar_query(sql,valores)

