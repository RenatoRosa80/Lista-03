"""
 A série de Fibonacci é formada pela seqüência 
 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até 
 que o valor seja maior que 500.
"""
# F(n) = F(n-1) + F(n-2), onde F(1) = 1 e F(2) = 1

#ENTRADA

n = (1)

if n <= 0:
    print("Dados inválidos!")
else:
    f1 = 1
    f2 = 1
    print(f1, f2, end=" ")

    while True:
        fn = f1 + f2
        if fn >= 500:
            break
        print(fn, end=" ")
        f1 = f2
        f2 = fn

