import configparser
import os
from pathlib import Path



class ConfigIni:
    DIRETORIO_CONFIG = Path(os.getenv("APPDATA") or Path.home()) / "FbPop"
    ARQUIVO_INI = DIRETORIO_CONFIG / "config.ini"

    # Verificação se o ini existe
    @staticmethod
    def verificar_ini():
        return ConfigIni.ARQUIVO_INI.exists()
       
    #Gerar ini
    @staticmethod
    def gerar_ini(dll_path,db_path,db_user,db_pass):
        config = configparser.ConfigParser()

        config["Firebird"] = {
            "client_library": dll_path,
            "database": db_path,
            "user": db_user,
            "password": db_pass,
            "charset": "UTF8"
        }

        ConfigIni.DIRETORIO_CONFIG.mkdir(parents=True, exist_ok=True)
        with open(ConfigIni.ARQUIVO_INI, "w", encoding="utf-8") as arquivo:
            config.write(arquivo)

    #Carregar ini
    @staticmethod
    def carregar_ini():
        config = configparser.ConfigParser()

        config.read(ConfigIni.ARQUIVO_INI, encoding="utf-8")
        
        return {
            "dll": config["Firebird"]["client_library"],
            "banco": config["Firebird"]["database"],
            "usuario": config["Firebird"]["user"],
            "senha": config["Firebird"]["password"],
            "charset": config["Firebird"]["charset"],
        }

    #Deletar ini
    @staticmethod
    def deletar_ini():
        if ConfigIni.ARQUIVO_INI.exists():
            ConfigIni.ARQUIVO_INI.unlink()
            return True

        return False