# Desafio -5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def reverse_word(word):
    word_reverse = ""
    for i in range(len(word) - 1, -1, -1):
        word_reverse += word[i]
    return word_reverse

word = input("Digite uma string para inverter: ")
word_reverse = reverse_word(word)
print("String invertida:", word_reverse)
