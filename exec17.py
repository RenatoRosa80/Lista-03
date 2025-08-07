"""
17. Faça um programa que calcule o fatorial de um número inteiro
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
#ENTRADA

fator = int(input(" Informe um número inteiro: "))

if fator < 0:
    print(" Dado informado é inválido!")
else:
    fatorial = 1
    print(f"{fator}! = ", end="")
for i in range(fator, 0, -1):
    fatorial *= i
    print(i, end="." if i > 1 else " = ")

    print(fatorial)


    
   