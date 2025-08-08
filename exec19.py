"""
18. Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.

19. Altere o programa anterior para que ele aceite apenas 
números entre 0 e 1000.
"""
# Pergunta quantos números o usuário deseja informar
quantidade = int(input("Quantos números você quer informar? "))

# Inicializa a lista para armazenar os números
numeros = []

# Lê os números com validação
for i in range(quantidade):
    while True:
        num = int(input(f"Informe o {i+1}º número (entre 0 e 1000): "))
        if 0 <= num <= 1000:
            numeros.append(num)
            break
        else:
            print("Número inválido! Digite um número entre 0 e 1000.")

# Processando os resultados
menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

# Exibe os resultados
print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
