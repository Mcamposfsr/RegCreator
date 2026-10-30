from ..conexao import Conexao

class ModelDummyPessoas:
    def __init__(self,conexao):
        self.conexao:Conexao = conexao

    #ESTADOS
    def select_estados(self):
        sql = "SELECT * FROM ESTADOS WHERE EST_CODIGO = 1;"
        return self.conexao.executar_query_consulta(sql)
    def insert_estados(self):
        sql = "INSERT INTO ESTADOS(EST_CODIGO,EST_SIGLA,EST_IBGE,EST_NOME) VALUES (1,'MY',0,'DUMMY');"
        self.conexao.executar_query_consulta(sql)

    # CIDADES
    def select_cidades(self):
        sql = "SELECT * FROM CIDADES WHERE CID_CODIGO = 1;"
        return self.conexao.executar_query_consulta(sql)
    def insert_cidades(self):
        sql = "INSERT INTO CIDADES(CID_CODIGO, EST_CODIGO, CID_NOME) VALUES (1, 1, 'DUMMY');"
        self.conexao.executar_query_consulta(sql)

    #EMPRESA
    def select_empresa(self):
        sql = "SELECT * FROM EMPRESAS WHERE EMP_CODIGO = 1"
        return self.conexao.executar_query_consulta(sql)
    def insert_empresa(self):
        sql = "INSERT INTO EMPRESAS(EMP_CODIGO,EMP_RAZAO_SOCIAL,EMP_FANTASIA,EMP_CNPJ,CID_CODIGO,EMP_CRT) VALUES (1,'DUMMY','DUMMY','46.638.393/0001-64',1,'S');"
        self.conexao.executar_query_consulta(sql)


    # ROTAS
    def select_rotas(self):
        sql = "SELECT * FROM ROTAS WHERE ROT_CODIGO = 1;"
        return self.conexao.executar_query_consulta(sql)
    def insert_rotas(self):
        sql = "INSERT INTO ROTAS(ROT_CODIGO, ROT_DESCRICAO, ROT_ATIVO) VALUES (1, 'DUMMY', 'S');"
        self.conexao.executar_query_consulta(sql)

    # SITUACOES
    def select_situacoes(self):
        sql = "SELECT * FROM SITUACOES WHERE SIT_CODIGO = 1;"
        return self.conexao.executar_query_consulta(sql)
    def insert_situacoes(self):
        sql = "INSERT INTO SITUACOES(SIT_CODIGO, SIT_DESCRICAO, SIT_PERMITE_VENDA) VALUES (1, 'DUMMY', 'S');"
        self.conexao.executar_query_consulta(sql)

    # CONVENIOS
    def select_convenios(self):
        sql = "SELECT * FROM CONVENIOS WHERE CNV_CODIGO = 1;"
        return self.conexao.executar_query_consulta(sql)
    def insert_convenios(self):
        sql = "INSERT INTO CONVENIOS(CNV_CODIGO, CNV_DESCRICAO) VALUES (1, 'DUMMY');"
        self.conexao.executar_query_consulta(sql)


    # BOLETOS
    def select_boletos(self):
        sql = "SELECT * FROM BOLETOS WHERE BOL_CODIGO = 1;"
        return self.conexao.executar_query_consulta(sql)
    def insert_boletos(self):
        sql = "INSERT INTO BOLETOS(BOL_CODIGO, BOL_DESCRICAO) VALUES (1, 'DUMMY');"
        self.conexao.executar_query_consulta(sql)

    