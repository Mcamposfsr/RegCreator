import configparser
from pathlib import Path


ARQUIVO_INI = Path(__file__).resolve().parent / "config.ini"

# Verificação se o ini existe
def verificar_ini():
    if ARQUIVO_INI.exists():
            return True
    else:
        return False


def gerar_ini(dll_path,db_path,db_user,db_pass):
    
    config = configparser.ConfigParser()

    config["Firebird"] = {
        "client_library": dll_path,
        "database": db_path,
        "user": db_user,
        "password": db_pass,
        "charset": "UTF8"
    }

    with open(ARQUIVO_INI, "w", encoding="utf-8") as arquivo:
        config.write(arquivo)

def carregar_ini():
    config = configparser.ConfigParser()

    config.read(ARQUIVO_INI, encoding="utf-8")
    
    return {
        "dll": config["Firebird"]["client_library"],
        "banco": config["Firebird"]["database"],
        "usuario": config["Firebird"]["user"],
        "senha": config["Firebird"]["password"],
        "charset": config["Firebird"]["charset"],
    }