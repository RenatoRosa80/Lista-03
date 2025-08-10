"""
14. Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares e a 
quantidade de números impares.
"""
# Inicializa os contadores
pares = 0
impares = 1

# Recebendo os 10 números
for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibindo os resultados
print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
    