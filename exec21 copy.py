"""
21. Faça um programa que peça um número inteiro e determine se ele é 
ou não um número primo. Um número primo é aquele que é divisível 
somente por ele mesmo e por 1.
"""
#ENTRADA
inteiro = int(input(" Informe um número inteiro: "))
print("Ou digite 'sair' para encerrar o programa.")

if inteiro <= 1:
    print(f"{inteiro} não é um número primo.")

else:
    numero_primo = True
    
    for i in range(2, int(inteiro**0.5) + 1):
        if inteiro % i == 0:
            numero_primo = False
            break
    
    if numero_primo:
        print(f"{inteiro} é um número primo.")
    else:
        print(f"{inteiro} não é um número primo.")

