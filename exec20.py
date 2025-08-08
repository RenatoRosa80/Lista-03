"""
Faça um programa que calcule o fatorial de um número inteiro
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120,
permitindo ao usuário calcular o fatorial várias vezes e 
limitando o fatorial a números inteiros positivos e menores que 16.
"""
#ENTRADA

while True:
    print("\nCalculadora de Fatorial")
    print("Digite um número inteiro positivo menor que 16 para calcular seu fatorial.")
    print("Ou digite 'sair' para encerrar o programa.")
    
    entrada = input("Número: ")
    
    if entrada.lower() == 'sair':
        print("Encerrando o programa...")
        break
    
    try:
        numero = int(entrada)
        
        if numero < 0:
            print("Erro: O número deve ser positivo.")
        elif numero >= 16:
            print("Erro: O número deve ser menor que 16.")
        else:
            fatorial = 1
            sequencia = []
            
            for i in range(numero, 0, -1):
                fatorial *= i
                sequencia.append(str(i))
            
            print(f"{numero}! = {'*'.join(sequencia)} = {fatorial}")
    
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido ou 'sair'.")