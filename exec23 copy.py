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
def encontrar_primos(n):
    """
    Encontra todos os números primos entre 1 e n, e conta o número de
    divisões realizadas.
    
    Args:
        n (int): O número limite fornecido pelo usuário.
        
    Returns:
        tuple: (lista de primos, número total de divisões)
    """
    primos = []
    total_divisoes = 0
    
    if n >= 2:
        primos.append(2)  # 2 é o único primo par
    
    for numero in range(3, n + 1, 2):  # Verifica apenas números ímpares
        eh_primo = True
        # Verifica divisibilidade até a raiz quadrada do número
        limite = int(numero ** 0.5) + 1
        for divisor in range(3, limite, 2):  # Testa apenas divisores ímpares
            total_divisoes += 1
            if numero % divisor == 0:
                eh_primo = False
                break
        
        if eh_primo:
            primos.append(numero)
    
    return primos, total_divisoes

# Entrada do usuário
n = int(input("Digite um número inteiro N maior que 1: "))

# Encontrar primos e contar divisões
primos, divisoes = encontrar_primos(n)

# Saída dos resultados
print(f"Números primos entre 1 e {n}:")
print(primos)
print(f"Total de divisões realizadas: {divisoes}")