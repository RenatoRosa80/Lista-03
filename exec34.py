"""
34. Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia. Um número primo é aquele que é divisível
apenas por um e por ele mesmo. Faça um programa que peça um número
inteiro e determine se ele é ou não um número primo.
"""
primo = ()
inteiro = int(input(" Informe um número inteiro: "))
if inteiro <= 1:
    print(" Nao é um número inteiro! ")
else:
    primo = True
    for i in range(2, int(inteiro ** 0.5) + 1):
        if inteiro %i == 0:
            primo= False
            break
    if primo:
        print(" é Primo")
    else:
        print(" Nao é primo")
            
        
    