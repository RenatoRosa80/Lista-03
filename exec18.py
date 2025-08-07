"""
18. Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.
"""
#ENTRADA
import math
menor_valor = 0
maior_valor = 1
soma = menor_valor + maior_valor

n = int(input(" Quantos números inteiros gostaria de inserir?"))

if n < 0:
    print(" Dado informado é inválido!")
else:
    numeros = []
    
for i in range(n):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    
menor_valor = min(numeros)
maior_valor = max(numeros)
soma = sum(numeros)
   
print(f" Menor número é: {menor_valor}")
print(f" Maior número é: {maior_valor}")
print(f" A soma dos números é: {soma}")




