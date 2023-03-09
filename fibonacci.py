# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)
# , escreva um programa na linguagem que desejar onde, informado um número, ele
# calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número
# informado pertence ou não a sequência.

num1 = int(input('Digite um número: '))

anterior = 0
atual = 1

while atual < num1:
    proximo = anterior + atual
    anterior = atual
    atual = proximo

if atual == num1:
    print(num1,'Pertence a sequência de Fibonacci !')

else:
    print(num1,'Não pertence a sequência de Fibonacci !')



