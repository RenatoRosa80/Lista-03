"""
15. A série de Fibonacci é formada pela seqüência 
1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série 
até o n-ésimo termo.
"""
"""
F(n) = F(n-1) + F(n-2), onde F(1) = 1 e F(2) = 1
"""
# Programa para gerar a série de Fibonacci até o n-ésimo termo

n = int(input("Informe o número de termos: "))

# Verificação de entrada
if n <= 0:
    print("Por favor, informe um número inteiro positivo.")
else:
    f1, f2 = 1, 1
    print(f1, end=" ")

    if n > 1:
        print(f2, end=" ")

    for _ in range(3, n + 1):
        f3 = f1 + f2
        print(f3, end=" ")
        f1, f2 = f2, f3

#Como o codigo funciona:
"""Entrada: O usuário informa n, que é o número de termos que deseja ver.

Caso especial: Se n <= 0, o programa alerta sobre entrada inválida.

Primeiros termos: Ele começa com f1 = 1 e f2 = 1.

Laço: Usa um for para calcular os próximos termos, 
sempre somando os dois anteriores. """