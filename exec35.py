"""35. Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos 
existentes entre 1 e um número inteiro informado pelo usuário.
"""


inteiro = int(input("Informe um número inteiro: "))

if inteiro < 2:
    print("Não há números primos nesse intervalo!")
else:
    print(f"Números primos entre 1 e {inteiro}:")

    for num in range(2, inteiro + 1):  # testa cada número até N
        primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            print(num)
