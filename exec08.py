# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

media = 0
soma = 0
for i in range(5):
    n = int(input(f" Digite o {i + 1}º : "))
    soma = soma + n

media = soma / 5
print(f" A soma é {soma} e a Média é {media} ")


