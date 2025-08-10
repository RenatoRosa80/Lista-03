"""
f1 e f2 guardam os dois primeiros valores da série.

Usamos um while True para repetir indefinidamente até encontrar o 
valor maior que 500.

Em cada passo, somamos f1 + f2 para obter o próximo número.

Se o próximo número for maior que 500, o break encerra o loop.

Caso contrário, exibimos o número e avançamos a sequência.
"""


# Série de Fibonacci até valor maior que 500

f1 = 0
f2 = 1

print(f1, f2, end=" ")

while True:
    f3 = f1 + f2
    if f3 > 500:
        break
    print(f3, end=" ")
    f1 = f2
    f2 = f3
