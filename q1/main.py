def count_word_frequency(word: str, sentence: str) -> int:
    quantidade = 0
    frase_minuscula = sentence.lower()
    palavra_minuscula = word.lower()
    palavras_frase = frase_minuscula.split()
    for p in palavras_frase:
        if p == palavra_minuscula:
            quantidade += 1
    return quantidade


# Questão 1 - Manipulação de listas e strings

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para buscar: ")

# Quantidade de Palavras
print(count_word_frequency(palavra, frase))