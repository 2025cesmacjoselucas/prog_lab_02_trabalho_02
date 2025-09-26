# Questão 4 - Verificador de Números Pares e Ímpares
# Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.

def eh_par(num: int) -> bool:
    return num % 2 == 0

numero = int(input("Digite um número: "))
if eh_par(numero):
    print("Par")
else:
    print("Ímpar")