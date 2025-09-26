# Q6 - Conversor de Moedas
# Crie a função que converte reais para dólares e dólares para reais (arquivo conversor.py)
# real_para_dolar e dolar_para_real. Caso o usuário não passe o tipo (real_para_dolar ou dolar_para_real) o default deve ser real_para_dolar <- padrão

from conversor import real_dolar_converter

valor = float(input("Digite o valor: "))
cotacao = float(input("Digite a cotação do dólar: "))
tipo = int(input("Deseja converter de (1) Real para Dólar ou (2) Dólar para Real? (padrão é 1): "))
if tipo == 2:
    resultado = real_dolar_converter(valor, cotacao, real_para_dolar=False)
    print(f"\n{valor:.2f} dólares equivalem a {resultado:.2f} reais.")
else:
    resultado = real_dolar_converter(valor, cotacao, real_para_dolar=True)
    print(f"\n{valor:.2f} reais equivalem a {resultado:.2f} dólares.")
