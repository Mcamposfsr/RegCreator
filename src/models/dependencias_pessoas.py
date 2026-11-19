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

    # FIDELIDADE
    def select_fidelidade(self):
        sql = "SELECT * FROM FIDELIDADE WHERE FID_CODIGO = 1;"
        return self.conexao.executar_query_consulta(sql)
    def insert_fidelidade(self):
        sql = "INSERT INTO FIDELIDADE(FID_CODIGO,FID_NOME_PROGRAMA) VALUES (1,'DUMMY')"
        self.conexao.executar_query_consulta(sql)

    # SEGMENTO
    def select_segmentos(self):
            sql = "SELECT * FROM SEGMENTOS WHERE SEG_CODIGO = 1;"
            return self.conexao.executar_query_consulta(sql)
    def insert_segmentos(self):
        sql = "INSERT INTO SEGMENTOS(SEG_CODIGO,SEG_DESCRICAO) VALUES (1,'DUMMY')"
        self.conexao.executar_query_consulta(sql)

    # CLASSES
    def select_classes(self):
            sql = "SELECT * FROM CLASSES WHERE CLA_CODIGO = 1;"
            return self.conexao.executar_query_consulta(sql)
    def insert_classes(self):
        sql = "INSERT INTO CLASSES(CLA_CODIGO,CLA_DESCRICAO) VALUES (1,'DUMMY')"
        self.conexao.executar_query_consulta(sql)

    # VENDEDOR
    def select_vendedores(self):
            sql = "SELECT * FROM VENDEDORES WHERE FUN_CODIGO = 1;"
            return self.conexao.executar_query_consulta(sql)
    def insert_vendedores(self):
        sql = "INSERT INTO VENDEDORES(FUN_CODIGO,FUN_NOME) VALUES (1,'DUMMY')"
        self.conexao.executar_query_consulta(sql)

    