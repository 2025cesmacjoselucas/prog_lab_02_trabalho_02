def real_dolar_converter(valor, cotacao, real_para_dolar=True):
    return valor / cotacao if real_para_dolar else valor * cotacao
    