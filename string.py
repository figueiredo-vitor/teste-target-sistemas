# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência
# ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


#string a inverter
string = '.mim arap edadinutropo amu arba e otrec ed euq orepse ' \
         ',sovitejbo son odacof erpmes ,aid adac a rohlem res ocsuB'

# converter o string em lista
lista = list(string)

# inverter ordem da lista
lista.reverse()

#nova string  com a lista invertida
string_reverse = ''.join(lista)

# immprimir string invertida
print(string_reverse)