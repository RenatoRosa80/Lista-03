"""
21. Faça um programa que peça um número inteiro e determine se ele é 
ou não um número primo. Um número primo é aquele que é divisível 
somente por ele mesmo e por 1.

22. Altere o programa de cálculo dos números primos, informando, 
caso o número não seja primo, por quais número ele é divisível.
"""

#ENTRADA
inteiro = int(input(" Informe um número inteiro: "))

if inteiro <= 1:
    print(f"{inteiro} não é um número primo.")

else:
    
    divisores = []
    numero_primo = True
    
    for i in range(2, inteiro):  # Testa todos os números de 2 até o anterior ao próprio
        if inteiro % i == 0:
            divisores.append(i)
            
    if not divisores:
        print(f"{inteiro} é um número primo.")
    else:
        print(f"{inteiro} não é um número primo.")
        print(f"Ele é divisível por: {divisores}")
    
    