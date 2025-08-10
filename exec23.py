"""
23. Faça um programa que mostre todos os primos entre 1 e N 
sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou 
para encontrar os números primos. Serão avaliados o funcionamento, 
o estilo e o número de testes (divisões) executados.
"""

"""
O jeito mais simples de verificar:

Se o número for menor ou igual a 1, ele não é primo.

Teste a divisão dele pelos números de 2 até a raiz quadrada do número:

Se alguma divisão for exata (resto zero), ele não é primo.

Se nenhuma divisão for exata, ele é primo.

"""

N = int(input("Digite o valor de N: "))
total_divisoes = 0

print(f"Números primos entre 1 e {N}:")

for num in range(2, N + 1):
    if num <= 1:
        continue
    
    eh_primo = True
    limite = int(num ** 0.5)
    
    for i in range(2, limite + 1):
        total_divisoes += 1
        if num % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print(num, end=" ")

print()
print(f"Total de divisões executadas: {total_divisoes}")
