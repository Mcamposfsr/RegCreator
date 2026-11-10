import random

class RandomData:
    #Dados
    POVOADOS = [
    "Lagoa Nova",
    "Sao Bento",
    "Barreiro",
    "Lagoa do Mato",
    "Umbuzeiro",
    "Baixa Grande",
    "Riacho Seco",
    "Morrinhos",
    "Boa Vista",
    "Lagoa das Pedras"
    ]

    PONTOS_REFERENCIA = [
    "Proximo a praca",
    "Ao lado da igreja",
    "Em frente a escola",
    "Proximo ao mercado",
    "Atras do posto de saude",
    "Proximo ao campo",
    "Ao lado da farmacia",
    "Em frente a quadra",
    "Proximo a entrada",
    "Ao lado do colegio"
    ]

    #Buscas
    @staticmethod
    def buscar_ponto_ref():
        return random.choice(RandomData.PONTOS_REFERENCIA)
    @staticmethod
    def buscar_povoado():
        return random.choice(RandomData.POVOADOS)

