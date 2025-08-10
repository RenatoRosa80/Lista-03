"""
15. A série de Fibonacci é formada pela seqüência 
1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série 
até o n-ésimo termo.
"""
"""
F(n) = F(n-1) + F(n-2), onde F(1) = 1 e F(2) = 1
"""

# Programa para gerar a série de Fibonacci até o n-ésimo termo (versão com lista)

n = int(input("Informe o número de termos: "))
fibonacci = [1, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(n - 2)]
print(fibonacci[:n])
