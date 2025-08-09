# 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
import math
qtd_numeros = int(input(" Quantos números deseja informar? "))
valores_soma = [] 


for i in range(qtd_numeros):
    numero = int(input(f" Digite o {i + 1}º número: "))
    valores_soma.append(numero)
print(valores_soma)
menor = min(valores_soma)
maior = max(valores_soma)
soma = sum (valores_soma)

print(f" O menor número é {menor}")
print(f" O maiorr número é {maior}")
print(f" A soma dos  números é {soma}")




