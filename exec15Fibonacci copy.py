"""
15. A série de Fibonacci é formada pela seqüência 
1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série 
até o n-ésimo termo.
"""
"""
F(n) = F(n-1) + F(n-2), onde F(1) = 1 e F(2) = 1
"""
# Programa para gerar a série de Fibonacci até o n-ésimo termo

# Programa para gerar a série de Fibonacci até o n-ésimo termo (versão com lista)

n = int(input("Informe o número de termos: "))

if n <= 0:
    print("Por favor, informe um número inteiro positivo.")
else:
    fibonacci = []

    f1, f2 = 1, 1
    if n >= 1:
        fibonacci.append(f1)
    if n >= 2:
        fibonacci.append(f2)

    for _ in range(3, n + 1):
        f3 = f1 + f2
        fibonacci.append(f3)
        f1, f2 = f2, f3

    print("Sequência de Fibonacci:", fibonacci)
