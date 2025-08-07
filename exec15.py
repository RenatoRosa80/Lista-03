"""
15. A série de Fibonacci é formada pela seqüência 
1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série 
até o n-ésimo termo.
"""
"""
F(n) = F(n-1) + F(n-2), onde F(1) = 1 e F(2) = 1
"""
# ENTRADA 
n = int(input(" Informe ate qual número deseja ver a sequencia de Fibonacci:"))

if n <= 0:
    print(" Dados inválidos! ")
else:
    f1 = 1
    f2 = 1
for i in range(n):
    print(f1, end=" ")
    
# Atualizando os termos
    proximo = f1 + f2
    f1 = f2
    f2 = proximo