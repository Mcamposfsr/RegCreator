from utilitarios import para_ascii,normalizar_doc
import random
from faker import Faker
from datetime import date

faker = Faker("pt_BR")

#PESSOAS 
def gerar_query_pessoas(tipo_pessoa):

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
        PES_EH_TRANSPORTADORA
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    RETURNING PES_CODIGO
    """

    #GERANDO VALORES
    nome = para_ascii(faker.name())
    endereco = para_ascii(faker.city())
    bairro = para_ascii(faker.neighborhood())
    numero = random.randint(1, 100)
    cpf = normalizar_doc(faker.cpf())

    valores = (
    tipo_pessoa,
    nome,
    endereco,
    numero,
    bairro,
    1,
    1,
    "44900-000",
    "Teste.com.br",
    cpf,
    "N",
    "N",
    "S",
    "N"
    )
    return valores,sql


#PESSOA JURÍDICA
def gerar_query_pj(fk_pessoas):

    #SQL TABELAS
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
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
    """

    #GERANDO VALORES
    fantasia = para_ascii(faker.company())
    fundacao = faker.date_between(start_date="-50y", end_date="today")
    cnpj = faker.cnpj()

    valores = (
    fk_pessoas,
    fantasia,
    fundacao,
    cnpj,
    "12345678901234",
    "12345678901234",
    faker.random_element(["S", "N"]),
    fantasia,
    1,
    faker.random_element(["S", "N"]),
    faker.random_element(["S", "N"]),
    faker.random_element(["S", "N"]),
    1,
    "12345678901234",
    1
    )
    return valores,sql


#PESSOA FÍSICA 
def gerar_query_pf(fk_pessoas):
    #SQL TABELAS
    sql = """
    INSERT INTO COMPLEMENTO_PES_F (
        PES_CODIGO,
        PES_APELIDO,
        PES_CPF,
        PES_RG
    )
    VALUES (?, ?, ?, ?)
    """

    #GERANDO VALORES
    cpf = faker.cpf()
    rg = faker.rg()
    apelido = faker.user_name()[:35]

    valores = (
    fk_pessoas,
    apelido,
    cpf,
    rg
    )

    return valores,sql

#CLIENTE 
def gerar_query_cliente(fk_pessoas):
    #SQL TABELAS

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
    VALUES (?, ?, ?, ?, ?, ? ,?)
    """

    #GERANDO VALORES
    pai = para_ascii(faker.name())
    mae = para_ascii(faker.name())
    estado_civil = faker.random_element(["SOL", "CAS", "SEP", "DIV", "VIU"])

    valores = (
    fk_pessoas,
    pai,
    mae,
    "BA",
    estado_civil,
    para_ascii(faker.name()) if estado_civil == "CAS" else "",
    faker.random_element(["S", "N"])
    )

    return valores,sql


#Complemento Cliente
def gerar_query_comp_cliente(fk_pessoas):
    #SQL TABELAS
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

    #GERANDO VALORES
    limite_credito = faker.pydecimal(left_digits=11, right_digits=2, positive=True)
    data_cadastro = date.today() 
    limite_atraso = random.randint(1,30)

    valores = (
    fk_pessoas,
    1,
    1,
    1,
    1,
    limite_credito,
    data_cadastro,
    "Cadastro gerado para teste",
    1,
    limite_atraso,
    "teste",
    ""
    )

    return valores,sql


def gerar_query_contatos(fk_pessoas):
    #SQL TABELAS


    sql = """
    INSERT INTO PESSOA_CONTATO (
        PES_CODIGO,
        CTC_NOME,
        CTC_NUMERO,
        CTC_MENSAGEIRO,
        CTC_EMAIL,
        CTC_PREF_XML,
        AUD_DATA_HORA_C
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    #GERANDO VALORES
    nome = para_ascii(faker.name())
    telefone = faker.cellphone_number().replace(" ", "").replace("-", "")
    email = nome.lower().replace(" ", ".") + "@example.com"

    valores = (
    fk_pessoas,
    nome,
    telefone,
    faker.random_element(["S", "N"]),
    email,
    faker.random_element(["S", "N"]),
    date.today() 
    )

    return valores,sql

