# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência
# ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


string = input("Digite uma Palavra para inverter: ")

# Convertendo a string em uma lista de caracteres
lista_chars = list(string)

# Definindo os índices iniciais e finais para a inversão
iniciais = 0
finais = len(lista_chars) - 1

# Invertendo os caracteres utilizando uma estratégia de dois ponteiros
while iniciais < finais:
    lista_chars[iniciais], lista_chars[finais] = lista_chars[finais], lista_chars[iniciais]
    iniciais += 1
    finais -= 1

# Convertendo a lista de caracteres de volta para uma string
string_invertida = "".join(lista_chars)

print(string_invertida)
