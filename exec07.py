#7. Faça um programa que leia 5 números e informe o maior número.
maior_numero = float("-inf")
menor_numero = float ("inf")



for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    # Verifica se o número digitado é o maior até agora
    if numero > maior_numero:
        maior_numero = numero
    
    # Verifica se o número digitado é o menor até agora
    if numero < menor_numero:
        menor_numero = numero

# Exibe o maior e o menor número
print(f"O maior número digitado foi: {maior_numero}")
print(f"O menor número digitado foi: {menor_numero}")

   




