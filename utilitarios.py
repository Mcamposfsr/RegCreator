import unicodedata

#Formartar texto para padrão ASCII
def para_ascii(texto):
    return(
        unicodedata.normalize("NFKD",texto)
        .encode("ascii","ignore")
        .decode("ascii")
)

#Receber valores de forma validada - Função que solicita a passagem de valores até determinado valor for válido
def input_validado(procedure,txt_erro):
    #Estado interno dos inputs
    estado = False
    while not estado: 
        try:
            #Caso a função retorne algo.
            any = procedure()
            estado = True

            return any
        except Exception as E:
            #Retornar error padrão
            if txt_erro == '':
                print(f"Falha no procedimento, error: {E}")
            #Retornar error passado na chamada
            print(txt_erro)

#Normalizar documentos
def normalizar_doc(doc):
    documento_normalizado = ""
    for char in doc:
        if char.isdigit():
            documento_normalizado = documento_normalizado + char
    return documento_normalizado