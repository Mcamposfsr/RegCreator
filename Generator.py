from utilitarios import para_ascii,normalizar_doc
import random
from faker import Faker

faker = Faker("pt_BR")

def gerar_registro_pessoas():

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
    """

    #GERANDO VALORES
    nome = para_ascii(faker.name())
    endereco = para_ascii(faker.city())
    bairro = para_ascii(faker.neighborhood())
    numero = random.randint(1, 100)
    cpf = normalizar_doc(faker.cpf())

    valores = (
    "F",
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

