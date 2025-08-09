"""
10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

11. Altere o programa anterior para mostrar no final a soma dos números.

"""

num1 = int(input(" Informe um número inteiro:"))
num2 = int(input(" Informe um segundo número inteiro:"))
soma = 0
for i in range(num1 + 1, num2 ):
    print(i, end= " ")
    soma = soma + i
print(f" A soma dos números digitados é {soma} ")
   