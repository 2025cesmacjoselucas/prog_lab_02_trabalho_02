# Q2 - Conversor de Temperatura
# Conversão entre Celsius e Fahrenheit
# Obrigração: criar um arquivo conversor.py e importar as funções

from conversor import to_celsius, to_fahrenheit

print("Conversor de Temperatura")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = int(input("Escolha uma opção (1 ou 2): "))

if opcao == 1:
    fahrenheit = to_fahrenheit(float(input("Digite a temperatura em Celsius: ")))
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f}")
elif opcao == 2:
    celsius = to_celsius(float(input("Digite a temperatura em Fahrenheit: ")))
    print(f"Temperatura em Celsius: {celsius:.2f}")
else:
    print("Opção inválida.")